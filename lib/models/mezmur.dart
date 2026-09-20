import 'package:cloud_firestore/cloud_firestore.dart';

class Mezmur {
  final String id;
  final String title;
  final String language;
  final String fullText;

  Mezmur({
    required this.id,
    required this.title,
    required this.language,
    required this.fullText,
  });

  factory Mezmur.fromFirestore(DocumentSnapshot doc) {
    Map data = doc.data() as Map<String, dynamic>;
    return Mezmur(
      id: doc.id,
      title: data['title'] ?? '',
      language: data['language'] ?? 'Unknown',
      fullText: data['fullText'] ?? '',
    );
  }
}
