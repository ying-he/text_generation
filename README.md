# 在线翻译生成新数据集

以NLP问题匹配任务中的经典数据集[quora_duplicate_questions.tsv](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs)为例，使用[有道翻译](http://fanyi.youdao.com/)在线翻译工具，将这一数据集中的文本内容自动翻译为中文，从而生成一个新的中文问题匹配数据集，该数据集含有40万对已标记的成对问题数据，可用于训练中文语义网络。

- quora_duplicate_questions.tsv.zip ：数据文件

- split_data.py ：对原数据文件进行分割，将容量为40 000的数据集切分成202个均含有2000行样本的小数据集文件，生成的数据集储存在路径"./raw/"里

- ydtrans.py ：爬虫实现自动获取有道在线翻译的函数

- ydtransMain.py ：批量处理数据文件与调用实现，生成202个含有已翻译中文问题文本的数据文件，储存在路径"./chinese/"里

- combineTrans.py ：将小数据集文件合并成与原数据文件格式相似的文件

- googletransTest.py ：使用[谷歌翻译](https://translate.google.cn/)工具，通过翻译生成新数据集，这是一个测试demo，该程序中使用了开源项目[googletrans](https://github.com/ssut/py-googletrans)模块

## 结果比较

通过对比两种在线工具的翻译结果，发现在英译中方面，有道翻译的表现比谷歌翻译要更好，以下是几个例子：

**Example 1**

```Which one dissolve in water quikly sugar, salt, methane and carbon di oxide?```

有道翻译结果：

```哪一种能在水中快速溶解糖、盐、甲烷和二氧化二碳?```
    
谷歌翻译结果：

```哪一种溶于水中的糖，盐，甲烷和二氧化碳？```


**Example 2**

```What are some of the best romantic movies in English?```

有道翻译结果：

```英语中最浪漫的电影有哪些?```

谷歌翻译结果：

```什么是英语最好的浪漫电影？```


**Example 3**

```Can I make 50,000 a month by day trading?```

有道翻译结果：

```我可以通过日内交易每月赚5万吗?```

谷歌翻译结果：

```我可以每天交易50,000个月吗？```

## 小结

不难看出，有道翻译的翻译容错性更好，翻译结果也更符合中文语境。

不同的语言在线翻译工具在不同的语言翻译上有不同的优势，在生成所需要的数据时，可以先在小数据集上比较各种工具的翻译表现，从而选择效果最佳的在线翻译工具来生成新数据，如此得到的文本数据质量也会更高。

