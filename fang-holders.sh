echo Holders: '<b><u>'$(curl https://ftmscan.com/token/0x49894fcc07233957c35462cfc3418ef0cc26129f -s | sed -n 's/.* holders \([^ ]*\).*/\1/p' | sed -n '1p')'</u></b>'
