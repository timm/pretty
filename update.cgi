#!/bin/bash

cat <<EOF
Content-Type: text/html;

<html>
  <head>
    <title>updating</title>
  </head>"
  <body>
    <p>
      $(date)
    </p>
    <pre>
      
      $(git pull origin master)
    </pre>
  </body>
</html>
EOF
[ -f "index.cgi"  ] && chmod 755 index.cgi
[ -f "update.cgi" ] && chmod 755 update.cgi
