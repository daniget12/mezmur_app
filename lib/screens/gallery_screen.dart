import 'package:flutter/material.dart';

class GalleryScreen extends StatelessWidget {
  const GalleryScreen({super.key});

  @override
  Widget build(BuildContext context) {
    // List all your church and ceremony photos here
    final List<Map<String, String>> allImages = [
      // Church Photos
      {'path': 'assets/images/church/church1.jpg', 'title': 'ቤተ ክርስቲያን 1'},
      {'path': 'assets/images/church/church2.jpg', 'title': 'ቤተ ክርስቲያን 2'},
      {'path': 'assets/images/church/church3.jpg', 'title': 'ቤተ ክርስቲያን 3'},

      // Ceremony Photos - Add your actual ceremony photos here
      {'path': 'assets/images/ceremony/timket.jpg', 'title': 'ትንሳኤ (Timket)'},
      {'path': 'assets/images/ceremony/easter.jpg', 'title': 'ፋሲካ (Easter)'},
      {'path': 'assets/images/ceremony/baptism.jpg', 'title': 'ጥምቀት (Baptism)'},
      {
        'path': 'assets/images/ceremony/christmas.jpg',
        'title': 'ገና (Christmas)'
      },
    ];

    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'የቤተ ክርስቲያን ፎቶዎች',
          style: TextStyle(color: Colors.white),
        ),
        backgroundColor: Colors.blue,
        centerTitle: true,
      ),
      body: GridView.builder(
        padding: const EdgeInsets.all(16),
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
          crossAxisSpacing: 16,
          mainAxisSpacing: 16,
          childAspectRatio: 1.0,
        ),
        itemCount: allImages.length,
        itemBuilder: (context, index) {
          final image = allImages[index];
          return GestureDetector(
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => FullScreenImage(
                    imagePath: image['path']!,
                    title: image['title']!,
                  ),
                ),
              );
            },
            child: Container(
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(12),
                boxShadow: [
                  BoxShadow(
                    color: Colors.grey.withOpacity(0.3),
                    spreadRadius: 2,
                    blurRadius: 5,
                  ),
                ],
              ),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(12),
                child: Stack(
                  fit: StackFit.expand,
                  children: [
                    Image.asset(
                      image['path']!,
                      fit: BoxFit.cover,
                      errorBuilder: (context, error, stackTrace) {
                        return Container(
                          color: Colors.grey[300],
                          child: Column(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              const Icon(Icons.broken_image, size: 50),
                              const SizedBox(height: 8),
                              Text(
                                image['title']!,
                                style: const TextStyle(fontSize: 12),
                                textAlign: TextAlign.center,
                              ),
                            ],
                          ),
                        );
                      },
                    ),
                    Positioned(
                      bottom: 0,
                      left: 0,
                      right: 0,
                      child: Container(
                        color: Colors.black54,
                        padding: const EdgeInsets.symmetric(vertical: 8),
                        child: Text(
                          image['title']!,
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 12,
                          ),
                          textAlign: TextAlign.center,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          );
        },
      ),
    );
  }
}

// Full screen image viewer
class FullScreenImage extends StatelessWidget {
  final String imagePath;
  final String title;

  const FullScreenImage(
      {super.key, required this.imagePath, required this.title});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        title: Text(title, style: const TextStyle(color: Colors.white)),
        backgroundColor: Colors.black,
        iconTheme: const IconThemeData(color: Colors.white),
      ),
      body: Center(
        child: GestureDetector(
          onTap: () => Navigator.pop(context),
          child: Image.asset(imagePath),
        ),
      ),
    );
  }
}
