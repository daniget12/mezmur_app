import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

class AboutScreen extends StatelessWidget {
  const AboutScreen({super.key});

  final String phoneNumber = "+251956612435";
  final String emailAddress = "danielgetahun1000@gmail.com";
  final String telegramUsername = "daniget12";

  Future<void> _makePhoneCall(BuildContext context) async {
    final Uri launchUri = Uri(scheme: 'tel', path: phoneNumber);
    if (await canLaunchUrl(launchUri)) {
      await launchUrl(launchUri);
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Could not make phone call')),
      );
    }
  }

  Future<void> _sendEmail(BuildContext context) async {
    final Uri launchUri = Uri(
      scheme: 'mailto',
      path: emailAddress,
      query:
          'subject=Mezmur App Feedback&body=Hello Daniel, I have a question about the Mezmur app...',
    );
    if (await canLaunchUrl(launchUri)) {
      await launchUrl(launchUri);
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Could not send email')),
      );
    }
  }

  Future<void> _openTelegram(BuildContext context) async {
    final Uri telegramUri =
        Uri(scheme: 'https', host: 't.me', path: telegramUsername);
    if (await canLaunchUrl(telegramUri)) {
      await launchUrl(telegramUri);
    } else {
      final Uri fallbackUri = Uri(
          scheme: 'https',
          host: 'web.telegram.org',
          path: 'k',
          query: '#@$telegramUsername');
      await launchUrl(fallbackUri);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Wa'ee Applikeshiniicha",
            style: TextStyle(color: Colors.white)),
        backgroundColor: Colors.blue,
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const SizedBox(height: 20),

            // DEVELOPER PHOTO - ADDED HERE
            Center(
              child: Container(
                width: 120,
                height: 120,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  border: Border.all(color: Colors.blue, width: 3),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.grey.withOpacity(0.3),
                      spreadRadius: 2,
                      blurRadius: 5,
                    ),
                  ],
                  image: DecorationImage(
                    image: AssetImage('assets/images/developer.jpg'),
                    fit: BoxFit.cover,
                    onError: (exception, stackTrace) {
                      // This handles missing image gracefully
                    },
                  ),
                ),
              ),
            ),
            const SizedBox(height: 20),

            const Center(
                child: Icon(Icons.music_note, size: 80, color: Colors.blue)),
            const SizedBox(height: 20),

            Center(
              child: Text(
                'Senbet Timihirt Bet Mezmur',
                style: TextStyle(
                    fontSize: 22,
                    fontWeight: FontWeight.bold,
                    color: Colors.blue[800]),
              ),
            ),
            const SizedBox(height: 10),
            const Center(
                child: Text('Version 1.0.0',
                    style: TextStyle(fontSize: 14, color: Colors.grey))),
            const SizedBox(height: 30),

            const Text('Ibsa:',
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            const SizedBox(height: 10),
            const Text(
              'Appilikeshiniin kun karaa kutaa faaruu barattota dilbataa M/A/Q/Mikaa`eel ayyana cuuphaa sababeefachuun kan qindaa`e yoo ta`u, Yeedaloo isaani barbaaduun akka qo`attan akkasumas dogoggora qubee fi jechaa uumameef nu ofkalchaa isinin jechaa bakka sirreffama barbaadutti sirreessun akkaa sirresinuuf karaa kanaa gadiitin nu qunamuu dandeessu.Kutaa Faaruu M/A/Q/Mikaa`eel irraa.',
              style: TextStyle(fontSize: 16, height: 1.3),
            ),
            const SizedBox(height: 30),

            const Text('NU ARGACHUUF:',
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            const SizedBox(height: 10),

            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                  color: Colors.grey[100],
                  borderRadius: BorderRadius.circular(8)),
              child: Column(
                children: [
                  ListTile(
                    leading: const Icon(Icons.telegram, color: Colors.blue),
                    title: const Text('Telegram'),
                    subtitle: Text('@$telegramUsername'),
                    onTap: () => _openTelegram(context),
                    trailing: const Icon(Icons.open_in_new, size: 16),
                  ),
                  const Divider(height: 1),
                  ListTile(
                    leading: const Icon(Icons.phone, color: Colors.green),
                    title: const Text('Lakkofsa Bilbilaa'),
                    subtitle: Text(phoneNumber),
                    onTap: () => _makePhoneCall(context),
                    trailing: const Icon(Icons.phone_in_talk, size: 16),
                  ),
                  const Divider(height: 1),
                  ListTile(
                    leading: const Icon(Icons.email, color: Colors.red),
                    title: const Text('Email'),
                    subtitle: Text(emailAddress),
                    onTap: () => _sendEmail(context),
                    trailing: const Icon(Icons.arrow_forward, size: 16),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
