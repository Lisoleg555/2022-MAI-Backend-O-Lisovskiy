sudo kill $(ps aux | grep nginx | tr -s " " | cut -f 2 -d " ")
