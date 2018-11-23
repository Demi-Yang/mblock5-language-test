# mblock5-language-test
Testing for multi-language of mblock projects.  Use python+unittest+HTMLTestRunner

# Introduction
>* FORMAT_RESULT:  待测试的翻译文件，建议每次测试前，手动更新为最新的翻译文件
>* test:  测试脚本，分三个模块 `mscratch` `mblock5` `ext`
>* util:  测试所需的工具函数
>* report:  测试报告的存放目录
>* run_tests.py:  执行测试脚本

# Usage
测试单个模块的单语种测试，如测试 `mblock5` 模块的 `德语` 翻译，执行以下命令：
<br/>
```
python .\test\mblock5\mblock5_test.py de
```
<br/><br/>
测试全部模块的单语种测试，如测试所有的 `德语` 翻译，执行以下命令：
<br/>
```
python run_tests.py de
```
<br/><br/>
测试全部模块的全部语种测试，执行以下命令：
<br/>
```
python run_tests.py all
```
