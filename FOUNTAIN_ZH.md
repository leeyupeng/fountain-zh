Fountain 语法中文集
===

# 简介

本文涉及到的 Fountain 语法为官方语法的子集，力求使用较少的语法来使用 Fountain 写作中文电影剧本。

#  模板文件

本文涉及到的 Fountain 语法在 [模板.fountain](./模板.fountain) 均有示例。

# 语法详情

## 剧本封面（Title Page）
由以下几行内容组成，其中英文及英文冒号部分是 Fountain 语法的关键词，不可更换。

- `Title: ` 剧本名称。
- `Credit:` 原著（如漫画，小说等）作者或相关贡献者等。无可留空
- `Author:` 作者。多名作者可用 逗号, 分割
- `Source:` 故事来源。该项可省略
- `Draft date:` 日期。该项可省略
- `Contact:` 联系信息。如电话、电子邮箱、地址等。可分多行输入。该项可省略

剧本封面内容结束后须空两行，导出文件后封面即可独占一页。如下所示：

```fountain
Title: 你好 Fountain
Credit:
Author: 某某某
Source: 根据真实故事改编
Draft date: 2018年X月
Contact:
地址：X市X路X号
电话：139-xxxx-xxxx
邮箱：xxx@yyy.com


```

## 场景标题（Scene Headings）

独占一行，以 点号. 开始，前后须空一行。地点和时间建议以 空格+英文横线+空格 分隔。如下所示：

```fountain

.内景 茶馆 - 清晨

```

## 动作描述（Action, or scene description）

也做场景描述，与场景标题间空一行，结束后须空一行。若有多行描述，之间空一行分隔。如下所示：

```fountain

.内景 茶馆 - 清晨

第一行描述。第一行描述。

第二行描述。第二行描述。

```

## 角色（Character）

以符号 @ 开始，前须空一行。如下所示：

```fountain

@角色1
```

## 台词（Dialogue）

紧跟角色名称下一行的文字即为台词。台词结束后须空一行。如下所示：

```fountain

@角色1
角色1的台词。角色1的台词。角色1的台词...

```

## 辅助描述（Parenthetical）

如果整段台词有辅助描述（Parenthetical），如：画外音等，可在角色名称后以 空格+英文括号() 起止。如下所示：

```fountain

@角色1 (画外音)
角色1的台词。角色1的台词。角色1的台词...

```

台词中如有穿插对台词和动作的描述，可在台词部分新起一行并用 英文括号() 起止，再新起一行继续写台词。如下所示：

```fountain

@角色1
角色1的台词。角色1的台词。
(靠近，小声的说)
角色1的台词...

```

## 大纲（Sections and Synopses）

或称作章节及梗概。可用于梳理写作思路和剧本结构，默认不会出现在导出文件中。大纲标题以 井号#+空格 开始，之后是大纲名称，前须空一行。大纲层级由井号数目决定。大纲说明紧跟大纲标题，以 等号=+空格 开始，结束后须空一行。如下所示：

```fountain

# 大纲第一层级
= 大纲说明

## 大纲第二层级
= 大纲说明

### 大纲第三层级
= 大纲说明

```

## 注释（Notes）
用以在写作过程中对剧本内容加以注释说明。以 两个方括号[[]] 起止。如下所示：

```fountain
注释开始[[此处为对剧本内容的注释，将不会出现在最终的导出文件中。]]注释结束。
```

## 歌词（Lyrics）
以 波浪字符~ 开始，首行前及末行后须空一行。如下所示：

```fountain

~啊多么辉煌
~那灿烂的阳光

```

也可考虑用做画面中出现的文字说明，如信件、通知内容等。如下所示：

```fountain

~请于今晚6点参加在茶馆的演出。
~谢谢。

```

## 强调文字（Emphasis）

具体如下。

- 下划线文字。以 下划线 起止。 如下所示：

```fountain
 _下划线_
 ```

- 粗体文字。以 两个星号 起止。 如下所示：

```fountain
 **粗体文字**
 ```

- 组合格式。如下所示：

```fountain
 _**下划线粗体文字**_
```

## 居中文字（Centered Text）

用 大于号小于号>< 起止，前后须空一行。如下所示：

```fountain

>完<

```

## 转场（Transition）

以 大于号+空格 开始，并前后须空一行。建议仅在非常必要的情况下使用转场，如：强调戏剧冲突或时间流逝等。如下所示：

```

> 叠化

```

# 其他语法格式

以上列出的即为全部的 Fountain 语法中文集。由于涉及到中文排版格式调整、相关软件及处理插件等原因，暂不建议使用其他官方语法格式，如：以感叹号起始强制声明动作描述、用 井号# 输入场景序号等。

关于如何添加场景序号请点击[查看](./README.md#添加删除场景序号)。

# Fountain 语法中文集 - 中英文对照表

可参考官方链接获得更详细的解释。

|中文|English|官方链接|
|:--:|:--:|:--:|
|剧本封面|Title Page|[Link](https://fountain.io/syntax#section-titlepage)|
|场景标题|Scene Headings|[Link](https://fountain.io/syntax#section-slug)|
|动作描述（或场景描述）|Action, or scene description|[Link](https://fountain.io/syntax#section-action)|
|角色|Character|[Link](https://fountain.io/syntax#section-character)|
|台词|Dialogue|[Link](https://fountain.io/syntax#section-dialogue)|
|辅助描述|Parenthetical|[Link](https://fountain.io/syntax#section-paren)|
|大纲（或章节及梗概）|Sections and Synopses|[Link](https://fountain.io/syntax#section-sections)|
|注释|Notes|[Link](https://fountain.io/syntax#section-notes)|
|歌词，或诗歌|Lyrics|[Link](https://fountain.io/syntax#section-lyrics)|
|强调文字|Emphasis|[Link](https://fountain.io/syntax#section-emphasis)|
|居中文字|Centered Text|[Link](https://fountain.io/syntax#section-centered)|
|转场|Transition|[Link](https://fountain.io/syntax#section-trans)|

# 内容分享
本文以 [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议授权。
