import 'package:flutter/material.dart';
import '../models/mezmur.dart';

class DetailScreen extends StatelessWidget {
  final Mezmur mezmur;

  const DetailScreen({super.key, required this.mezmur});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          mezmur.title,
          style: const TextStyle(color: Colors.white),
        ),
        backgroundColor: Colors.blue,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Text(
              mezmur.fullText,
              style: const TextStyle(
                fontSize: 18,
                height: 1.5,
              ),
            ),
            const SizedBox(height: 30),
            // Icons at the end of Mezmur
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Column(
                  children: [
                    Icon(Icons.auto_awesome, size: 30, color: Colors.brown[700]),
                    const SizedBox(height: 4),
                    const Text('ቅዱስ'),
                  ],
                ),
                Column(
                  children: [
                    Icon(Icons.celebration, size: 30, color: Colors.blue[700]),
                    const SizedBox(height: 4),
                    const Text('ቤተ ክርስቲያን'),
                  ],
                ),
                Column(
                  children: [
                    Icon(Icons.favorite, size: 30, color: Colors.red),
                    const SizedBox(height: 4),
                    const Text('ፍቅር'),
                  ],
                ),
              ],
            ),
            const SizedBox(height: 20),
          ],
        ),
      ),
    );
  }
}
