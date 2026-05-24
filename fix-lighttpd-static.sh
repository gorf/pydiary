#!/bin/bash
# 修复 gentoogle.com 的 Django admin 静态文件配置
# 在服务器上以 root 执行: bash fix-lighttpd-static.sh

CONF="/etc/lighttpd/lighttpd.conf"
BACKUP="/etc/lighttpd/lighttpd.conf.bak.$(date +%Y%m%d%H%M%S)"

cp "$CONF" "$BACKUP" && echo "已备份到 $BACKUP"

awk '
/^\$HTTP\["host"\] =~ "\^gentoogle\.com/ { in_gentoogle=1; print; next }
in_gentoogle && /^\}/ { in_gentoogle=0 }

in_gentoogle && /"\/admin_media" => "\/usr\/lib\/python2.7\/site-packages\/django\/contrib\/admin\/media"/ {
  print "                \"/static/\" => \"/home/lq/pylogs/static/\","
  print "                \"/media/\"  => \"/home/lq/pylogs/media/\","
  next
}
in_gentoogle && /"\^\(\/admin_media\.\*\)\$" => "\$1"/ { next }
in_gentoogle && /"\^\(\/media\.\*\)\$" => "\$1"/ {
  print "        \"^(/static/.*)$\" => \"\\$1\","
  print "        \"^(/media/.*)$\" => \"\\$1\","
  next
}
{ print }
' "$BACKUP" > "$CONF"

echo "配置已修改，请检查: diff $BACKUP $CONF"
echo ""
echo "然后执行:"
echo "  cd /home/lq/pylogs && python manage.py collectstatic --noinput"
echo "  systemctl reload lighttpd  或  /etc/init.d/lighttpd reload"
