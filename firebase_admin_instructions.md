# Firebase Admin Setup Guide for Mezmur App

This guide will walk you through setting up Firebase for your Mezmur app, creating the necessary database structure, and adding your content securely.

## 1. Create and Connect Firebase Project

1. Go to the [Firebase Console](https://console.firebase.google.com/) and create a new project.
2. Once created, you need to connect your Flutter app to this project.
3. Open your terminal in the `mezmur_app` folder and run the Firebase CLI tools:
   ```bash
   # Install Firebase CLI if you haven't already
   npm install -g firebase-tools

   # Login to your Google account
   firebase login

   # Install FlutterFire CLI
   dart pub global activate flutterfire_cli

   # Configure your Flutter app with the Firebase project
   flutterfire configure
   ```
   *(Select your newly created Firebase project and the platforms you want to support - Android/iOS/Web)*.

## 2. Enable Firestore and Storage

1. In the Firebase Console, go to **Build > Firestore Database** and click **Create database**.
2. Start in **Production mode**.
3. Choose a location closest to your users and click **Enable**.
4. Go to **Build > Storage** and click **Get started**. Follow the steps to enable it.

## 3. Configure Security Rules

We need to make sure that anyone can read the Mezmurs and Events, but only authenticated Admins can write or delete them.

### Firestore Rules
Go to **Firestore Database > Rules** and paste this:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    
    // Allow anyone to read data
    match /{document=**} {
      allow read: if true;
    }
    
    // ONLY allow admins to write
    match /mezmurs/{mezmurId} {
      allow write: if request.auth != null; 
    }
    
    match /events/{eventId} {
      allow write: if request.auth != null;
    }
  }
}
```

### Storage Rules
Go to **Storage > Rules** and paste this:

```javascript
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /{allPaths=**} {
      allow read: if true;
      allow write: if request.auth != null;
    }
  }
}
```

## 4. How to Add Mezmurs (Admin Console)

1. Go to **Firestore Database** in the Firebase Console.
2. Click **Start collection**.
3. Collection ID: `mezmurs`
4. Add your first Document:
   - Click **Auto-ID** for the Document ID.
   - Add Field: `title` (Type: string) - Value: e.g., "ARGADHEEN JIRA"
   - Add Field: `language` (Type: string) - Value: e.g., "Oromo"
   - Add Field: `fullText` (Type: string) - Value: *(paste your mezmur lyrics here)*
5. Click **Save**.

## 5. How to Add Events with Photos (Admin Console)

### Step A: Upload Photo
1. Go to **Storage** in the Firebase Console.
2. Create a folder called `events` (optional, but good for organization).
3. Click **Upload file** and select your event photo.
4. Once uploaded, click on the file name. In the right pane, under "File location", look for **Download URL** and click the small link icon to copy it.

### Step B: Create Event Post
1. Go to **Firestore Database**.
2. Click **Start collection** (if `events` doesn't exist yet).
3. Collection ID: `events`
4. Add Document:
   - Click **Auto-ID**.
   - Add Field: `title` (Type: string) - Value: e.g., "Timket Celebration"
   - Add Field: `description` (Type: string) - Value: e.g., "Join us for the annual Timket celebration..."
   - Add Field: `date` (Type: timestamp) - Value: Select the date and time.
   - Add Field: `imageUrl` (Type: string) - Value: *(Paste the Download URL you copied from Storage)*
5. Click **Save**.

That's it! Your app will instantly update and show the new events and mezmurs to all users.
