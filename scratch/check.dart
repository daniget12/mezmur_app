import 'dart:io';

void main() {
  final text = File(r'scratch\parse_mezmurs.dart').readAsStringSync();
  final startIndex = text.indexOf('1.ARGADHEEN JIRA!!!');
  final actual = text.substring(startIndex);
  final pattern = RegExp(r'^(\d+)\s*\.\s*', multiLine: true);
  final matches = pattern.allMatches(actual).map((m) => int.parse(m.group(1)!)).toSet();
  for (int i = 1; i <= 174; i++) {
    if (!matches.contains(i)) print('Missing: $i');
  }
}
