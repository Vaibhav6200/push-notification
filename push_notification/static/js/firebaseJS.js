importScripts("https://www.gstatic.com/firebasejs/8.10.1/firebase-app.js");
importScripts("https://www.gstatic.com/firebasejs/8.10.1/firebase-messaging.js");

const firebaseConfig = {
   apiKey: "AIzaSyCeCIpWKbjq8oRHKRs_AyjVx2QpD1jdAUg",
   authDomain: "notification-2a4ae.firebaseapp.com",
   projectId: "notification-2a4ae",
   storageBucket: "notification-2a4ae.appspot.com",
   messagingSenderId: "195250316189",
   appId: "1:195250316189:web:166b90381e28b0a9d64574",
   measurementId: "G-RH957S0JXD"
};

firebase.initializeApp(firebaseConfig);
const messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(payload=>{
    console.log( "[firebase-messaging-sw.js] Received background message ", payload);
    const notification = JSON.parse(payload);
    const notificationOption = {
        body: notification.body,
        icon: notification.icon
    };
    return self.registration.showNotification(payload.notification.title, notificationOption);
});