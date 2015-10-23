#!/bin/bash

cat <<-EOF
Content-Type: text/html;

<html>
<head>
<title>file</title>
</head>
<body>
<p>
$(date)
</p>
</body>
</html>
EOF
