import 'package:cloud_firestore/cloud_firestore.dart';
import '../models/mezmur.dart';
import '../models/event_model.dart';

class FirebaseService {
  FirebaseFirestore get _firestore => FirebaseFirestore.instance;

  // Get stream of all mezmurs
  Stream<List<Mezmur>> getMezmursStream() {
    return _firestore.collection('mezmurs').snapshots().map((snapshot) {
      return snapshot.docs.map((doc) => Mezmur.fromFirestore(doc)).toList();
    });
  }

  // Get stream of all events, ordered by date descending
  Stream<List<EventModel>> getEventsStream() {
    try {
      return _firestore
          .collection('events')
          .orderBy('date', descending: true)
          .snapshots()
          .map((snapshot) {
        return snapshot.docs
            .map((doc) => EventModel.fromFirestore(doc))
            .toList();
      });
    } catch (e) {
      return Stream.error(e);
    }
  }
}
