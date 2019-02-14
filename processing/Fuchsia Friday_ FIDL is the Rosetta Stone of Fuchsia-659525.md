#Fuchsia Friday: FIDL is the Rosetta Stone of Fuchsia
![](https://i2.wp.com/9to5google.com/wp-content/uploads/sites/4/2018/05/fuchsia-friday-fidl.png)

With all the developer excitement following Google I/O this week, we’re keeping in theme with a developer-oriented Fuchsia Friday.

The modern programmer usually has more than one programming language under their belt, with each one bringing its own unique strengths to the challenge at hand. This isn’t always the case, with some developers taking one language they know (usually Javascript) and throwing it at every problem known to man. Or worse, sometimes the platform or OS itself restricts the languages one can use.

Wherever you may fall in the programming knowledge spectrum, Fuchsia wants to accommodate you, instead of dictating how you are supposed to get the job done. To do this, the Fuchsia Team has created FIDL. FIDL works in two parts, the Fuchsia Interface Definition Language itself, and an underlying system that connects the various languages together.

As of now, FIDL supports 5 languages, with more likely coming in the future
* Dart – A language created by Google that should make Java and Javascript devs feel at home. Also the primary language for Flutter.
* Go – Another Google language, primarily used in web servers
* C++ / C – Two trusty languages, especially useful for low-level programming
* Rust – Mozilla’s relatively successful attempt at a replacement for C++

Let’s say you write a library in Go, but want to use it in a Dart (or Flutter) application. You should be able to use the FIDL language to create an ‘interface’ and connect it to your Go code as an ‘implementation.’ The FIDL system will then generate ‘bindings’ for all supported languages, so you can use your Go code in Dart.

Now perhaps some time has passed, you realized that Go wasn’t really the best tool for the job, and decided to rewrite the library in Rust. With FIDL, you should be able to specify your Rust code as the new implementation. That’s it. You’re done. Your Dart code shouldn’t change, because the FIDL interface didn’t change. That’s the simplified version, anyway.

Interestingly, the FIDL system is in such common use in Fuchsia development that the Fuchsia Team has even developed an extension for VS Code to assist in writing better FIDL code.

If you’re interested in learning more about FIDL and how to use it, check out the official tutorial in the Fuchsia documentation. On that page, you can find simple examples of calling C++ code from Dart and vice versa.

***
本文由[Fuchsia OS 中文社区出品](https://fuchsia-china.com)翻译出品               
原作者：Kyle Bradshaw； 译者：（替换为译者名字和作者地址）；校对： （替换为译者名字和作者地址）       
原文链接：https://9to5google.com/2018/05/11/fuchsia-friday-fidl-is-the-rosetta-stone-of-fuchsia/       
本文链接：https://fuchsia-china.com/×××（发布后替换）
