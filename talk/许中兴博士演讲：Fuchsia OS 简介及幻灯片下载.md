许中兴博士在开源开发工具大会 HelloGCC 2018上发表了一个关于 Fuchsia 的精彩演讲,在征得本人同意的情况下，Fuchsia OS 中文社区将原幻灯片稍作整理，发表于社区网站，希望可以帮助更多正在学习 Fuchsia 系统的朋友，在此先感谢中兴博士的付出和支持，这里是是 [GitHub 地址](https://github.com/xuzhongxing/)，欢迎关注。

 - 本演讲的 PDF 下载地址是：[https://xuzhongxing.github.io/201806fuchsia.pdf](https://xuzhongxing.github.io/201806fuchsia.pdf) 
 - Fuchsia 中文社区备份下载：[https://fuchsia-china.com/dl/201806fuchsia.pdf](https://fuchsia-china.com/dl/201806fuchsia.pdf)
以下为演讲内容整理：
***

# Fuchsia的来历
 - 多年的Android, ChromeOS开发经验⼀⽅⾯让Google在操作系统⽅⾯积累了⾜够多的⼈才和组件，另⼀⽅⾯也充分认识到了Linux kernel很多的局限性
 - Fuchsia是⼀个全新的操作系统的统称。Google挑选了⼀系列它认为合适的技术和组件进⼊这个操作系统，⽐如：微内核，基于能⼒的访问控制，Vulkan图形接⼝，3D桌⾯渲染Scenic，Flutter应⽤开发框架。⽬前⽀持的编程语⾔是：C/C++, Go, Rust, Dart
 - Google2016年中放出了所有的代码，但是没有正式宣布这个项⽬的⽬标，开发社区⽬前有⼀个IRC频道进⾏交流
 - ⽀持的架构是X86-64和ARM 64，⽀持的设备从IoT到服务器

# 现代通⽤、开放OS需要⾯对的⽅⾯
 - 上游硬件⼚商
 - 下游应⽤开发者
 - 设备友商
 - ⽤户
 - ⿊客

# Fuchsia解决现代OS痛点
 - 原⽣进程沙箱，解决应⽤安全和分发问题（⿊客）
   - Linux: namespace, control group, unionfs => docker
 - 稳定的驱动接⼝，硬件⼚商可独⽴维护硬件驱动（硬件）
 - 系统模块化，分层，设备⼚商可以灵活定制专有系统（友商）
 - 基于Vulkan和物理渲染的纯3D UI，全局光照（⽤户）
 - Flutter应⽤开发框架（开发者）

# 关于进程沙箱，Fuchsia重新思考三个Unix的基础抽象机制
- 全局⽂件系统
- ⽤户
- 进程的创建

# 全局⽂件系统
 - 在Unix⾥，存在⼀个全局的根⽂件系统
  - 它是每个进程共享的基础资源
  - ⽂件系统涵盖了⾮⽂件资源：/proc, /sys, ..
  - ⽹络是例外
 - 在Fuchsia⾥，没有全局根⽂件系统
  - ⽂件和⽂件系统成为⼀个局部概念（局限在每个⽂件系统进程⾥），从⽽在进程内核数据结构⾥
没有file
  - ⽤namespace来定义⼀个进程能够访问的资源
   - 每个name（路径）对应⼀个资源进程channel 的handle
  - “/“ -> root vfs service handle, “/dev” -> dev fs service handle, “/net/dns” -> DNS service handle

# User
 - 在Unix中，user本来是⽤作不同的⽤户登录共享服务器的机制
  - user是真正的⽤户
  - 后来主要⽤作权限控制，弱化的沙箱机制
 - 在Fuchsia中，在底层(Zircon, Garnet)没有⽤户的概念
  - ⽤namespace来控制进程能够访问的资源
  - Capability-based access control
  - 从⽽在进程⾥没有uid

# 进程的创建
 - 在Unix中，新的进程由⽼的进程fork⽽来
  - 新的进程继承⽗进程的全部资源
  - ⼀种偷懒的设计
 - 在Fuchsia中，新进程的创建需要从头开始
  - 创建process, thread
  - ⽗进程建⽴初始的namespace到资源channel handle的映射
  - 调⽤process_start显式的告诉内核新的进程可以跑了
 - 在Fuchsia内核的process数据结构⾥，没有file和uid

# 仿佛是专⻔针对漏洞利⽤作出的设计
 - 典型的漏洞利⽤步骤
  - fork()/exec()开反向shell
  - 继承uid(或者通过获得root uid进⾏提权)获得泛在授权
  - 访问全局⽂件系统
 - 在Fuchsia⾥，以上机制全都不存在
  - 创建进程时显式建⽴root namespace
  - 没有user，从⽽没有ambient authority (DAC/MAC)
  - Capability-based access control
   - 能访问的资源是⽗进程赋予的namespace
   - 看不到初始namespace之外的任何资源

# 微内核
 - Linus vs Tanenbaum的论战
  - Tanenbaum: Linux是七⼗年代的技术。在1991年写宏内核是错误的。争论早就结束了，微内核已经赢了。我是教授，Minix只是我的hobby，所以别拿Minix说事。
  - Linus: Linux⽐你写的Minix强多了。微内核只是你们学术界的玩具，我看过所有的关于微内核效率优化的论⽂，它们实际上只是在重复宏内核早就⽤过的技巧
 - Mach, Hurd
  - Performance overhead
  - Context switching (user space <=> kernel space)
 - Thread scheduling

![](https://fuchsia-china.com/wp-content/uploads/2019/01/img10.png)
![](https://fuchsia-china.com/wp-content/uploads/2019/01/img12.png)
	
# 世界需要新的操作系统
 - Windows⽼迈⻰钟，历史负担太重，微软⾃⼰的创新Midori胎死腹中，因为⽆法承受在新的框架中重新实现⼀遍Windows的全部功能，只能在原地进⾏重构
 - Linux只关⼼服务器的世界，就像⼀个专注于在甲板下⾯锅炉房⾥⼲活的锅炉⼯，上不得桌
 - MacOS, iOS封闭在苹果的硬件⽣态⾥
 - Android为了弥补Linux的缺点打上了⼀个厚厚的中间层，不断在做着妥协
 - GNU Hurd作为GNU项⽬“最后的组件”⼀直未能产品化，原因是“微内核消息传递机制debug太困难”？
 - Unix的后继者Plan 9于2002年发布了最后⼀个版本，它的余热随着作者融⼊了Go

# Fuchsia在各个平台上的可能的优势
 - 在服务器平台上，原⽣的进程沙箱机制将带来新的安全特性和容器机制
 - 在桌⾯平台上，类似于游戏3D引擎pipeline的图形栈以及毫⽆遗产负担的实现将使电⼦娱乐应⽤变得更为⾼效；⽆缝兼容庞⼤的Android⽣态
 - 在移动平台上，系统的模块化⽅便第三⽅设备⼚商的全⾯
定制，驱动框架⽅便硬件⼚商编写和维护私有驱动

![](https://fuchsia-china.com/wp-content/uploads/2019/01/img17.png)

# Fuchsia分层
 - Fuchsia是⼀个像Lego玩具⼀样组装起来的操作系统
  - ⾕歌在设计时已经考虑了其他⼚商可能会深度定制适配⾃⼰产品的操作系统，所以模块化做得⽐Android彻底很多
  - ⼚商的深度定制可以从以下任意⼀层开始
 - Zircon: 微内核，基础服务进程（设备管理器，核⼼设备驱动，libc, 进程间通信接⼝库fidl)
 - Garnet: 设备层⾯的系统服务：软件安装，通信，媒体，图形，包管理，更新系统等
 - Peridot: ⽤户体验的基础设施层：模块，⽤户，存储服务，等等
 - Topaz: 系统的基础应⽤，Web, Dart, Flutter
 - 这些名字来⾃于Steven Universe

# Fuchsia启动流程
![Fuchsia启动流程](https://fuchsia-china.com/wp-content/uploads/2019/01/img19.png)
![](https://fuchsia-china.com/wp-content/uploads/2019/01/img20.png)
# 第⼀个⽤户态进程的创建
 - 之前的微内核⼀般需要实现⼀个基本的⽂件系统加载功能在内核⾥，然后加载第⼀个⽤户进程⽂件，之后就不再使⽤内核⾥的⽂件系统功能
 - Zircon把第⼀个⽤户态进程的ELF⽂件嵌⼊进内核映像⾥，
这样就不需要从⽂件系统⾥加载了。

# 系统调⽤vDSO
 - 内核映像还嵌⼊了⼀个vDSO，包含了系统调⽤⼊⼝
 - 这个vDSO被映射到每个进程的内存地址空间⾥
 - 它本身是ELF shared object⽂件格式，但是⼜不是以⽂件形态存在，所以叫做vDSO
 - Linux kernel也⽤这种⽅式实现了⼀些简单的系统调⽤，⽐如getdaytime()。但是Zircon并不是为了避免切换内核态，⽽是把系统调⽤的代码嵌⼊到了内核⾥。

# 内核态功能
 - 虚拟内存和物理内存管理
  - vmo: virtual memory object: 包含物理⻚
 - 进程和线程管理
  - Handle指向内核中的各种对象
 - 进程间通信
  - channel
  - MessagePack
  - signal and wait
 - 中断处理
  - 唤醒等待该中断的⽤户线程
 - 没有POSIX⽀持

# Zircon⽤户态
- devmgr, devhost, svchost, fshost
- appmgr
- sysmgr
- Fuchsia定义了⼀套稳定的DDK接⼝，硬件⼚商开发⾃⼰的闭源驱动的⽅便性⼤⼤提⾼了。因为Linux kernel是拒绝提供稳定的内核内部驱动接⼝的。要想被官⽅维护，就得放进内核⾥，否则只能⾃⼰跟着内核去改接⼝。
- 内核不提供POSIX⽀持，⽤户层可以模拟⼀部分POSIX接⼝

# channel
 - channel是进程间通信的（唯⼀）机制
 - ⼀个channel有2个handle，h1, h2，从⼀头写⼊消息，从另⼀头读出消息
 - ⼀个进程在创建时有⼀些初始channel handle
 - 要与⼀个服务x建⽴通信，进程创建⼀个channel，⾃⼰拿h1，把h2通过已有的channel (root_svc) 发送给相应的服务，服务拿到h2，将其放到⾃⼰的事件监听循环⾥
  - 示意api：connectToService(root_svc, “x”, h2)
  - ⽐如open()，在linux⾥会在进程的内核数据结构⾥增加打开的⽂件描述符，不涉及到其他进程；在fuchsia⾥则是创建⼀个channel, 把远端发送给相应的服务，建⽴通信通道
 - channel_write()把消息写到另⼀个进程能看到的地⽅。进程间是不共享内存地址空间的。只有内核的地址空间是进程共享的。所以channel_write()必须是⼀个系统调⽤，切换到内核地址空间⾥进⾏消息写⼊。⼀旦切换到内核地址空间⾥，就能看到另⼀个handle了。写到那个handle的消息队列⾥，等另外⼀个进程切换到内核地址空间⾥，就能看到消息了。

# channel的实现
![](https://fuchsia-china.com/wp-content/uploads/2019/01/img26.png)

# Kernel Address Space Layout Randomization
 - ELF的加载位置是随机的，并不是遵守ELF program header⾥规定的v_addr
 - 会在加载时对符号地址进⾏修正

# Fuchsia⽬前的运⾏环境
 - Qemu
 - 最⽅便的环境，没有GUI
 - Intel NUC
 - ⽬前最好的测试环境，有GUI
 - Vim2 dev board
 - 学习ARM64架构，等⾕歌开放出GPU驱动和Bootloader

# Qemu
 - 在Qemu中可以直接运⾏
  - booloader加载到0x40080000
  - 内核加载到0x40090000
  - ramdisk加载到0x48000000
  - 0x40000000-0x40080000之间是FDT flattened device tree

# Intel NUC
 - 开发机启动paving服务，会将整个Fuchsia操作系统刷到NUC上。
 - 启动zircon到zedboot模式，会直接连接开发机

# Khadas Vim2开发板
 - Amlogic S912 SoC
 - Quad Core A53
 - Mali-T450MP5 GPU
 - 3G DDR4
 - 64G eMMC storage
 - HDMI, USB-C, USB 2.0, TF Card, Ethernet, WiFi,Bluetooth

# Vim2的启动
 - Arm Trusted Firmware:
 - BL1 in ROM
 - Custom u-boot: BL2 + BL30 +BL31 + BL32 + u-boot(BL33)
 - 其中bl2,bl30,bl31,bl32都是amlogic提供的binary
 - bl33从emmc offset 0x50200处开始，加载到内存16MB处执⾏。
 - 使⽤fastboot协议可以⽤usb-c将zircon kernel写⼊boot分区
 - 需要⼀个适合zircon的bootloader来启动zircon，但是Google尚未放出
 - 所以还不能启动zircon

# 系统软件研发能⼒的获得
 - 系统软件与应⽤软件不同
  - 有⼤量的缄默知识，⻓期积累的know-how
  - ⼯具链：gcc, ld, as, clang, ELF,
  - 微处理器：X86, ARM,
  - 周边设备：UEFI, ACPI, APIC, PCIE, USB, SATA, AHCI, GPU …
  - 知识存在于代码中，没有系统化的know-how⽂档，硬件标准⽂档⼀般都是1000+⻚
  - 写玩具系统容易，产品级的设计⾮常困难：⽀持海量的设备，应⽤，负载
 - 要经过以下四个阶段
  - 模仿
  - 理解
  - 掌握
  - 创新

# 总结
 - Fuchsia在安全⽅⾯具有重要的创新
 - 在未来Fuchsia会成为⼀个⾮常重要的操作系统

# ⼀些笔记
 - https://github.com/xuzhongxing/fuchsia-notes

***
许中兴博士的演讲非常精彩，基本上把目前 Fuchsia 的状况做了一个全面性的介绍，欢迎大家关注中兴博士的 GitHub，同时 Fuchsia OS 中文社区接下来也会根据中兴笔记推出 Fuchsia 内核笔记，敬请期待。
