# Requirements #
  * Python 2.5.2                       http://www.python.org
  * Django v1.1                        http://www.djangoproject.org
  * PIL(Python Imaging Library 1.1.6)  http://www.pythonware.com/products/pil/
  * jQuery 1.2.3                       http://jquery.com

# 安装 #
  1. 请先参考Python及Django安装方法安装好python和django.
  1. 解压pylogs
  1. 进入pylogs解压目录修改settings.py中的数据库类型及连接参数，并设置MEDIA\_ROOT为实际media目录的绝对路径
  1. 运行python manage.py syncdb同步数据库结构

  * 运行manage.py runserver测试服务器是否能运行成功，如出错请根据错误提示修正错误。
  * 如果用到发表评论验证码功能，则需要安装PIL1.1.6。

# 站点参数设置 #
登录后台,在blog app下的"站点设置"表中添加设置项,可用的设置项:
|**设置名称**            |**说明**                                  |
|:---------------------------|:-------------------------------------------|
|SiteName              |站点名称                                |
|SiteSubTitle          |站点副标题                              |
|Theme                 |主题名称                                |
|AuthorName            |作者名称(用于feed中显示author)          |
|SiteKeywords          |站点关键字(对应head中的meta keywords)   |
|SiteDescription       |站点描述(对应head中的meta description)  |

如果你在安装过程中遇到问题，请到http://groups.google.com/group/pylogs 中提出。