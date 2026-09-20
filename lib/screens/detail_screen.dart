import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../models/mezmur.dart';
import '../services/favorites_manager.dart';

class DetailScreen extends StatefulWidget {
  final Mezmur mezmur;

  const DetailScreen({super.key, required this.mezmur});

  @override
  State<DetailScreen> createState() => _DetailScreenState();
}

class _DetailScreenState extends State<DetailScreen> {
  double _fontSize = 18.0;

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
    setState(() {}); // Rebuild to update favorite icon
  }

  void _increaseFontSize() {
    setState(() {
      if (_fontSize < 36.0) _fontSize += 2.0;
    });
  }

  void _decreaseFontSize() {
    setState(() {
      if (_fontSize > 12.0) _fontSize -= 2.0;
    });
  }

  void _copyToClipboard() {
    Clipboard.setData(ClipboardData(
        text: "${widget.mezmur.title}\n\n${widget.mezmur.fullText}"));
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text('Mezmur copied to clipboard!'),
        behavior: SnackBarBehavior.floating,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final isFavorite = FavoritesManager().isFavorite(widget.mezmur.id);

    return Scaffold(
      appBar: AppBar(
        title: Text(widget.mezmur.title),
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
        actions: [
          IconButton(
            icon: Icon(
              isFavorite ? Icons.favorite : Icons.favorite_border,
              color: isFavorite ? Colors.redAccent : null,
            ),
            tooltip: isFavorite ? 'Remove from Favorites' : 'Add to Favorites',
            onPressed: () {
              FavoritesManager().toggleFavorite(widget.mezmur.id);
            },
          ),
          IconButton(
            icon: const Icon(Icons.remove_circle_outline),
            tooltip: 'Decrease Font Size',
            onPressed: _decreaseFontSize,
          ),
          IconButton(
            icon: const Icon(Icons.add_circle_outline),
            tooltip: 'Increase Font Size',
            onPressed: _increaseFontSize,
          ),
          IconButton(
            icon: const Icon(Icons.copy),
            tooltip: 'Copy Mezmur',
            onPressed: _copyToClipboard,
          ),
          const SizedBox(width: 8),
        ],
      ),
      body: Hero(
        tag: 'mezmur-${widget.mezmur.id}',
        child: Material(
          color: Colors.transparent,
          child: Container(
            color: Theme.of(context).scaffoldBackgroundColor,
            child: SingleChildScrollView(
              padding: const EdgeInsets.symmetric(horizontal: 24.0, vertical: 32.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                        decoration: BoxDecoration(
                          color: Theme.of(context).colorScheme.primaryContainer,
                          borderRadius: BorderRadius.circular(20),
                        ),
                        child: Text(
                          'Mezmur #${widget.mezmur.id}',
                          style: TextStyle(
                            fontWeight: FontWeight.bold,
                            color: Theme.of(context).colorScheme.onPrimaryContainer,
                          ),
                        ),
                      ),
                      Text(
                        widget.mezmur.language,
                        style: TextStyle(
                          color: Theme.of(context).colorScheme.secondary,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 32),
                  Text(
                    widget.mezmur.fullText,
                    style: TextStyle(
                      fontSize: _fontSize,
                      height: 1.8,
                      fontWeight: FontWeight.w500,
                    ),
                  ),
                  const SizedBox(height: 32),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
