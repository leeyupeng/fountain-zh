:warning: 该项目已暂停维护
===
欢迎使用最新的开源项目 in剧本 https://github.com/injuben/injuben

---

用 Fountain 写作中文电影剧本
===

**Fountain** https://fountain.io 是一款开源的剧本写作框架，由电影 <**Big Fish**>(大鱼)的编剧 John August 等人设计开发，可基于纯文本编辑并导出[美国电影工业"事实标准"格式](https://www.oscars.org/nicholl/screenwriting-resources)的剧本。目前已有[多款第三方软件和语法高亮插件](https://fountain.io/apps)。本文将具体关注如何在Mac平台使用 **Fountain** 及相关软件进行**中文电影剧本写作**。

# 操作系统

本文所涉及到的导出软件目前仅支持 Mac 平台，因此下文中的主要内容只适用于 macOS X。

# 详细介绍

## 快速一览

以下两个文件可以为大家提供对 **Fountain** 快速直观的认识。

- [小城之春.fountain](./小城之春.fountain)，**Fountain** 源文件，纯文本格式。内容节选整理自**李天济**先生编剧，**费穆**先生导演的电影《小城之春》(1948)。

- [小城之春.pdf](./小城之春.pdf)，由  **Marked 2** 导出的PDF文件。采用12pt的 STSong 和 PingFangSC 混排。**Marked 2** 具体安装和配置请见下方。

注：PDF 文件建议使用 [Adobe Acrobat Reader DC](https://get.adobe.com/cn/reader/) 打开。

如下所示：左侧是导出的PDF文件，右侧是在编辑软件 **Atom** 中打开的 Fountain 源文件。

![小城之春](https://thumbs.gfycat.com/SpecificAnotherCopperhead-size_restricted.gif)

## 软件选择

### 剧本编辑软件 - Atom

**Atom** 是 GitHub 推出的一款开源的文本编辑软件，有丰富的插件支持。

|软件名称|功能亮点|免费/收费|
|:--:|:--|:--|
|Atom<br />(安装 fountain-zh 插件)|<ul><li>Fountain 语法高亮</li><li>通过拖拽调整场景顺序</li><li>集成 Git 版本管理</li><li>可通过 Teletype 进行协同编辑<ul>|开源免费|

Fountain 源文件是纯文本格式，可以使用任意其他纯文本编辑器进行编辑，包括能在不同设备之间同步的云编辑软件等，在此就不再赘述。

### 剧本导出软件 - Marked 2

**Marked 2** 是一款预览软件，专注预览及导出功能。

通过自定义导出样式和预处理脚本能够较好的处理中文字体及排版。推荐购买。

|软件名称|导出主要格式支持|功能亮点|免费/收费|
|:--:|:--|:--|:--|
|Marked 2|<ul><li>pdf </li><li>docx</li><li>html</li></ul>|<ul><li>CSS 自定义导出样式</li><li>支持预处理脚本</li><ul>|免费版：试用7天 <br /> 收费版：功能与免费版相同|

## 软件安装及配置

以下安装和配置过程预计需要10分钟（不含下载时间）。

### Atom

#### 安装及配置

1. Aom 官网 https://atom.io 下载解压并拖至Applications（应用程序），启动
1. 选择菜单 `Atom -> Preferences`
1. 点击 `Core`
1. 取消勾选 `Open Empty Editor On Start`
1. 下拉选项 `Restore Previous Windows On Start` 更改为 `always`
1. 点击 `Editor`
1. 在 `FontFamily` 选项中最前端输入 **STSong,** (注意有逗号)
1. 在 `FontSize` 选项中输入 **16**
1. 选择菜单 `Packages -> Settings View -> Manage Packages`
1. 输入  **wrap-guid** 并搜索
1. 点击 `wrap-guid`的`Disable` 按钮禁用 `wrap-guid`
1. 输入 **autosave** 并搜索
1. 点击 `autosave` 的 `Settings` 按钮，勾选 `Enabled` 启用 `autosave`
1. 选择菜单 `Packages -> Settings View -> Install Packages/Themes`
1. 输入 **soft-wrap-indicator** 搜索并安装
1. 输入 **fountain-zh** 搜索并安装
1. 点击 `fountain-zh` 的 `Settings` 按钮
1. 在 `Preferred Line Length` 选项中输入 **73**

#### 测试 Atom

1. 下载文件 [你好-Fountain.fountain](./你好-Fountain.fountain) (打开链接后点击 `raw` ，使用浏览器另存或快捷键 Command+S 保存即可)
1. 选择 Atom 的菜单 `File -> Open`, 打开文件 `你好-Fountain.fountain`
1. 反复点击底部状态栏的 `Wrap` 按钮可启用/禁用自动换行
1. 选择菜单 `Packages -> Fountain -> 显示/隐藏 大纲视图`，或使用快捷键 Ctrl+Alt+O
1. 在`场景及大纲`视图内点击 `场景` 按钮使其高亮，将显示剧本中所用到的场景列表，可通过双击场景名称定位剧本中的位置
1. 在`场景及大纲`视图内点击 `可拖拽` 按钮使其高亮，即可通过拖拽场景标题调整场景标题及场景相关内容的顺序

### Marked 2

#### 安装及配置

1. 下载预处理脚本 [fountain_zh.py](./fountain_zh.py)
1. Marked 2 官网 http://marked2app.com 下载、安装并启动
1. 选择菜单 `Marked 2 -> Preferences` 打开选项面板
1. 选择面板的 `Advance` 选项， 选择`PreProcessor`，勾选 `Enable Custom Preprocessor`
1. 在 `Path:` 中输入 **/usr/bin/python**
1. 在 `Args:` 中输入预处理脚本 fountain_zh.py 在本机的绝对路径，如： **/Users/fountain/Downloads/fountain_zh.py** （注：在 Finder 里选中 fountain_zh.py ，按快捷键 Option+Command+C 即可拷贝到文件的绝对路径，再粘贴到 `Args:` 中即可）
1. 勾选 `Automatically enable for new windows`
1. 点击按钮 `Update Permissions` -> `Ok, let's do it` -> `OK`
1. 选择面板的 `Export` 选项，取消勾选 `Custom font size for export/print`
1. 选择面板的 `Style` 选项，点击 `Additional CSS:` 旁边的按钮 `Edit CSS`
1. 拷贝粘贴下方的CSS代码，完成后点击 `Done`，并关闭选项面板

```css
body {
color: #000000;
}

section > p, #script-title > p {
font-family: STSong, SimSun;
font-size: 12pt;
line-height: 1.5em;
}

#wrapper p {
word-break: break-all !important;
}

#script-title > p.title, p.contact, p.draft.date, .character, .scene-heading, .transition, .lyrics, strong, .center {
font-family: PingFangSC-Light, PingFangTC-Light, SimHei, sans-serif;
}

aside.contactinfo {
width: 100%;
float: right;
text-align: right;
}

aside.contactinfo > p.draft.date, aside.contactinfo > p.contact {
margin-left: 50%;
margin-bottom: 0;
width: 48%;
float: right;
text-align: left;
display: block;
}

aside.contactinfo > p.draft.contact {
margin-top: 0;
}

.scene-heading, strong {
font-family: PingFangSC-Regular, PingFantTC-Regular, SimHei, sans-serif;
}

.page-break, .scene-number-left, .scene-number-right {
font-family: CourierPrime, Courier, serif;
}

.transition {
color: #101010;
}
```

#### 测试 Marked 2

1. 选择菜单 `File -> Open`, 打开文件 `你好-Fountain.fountain`
1. 选择右下方设置按钮（小齿轮）-> `Use Custom Preprocessor`， 或使用快捷键 Ctrl+Alt+Command+C ,  确保预处理脚本为启用状态（启用后会有一个橙色的小圆形出现在底部右侧，未启用则为灰色，也可点击该小圆形进行切换）
1. 选择菜单 `File -> Export As -> Save PDF (Paginated)` 即可导出文件

注：每次打开一个新文件时，请确保预处理脚本为启用状态再导出。

##  Fountain 语法

### 快速入门

本节将通过如下一段样例对常用的 Fountain 语法进行介绍。

```fountain

.内景 茶馆 - 清晨

此处可以开始撰写动作及场景描述。

@角色1
此处可以开始撰写角色台词。

```

#### 场景标题

场景标题独占一行，以 点号. 开始，并前后须空一行。如下所示：

```fountain

.内景 茶馆 - 清晨

```


#### 动作/场景描述

动作描述、场景描述等应与场景标题间空一行，后也须空一行。如下所示：

```fountain

.内景 茶馆 - 清晨

此处可以开始撰写动作及场景描述。

```

#### 角色

角色名称以符号 @ 开始。前须空一行。如下所示：

```fountain

@角色1
```

#### 台词

紧跟角色的下一行文字即被视为台词。台词结束后须空一行。如下所示：

```fountain

@角色名称
此处可以开始撰写角色台词。

```

### 更多 Fountain 语法

关于 Fountain 语法的中文介绍请参考 [Fountain 语法中文集](FOUNTAIN_ZH.md)

## 软件使用示例

### 移动场景及大纲视图

鼠标拖拽视图即可移动。

![移动场景及大纲视图](https://thumbs.gfycat.com/KindlyInsistentHarrierhawk-size_restricted.gif)

### 定位场景

双击场景标题名称即可快速定位。

![定位场景](https://thumbs.gfycat.com/LightheartedNimbleDanishswedishfarmdog-size_restricted.gif)

### 调整场景顺序

用鼠标拖拽场景标题即可调整场景顺序。

![调整场景顺序](https://thumbs.gfycat.com/RigidSpicyAustrianpinscher-size_restricted.gif)

### 使用大纲及调整大纲顺序

大纲也可使用鼠标拖拽进行顺序调整。

![使用大纲](https://thumbs.gfycat.com/DenseNaiveKestrel-size_restricted.gif)


### 快速查找场景

快捷键 Command+R 可快速查找场景。

![快速查找场景](https://thumbs.gfycat.com/LightGivingHerald-size_restricted.gif)

### [分屏](https://support.apple.com/zh-cn/HT204948)工作模式

可选择在写作后期做文字调整时使用。如下所示，每次保存右边 Atom 中的 Fountain 文档时，左侧的 Marked 2 会自动刷新预览。

![分屏](https://thumbs.gfycat.com/DefensiveDisguisedAsiaticmouflon-size_restricted.gif)

### 添加/删除场景序号

如果剧本进入拍摄阶段，需要添加场景序号时，可参考以下步骤：

1. 选择 `Marked 2 -> Preferences` -> `Advance` -> `PreProcessor`
1. 在 `Args:` 中的预处理脚本末尾增加参数 ` -s`，如： **/Users/fountain/Downloads/fountain_zh.py -s**
1. 右键点击文档，选择 `Refresh` 刷新文档即可看到场景编号。反之移除 ` -s`
1. 关闭选项面板，导出文件即可

![场景序号](https://thumbs.gfycat.com/ComposedDecimalAmazonparrot-size_restricted.gif)

# 相关问题

[相关问题列表](./ISSUES.md)

其他问题请提交至 [Issues](https://github.com/leeyupeng/fountain-zh/issues)

# 内容分享
本文以 [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议授权。
