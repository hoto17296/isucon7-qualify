nginx-reload:
	sudo rm /tmp/nginx-access.log
	sudo systemctl restart nginx

alp:
	cat /tmp/nginx-access.log | alp --aggregates="/icons/.+,/profile/.+,/channel/.+,/history/.+,/(fonts|js|css)/.+" | less -sS
