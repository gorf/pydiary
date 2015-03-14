# 更新日志(CHANGELOG) #

## 2009-6-28 _version: 1.15beta_ ##
  1. 改进rss输出,添加基于settings.py的基本rss输出相关配置项

## 2009-6-19 _version: 1.15beta_ ##
  1. 增加使用markdown标记语言编辑blog post的功能

## 2009-6-14 _version: 1.15beta_ ##
  1. 处理 连接名字段包含空格或中文时,前端点击该链接时出现404错误

## 2009-6-12 _version: 1.15beta_ ##
  1. 处理post减少关联tag后，相关tag reference\_count属性未更新问题
  1. 处理 todo系统中添加的私有project在没有关联task时,非登录用户也能查看 问题

## 2009-3-24 _version: 1.15beta_ ##
  1. 支持手机访问
  1. Bug修复

## 2008-11-19 _version: 1.14beta_ ##
  1. 支持metaWeblog API

## 2008-10-8 _version: 1.14beta_ ##
  1. 程序全部迁移至Django 1.0final
  1. 修正tags页的错误
  1. 修复几处bug

## 2008-08-12 _version: 1.13beta_ ##
  1. 增加Django v1.0alpha支持，修复使用Django v1.0管理界面没有model修改的错误（使用方法见README文件)
  1. i18n完善

## 2008-08-10 _version: 1.13beta_ ##
  1. 修改模板选择结构
  1. 修正几处样式错误
  1. i18n完善

## 2008-08-08 _version: 1.13beta_ ##
  1. 新增奥运主题 beijing2008
  1. 修复几处bug

## 2008-07-26 _version: 1.12beta_ ##
  1. 加入了单元测试
  1. 合并几个tags文件
  1. 加入简单的SEO优化
  1. 修复几处bug,对代码进行优化

## 2008-07-22 _version: 1.12beta_ ##
  1. urls.py中urlpattern使用url()命名，避免拼接url字符串，方便修改url策略

## 2008-07-02 _version: 1.12beta_ ##
  1. 增加“相关文章”功能
  1. 开发tinymce上传管理插件（DFM(v0.1beta)基于django）,方便在发表文章时上传图片及文件
  1. 修复几个bug

## 2008-05-27 _version: 1.11beta_ ##
  1. 修复几个bug
  1. 对代码进行了进一步的整理及优化(多谢dreamingk帮我review code及提出的建议)

## 2008-05-21 _version: 1.11beta_ ##
  1. 修正tag统计错误的bug

## 2008-05-20 _version: 1.11beta_ ##
  1. 代码清理及bug修复
  1. 更新获取归档月份列表的方式[直接sql查询 -> objects.date()]

## 2008-05-10 _version: 1.11beta_ ##
  1. 增加最新文章，最新评论，热门文章等tags
  1. 完善todo的i18n

## 2008-05-05 _version: 1.10beta_ ##
  1. 增加tags页，显示所有的标签，按引用次数显示不同大小


## 2008-04-23 _version: 1.10beta_ ##
  1. Todo功能上线测试，使了强大的jQuery框架
  1. 修正几个小错误


## 2008-04-11 _version: 1.10beta_ ##
  1. 代码高亮使用js的syntaxhighlighter 替代pygments,减少pylogs对python包的依赖
  1. 后台tinymce编辑器添加插入代码功能，配合syntaxhighlighter使用

## 2008-03-21 ##
  1. 集成几个模板为一个模板文件
  1. 修正几个css的问题
  1. 增加查看标签文章列表


## 2008-03-20 _version: 1.10beta_ ##
  1. 增加皮肤支持
  1. 增加了一套新的皮肤 techicon
  1. 管理界面加入tinymce编辑器
  1. 修正几处css问题

## 2008-3-5 _version: 1.01beta_ ##
  1. 评论改为正序排列，方便阅读
  1. 添加发表评论成功提示信息
  1. 修正导入的文章中的\r\n在显示文章时不能正常解析为换行的bug
  1. 修正订阅链接重复编码致使订阅中不能显示图片的bug

## 2008-1-15 ##
  1. 加入“归档”功能
  1. i18n支持
  1. 修复url解析月份时的错误

## 2008-1-13 ##
  1. 加入highslide图片浏览效果
  1. 修复几处小的错误

## 2008-1-12 ##
  1. 成功导入原有wordpress上的数据
  1. 加入代码高亮功能，并且在dreamhost上成功安装Pygments
  1. 修复几处小的错误

## 2008-1-10 _version: 1.0beta_ ##
  1. 美化皮肤，界面更加漂亮了