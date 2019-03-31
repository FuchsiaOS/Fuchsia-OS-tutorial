
Fuchsia Friday: How Flutter is paving the way for Fuchsia (and our first Fuchsia app!)
Kyle Bradshaw
- Mar. 2nd 2018 5:29 pm
![](https://i0.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/03/fuchsia-friday-flutter.png)

Earlier this week, Google’s new cross-platform mobile app framework Flutter hit Beta. To celebrate that, let’s take a closer look at what Flutter is doing for app development today, and how it’s preparing developers and users alike for Fuchsia. 
 
Flutter is an open source, cross-platform mobile app development framework. It currently supports iOS and Android development, with potential for desktop support in the future. Flutter sets itself apart from competition like React Native and Xamarin through consistency across platforms.

A Flutter app made using Material Design will look exactly the same on iOS as it does on Android. Additionally, Flutter is powered by Google’s Dart programming language, which should feel familiar to developers of various backgrounds.

If you need a little bit of a debrief on what Flutter is, check out the new Google Developers video that the company just published last week:
![]()
（说明：该视频届时将上传到网站服务器上）

I’ve actually been working with Flutter in my personal time for over a year now, and can say I’ve thoroughly enjoyed it. For sake of demonstration today, I’ve made a special 9to5Google demo app in around half an hour. All it does is provide a list of phones we’ve reviewed, and let you read through the reviews. It’s very simple and it’s more of a mockup than a full app (it uses manually filled in data, for one), but it could easily be turned into something more useful.
![VS Code with Flutter project](https://i0.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/03/screenshot-from-2018-03-02-12-25-36.png)
![An example of the app running on Android](https://i2.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/03/capture_2018-03-02-12-29-53.png)

That’s all fun and games, but you’re probably thinking “Why is this in Fuchsia Friday?” If so, you’re asking the right question. Everything you’ve seen in Fuchsia is powered by Flutter. We first figured this out back in May, with the Armadillo preview that made rounds on Android. Right off the bat, this should tell you a few things.

The first is that Flutter’s widget system is extremely flexible. In addition to the traditional Material Design widgets, and the included “Cupertino” (iOS style) widgets, developers can also create their own custom designed widgets to meet their needs. This ability to design custom widgets is core to many pieces of Fuchsia’s UI, such as the Now feed.

![Now Feed, powered by Flutter – Image: Ars Technica](https://9to5google.com/wp-content/uploads/sites/4/2018/03/google-fuchsia-1-2018-28-1440x1080.jpg)

Secondly, it’s clear that Flutter is not going to disappear or be abandoned any time soon. Google’s betting big on Flutter, as can be seen from its presence at I/O 2017 and another big push coming for I/O 2018. This is a smart move by Google, assuming Fuchsia will be important later. Get developers comfortable with Flutter years before forcing everyone to switch.

There’s another level to this plan, though. As some have noted, one of the hardest things about creating a new operating system is the potential lack of third-party apps. Most people won’t buy a device that doesn’t have good apps, and developers won’t make apps for a device that isn’t selling. What they might not realize, however, is that by making Android & iOS apps with Flutter, they are making ready-to-go Fuchsia apps!

This week, I was able to get Fuchsia up and running on a Pixelbook (Cheers, Ben!). Remember that demo app from earlier? With a simple copy & paste, that app works perfectly on Fuchsia. Here’s what it looks like.

![](https://9to5google.com/wp-content/uploads/sites/4/2018/03/20180302_173431.jpg)

Sure, there will be Fuchsia-specific features that can enrich the experience (check out one example in our breakdown of Entities), but before Fuchsia is even released, there will be hundreds of compatible apps. With this future-minded perspective, it’s easy to get excited for Flutter. If you want to learn more and get a head start on Fuchsia, check out Flutter’s Get Started guide.

Fuchsia Friday is a new series where we dive into the Fuchsia source code and interpret what the current state of the OS might mean for the finished product. All information in this article is speculation based on available information and is subject to change.
***
本文由[Fuchsia OS 中文社区出品](https://fuchsia-china.com)翻译出品               
原作者：Kyle Bradshaw； 译者：（替换为译者名字和作者地址）；校对： （替换为译者名字和作者地址）       
原文链接：https://9to5google.com/2018/03/02/fuchsia-friday-first-fuchsia-app/        
本文链接：https://fuchsia-china.com/×××（发布后替换）
