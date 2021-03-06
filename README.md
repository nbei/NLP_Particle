# NLP 第一次大作业

​	此次作业主要是来完成对分词任务的几种重要的方法的理解与运用，其中最基本的就有基于训练字典的传统的模式匹配方式，以及使用统计方法的CRF++工具的训练模型。在本次作业中，笔者实现了两种分词方法，并对两种方法的一些实验结果做了一定的分析。

​	下面，将分别介绍模式匹配方法与CRF++两种方法，然后再对两者进行一下比较与分析。同时在本文的最后会有代码的详细使用方法，以便助教以及其他人评测的时候能够方便使用。

### 模式匹配方法

​	首先模式匹配方法的思想非常简单，就是通过训练数据集，形成一个非常大的字典，然后就可以通过搜索字典中是否存在对应的词来进行分词。模式匹配方法有三种不同的实现方式：正向最长匹配，逆向最长匹配以及双向匹配。当然最后一种双向匹配就是前两者里面取最优的结果，对于前两者来说，往往逆向最长匹配能够获得较好的结果。

​	在代码文件中，`prob1_worddic.py`文件里面是笔者得到训练数据字典的源代码，这里为了后面搜索遍历，笔者使用了一点小trick，在将字典存储的时候，将不同长度的字典归为一类，对于特别长的词（超过一定阈值的长度的词）就单独划分为一类，这样在后续的从字典中选词的时候就会方便和快速许多。由`prob1_worddic.py`文件生成的字典已经被存储在了`train_word_dic.npy`中，使用的时候只需要用`numpy`中的对应加载函数加载即可。

​	对于正向最长匹配和逆向最长匹配来说，他们的基本思想都是非常一致的，可以说是一种贪心的算法，想要找到这个句子中最长的能够匹配的单词，只不过是一个从句子的开头开始寻找，后者是从句子的尾部开始。大量的实验证明，后向匹配算法大部分时候都会优于前向匹配算法。而对于双向匹配算法，则是在正向最长匹配算法和逆向最长匹配算法的结果中选取一个分出来的词数最少的算法。

​	在` prob1_1.0.py`中，同时实现了三种算法，并且分别将三种算法的结果输出到了对应的`txt`文件中，之后我们使用`icwb2`里面自带的`score`脚本来实现对结果的评分，这里要说明一点的是，助教大大给的help文档可能是有点错误的，笔者是在看了`icwb2`里面的`README`文档才知道了对于`score`脚本的真正的用法，注意`score`脚本需要你提供你训练时使用的字典，这个字典是那种一般的字典。在`res_score`里面存放了用模式匹配法得到的3种方法在测试集上的结果，同时还有对应的`score`脚本生成的`txt`文件。

​	对于前向匹配与后向匹配算法的结果，在`analyse_back_forward.py`文件中，笔者编写了处理比较两者的几个重要参数的程序，其中重点比较的是两者的**recall**与**precise**，以及比较两者结果的单词的数目。其python脚本生成的结果如下所示：

```basic
------------------------FINAL REPORT : ------------------------
backward_recall_mean : 0.841544    forward_recall_mean : 0.841581 
backward_precise_mean : 0.895310   forward_precise_mean : 0.894899 
backward_res_length < forward_res_length : 26
```

**对于结果分析：**

​	首先不难发现，其实在这种小样本集上，两者的*recall*和*precise*没有太大的差别，而且即使是在大的样本集上，目前而言也是从实验的观察上来讲逆向匹配算法要更加优秀一些。当然，在实际应用中，更加稳妥的方式是使用双向匹配的方式，来寻找到最佳的分词结果。但是从分出来的词的数目上来看，确实逆向匹配算法的效果要更加优秀。

### 统计方法——CRF

​	CRF方法是通过训练模板，然后生成基于统计方法的分词模型，实现分词任务的一种基本方法，而且目前也有大量的开源程序包提供CRF模型的应用，这里助教推荐使用的是CRF++开源程序包。这个程序包目前网上已经有大量的教程，这里笔者就做了一个非常简单的基于CRF++的在ICWB2上的一个尝试。至于CRF++的配置，以及具体是怎么得到的最后的CRF的model和测试集上的结果，在最后的README以及`README.md`文件中均有详细的说明，这里就不再赘述了。

**使用某个字在词中的位置特征——4Tag**

​	基于4Tag的测试模型已经放在了`./crf++/4.model`，测试集的结果已经放在了`./crf++/4.test.rst`，但是由于要使用`icwb2`的脚本进行评分，所以还需要对`4.test.rst`用`prob2_tidyres.py`脚本进行一下处理生成对应的`4.test.score.utf8`。之后，使用`icwb2`的评分脚本，可以得到`./crf++./score_crf.txt`，我们使用`analyse_back_forward.py`文件，对crf++的模型的结果做出一定的整理。

```basic
------------------------FINAL REPORT : ------------------------
backward_recall_mean : 0.841544    forward_recall_mean : 0.841581 
backward_precise_mean : 0.895310   forward_precise_mean : 0.894899 
backward_res_length < forward_res_length : 26
crf_recall_mean : 0.903718         crf_precise_mean : 0.878390
crf_res_length < backward_res_length : 1336
```

​	这里我们不难发现，crf++的4Tag模型做出来的分词结果的`recall`已经比正向最长匹配与逆向最长匹配相比有了明显地提升，但是此模型的`precise`却还是没有很大的提升，甚至只是介于正向最长匹配与逆向最长匹配算法之间。当然，crf模型还有更多的上升空间，比如可以使用6Tag模型去进行分词，以及还可以使用更多的特征来训练model。而且另一个值得关注的地方是，使用crf模型做出的分词结果要比逆向最长匹配算法得到的结果的单词数目还要明显地少，其实这个从`recall`指标上就能够初步推断出来了。综上而言，相比于简单的传统的模式匹配的方法，基于统计模型的方法还是更加优秀。

**4Tag与基于字的频数特征**

​	在使用4Tag的基础上，我们又增加一个数据特征，就是某个字在训练集上出现的频数特征，采用同样的方法得到了如下结果：

```basic
------------------------FINAL REPORT : ------------------------
backward_recall_mean : 0.841544    forward_recall_mean : 0.841581 
backward_precise_mean : 0.895310   forward_precise_mean : 0.894899 
backward_res_length < forward_res_length : 26
crf_recall_mean : 0.903718         crf_precise_mean : 0.877926
crf_res_length < backward_res_length : 1336
crf_4fre_recall_mean : 0.903718         crf_4fre_precise_mean : 0.877926
crf_4fre_res_length < crf_res_length : 1
```

​	可是这里我却惊人地发现，频数特征竟然并没有对于4Tag的方法有什么优化，整体的参数没有太大的变化，只是在某一个句子的分词的长度上有一点差别。思来想去，有可能的情况就是这个数据的数量还是太小了，而且测试数据发现也是大部分跟训练数据非常相像的数据，频数特征在CRF的评判系统中并没有起到非常至关重要的作用。

### 总结

​	这次大作业主要是完成了对于分词中，常用的两种算法的实现以及不同算法的分析，综上来看，基于模式匹配的方法虽然简单易行，但是分词的准确度不尽人意。而对于CRF方法，其有非常大的优化空间，比如采用什么样的特征，以及特征模板的编写等等，这些都是需要去进一步探索的。



## README

### 文件清单：

prob1_worddic.py: 此代码用来得到training里面的字典,然后存入train_word_dic.npy文件之中

prob1_1.0.py: 此代码中实现了模式匹配的三种算法

prob1_words.py: 好像他的score文件的用法需要一个training的words的字典，这个就是来做那个单纯的字典的

prob2_datapre.py: 此代码主要用来将训练数据进行预处理,使其符合CRF++的模式,这里只用训练集的单词的特征,使用的是4Tag模型

prob2_datapre2.0.py: 此代码主要用来将训练数据进行预处理,使其符合CRF++的模式这里使用的是4Tag模型,再加上对应的字在训练集中出现的次数的特征,训练集中某个字出现的次数,可以通过加载train_woards.npy来得到

prob2_testdatapre.py: 此代码主要用来将test数据集做预处理,使其能够被crf++使用

prob2_tidyres.py: 此代码主要用来将test得到的结果进行出来，形成正常的文本

get_tain_words.py: 在使用CRF训练的时候,需要用到不同的特征,这里提供一个字典帮助得到CRF中需要使用的字的频数特征

analyse_back_forward.py: 此文件主要用来对所有的结果进行对比，生成**FINAL REPORT**

**关于使用：**上面的每个文件都可以直接运行，且不需要特别的参数设置，而且在文档中已经有了对这个文件作用的详细描述。

**下面说一下CRF++:**

本实验中所用的crf++是从此[CRF++-0.54.tar.gz](http://sourceforge.net/projects/crfpp/files/crfpp/0.54/CRF%2B%2B-0.54.tar.gz/download)处下载的，下载之后只需要解压然后进入对应目录之后，执行如下命令即可：

```basic
./configure
make
sudo make install
```

注意在最后一步一定要用sudo权限去运行，否则在使用过程中会出现错误。

使用CRF++比较简单，我们需要准备几个文件，一个就是`template`，里面是我们对CRF使用的模板的定义，另一个是`trainfile.utf8`，里面是我们提供的训练样本，注意这里的训练样本与之前的不同，需要人工（代码）标定特征，这样我们就可以通过训练得到对应的model：

```basic
./crf_learn -f 3 -c 4.0 template 4.trainfile.utf8 4.model 
```

最后一个4.model是我们生成的模型，之后我们可以用其去进行test，注意当我们使用更多特征的时候，我们需要对test添加其对应的feature，这部分代码已经放在了`prob2_datapre2.0.py`中，然后可以运行如下命令进行test：

```basic
./crf_test -m 4.model 4.test.data > 4.test.rst 
```

这里要注意的是，其生成的4.test.rst需要我们进一步处理才能够被icwb2使用，这一部分代码已经被放在了`prob2_tidyres.py`里面。