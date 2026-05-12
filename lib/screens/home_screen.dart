import 'package:flutter/material.dart';
import '../data/mezmur_data.dart';
import '../models/mezmur.dart';
import 'detail_screen.dart';
import 'about_screen.dart';
import 'notes_screen.dart';
import 'gallery_screen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    // Get all mezmurs and sort alphabetically by title
    List<Mezmur> allMezmurs = MezmurData.getMezmurs();

    // Sort alphabetically (case-insensitive)
    allMezmurs
        .sort((a, b) => a.title.toLowerCase().compareTo(b.title.toLowerCase()));

    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Baafata Faaruu',
          style: TextStyle(
              color: Colors.white, fontSize: 20, fontWeight: FontWeight.bold),
        ),
        backgroundColor: Colors.blue,
        centerTitle: true,
      ),
      body: ListView.builder(
        itemCount: allMezmurs.length,
        itemBuilder: (context, index) {
          final mezmur = allMezmurs[index];
          final number = index + 1;
          return Card(
            margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 6),
            elevation: 2,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(12),
            ),
            child: ListTile(
              leading: Container(
                width: 45,
                height: 45,
                decoration: BoxDecoration(
                  color: Colors.blue[100],
                  borderRadius: BorderRadius.circular(25),
                ),
                child: Center(
                  child: Text(
                    '$number',
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                      color: Colors.blue[800],
                    ),
                  ),
                ),
              ),
              title: Text(
                mezmur.title,
                style: const TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.w500,
                ),
              ),
              subtitle: Text(
                '${mezmur.language}',
                style: TextStyle(fontSize: 12, color: Colors.grey[600]),
              ),
              trailing:
                  const Icon(Icons.chevron_right, size: 24, color: Colors.blue),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => DetailScreen(mezmur: mezmur),
                  ),
                );
              },
            ),
          );
        },
      ),
      bottomNavigationBar: BottomNavigationBar(
        type: BottomNavigationBarType.fixed,
        backgroundColor: Colors.white,
        selectedItemColor: Colors.blue,
        unselectedItemColor: Colors.grey,
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.music_note), label: 'መዝሙር'),
          BottomNavigationBarItem(icon: Icon(Icons.photo_library), label: 'ፎቶ'),
          BottomNavigationBarItem(icon: Icon(Icons.note), label: 'ማስታወሻ'),
          BottomNavigationBarItem(icon: Icon(Icons.info), label: 'ስለ'),
        ],
        onTap: (index) {
          if (index == 0) {
            // Already on home screen
          } else if (index == 1) {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const GalleryScreen()),
            );
          } else if (index == 2) {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const NotesScreen()),
            );
          } else if (index == 3) {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const AboutScreen()),
            );
          }
        },
      ),
    );
  }
}
