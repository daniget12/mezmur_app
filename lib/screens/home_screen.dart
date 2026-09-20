import 'package:flutter/material.dart';
import '../models/mezmur.dart';
import '../data/mezmur_data.dart';
import '../services/favorites_manager.dart';
import 'detail_screen.dart';
import 'about_screen.dart';
import 'notes_screen.dart';
import 'events_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _currentIndex = 0;
  String _searchQuery = '';
  String _selectedLanguage = 'All'; // 'All', 'Favorites', 'Afaan Oromo', 'Amharic'

  @override
  void initState() {
    super.initState();
    FavoritesManager().addListener(_onFavoritesChanged);
  }

  @override
  void dispose() {
    FavoritesManager().removeListener(_onFavoritesChanged);
    super.dispose();
  }

  void _onFavoritesChanged() {
    setState(() {}); // Rebuild to update favorite UI
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Baafata Faaruu',
          style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
        ),
        centerTitle: true,
        flexibleSpace: Container(
          decoration: BoxDecoration(
            gradient: LinearGradient(
              colors: [
                Theme.of(context).colorScheme.primary,
                Theme.of(context).colorScheme.primary.withOpacity(0.8),
              ],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
          ),
        ),
      ),
      body: _buildBody(),
      bottomNavigationBar: _buildBottomNav(),
    );
  }

  Widget _buildBottomNav() {
    return BottomNavigationBar(
      type: BottomNavigationBarType.fixed,
      currentIndex: _currentIndex,
      selectedItemColor: Theme.of(context).colorScheme.secondary,
      unselectedItemColor: Colors.grey,
      items: const [
        BottomNavigationBarItem(icon: Icon(Icons.music_note), label: 'Faaruu'),
        BottomNavigationBarItem(icon: Icon(Icons.event), label: 'Ayyaana'),
        BottomNavigationBarItem(icon: Icon(Icons.note), label: 'Yadannoo'),
        BottomNavigationBarItem(icon: Icon(Icons.info), label: 'Wa\'ee'),
      ],
      onTap: (index) {
        setState(() {
          _currentIndex = index;
        });
        if (index == 2) {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => const NotesScreen()),
          ).then((_) => setState(() => _currentIndex = 0));
        } else if (index == 3) {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => const AboutScreen()),
          ).then((_) => setState(() => _currentIndex = 0));
        }
      },
    );
  }

  Widget _buildBody() {
    if (_currentIndex == 1) {
      return const EventsScreen();
    }

    // Filter Mezmurs
    List<Mezmur> filteredMezmurs = mezmurs.where((m) {
      final matchesSearch = m.title.toLowerCase().contains(_searchQuery.toLowerCase()) ||
                            m.id.contains(_searchQuery);
      
      bool matchesLanguage = true;
      if (_selectedLanguage == 'Favorites') {
        matchesLanguage = FavoritesManager().isFavorite(m.id);
      } else if (_selectedLanguage != 'All') {
        matchesLanguage = m.language == _selectedLanguage;
      }
      
      return matchesSearch && matchesLanguage;
    }).toList();

    return Column(
      children: [
        _buildSearchBar(),
        _buildLanguageFilters(),
        Expanded(
          child: filteredMezmurs.isEmpty
              ? _buildEmptyState()
              : ListView.builder(
                  padding: const EdgeInsets.symmetric(vertical: 8),
                  itemCount: filteredMezmurs.length,
                  itemBuilder: (context, index) {
                    return _buildMezmurCard(filteredMezmurs[index]);
                  },
                ),
        ),
      ],
    );
  }

  Widget _buildSearchBar() {
    return Padding(
      padding: const EdgeInsets.fromLTRB(16, 16, 16, 8),
      child: TextField(
        decoration: InputDecoration(
          hintText: 'Search by title or number...',
          prefixIcon: const Icon(Icons.search),
          filled: true,
          fillColor: Theme.of(context).colorScheme.surfaceContainerHighest.withOpacity(0.5),
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(30),
            borderSide: BorderSide.none,
          ),
          contentPadding: const EdgeInsets.symmetric(horizontal: 20, vertical: 0),
        ),
        onChanged: (value) {
          setState(() {
            _searchQuery = value;
          });
        },
      ),
    );
  }

  Widget _buildLanguageFilters() {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
      child: SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: ['All Mezmurs', 'Favorites'].map((String option) {
            final isSelected = _selectedLanguage == option || (_selectedLanguage == 'All' && option == 'All Mezmurs');
            return Padding(
              padding: const EdgeInsets.symmetric(horizontal: 4),
            child: ChoiceChip(
              label: Text(option),
              selected: isSelected,
              onSelected: (bool selected) {
                if (selected) {
                  setState(() {
                    _selectedLanguage = option == 'All Mezmurs' ? 'All' : option;
                  });
                }
              },
              selectedColor: Theme.of(context).colorScheme.primaryContainer,
              labelStyle: TextStyle(
                color: isSelected 
                    ? Theme.of(context).colorScheme.onPrimaryContainer
                    : Theme.of(context).colorScheme.onSurfaceVariant,
                fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
              ),
            ),
          );
        }).toList(),
        ),
      ),
    );
  }

  Widget _buildMezmurCard(Mezmur mezmur) {
    return Hero(
      tag: 'mezmur-${mezmur.id}',
      child: Card(
        margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 6),
        elevation: 1,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        child: InkWell(
          borderRadius: BorderRadius.circular(16),
          onTap: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => DetailScreen(mezmur: mezmur)),
            );
          },
          child: Padding(
            padding: const EdgeInsets.symmetric(vertical: 8, horizontal: 8),
            child: ListTile(
              leading: Container(
                width: 48,
                height: 48,
                decoration: BoxDecoration(
                  color: Theme.of(context).colorScheme.primaryContainer,
                  shape: BoxShape.circle,
                ),
                child: Center(
                  child: Text(
                    mezmur.id,
                    style: TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                      color: Theme.of(context).colorScheme.onPrimaryContainer,
                    ),
                  ),
                ),
              ),
              title: Text(
                mezmur.title,
                style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w600),
              ),
              subtitle: Text(
                mezmur.language,
                style: TextStyle(
                  fontSize: 13, 
                  color: Theme.of(context).colorScheme.secondary,
                  fontWeight: FontWeight.w500,
                ),
              ),
              trailing: Icon(
                Icons.arrow_forward_ios, 
                size: 16, 
                color: Theme.of(context).colorScheme.outline,
              ),
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildEmptyState() {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(Icons.search_off, size: 64, color: Theme.of(context).colorScheme.outline),
          const SizedBox(height: 16),
          Text(
            'No Mezmurs found.',
            style: TextStyle(color: Theme.of(context).colorScheme.onSurfaceVariant, fontSize: 16),
          ),
        ],
      ),
    );
  }
}
