# 世界地圖冊版條款數據 2004/02/28 ?故來

# 這個文件是道具數據的定義文件。
# 最好不要變更這個文件。詳細請看手冊。

@@DEFINE
	version	04-02-28(WA)		#★商品數據版本記載
					# 最後的「WA」表現世界地圖冊版。
					# 如果自行製作把獨自道具做為眼珠子的商人故事，
					# 記得變更號碼。

	scale	個			#★默認的數單位
	type0	全			#全道具的集合
	type1	素材
	type2	食物
	type3	調味
	type4	紡織品
	type5	工藝
	type6	船舶
	type7	船隊
	type8	航海
	type9	道具
	
	job	shipb		造船家		#★職業編碼英小字10個字以內
	job	pirate		海盜
	job	pros		海軍司令
	job	explore		探險家
	job	trader		貿易商

	MaxMoney	999999999	#★最大資金
	
	set NewShopMoney	200000					#最初資金 (@@FUNCNEW之使用)
	set NewShopTime		14*60*60				#最初持有時間(以[秒]為單位) (@@FUNCNEW之使用)
	set NewShopItem		陳列棚架工具:1:禮物券:10	#最初持有道具 (@@FUNCNEW之使用) 格式 道具名:數量:道具名:數量:...
	
	TimeEditShowcase	10m		#★展覽陳列棚架操作時間
	TimeShopping		20m		#★進貨時間(舊版SOLD OUT的兼容性確保。現在不使用)
	TimeSendItem		20m		#★道具進貨/移動時間(基本)
	TimeSendItemPlus	20s		#★道具進貨/移動時間(1周的追加時間)
	TimeSendMoney		20m		#★資金移動時間(基本)★2001-06-06追加
	TimeSendMoneyPlus	100000		#★廢物處理時間計算用金額(關於這個金額TimeSendMoney時間之消費)★2001-06-06追加
	
	CostShowcase1		0		#★陳列棚架1個時間維持費
	CostShowcase2		2000	#陳列棚架2個時間維持費
	CostShowcase3		4000	#陳列棚架3個時間維持費
	CostShowcase4		8000	#陳列棚架4個時間維持費
	CostShowcase5		16000	#陳列棚架5個時間維持費
	CostShowcase6		32000	#陳列棚架6個時間維持費
	CostShowcase7		64000	#陳列棚架7個時間維持費
	CostShowcase8		128000	#陳列棚架8個時間維持費
	
	ItemUseTimeRate		1		#★道具使用時時間計算補正倍率(@USE內time,exptime有效)★2001-06-06追加
	
	#★宏定義
	#  這個記述例子，變數 TOWN_TYPE (_config.cgi?$TOWN_TYPE) 的判斷變更時間消費。
	#  sotype1  -> [加工類型] 加工時間收短模式				(MUTOYS的黃玉街)
	#  sotype2  -> [資源類型] 素材集取時間收短模式				(MUTOYS的黃玉郊外)
	#  timehalf -> [先進類型] 全時間收短模式				(MUTOYS的紫晶街)
	#  其他   -> [途中類型] 通常時間模式				(MUTOYS的石榴石街)
	#
	#???設定???????、「@@IF towntype eq material @@USEMACRO_timechange」???使?方????。
	#???、towntype ? material ?場合??、??? _timechange ??行??、以降?時間?短縮????。
	#??? _timenormal ?時間?元?????。(timehalf以外)
	#
	#??仕組??理解??????????知識?必要????思???。
	#上記?明?使用方法?分????場合?、手?付???方?無難??。
	#
	
	set	TOWN_TYPE	$$TOWN_TYPE	#★_config.cgi?指定??街????取得/設定
	@@IF TOWN_TYPE eq timeharf set TOWN_TYPE timehalf # ver.2002-01-01-a ????互換確保
	
	set towntype normal                           # ?? towntype ? normal ?初期化??
	@@IF TOWN_TYPE eq sotype1 set towntype manufac  # TOWN_TYPE ? sotype1 ???? towntype ? manufac ???
	@@IF TOWN_TYPE eq sotype2 set towntype material # TOWN_TYPE ? sotype2 ???? towntype ? material ???
	#???定義
	@@SETMACRO _timenormal "@@DEFINE ItemUseTimeRate 1"
	@@IF TOWN_TYPE eq timehalf @@SETMACRO _timenormal "@@DEFINE ItemUseTimeRate 0.5" # TOWN_TYPE ? timehalf ?場合????定義
	@@IF TOWN_TYPE eq timequarter @@SETMACRO _timenormal "@@DEFINE ItemUseTimeRate 0.25" # TOWN_TYPE ? timequarter ?場合????定義
	@@SETMACRO _timechange "@@DEFINE ItemUseTimeRate 0.75"
	#??? _timenormal ?行
	@@USEMACRO _timenormal

#★以下???書式?街????判定?、?????行???????。
@@IF towntype eq manufac @@USEMACRO_timechange #----------------------------------------------------

@@ITEM
	no		18
	type	航海
	code	bread
	name	方包
	info	航海的必需品
	price	100
	limit	1000/1000
	pop	20m
	plus	20m
	base	100/100000
	scale	食
	cost	20
	point	5%
@@ITEM
	no		19
	type	航海
	code	lamb
	name	羊羔酒
	info	航海的必需品
	price	200
	limit	500/500
	pop	40m
	plus	20m
	base	100/50000
	scale	桶
	cost	20
	point	10%

@@ITEM
	no		20
	type	航海
	code	seaman
	name	水手
	info	使船運作的人手
	price	1200
	limit	800/800
	pop	1d
	plus	20m
	base	10000/100000
	scale	人
	flag	noshowcase|human|norequest

@@ITEM
	no		1
	type	道具
	code	book-bd
	name	造船指導的書
	info	解說造船方法的指導書
	price	10000
	limit	1/0.1
	pop	1d
	plus	2h
	scale	本
	flag	noshowcase
	@@use
		time	120m
		exp		2%
		exptime	40m
		job		造船家	times/1.5
		scale	回
		action	製造
		name	製造小型漢撤式帆船
		info	製造小型漢撤式帆船，只適用於歐洲及非洲
		okmsg	製造了小型漢撤式帆船
			use		1	木材
			use		1	帆布
			get		1	小型漢撤式帆船
	@@use
		time	3h
		exp		2%
		exptime	1h
		scale	回
		action	製造
		name	製造英國雙桅三角帆船
		info	製造英國雙桅三角帆船，只適用於歐洲及非洲及中近東
		okmsg	製造了英國雙桅三角帆船
		ngmsg	製造失敗了…
			needjob	造船家
			needexp	10%
			use		1	木材
			use		1	帆布
			get		1	英國雙桅三角帆船	90%
	@@use
		time	6h
		exp		4%
		exptime	2h
		scale	回
		action	製造
		name	製造巨型槳帆並用船
		info	製造巨型槳帆並用船，只適用於非洲及中近東及印度
		okmsg	製造了巨型槳帆並用船
		ngmsg	製造失敗了…
			needjob	造船家
			needexp	30%
			use		3	木材
			use		1	帆布
			get		1	巨型槳帆並用船	90%
	@@use
		time	12h
		exp		4%
		exptime	4h
		scale	回
		action	製造
		name	製造大型西班牙方形帆船
		info	製造大型西班牙方形帆船，只適用於中近東及印度及亞洲
		okmsg	製造了大型西班牙方形帆船
		ngmsg	製造失敗了…
			needjob	造船家
			needexp	30%
			use		5	木材
			use		3	帆布
			get		1	大型西班牙方形帆船	90%
	@@use
		time	24h
		exp		8%
		exptime	8h
		scale	回
		action	製造
		name	製造大型威尼斯白刃帆船
		info	製造大型威尼斯白刃帆船，只適用於印度及亞洲及新大陸
		okmsg	製造了大型威尼斯白刃帆船
		ngmsg	製造失敗了…
			needjob	造船家
			needexp	50%
			use		10	木材
			use		6	帆布
			get		1	大型威尼斯白刃帆船	90%
	@@use
		time	24h
		exp		8%
		exptime	8h
		scale	回
		action	製造
		name	製造北海多桅橫方帆大船
		info	製造北海多桅橫方帆大船，只適用於亞洲及新大陸
		okmsg	製造了北海多桅橫方帆大船
		ngmsg	製造失敗了…
			needjob	造船家
			needexp	50%
			use		10	木材
			use		6	帆布
			get		1	北海多桅橫方帆大船	90%
	@@use
		time	36h
		exp		10%
		exptime	12h
		scale	回
		action	製造
		name	製造戰列艦
		info	製造戰列艦，只適用於亞洲及新大陸
		okmsg	製造了戰列艦
		ngmsg	製造失敗了…
			needjob	造船家
			needexp	60%
			use		18	木材
			use		7	帆布
			get		1	戰列艦	90%

@@IF towntype eq material @@USEMACRO_timechange #-------------------------------------------------

@@ITEM
	no		26
	type	船隊
	code	convoy-aa
	name	第一探險船隊
	info	面向探險船隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	歐洲的探險派遣
		info	對歐洲的海面區域適應性
		param	26,1
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	非洲的探險派遣
		info	對非洲的海面區域適應性
		param	26,2
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	中近東的探險派遣
		info	對中近東的海面區域適應性
		param	26,3
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	印度的探險派遣
		info	對印度的海面區域適應性
		param	26,4
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	亞洲的探險派遣
		info	對亞洲的海面區域適應性
		param	26,5
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	新大陸的探險派遣
		info	對新大陸的海面區域適應性
		param	26,6
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接探險船隊
		info	確認船隊是不是返回港
		param	26
		funcb	onlyexp
		func	meetexp
		arg	nocount
@@ITEM
	no		27
	type	船隊
	code	convoy-ab
	name	第二探險船隊
	info	面向探險船隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	歐洲的探險派遣
		info	對歐洲的海面區域適應性
		param	27,1
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	非洲的探險派遣
		info	對非洲的海面區域適應性
		param	27,2
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	中近東的探險派遣
		info	對中近東的海面區域適應性
		param	27,3
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	印度的探險派遣
		info	對印度的海面區域適應性
		param	27,4
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	亞洲的探險派遣
		info	對亞洲的海面區域適應性
		param	27,5
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	新大陸的探險派遣
		info	對新大陸的海面區域適應性
		param	27,6
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接探險船隊
		info	確認船隊是不是返回港
		param	27
		funcb	onlyexp
		func	meetexp
		arg	nocount
@@ITEM
	no		28
	type	船隊
	code	convoy-ac
	name	第三探險船隊
	info	面向探險船隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	歐洲的探險派遣
		info	對歐洲的海面區域適應性
		param	28,1
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	非洲的探險派遣
		info	對非洲的海面區域適應性
		param	28,2
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	中近東的探險派遣
		info	對中近東的海面區域適應性
		param	28,3
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	印度的探險派遣
		info	對印度的海面區域適應性
		param	28,4
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	亞洲的探險派遣
		info	對亞洲的海面區域適應性
		param	28,5
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	新大陸的探險派遣
		info	對新大陸的海面區域適應性
		param	28,6
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接探險船隊
		info	確認船隊是不是返回港
		param	28
		funcb	onlyexp
		func	meetexp
		arg	nocount
@@ITEM
	no		29
	type	船隊
	code	convoy-ad
	name	第四探險船隊
	info	面向探險船隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	歐洲的探險派遣
		info	對歐洲的海面區域適應性
		param	29,1
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	非洲的探險派遣
		info	對非洲的海面區域適應性
		param	29,2
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	中近東的探險派遣
		info	對中近東的海面區域適應性
		param	29,3
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	印度的探險派遣
		info	對印度的海面區域適應性
		param	29,4
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	亞洲的探險派遣
		info	對亞洲的海面區域適應性
		param	29,5
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	新大陸的探險派遣
		info	對新大陸的海面區域適應性
		param	29,6
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接探險船隊
		info	確認船隊是不是返回港
		param	29
		funcb	onlyexp
		func	meetexp
		arg	nocount

@@ITEM
	no		30
	type	船隊
	code	convoy-ba
	name	第一貿易船隊
	info	面向貿易船隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	歐洲的貿易派遣
		info	對歐洲的海面區域適應性
		param	30,1
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	非洲的貿易派遣
		info	對非洲的海面區域適應性
		param	30,2
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	中近東的貿易派遣
		info	對中近東的海面區域適應性
		param	30,3
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	印度的貿易派遣
		info	對印度的海面區域適應性
		param	30,4
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	亞洲的貿易派遣
		info	對亞洲的海面區域適應性
		param	30,5
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	新大陸的貿易派遣
		info	對新大陸的海面區域適應性
		param	30,6
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接貿易船隊
		info	確認船隊是不是返回港
		param	30
		funcb	onlyexp
		func	meetrtp
		arg	nocount
@@ITEM
	no		31
	type	船隊
	code	convoy-bb
	name	第二貿易船隊
	info	面向貿易船隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	歐洲的貿易派遣
		info	對歐洲的海面區域適應性
		param	31,1
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	非洲的貿易派遣
		info	對非洲的海面區域適應性
		param	31,2
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	中近東的貿易派遣
		info	對中近東的海面區域適應性
		param	31,3
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	印度的貿易派遣
		info	對印度的海面區域適應性
		param	31,4
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	亞洲的貿易派遣
		info	對亞洲的海面區域適應性
		param	31,5
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	新大陸的貿易派遣
		info	對新大陸的海面區域適應性
		param	31,6
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接貿易船隊
		info	確認船隊是不是返回港
		param	31
		funcb	onlyexp
		func	meetrtp
		arg	nocount
@@ITEM
	no		32
	type	船隊
	code	convoy-bc
	name	第三貿易船隊
	info	面向貿易船隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	歐洲的貿易派遣
		info	對歐洲的海面區域適應性
		param	32,1
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	非洲的貿易派遣
		info	對非洲的海面區域適應性
		param	32,2
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	中近東的貿易派遣
		info	對中近東的海面區域適應性
		param	32,3
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	印度的貿易派遣
		info	對印度的海面區域適應性
		param	32,4
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	亞洲的貿易派遣
		info	對亞洲的海面區域適應性
		param	32,5
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	新大陸的貿易派遣
		info	對新大陸的海面區域適應性
		param	32,6
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接貿易船隊
		info	確認船隊是不是返回港
		param	32
		funcb	onlyexp
		func	meetrtp
		arg	nocount
@@ITEM
	no		33
	type	船隊
	code	convoy-bd
	name	第四貿易船隊
	info	面向貿易船隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	歐洲的貿易派遣
		info	對歐洲的海面區域適應性
		param	33,1
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	非洲的貿易派遣
		info	對非洲的海面區域適應性
		param	33,2
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	中近東的貿易派遣
		info	對中近東的海面區域適應性
		param	33,3
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	印度的貿易派遣
		info	對印度的海面區域適應性
		param	33,4
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	亞洲的貿易派遣
		info	對亞洲的海面區域適應性
		param	33,5
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派遣
		name	新大陸的貿易派遣
		info	對新大陸的海面區域適應性
		param	33,6
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接貿易船隊
		info	確認船隊是不是返回港
		param	33
		funcb	onlyexp
		func	meetrtp
		arg	nocount

@@ITEM
	no		34
	type	船隊
	code	convoy-ca
	name	第一武裝艦隊
	info	面向戰鬥艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	歐洲
		info	對歐洲的海面區域適應性
		param	34,1
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	非洲
		info	對非洲的海面區域適應性
		param	34,2
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	中近東
		info	對中近東的海面區域適應性
		param	34,3
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	印度
		info	對印度的海面區域適應性
		param	34,4
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	亞洲
		info	對亞洲的海面區域適應性
		param	34,5
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	新大陸
		info	對新大陸的海面區域適應性
		param	34,6
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接武裝艦隊
		info	確認艦隊是不是返回港
		param	34
		funcb	onlyexp
		func	meetpp
		arg	nocount
@@ITEM
	no		35
	type	船隊
	code	convoy-cb
	name	第二武裝艦隊
	info	面向戰鬥艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	歐洲
		info	對歐洲的海面區域適應性
		param	35,1
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	非洲
		info	對非洲的海面區域適應性
		param	35,2
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	中近東
		info	對中近東的海面區域適應性
		param	35,3
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	印度
		info	對印度的海面區域適應性性
		param	35,4
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	亞洲
		info	對亞洲的海面區域適應性
		param	35,5
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	新大陸
		info	對新大陸的海面區域適應性
		param	35,6
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接武裝艦隊
		info	確認艦隊是不是返回港
		param	35
		funcb	onlyexp
		func	meetpp
		arg	nocount
@@ITEM
	no		36
	type	船隊
	code	convoy-cc
	name	第三武裝艦隊
	info	面向戰鬥艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	歐洲
		info	對歐洲的海面區域適應性
		param	36,1
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	非洲
		info	對非洲的海面區域適應性
		param	36,2
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	中近東
		info	對中近東的海面區域適應性
		param	36,3
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	印度
		info	對印度的海面區域適應性性
		param	36,4
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	亞洲
		info	對亞洲的海面區域適應性
		param	36,5
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	新大陸
		info	對新大陸的海面區域適應性
		param	36,6
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接武裝艦隊
		info	確認艦隊是不是返回港
		param	36
		funcb	onlyexp
		func	meetpp
		arg	nocount
@@ITEM
	no		37
	type	船隊
	code	convoy-cd
	name	第四武裝艦隊
	info	面向戰鬥艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	歐洲
		info	對歐洲的海面區域適應性
		param	37,1
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	非洲
		info	對非洲的海面區域適應性
		param	37,2
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	中近東
		info	對中近東的海面區域適應性
		param	37,3
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	印度
		info	對印度的海面區域適應性性
		param	37,4
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	亞洲
		info	對亞洲的海面區域適應性
		param	37,5
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	新大陸
		info	對新大陸的海面區域適應性
		param	37,6
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接武裝艦隊
		info	確認艦隊是不是返回港
		param	37
		funcb	onlyexp
		func	meetpp
		arg	nocount

@@USEMACRO_timenormal #-------------------------------------------------------------------------------

@@ITEM
	no		39
	type	航海
	code	discover-a
	name	發現報告書(歐洲)
	info	在探險時發現了新的事物
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	申報
		name	對王國申報
		info	對王國申報發現的新事物
		func	disc
		param	1
		arg	nocount
			use		1	發現報告書(歐洲)
@@ITEM
	no		40
	type	航海
	code	discover-b
	name	發現報告書(非洲)
	info	在探險時發現了新的事物
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	申報
		name	對王國申報
		info	對王國申報發現的新事物
		func	disc
		param	2
		arg	nocount
			use		1	發現報告書(非洲)
@@ITEM
	no		41
	type	航海
	code	discover-c
	name	發現報告書(中近東)
	info	在探險時發現了新的事物
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	申報
		name	對王國申報
		info	對王國申報發現的新事物
		func	disc
		param	3
		arg	nocount
			use		1	發現報告書(中近東)
@@ITEM
	no		42
	type	航海
	code	discover-d
	name	發現報告書(印度)
	info	在探險時發現了新的事物
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	申報
		name	對王國申報
		info	對王國申報發現的新事物
		func	disc
		param	4
		arg	nocount
			use		1	發現報告書(印度)
@@ITEM
	no		43
	type	航海
	code	discover-e
	name	發現報告書(亞洲)
	info	在探險時發現了新的事物
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	申報
		name	對王國申報
		info	對王國申報發現的新事物
		func	disc
		param	5
		arg	nocount
			use		1	發現報告書(亞洲)
@@ITEM
	no		44
	type	航海
	code	discover-f
	name	發現報告書(新大陸)
	info	在探險時發現了新的事物
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	申報
		name	對王國申報
		info	對王國申報發現的新事物
		func	disc
		param	6
		arg	nocount
			use		1	發現報告書(新大陸)

@@ITEM
	no		45
	type	航海
	code	town-a
	name	新城市的地圖(歐洲)
	info	在探險時發現了的貿易城市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	城市的名字
		scale	回
		action	命名建設
		name	建設商行
		info	使命名城市能貿易
		param	1
		func	newtown
			use		1	新城市的地圖(歐洲)
@@ITEM
	no		46
	type	航海
	code	town-b
	name	新城市的地圖(非洲)
	info	在探險時發現了的貿易城市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	城市的名字
		scale	回
		action	命名建設
		name	建設商行
		info	使命名城市能貿易
		param	2
		func	newtown
			use		1	新城市的地圖(非洲)
@@ITEM
	no		47
	type	航海
	code	town-c
	name	新城市的地圖(中近東)
	info	在探險時發現了的貿易城市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	城市的名字
		scale	回
		action	命名建設
		name	建設商行
		info	使命名城市能貿易
		param	3
		func	newtown
			use		1	新城市的地圖(中近東)
@@ITEM
	no		48
	type	航海
	code	town-d
	name	新城市的地圖(印度)
	info	在探險時發現了的貿易城市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	城市的名字
		scale	回
		action	命名建設
		name	建設商行
		info	使命名城市能貿易
		param	4
		func	newtown
			use		1	新城市的地圖(印度)
@@ITEM
	no		49
	type	航海
	code	town-e
	name	新城市的地圖(亞洲)
	info	在探險時發現了的貿易城市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	城市的名字
		scale	回
		action	命名建設
		name	建設商行
		info	使命名城市能貿易
		param	5
		func	newtown
			use		1	新城市的地圖(亞洲)
@@ITEM
	no		50
	type	航海
	code	town-f
	name	新城市的地圖(新大陸)
	info	在探險時發現了的貿易城市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	城市的名字
		scale	回
		action	命名建設
		name	建設商行
		info	使命名城市能貿易
		param	6
		func	newtown
			use		1	新城市的地圖(新大陸)

@@ITEM
	no		51
	type	工藝
	code	coin
	name	金幣
	info	王國發行的金幣。銷售變賣
	price	10000
	limit	500
	base	10/20
	plus	-1h
	pop	2h
	scale	枚
	point	75%
@@ITEM
	no		52
	type	食品
	code	wine
	name	葡萄酒
	info	歐洲特產的食品
	price	10000
	limit	100
	base	10/20
	plus	-1h
	pop	16h
	scale	桶
	point	300%
@@ITEM
	no		53
	type	食品
	code	cheese
	name	乳酪
	info	歐洲特產的食品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	3h
	scale	塊
	point	60%
@@ITEM
	no		54
	type	調味
	code	olive
	name	橄欖油
	info	歐洲特產的調味料
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	90m
	scale	桶
	point	30%
@@ITEM
	no		55
	type	紡織品
	code	woolen
	name	毛紡織品
	info	歐洲特產的紡織品
	price	5000
	limit	200
	base	10/20
	plus	-1h
	pop	8h
	scale	箱
	point	150%
@@ITEM
	no		56
	type	工藝
	code	stained
	name	彩色玻璃
	info	歐洲特產的工藝品
	price	8000
	limit	120
	base	10/20
	plus	-1h
	pop	12h
	scale	箱
	point	200%
@@ITEM
	no		57
	type	工藝
	code	sculpture
	name	雕刻
	info	歐洲特產的工藝品
	price	4000
	limit	250
	base	10/20
	plus	-1h
	pop	6h
	scale	箱
	point	120%
@@ITEM
	no		58
	type	工藝
	code	gun
	name	鐵砲
	info	歐洲特產的工藝品
	price	3000
	limit	300
	base	10/20
	plus	-1h
	pop	5h
	scale	箱
	point	80%

@@ITEM
	no		59
	type	素材
	code	gold
	name	金
	info	非洲特產的素材
	price	5000
	limit	200
	base	10/20
	plus	-1h
	pop	10h
	scale	箱
	point	300%
@@ITEM
	no		60
	type	素材
	code	diamond
	name	鑽石
	info	非洲特產的素材
	price	10000
	limit	100
	base	10/20
	plus	-1h
	pop	20h
	scale	箱
	point	600%
@@ITEM
	no		61
	type	素材
	code	coral
	name	珊瑚
	info	非洲特產的素材
	price	2500
	limit	400
	base	10/20
	plus	-1h
	pop	5h
	scale	箱
	point	140%
@@ITEM
	no		62
	type	素材
	code	ivory
	name	象牙
	info	非洲特產的素材
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		63
	type	食品
	code	coffee
	name	咖啡
	info	非洲特產的食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	箱
	point	40%
@@ITEM
	no		64
	type	調味
	code	salt
	name	鹽
	info	非洲特產的調味料
	price	400
	limit	2500
	base	10/20
	plus	-1h
	pop	40m
	scale	箱
	point	15%
@@ITEM
	no		65
	type	調味
	code	tamarindo
	name	雞精
	info	非洲特產的調味料
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	箱
	point	30%

@@ITEM
	no		66
	type	素材
	code	ironore
	name	鐵礦石
	info	中近東特產的素材
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		67
	type	素材
	code	sulfur
	name	硫磺
	info	中近東特產的素材
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		68
	type	食品
	code	honey
	name	蜂蜜
	info	中近東特產的食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	箱
	point	25%
@@ITEM
	no		69
	type	調味
	code	sugar
	name	砂糖
	info	中近東特產的調料
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	箱
	point	25%
@@ITEM
	no		70
	type	紡織品
	code	carpet
	name	地毯
	info	中近東特產的紡織品
	price	2500
	limit	400
	base	10/20
	plus	-1h
	pop	5h
	scale	箱
	point	180%
@@ITEM
	no		71
	type	紡織品
	code	hemptext
	name	麻織品
	info	中近東特產的紡織品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	120%
@@ITEM
	no		72
	type	工藝
	code	bicornis
	name	犀角
	info	中近東特產的工藝品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	100%

@@ITEM
	no		73
	type	素材
	code	saltpeter
	name	硝石
	info	印度特產的素材
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		74
	type	素材
	code	sapphire
	name	藍寶石
	info	印度特產的素材
	price	5000
	limit	200
	base	10/20
	plus	-1h
	pop	10h
	scale	箱
	point	300%
@@ITEM
	no		75
	type	調味
	code	pepper
	name	胡椒
	info	印度特產的調味料
	price	2500
	limit	400
	base	10/20
	plus	-1h
	pop	200m
	scale	箱
	point	150%
@@ITEM
	no		76
	type	調味
	code	cinnamon
	name	肉桂
	info	印度特產的調味料
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	箱
	point	25%
@@ITEM
	no		77
	type	紡織品
	code	cottonfab
	name	棉織品
	info	印度特產的紡織品
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		78
	type	紡織品
	code	printing
	name	印花布
	info	印度特產的紡織品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	100%
@@ITEM
	no		79
	type	工藝
	code	tortoiseshell
	name	玳瑁
	info	印度特產的工藝品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	100%

@@ITEM
	no		80
	type	素材
	code	pearl
	name	珍珠
	info	亞洲特產的素材
	price	5000
	limit	200
	base	10/20
	plus	-1h
	pop	10h
	scale	箱
	point	250%
@@ITEM
	no		81
	type	食品
	code	sake
	name	清酒
	info	亞洲特產的食品
	price	5000
	limit	200
	base	10/20
	plus	-1h
	pop	10h
	scale	桶
	point	250%
@@ITEM
	no		82
	type	食品
	code	greentea
	name	茶
	info	亞洲特產的食品
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		83
	type	紡織品
	code	silkfab
	name	絲織品
	info	亞洲特產的紡織品
	price	10000
	limit	100
	base	10/20
	plus	-1h
	pop	20h
	scale	箱
	point	750%
@@ITEM
	no		84
	type	工藝
	code	ukiyoe
	name	浮世繪
	info	亞洲特產的工藝品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	120%
@@ITEM
	no		85
	type	工藝
	code	lacquer
	name	漆器
	info	亞洲特產的工藝品
	price	4000
	limit	250
	base	10/20
	plus	-1h
	pop	8h
	scale	箱
	point	200%
@@ITEM
	no		86
	type	工藝
	code	katana
	name	刀
	info	亞洲特產的工藝品
	price	8000
	limit	120
	base	10/20
	plus	-1h
	pop	16h
	scale	箱
	point	400%

@@ITEM
	no		17
	type	素材
	code	silver
	name	銀
	info	新大陸特產的素材
	price	4000
	limit	250
	base	10/20
	plus	-1h
	pop	8h
	scale	箱
	point	200%
@@ITEM
	no		12
	type	素材
	code	emerald
	name	祖母綠
	info	新大陸特產的素材
	price	10000
	limit	100
	base	10/20
	plus	-1h
	pop	20h
	scale	箱
	point	500%
@@ITEM
	no		13
	type	食品
	code	cacao
	name	可可樹
	info	新大陸特產的食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	桶
	point	25%
@@ITEM
	no		14
	type	食品
	code	corn
	name	玉米
	info	新大陸特產的食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	桶
	point	25%
@@ITEM
	no		38
	type	食品
	code	tamato
	name	西紅柿
	info	新大陸特產的食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	桶
	point	25%
@@ITEM
	no		23
	type	食品
	code	tobacco
	name	香煙
	info	新大陸特產的食品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	150%
@@ITEM
	no		21
	type	食品
	code	pumpkin
	name	南瓜
	info	新大陸特產的食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	桶
	point	25%

@@ITEM
	no		5
	type	船舶
	code	ship-a
	name	小型漢撤式帆船
	info	小規模帆船。
	price	20000
	limit	50
	base	5/10
	plus	-1h
	pop	32h
	scale	隻
	point	2h
@@ITEM
	no		6
	type	船舶
	code	ship-c
	name	英國雙桅三角帆船
	info	小規模帆船。
	price	40000
	limit	25
	base	5/10
	plus	-1h
	pop	72h
	scale	隻
	point	4h
@@ITEM
	no		7
	type	船舶
	code	ship-b
	name	巨型槳帆並用船
	info	中規模漕船。
	price	60000
	limit	16
	base	5/10
	plus	-1h
	pop	108h
	scale	隻
	point	6h
@@ITEM
	no		8
	type	船舶
	code	ship-d
	name	大型西班牙方形帆船
	info	中規模帆船。
	price	80000
	limit	12
	base	5/10
	plus	-1h
	pop	150h
	scale	隻
	point	8h
@@ITEM
	no		9
	type	船舶
	code	ship-e
	name	大型威尼斯白刃帆船
	info	大規模帆船。
	price	160000
	limit	10
	base	5/10
	plus	-1h
	pop	300h
	scale	隻
	point	16h
@@ITEM
	no		10
	type	船舶
	code	ship-f
	name	北海多桅橫方帆大船
	info	大規模帆船。
	price	320000
	limit	10
	base	5/10
	plus	-1h
	pop	600h
	scale	隻
	point	50h
@@ITEM
	no		11
	type	船舶
	code	ship-g
	name	戰列艦
	info	巨大漕船。
	price	480000
	limit	10
	base	5/10
	plus	-1h
	pop	900h
	scale	隻
	point	80h

@@ITEM
	no		15
	type	道具
	code	wood
	name	木材
	info	船的材料
	price	5000
	limit	100/100
	pop	10d
	plus	10m
	base	100/10000
	scale	束
	cost	100
@@ITEM
	no		16
	type	道具
	code	cloth
	name	帆布
	info	船桅的材料
	price	3000
	limit	100/100
	pop	10d
	plus	10m
	base	100/10000
	scale	枚
	cost	100

@@ITEM
	no		2
	type	道具
	code	jobchange
	name	職業的秘密
	info	為了各種各樣的就職業的書
	price	25000
	limit	1/1
	pop	0
	base	10/200
	scale	本
	plus	2h
	@@USE
		time	20m
		scale	回
		action	確認
		name	觀察現在的職業不足狀況
		info	現時的職業分配情況
		arg	nocount
		func	jobwant
	@@USE
		time	6h
		action	職業交換
		scale	回
		arg		nocount
		name	成為造船家
		info	對造船家做就職證明
		param	1,26:27:28:29:30:31:32:33:34:35:36:37,0.2,shipb
		funcb	jobcheck
			need		1	造船指導的書
			use		1	職業的秘密
		func	jobport
	@@USE
		time	6h
		action	職業交換
		scale	回
		arg		nocount
		name	成為貿易商
		info	對貿易商做就職證明
		param	30,1:26:27:28:29:34:35:36:37,0.2,trader
		funcb	jobcheck
			use		1	職業的秘密
		func	jobport
	@@USE
		time	6h
		action	職業交換
		scale	回
		arg		nocount
		name	成為探險家
		info	對探險家做就職證明
		param	26,1:30:31:32:33:34:35:36:37,0.2,explore
		funcb	jobcheck
			use		1	職業的秘密
		func	jobport
	@@USE
		time	6h
		action	職業交換
		scale	回
		arg		nocount
		name	成為海盜
		info	對海盜做就職證明
		param	34,1:26:27:28:29:30:31:32:33,0.2,pirate
		funcb	jobcheck
			use		1	職業的秘密
		func	jobport
	@@USE
		time	6h
		action	職業交換
		scale	回
		arg		nocount
		name	成為海軍司令
		info	對海軍司令做就職證明
		param	34,1:26:27:28:29:30:31:32:33,0.2,pros
		funcb	jobcheck
			use		1	職業的秘密
		func	jobport

@@ITEM
	no		3
	type	道具
	code	cm
	name	廣告塑料袋
	info	能提高受歡迎的事也失敗…
	price	100000
	limit	1/0.1
	pop	10d
	plus	5d
	base	10/50
	scale	塑料袋
	cost	10000
	@@use
		time	10h
		exp	10%
		scale	回
		action	廣告塑料袋
		name	出自店的廣告
		info	能提高自己的店的人氣
		arg		nocount
			use		1	廣告塑料袋
		func	_local_
				my $up=int(500*(2-$DT->{rank}/5000));
				if ( rand(1000)<250 ) {
					$DT->{rank}-=$up;
					$DT->{rank}=1000 if $DT->{rank}<1000;
					my $ret="廣告的效果：人氣".int($up/100)."%下降";
					WriteLog(0,$DT->{id},$ret);
					WriteLog(3,0,$DT->{shopname}."不過得到效果是相反。");
					return $ret;
				}
				$DT->{rank}+=$up;
				$DT->{rank}=10000 if $DT->{rank}>10000;
				my $ret="出了廣告：人氣".int($up/100)."%提高";
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DT->{shopname}."出了廣告。");
				return $ret;
			_local_
	@@use
		time	10h
		exp	0%
		name	出其他店的廣告
		info	能提高其他店的人氣
		arg		target|nocount
			use		1	廣告塑料袋
		func	_local_
				return '不能指定自店' if ($DT==$DTS);
				my $up=int(500*(2-$DTS->{rank}/5000));
				$DTS->{rank}+=$up;
				$DTS->{rank}=10000 if $DTS->{rank}>10000;
				my $ret="出了廣告：".$DTS->{shopname}."的人氣".int($up/100)."%提高";
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DT->{shopname}."".$DTS->{shopname}."出了廣告。");
				return $ret;
			_local_
	@@use
		time	16h
		exp	0%
		name	公會的廣告
		info	能提高公會所屬店全部的人氣
		arg		nocount
			use		1	廣告塑料袋
		func	_local_
				return '因為沒加入公會所以不能出公會的廣告' if !$DT->{guild};

				WriteLog(3,0,$DT->{shopname}."公會「".$main::GUILD{$DT->{guild}}->[$GUILDIDX_name]."」出了廣告。");
				foreach my $DTS (@DT)
				{
				next if ($DTS->{guild} ne $DT->{guild});
				my $up=int(500*(2-$DTS->{rank}/5000));
				$DTS->{rank}+=$up;
				$DTS->{rank}=10000 if $DTS->{rank}>10000;
				my $ret="出了公會廣告：".$DTS->{shopname}."的人氣".int($up/100)."%提高";
				WriteLog(0,$DT->{id},$ret);
				}
				return '出了公會廣告';
			_local_
@@ITEM
	no		4
	type	道具
	code	edit-showcase
	name	陳列棚架工具
	info	新增及減少陳列棚架的必要工具
	price	0
	limit	1/1
	pop	0
	plus	1d
	scale	配套元件
	flag	noshowcase|norequest
	@@use
		time	1h
		scale	回
		action	工作
		price	10000
		name	把陳列棚架改為1個
		info	把陳列棚架改為1個
		arg		nocount		#★使用時的選擇項指定
							#  nocount -> 沒有使用回數選擇
		param	1			#★獨自函數用參數
			use	1	陳列棚架工具
		func	_local_
			# ★陳列棚架數變更
			#   param1 變更後的棚架數
			my $oldcnt=$DT->{showcasecount};
			my $newcnt=$USE->{param1};
			$DT->{showcasecount}=$newcnt;
			
			if($oldcnt<$newcnt)
			{
				foreach ($oldcnt..$newcnt-1)
				{
					$DT->{showcase}[$_]=0;
					$DT->{price}[$_]=0;
				}
			}
			if($oldcnt>$newcnt)
			{
				splice(@{$DT->{showcase}},$newcnt);
				splice(@{$DT->{price}},$newcnt);
			}
			my $ret="陳列棚架改為$DT->{showcasecount}個了";
			WriteLog(0,$DT->{id},$ret);
			WriteLog(0,0,$DT->{shopname}."的陳列棚架改為$DT->{showcasecount}個了。");
			
			return $ret;
		_local_
	@@use
		time	2h
		price	20000
		name	把陳列棚架改為2個
		info	把陳列棚架改為2個
		func	_local_1
		arg		nocount
		param	2
			use	1	陳列棚架工具
	@@use
		time	3h
		price	30000
		name	把陳列棚架改為3個
		info	把陳列棚架改為3個
		func	_local_1
		arg		nocount
		param	3
			use	1	陳列棚架工具
	@@use
		time	4h
		price	40000
		name	把陳列棚架改為4個
		info	把陳列棚架改為4個
		func	_local_1
		arg		nocount
		param	4
			use	1	陳列棚架工具
	@@use
		time	5h
		price	50000
		name	把陳列棚架改為5個
		info	把陳列棚架改為5個
		func	_local_1
		arg		nocount
		param	5
			use	1	陳列棚架工具
	@@use
		time	6h
		price	60000
		name	把陳列棚架改為6個
		info	把陳列棚架改為6個
		func	_local_1
		arg		nocount
		param	6
			use	1	陳列棚架工具
	@@use
		time	7h
		price	70000
		name	把陳列棚架改為7個
		info	把陳列棚架改為7個
		func	_local_1
		arg		nocount
		param	7
			use	1	陳列棚架工具
	@@use
		time	8h
		price	80000
		name	把陳列棚架改為8個
		info	把陳列棚架改為8個
		func	_local_1
		arg		nocount
		param	8
			use	1	陳列棚架工具
@@ITEM
	no		22
	type	道具
	code	book-help
	name	幫助生活之書
	info	這本書可以幫助你解決不少問題
	price	0
	limit	1/1
	pop	0
	plus	4h
	scale	本
	flag	noshowcase
	@@USE
		time	20m
		scale	回
		action	確認
		name	現時的職業的數量
		info	以便知道自己的職業是否合適現時的形勢
		arg	nocount
		func	jobwant
	@@use
		time	40m
		scale	回
		action	購入
		price	1200
		name	市場無方包買入怎麼算
		info	通過特別途徑購入方包(10箱單位)
		okmsg	買入了方包
			get		10	方包
	@@use
		time	40m
		scale	回
		action	購入
		price	2400
		name	市場無羊羔酒買入怎麼算
		info	通過特別途徑購入羊羔酒(10桶單位)
		okmsg	買入了羊羔酒
			get		10	羊羔酒
	@@use
		time	40m
		scale	回
		action	僱用
		price	15000
		name	市場無水手僱傭怎麼算
		info	在特別途徑僱傭海員(10人單位)
		okmsg	僱用海員
			get		10	水手
	@@use
		time	10m
		scale	回
		action	銷售
		name	把過多金幣轉賣給人民
		info	以幫助資金不足之時用
		okmsg	銷售了金幣
			use		1	金幣
		func	_local_
			$DT->{money}+=8000 * $count;
			return "變賣額：\\".(8000 * $count);
		_local_
	@@use
		time	8h
		scale	回
		action	工作
		name	因生活困難而去工作
		info	以解決現時的資金問題
		okmsg	辛苦地終於找得工錢維生
			get		2	金幣

@@ITEM
	no		24
	type	道具
	code	gift
	name	禮物券
	info	與其他職業的人換取好的物品
	price	10000
	cost	10
	limit	10/0
	scale	枚
	@@USE
		time	20m
		scale	回
		action	勸告
		name	交換禮物券注意
		info	先聽從海邊的男人勸告
		arg	nocount
		func	advice
			need		10	禮物券
	@@USE
		time	20m
		scale	回
		action	確認
		name	觀察現在的職業不足狀況
		info	以便知道我應該成為甚麼職業
		arg	nocount
		func	jobwant
			need		10	禮物券
	@@USE
		time	20m
		scale	回
		action	交換
		name	與造船家交換物品
		info	成為造船家必須得到的物品
		okmsg	記得努力
			use		10	禮物券
			get		1	造船指導的書
	@@USE
		time	20m
		scale	回
		action	交換
		name	與貿易商交換物品
		info	成為貿易商必須得到的物品
		okmsg	記得努力
			use		10	禮物券
			get		5	小型漢撤式帆船
			get		20	金幣
			get		1	職業的秘密
			get		1	幫助生活之書
	@@USE
		time	20m
		scale	回
		action	交換
		name	與探險家交換物品
		info	成為探險家必須得到的物品
		okmsg	記得努力
			use		10	禮物券
			get		5	小型漢撤式帆船
			get		20	金幣
			get		1	職業的秘密
			get		1	幫助生活之書
	@@USE
		time	20m
		scale	回
		action	交換
		name	與海盜交換物品
		info	成為海盜必須得到的物品
		okmsg	記得努力
			use		10	禮物券
			get		5	小型漢撤式帆船
			get		10	金幣
			get		1	職業的秘密
			get		1	幫助生活之書
	@@USE
		time	20m
		scale	回
		action	交換
		name	與海軍司令交換物品
		info	成為海軍司令必須得到的物品
		okmsg	記得努力
			use		10	禮物券
			get		5	小型漢撤式帆船
			get		10	金幣
			get		1	職業的秘密
			get		1	幫助生活之書

@@ITEM
	no		25
	type	道具
	code	slot
	name	抽獎券
	info	新奇的券
	price	20000
	cost	100
	limit	10/1.2
	plus	-10h
	scale	枚
	pop	10d
	flag	noshowcase
	@@use
		time	20m
		scale	回
		action	拉
		name	使用抽獎券
		info	不知自己運氣可以得到甚麼好東西
		arg		nocount
		ngmsg	完全無得到任何好東西…
			use		1	抽獎券
			get		1	禮物券		5%		抽到禮物券！
			get		1	廣告塑料袋		10%		抽到廣告塑料袋！
			get		1	職業的秘密		5%		抽到職業的秘密！
			get		1	看門狗			5%		抽到看門狗！
			get		1	禁止的邪惡聖經	10%		抽到禁止的邪惡聖經！
			get		1	方包			5%		抽到方包！
			get		1	羊羔酒			5%		抽到羊羔酒！

@@ITEM
	no		87
	type	道具
	code	defence-manbiki
	name	看門狗
	info	能看管商店的高級血統狗
	price	500000
	cost	5000
	limit	1/0.5
	pop	1d
	plus	30m
	scale	匹
	flag	noshowcase|onlysend|human

@@ITEM
	no		88
	type	道具
	code	badgossip
	name	禁止的邪惡聖經
	info	使平常人做一些原本不可以做的事情
	price	50000
	cost	5000
	limit	1/1
	pop	0
	plus	1d
	scale	本
	@@use
		time	10h
		exp	20%
		exptime	8h
		scale	回
		price	50000
		scale	回
		action	開始
		price	0
		name	光浩的隱藏日記
		info	這是一本可以教導人如何下降敵人的店舖人氣的日記
		arg	target|nocount
			needpoint	20000
		func	_local_
			my $ret;
			if(rand(1000)<800 && !$DTS->{exp}{@@ITEMNO"廣告塑料袋"})
			{
				$DTS->{rank}-=int($DTS->{rank}/3);
				$ret=$DTS->{shopname}.'發放壞的傳言成功了';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(2,0,$DTS->{shopname}.'因為壞的傳言而人氣下降了。');
			}
			else
			{
				$DTS->{exp}{@@ITEMNO"廣告塑料袋"}-=100;
				$DTS->{exp}{@@ITEMNO"廣告塑料袋"}=0 if ($DTS->{exp}{@@ITEMNO"廣告塑料袋"} < 0);
				$DT->{rank}-=int($DT->{rank}/4);
				$ret=$DTS->{shopname}.'發放壞的傳言失敗了';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DTS->{shopname}."反之向".$DT->{shopname}.'發放壞的傳言。');
			}
			return $ret;
			_local_
	@@use
		time	10h
		exp	25%
		exptime	8h
		scale	回
		action	偷竊
		price	50000
		name	猶太教教士的柏古尼
		info	這個是教導人如何偷取別人的金錢
			needpoint	20000
		func	stole
		arg		target|nocount

@@ITEM
	no		89 #道具編號自己改
	type	道具 #道具種類也自己修改
	code	sweep-robot #道具代碼（限定英文）
	name	掃除機器人 #道具名稱
	info	自動幫你打掃的機器人 #道具說明
	price	1000000 #定價
	limit 1/1 #持有上限（店中/市場）
	pop 0	#放在架上賣出速度（0的話就是賣不掉）
	plus 1d	#市場補貨速度
	scale 台	#單位
	cost 100000	#維持費
	flag noshowcase|norequest	#不能放在架上賣|不能到依賴所要求
		funct _local_	#定期執行的程式，只要持有就會自動執行
			my($ITEM,@DT)=@_;
			foreach my $DT (@DT)
			{
				$DT->{trush} -= $TIMESPAN*100; #每秒減少100的垃圾（1kg=10000）
				$DT->{trush} = 0 if $DT->{trush} <0;
			}
			return;
		_local_

#------------------------------活動
@@event
	start		10%
	basetime	5h
	plustime	5h
	code		happy
	startmsg	感謝祭已經開始了。
	endmsg		感謝祭已經結束了。
	info		感謝祭時好熱鬧。
	func		_local_
		my $time=$main::TIMESPAN;
		$time=10*3600 if $time>10*3600; # 限制最大10％
		$time=int($time/36);
		
		foreach(@DT)
		{
			$_->{rank}+=int(rand($time));
			$_->{rank}=10000 if $_->{rank}>10000;
		}
		return 0;
	_local_

@@EVENT
	start		150%
	basetime	0h
	plustime	0h
	code		message
	info		消息
	startfunc	_local_
		my @message=(
		'哲學者「這個大地，像有一個人用水包圍著。」',
		'宗教家「世界上是有可能有一隻體長500km的烏龜。」',
		'天文學者「這個大地一定是像圓球的形狀。」',
		'冒險家「如果世界是圓的，那麼西邊必定可以到達印度。」',
		'海員「若不盡的去西方邊的話，就會到達世界的盡頭了。」',
		'酒館老闆娘「如果世界是圓的，那麼另一邊的人就趺下來了。」',
		'航海家「遙遠地東方，好像有一個國家甚麼也是由黃金造成。」',
		'航海家「在遙遠地西方的森林裡，好像有基督的樂園。」',
		'水手「在南的岬的妖精，因為妖精的歌聲．所有船也沉下了。」',
		'水手「假若一首船只發出光而不熱的話。那就是幽靈船了。」',
		'冒險家「比船還更大的章魚襲擊，所有也船必定沉沒。」',
		);
		my $cnt=int(rand(scalar(@message)));
		return (0,$message[$cnt]);
	_local_


@@FUNCINIT
#職業把「探險家」的場合，對買東西必要的時間做為1/2。
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/2) if $DT->{job} eq 'explore';

@@FUNCITEM
######################################################################
# ★Jobuchenjichekku
######################################################################
sub jobcheck
{
my($USE)=@_;
return 1 if ($DT->{job} eq $USE->{param4});
return 0;
}

######################################################################
# ★職業交換
######################################################################
sub jobport
{
	$DT->{job}=$USE->{param4};
	WriteLog(3,0,$DT->{shopname}.'轉成「'.$main::JOBTYPE{$USE->{param4}}.'」職業。');
	main::RequireFile('inc-sea.cgi');

	my $ret;
	my $exp1=$DT->{exp}{$USE->{param1}};
	my $exp2=0;
	$ret.="一個人獨自走向轉職的道路。<br><br>";
	$ret.="<TABLE><tr><td>";
	$ret.=main::GetTagImgKao('amuza','amza')."主神：<br>";
	$ret.="…我想成為".$main::JOBTYPE{$USE->{param4}}."。<br>";
	$ret.='希望你能使我變成我想變的職業！<br>就在這裡展現出你的力量<b>'.$DT->{shopname}."</b><br>";
	$ret.=$main::JOBTYPE{$USE->{param4}}."神會寬恕及賜予走路的光！";
	$ret.="</td></tr></table><br>";
	$ret.="變成".$main::JOBTYPE{$USE->{param4}}."職業。<br>";
	
	foreach my $exps (split(/:/,$USE->{param2}))
	{
		my $exp=$DT->{exp}{$exps};
		next if (!$DT->{item}[$exps-1] && !$exp);
		$exp2+=$exp;
		delete($DT->{exp}{$exps});
		main::DeleteSeaSub("$DT->{id}-abi$exps");
		main::DeleteSeaSub("$DT->{id}-exp$exps");
		my $msg=$ITEM[$exps]->{name}.'扔掉了';
		if ($DT->{item}[$exps-1])
			{
			$DT->{item}[$exps-1]=0;
			$msg.="（領取費 \\50000）";
			$DT->{money}+=50000;
			}
		$msg.="。";
		WriteLog(0,$DT->{id},$msg);
		$ret.=$msg."<br>";
	}
	$exp2=int($exp2*$USE->{param3});
	$exp1+=$exp2;
	$exp1=1000 if $exp1>1000;
	$msg=$ITEM[$USE->{param1}]->{name}."熟練度 ".int($exp1/10)."% 變成了。";
	WriteLog(0,$DT->{id},$msg);
	$ret.=$msg."<br>";
	$DT->{exp}{$USE->{param1}}=$exp1;
	return $ret;
}

######################################################################
#★探險船隊的派遣
######################################################################
sub exploring
{
	my $itemno=$USE->{param1};	#派遣??船
	my $data=$USE->{param2};	#派遣海域
	my $ability=$ship[$data+4];	#能力
	main::ReadSea($data);
	my @subdata;
	$subdata[0]=$main::NOW_TIME + 3600*11 + int(rand(7200));
	$subdata[1]=$data;

	# 生???判定
	if ($main::Pir * 12 > 100 + rand(1900 - $DT->{exp}{$itemno}))
		{
		$subdata[2]=1;	#海?藻屑
		}
		else
		{
		$subdata[2]=0;
		
		# ?見物判定
		if ($main::Civ + 20 < rand($ability) + int($DT->{exp}{$itemno} / 50))
			{
			$subdata[3]=1;
			$main::Civ+=int(rand(3) + 1);
			$main::Civ=100 if ($main::Civ > 100);
			}
		# 都市?見判定
		$subdata[4]=1 if (rand(100)+ ($main::Townnum * 12) < $ability + int($DT->{exp}{$itemno} / 50));
		}
	main::WriteSea($data);
	main::WriteSeaSub("$DT->{id}-exp$itemno",@subdata);
	my $ret;
	$ret.=qq|<IMG width="112" height="150" SRC="$main::IMAGE_URL/map/ship1.png"><br>|;
	my @AREA=("","歐洲","非洲","中近東","印度","亞洲","新大陸");
	$ret.=$AREA[$data]."派遣了探險船隊。";
	WriteLog(0,0,$DT->{shopname}."已經向".$AREA[$data]."派遣了探險船隊。");
	return $ret;
}

######################################################################
# ★探險船隊派遣前核對
######################################################################
sub beforeexp
{
my($USE)=@_;
my $itemno=$USE->{param1};	#派遣??船
my $data=$USE->{param2};	#派遣海域
return 1 if ($DT->{job} ne 'explore');
return 1 if -e(main::GetPath($main::SUBDATA_DIR,$DT->{id}."-exp".$itemno));
if (!$ship[0])
	{
	main::RequireFile('inc-sea.cgi');
	@ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	}
return 1 if $ship[$data+4] < 1;
$USE->{info}.="<b>".$ship[$data+4]."</b>%";
$USE->{use}[0]->{no}=@@ITEMNO "方包";
$USE->{use}[0]->{count}=$ship[11];
$USE->{use}[0]->{proba}=1000;
$USE->{use}[1]->{no}=@@ITEMNO "羊羔酒";
$USE->{use}[1]->{count}=$ship[12];
$USE->{use}[1]->{proba}=1000;
$USE->{use}[2]->{no}=@@ITEMNO "水手";
$USE->{use}[2]->{count}=$ship[13];
$USE->{use}[2]->{proba}=1000;
return 0;
}

######################################################################
# ★只派遣中的時候可
######################################################################
sub onlyexp
{
my($USE)=@_;
my $itemno=$USE->{param1};	#派遣??船
return 0 if -e(main::GetPath($main::SUBDATA_DIR,$DT->{id}."-exp".$itemno));
return 1;
}

######################################################################
#★探險船隊的迎接
######################################################################
sub meetexp
{
	my $itemno=$USE->{param1};	#派遣??船
	main::RequireFile('inc-sea.cgi');
	my @subdata=main::ReadSeaSub("$DT->{id}-exp$itemno");
	my @ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	my $seaman=$ship[13];		#水夫
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="570"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/harbor.png);" valign="top"><br><br>|;

	if ($main::NOW_TIME < $subdata[0])
		{
		$ret.="已經到港口看過了，船隊還未回來的。<br>";
		$ret.="還是遲點先再來吧。</tr></table>";
		return $ret;
		}
	main::DeleteSeaSub("$DT->{id}-exp$itemno");
	if ($subdata[2])
		{
		$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship2.png">|;
		$ret.="已經是船隊應該回來的時候。<br>";
		$ret.="可是，等了很久船隊還未回來。<br><br>";
		$ret.="難度已埋沒於海裡的碎藻。<br>";
		$ret.="那就是被海盜擊沉了…。<br>";
		$ret.="</tr></table>";
		UseItem($itemno,1);
		delete $DT->{exp}{$itemno};
		main::DeleteSeaSub("$DT->{id}-abi$itemno");
		WriteLog(2,0,$DT->{shopname}.'探險船隊於海裡的碎藻沉沒了。');
		return $ret;
		}
	$seaman=int($seaman * (70 + rand(30)) / 100);
	AddItem(@@ITEMNO "水手",$seaman);
	$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship1.png">|;
	$ret.=main::GetTagImgKao('提督','exp','align="left" ')."<SPAN>提督</SPAN>：我們已經回來。<br>";
	$ret.="因為遇上颱風及海盜，<br>只有$seaman位水手平安回來。<br>";
	if ($subdata[3])
		{
		$ret.="此次的航海的途中，發現了新的事物。<br>";
		$ret.="<SPAN>報告書</SPAN>書中寫到，發現了不明地方。<br>";
		AddItem((38 + $subdata[1]),1);
		}
		else
		{
		$ret.="此次的航海，無發現任何新的事物。<br>";
		}
	if ($subdata[4])
		{
		$ret.="比新事物更重要的事，<b>就是發現了新的陸地</b>。<br>";
		$ret.="<SPAN>新的貿易城市</SPAN>可以建設了！<br>";
		AddItem((44 + $subdata[1]),1);
		}
		else
		{
		$ret.="此次的航海，無發現任何新的陸地。<br>";
		}
	$ret.="這個報告已經結束。讓我於下一次航海時先休息一下。";
	$ret.="</tr></table>";
	return $ret;
}

######################################################################
#★發現物
######################################################################
sub disc
{
	my $no=$USE->{param1} - 1;
	my @DISCOVER=(
		[
		['煉金術','希望可以研究變錢的方法。只是材料不輕易得到。',55],
		['半獸人的斧子','半獸人使用的斧子。把手的部分提高呻吟聲。',72],
		['弗蘭克王的佩刀','弗蘭克王使用的佩刀。被鑲嵌寶石。',75],
		['猶大的魔衣','背叛了基督的猶大穿的衣。詛咒持有的人。',65],
		['阿提拉的鎧甲','阿提拉王穿的鎧甲。沉重到不能舉起。',65],
		['逆周圍的懷錶','針向反圍前進的錶。不需螺絲自己也轉動。',75],
		['滅亡的十字架','基督處刑時候被釘了身體的十字架。',60],
		['Stonehenge','就是一些圍繞著石柱的遺跡。',60],
		],
		[
		['麒麟','從身體發生五色的磷光的靈獸。有牛的尾巴和馬的蹄，腹下黃色的。',90],
		['人草','在地面長的人的種族。',65],
		['眼頭人','只有得及只有眼睛的種族。',70],
		['步行杖','步行用的杖，可減輕辛苦。',75],
		['Hamapegga的劍','古代的王的劍。全部用純金造成。',100],
		['邪神的像','祭祀了蛇的身姿的邪神像。',60],
		['斯芬克斯','獅鷲獸。喜歡出迷及只吃解不開迷的人。',70],
		['維多利亞瀑布','大地的水裂縫注入的巨大的瀑布。',60],
		],
		[
		['Saradin的鎧甲','古代的王的鎧甲。怎樣攻擊也不會壞。',60],
		['天球儀','在圓的球體上畫出星空情況的藝術品。',80],
		['克麗奧佩特拉的地毯','美麗的刺繡的地毯。據說由絕世的美女所造的。',100],
		['大油燈','靠油燈生活的人的種族。',75],
		['古蘭經','這個地域的民族作為紀念的書。什麼重要的事好像被記下。',50],
		['Sumer的粘土板','古代的人記下的文字。與我們的語言很相似。',50],
		['布卷人','用布包緊全身的人種族。',60],
		['十字軍的寶劍','十字軍的隊長作為遠征時用的寶劍。',80],
		],
		[
		['象','鼻子長的巨大的靈獸。軀體很粗，有八隻腳。',80],
		['首領族','與我們人類有少少不相似的種族。',60],
		['食金蟲','把金錢作為食物的蟲。',60],
		['金斗雲','可使人飛行的雲。',75],
		['Sutuba','用石頭造成的巨大塔。內裡的神被供奉。',50],
		['Mugaru的寶盾','傳到古代王國的傳說的盾。藍寶石散開的Bamerarete。',100],
		['勇氣的人的蛀蟲笪','古代的英雄使用這樣的蛀蟲笪。',80],
		['塔其馬哈','為了古代的王而供奉女性蓋的巨大寺院。',70],
		],
		[
		['驢','這個地域的民族的工具。',90],
		['妖刀村正','帶有了妖氣的劍。佔領持有者的心，迫使到復仇心。',70],
		['浦島的玉匣','從海中的樂園帶回的寶物。附近好像有龍宮城。',100],
		['Harakiri人','喜歡腹親自的切人的種族。',75],
		['桃花源的地圖','表示了傳說的樂園的位置的地圖。附近好像有桃花源。',100],
		['冬蟲夏草','半蟲半植物。冬天做著蟲的身姿，到夏天的話變成草。',80],
		['高麗人參','治療百病的傳說的胡蘿蔔。',80],
		['萬里長城','為了古代的王抵禦外敵的侵入構築了的牆。',70],
		],
		[
		['金錢蛙','活的青蛙，身體用黃金造成。',90],
		['挫折的遺跡','祭奠了基督的設施的殘骸。好像傳說的聖地Puresute·Joan的悲慘的下場。',120],
		['黃金的河','代替水的黃金流動的河。不久便有黃金國。',100],
		['Nazka地上畫兒','在地上被畫的巨大的鳥的畫兒。',75],
		['Moai的石像','在海岸上被排列成的巨大的人臉石像。',100],
		['刺青的人','臉和身體，喜歡用青和紅等涂的人的種族。',75],
		['美人魚','腰部以下是魚的人的種族。',90],
		['空中遺跡','空中存在的城市的遺跡。在上居住的人已全部死滅。',80],
		],
	);
	my @MYDIS=@{$DISCOVER[$no]};
	my $num=int(rand(scalar(@MYDIS))) + 0;
	my @msg=@{$MYDIS[$num]};
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="455"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/discover.png);" valign="top"><br><br>|;
	$no++;
	$num++;
	$ret.=qq|<IMG width="60" height="80" align="left" SRC="$main::IMAGE_URL/disc/$no-$num.png">|;
	$ret.="<SPAN>$msg[0]</SPAN><br><br>";
	$ret.="$msg[1]</tr></table>";
	$ret.="<br>從國王賜給獎賞".main::GetTagImgItemType(51)."金幣".($msg[2])."</b>枚領取了。";
	AddItem(51,$msg[2]);
	return $ret;
}

######################################################################
#★都市建設
######################################################################
sub newtown
{
	my $data=$USE->{param1};	#派遣海域
	$name=$USE->{arg}->{message};
	main::RequireFile('inc-sea.cgi');
	main::ReadSea($data);
	my $ret;
	if ($main::Townnum > 9)
		{
		$ret.='這個發現的新城市，已經建設了商行。<br>';
		$ret.='由於已經有人建設了商行。<br>';
		$ret.='到底是誰人先發現先！';
		return $ret;
		}
	main::OutError('請填上城市的名字。') if !$name;
	my @TOWN=(
		[
		[@@ITEMNO "葡萄酒",20,10],
		[@@ITEMNO "乳酪",15,10],
		[@@ITEMNO "橄欖油",25,5],
		[@@ITEMNO "毛紡織品",10,15],
		[@@ITEMNO "彩色玻璃",20,10],
		[@@ITEMNO "雕刻",20,10],
		[@@ITEMNO "鐵砲",15,10],
		],
		[
		[@@ITEMNO "金",10,5],
		[@@ITEMNO "鑽石",10,10],
		[@@ITEMNO "珊瑚",15,10],
		[@@ITEMNO "象牙",15,15],
		[@@ITEMNO "咖啡",10,10],
		[@@ITEMNO "鹽",20,10],
		[@@ITEMNO "雞精",20,10],
		],
		[
		[@@ITEMNO "鐵礦石",10,10],
		[@@ITEMNO "硫磺",10,10],
		[@@ITEMNO "蜂蜜",15,10],
		[@@ITEMNO "砂糖",15,15],
		[@@ITEMNO "地毯",8,7],
		[@@ITEMNO "麻織品",10,5],
		[@@ITEMNO "犀角",5,15],
		],
		[
		[@@ITEMNO "硝石",10,10],
		[@@ITEMNO "藍寶石",10,5],
		[@@ITEMNO "胡椒",1,4],
		[@@ITEMNO "肉桂",10,15],
		[@@ITEMNO "棉織品",15,10],
		[@@ITEMNO "印花布",10,10],
		[@@ITEMNO "玳瑁",10,5],
		],
		[
		[@@ITEMNO "珍珠",10,10],
		[@@ITEMNO "清酒",10,10],
		[@@ITEMNO "茶",5,10],
		[@@ITEMNO "絲織品",5,15],
		[@@ITEMNO "浮世繪",10,5],
		[@@ITEMNO "漆器",5,15],
		[@@ITEMNO "刀",5,10],
		],
		[
		[@@ITEMNO "銀",5,10],
		[@@ITEMNO "祖母綠",5,10],
		[@@ITEMNO "可可樹",5,15],
		[@@ITEMNO "玉米",5,15],
		[@@ITEMNO "西紅柿",10,5],
		[@@ITEMNO "香煙",5,5],
		[@@ITEMNO "南瓜",5,10],
		],
	);
	$no=$data - 1;
	my @MYDIS=@{$TOWN[$no]};
	my $num=int(rand(scalar(@MYDIS))) + 0;
	my @msg=@{$MYDIS[$num]};
	my $price=int($ITEM[$msg[0]]->{price} * ($msg[1] + rand($msg[2])) / 100);
	my $life=$main::NOW_TIME + 86400*8 + int(rand(86400) * 4);
	foreach(1..$#main::SEA)
		{
		my @buf=split(',',$main::SEA[$_]);
		$life++ if $buf[0] == $life;
		main::OutError('有同樣的名字的城市。請改不同的名字。') if $buf[1] eq $name;
		}
	push (@main::SEA,"$life,$name,$DT->{id},$msg[0],$price,0\n");
	$main::Civ+=int(rand(3));
	$main::Civ=100 if ($main::Civ > 100);
	$main::Pir+=int(rand(4));
	$main::Pir=100 if ($main::Pir > 100);
	main::WriteSea($data);
	$ret.=qq|<IMG width="255" height="153" SRC="$main::IMAGE_URL/map/trade.jpg"><br><br>|;
	$ret.='建設了商行。<br>「<b>'.$USE->{arg}->{message}.'</b>」城市可以貿易了。';
	WriteLog(2,0,$DT->{shopname}.'發現「'.$USE->{arg}->{message}.'」城市。');
	return $ret;
}

######################################################################
# ★貿易船?派遣前????
######################################################################
sub routesel
{
my($USE)=@_;
my $itemno=$USE->{param1};	#派遣??船
my $data=$USE->{param2};	#派遣海域
return 1 if ($DT->{job} ne 'trader');
return 1 if -e(main::GetPath($main::SUBDATA_DIR,$DT->{id}."-exp".$itemno));
if (!$ship[0])
	{
	main::RequireFile('inc-sea.cgi');
	@ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	}
return 1 if $ship[$data+4] < 1;
$USE->{info}.="<b>".$ship[$data+4]."</b>%";
main::ReadSea($data);
return 1 if $main::Townnum < 1;
$USE->{argselect}=';';
foreach(1..$main::Townnum)
	{
	my($date,$name,$other)=split(',',$main::SEA[$_],3);
	$USE->{argselect}.=$_.';'.$name.';';
	}
$USE->{use}[0]->{no}=@@ITEMNO "方包";
$USE->{use}[0]->{count}=$ship[11];
$USE->{use}[0]->{proba}=1000;
$USE->{use}[1]->{no}=@@ITEMNO "羊羔酒";
$USE->{use}[1]->{count}=$ship[12];
$USE->{use}[1]->{proba}=1000;
$USE->{use}[2]->{no}=@@ITEMNO "水手";
$USE->{use}[2]->{count}=$ship[13];
$USE->{use}[2]->{proba}=1000;
return 0;
}

######################################################################
#★貿易船??派遣
######################################################################
sub route
{
	my $itemno=$USE->{param1};	#派遣??船
	my $data=$USE->{param2};	#派遣海域
	my $ability=int($ship[$data+4] / 2);	#積載量（ｘ万?相?）
	my $sel=$USE->{arg}->{select};

	#派遣?????
	my @buf=split(',',$main::SEA[$sel]);
	main::OutError("「$buf[1]」物產因為供應過少，不能派遣。<br>請變更派遣地方。") if ($buf[0] < $main::NOW_TIME);
	$main::SEA[$sel]="$buf[0],$buf[1],$buf[2],$buf[3],$buf[4],".($buf[5] + 1)."\n";
	main::WriteSea($data);

	my @subdata;
	$subdata[0]=$main::NOW_TIME + 3600*11 + int(rand(7200));

	# 生???判定
	$subdata[1]=1 if ($main::Pir * 12 > 100 + rand(1900 - $DT->{exp}{$itemno}));

	#貿易量
	$subdata[2]=$buf[1];
	$subdata[3]=$buf[3];
	$subdata[4]=int($ITEM[$buf[3]]->{limit} * $ability / 100);
	$subdata[5]=$buf[4] * $subdata[4];

	# ?見者?利益?生
	if (defined($main::id2idx{$buf[2]}))
		{
		$DT[$main::id2idx{$buf[2]}]->{money}+=int($subdata[5] / 2);
		$DT[$main::id2idx{$buf[2]}]->{saletoday}+=int($subdata[5] / 2);
		}
	main::WriteSeaSub("$DT->{id}-exp$itemno",@subdata);
	my $ret;
	$ret.=qq|<IMG width="112" height="150" SRC="$main::IMAGE_URL/map/ship1.png"><br>|;
	$ret.="「$buf[1]」派遣了貿易船隊。";
	return $ret;
}

######################################################################
#★貿易船??出迎?
######################################################################
sub meetrtp
{
	my $itemno=$USE->{param1};	#派遣??船
	main::RequireFile('inc-sea.cgi');
	my @subdata=main::ReadSeaSub("$DT->{id}-exp$itemno");
	my @ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	my $seaman=$ship[13];		#水夫
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="570"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/harbor.png);" valign="top"><br><br>|;

	if ($main::NOW_TIME < $subdata[0])
		{
		$ret.="已經到港口看過了，船隊還未回來的。<br>";
		$ret.="還是遲點先再來吧。</tr></table>";
		return $ret;
		}
	main::DeleteSeaSub("$DT->{id}-exp$itemno");
	if ($subdata[1])
		{
		$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship2.png">|;
		$ret.="已經是船隊應該回來的時候。<br>";
		$ret.="可是，等了很久船隊還未回來。<br><br>";
		$ret.="難度已埋沒於海裡的碎藻。<br>";
		$ret.="那就是被海盜擊沉了…。<br>";
		$ret.="</tr></table>";
		UseItem($itemno,1);
		delete $DT->{exp}{$itemno};
		main::DeleteSeaSub("$DT->{id}-abi$itemno");
		WriteLog(2,0,$DT->{shopname}.'貿易船隊永遠沈沒於大海中了。');
		return $ret;
		}
	$seaman=int($seaman * (70 + rand(30)) / 100);
	AddItem(@@ITEMNO "水手",$seaman);
	$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship1.png">|;
	$ret.=main::GetTagImgKao('提督','rtp','align="left" ')."<SPAN>提督</SPAN>：我們已經回來。<br>";
	$ret.="因為遇上颱風及海盜，<br>只有$seaman位水手平安回來。<br>";
	$ret.="此次的貿易，城市「$subdata[2]」基於，<br>";
	$ret.=main::GetTagImgItemType($subdata[3]).$ITEM[$subdata[3]]->{name}."了 ";
	$ret.=$subdata[4].$ITEM[$subdata[3]]->{scale}."能購入。<br>";
	$ret.="作為進貨的費用，\\".$subdata[5]."懸掛了。<br>";
	$DT->{money}-=$subdata[5];
	$DT->{paytoday}+=$subdata[5];
	AddItem($subdata[3],$subdata[4]);
	$ret.="報告是以上的通行。";
	$ret.="</tr></table>";
	return $ret;
}

######################################################################
# ★武?艦隊派遣前????
######################################################################
sub nowpp
{
my($USE)=@_;
my $itemno=$USE->{param1};	#派遣??船
my $data=$USE->{param2};	#派遣海域
if ($DT->{job} eq 'pirate') {$USE->{name}.="掠奪派遣";}
elsif ($DT->{job} eq 'pros') {$USE->{name}.="偵察派遣";}
else {return 0;}
return 1 if -e(main::GetPath($main::SUBDATA_DIR,$DT->{id}."-exp".$itemno));
if (!$ship[0])
	{
	main::RequireFile('inc-sea.cgi');
	@ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	}
return 1 if $ship[$data+4] < 1;
$USE->{info}.="<b>".$ship[$data+4]."</b>%";
$USE->{use}[0]->{no}=@@ITEMNO "方包";
$USE->{use}[0]->{count}=$ship[11];
$USE->{use}[0]->{proba}=1000;
$USE->{use}[1]->{no}=@@ITEMNO "羊羔酒";
$USE->{use}[1]->{count}=$ship[12];
$USE->{use}[1]->{proba}=1000;
$USE->{use}[2]->{no}=@@ITEMNO "水手";
$USE->{use}[2]->{count}=$ship[13];
$USE->{use}[2]->{proba}=1000;
return 0;
}

######################################################################
#★武?艦隊?派遣
######################################################################
sub attack
{
	my $itemno=$USE->{param1};	#派遣??船
	my $data=$USE->{param2};	#派遣海域
	my $ability=$ship[$data+4];	#能力
	main::ReadSea($data);
	my @subdata;
	$subdata[0]=$main::NOW_TIME + 3600*11 + int(rand(7200));
	$subdata[1]=$data;
	my $ret;
	$ret.=qq|<IMG width="112" height="150" SRC="$main::IMAGE_URL/map/ship1.png"><br>|;
	my @AREA=("","歐洲","非洲","中東和近東","印度","亞洲","新大陸");

	if ($DT->{job} eq 'pros')
	{
	# 海軍??理
	# 生???判定
	if ($main::Pir * 6 > 100 + rand(1900 - $DT->{exp}{$itemno}))
		{
		$subdata[2]=1;	#海?藻屑
		}
		else
		{
		# 海賊出現率低下
		$main::Pir-=int(rand(5)) + 6;
		$main::Pir=0 if ($main::Pir < 0);
		# 海軍偵察率上昇
		$main::Pro+=int(rand(5)) + 4;
		$main::Pro=100 if ($main::Pro > 100);
		}
	$ret.=$AREA[$data]."派遣了海軍";
	WriteLog(0,0,$DT->{shopname}."已經向".$AREA[$data]."派遣了海軍。");
	}
	else
	{
	# 海賊??理
	# 生???判定
	if ($main::Pro * 16 > 100 + rand(1900 - $DT->{exp}{$itemno}))
		{
		$subdata[2]=1;	#海?藻屑
		}
		else
		{
		# 海賊出現率上昇
		$main::Pir+=int(rand(5)) + 4;
		$main::Pir=100 if ($main::Pir > 100);
		}
	$ret.=$AREA[$data]."派遣了海盜船。";
	WriteLog(2,0,$AREA[$data]."好像有海盜出沒。");
	}
	if (!$subdata[2])
		{
		$subdata[2]=0;
		# 金貨
		$subdata[3]=int(($ability / 4) + ($DT->{exp}{$itemno} / 100) + rand(5));
		# 貿易品
		if ($main::Townnum > 0 && $main::Pir > rand(20))
			{
			my $sel=int(rand($main::Townnum)) + 1;
			my @buf=split(',',$main::SEA[$sel]);
			$subdata[4]=$buf[3];
			$subdata[5]=int($ITEM[$buf[3]]->{limit} * $ability / 200);
			}
		}
	main::WriteSea($data);
	main::WriteSeaSub("$DT->{id}-exp$itemno",@subdata);
	return $ret;
}

######################################################################
#★武?艦隊?出迎?
######################################################################
sub meetpp
{
	my $itemno=$USE->{param1};	#派遣??船
	main::RequireFile('inc-sea.cgi');
	my @subdata=main::ReadSeaSub("$DT->{id}-exp$itemno");
	my @ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	my $seaman=$ship[13];		#水夫
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="570"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/harbor.png);" valign="top"><br><br>|;

	if ($main::NOW_TIME < $subdata[0])
		{
		$ret.="已經到港口看過了，船隊還未回來的。<br>";
		$ret.="還是遲點先再來吧。</tr></table>";
		return $ret;
		}
	main::DeleteSeaSub("$DT->{id}-exp$itemno");
	if ($DT->{job} eq 'pros')
	{
	# 海軍??理
	if ($subdata[2])
		{
		$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship2.png">|;
		$ret.="已經是船隊應該回來的時候。<br>";
		$ret.="可是，等了很久船隊還未回來。<br><br>";
		$ret.="難度已埋沒於海裡的碎藻。<br>";
		$ret.="我的海軍是被海盜擊沉了…。<br>";
		$ret.="</tr></table>";
		UseItem($itemno,1);
		delete $DT->{exp}{$itemno};
		main::DeleteSeaSub("$DT->{id}-abi$itemno");
		WriteLog(2,0,$DT->{shopname}.'的海軍因為被海盜強烈攻擊，最終沉沒了。');
		return $ret;
		}
	$seaman=int($seaman * (40 + rand(30)) / 100);
	AddItem(@@ITEMNO "水手",$seaman);
	$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship1.png">|;
	$ret.=main::GetTagImgKao('提督','pro','align="left" ')."<SPAN>提督</SPAN>：我們已經回來。<br>";
	$ret.="因為遇上颱風及海盜，<br>只有$seaman位水手平安回來。<br>";

	if ($subdata[3])
		{
		$ret.="今次已經把海盜的基地破壞了。<br>";
		$ret.=main::GetTagImgItemType(51)."沒收 $subdata[3]枚金幣。<br>";
		AddItem(51,$subdata[3]);
		}
	if ($subdata[4])
		{
		$ret.="因為偵察時遇上海盜，便與他們開戰，我們戰勝了，<br>";
		$ret.=main::GetTagImgItemType($subdata[4]).$ITEM[$subdata[4]]->{name}."了 ";
		$ret.=$subdata[5].$ITEM[$subdata[4]]->{scale}."沒收了。<br>";
		AddItem($subdata[4],$subdata[5]);
		}
	$ret.="以上報告結束。因為貢獻給治安而感到驕傲。";
	$ret.="</tr></table>";
	return $ret;
	}
	# 海賊??理
	if ($subdata[2])
		{
		$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship2.png">|;
		$ret.="已經是船隊應該回來的時候。<br>";
		$ret.="可是，等了很久船隊還未回來。<br><br>";
		$ret.="難度已埋沒於海裡的碎藻。<br>";
		$ret.="我的海盜船是被海軍擊沉了…。<br>";
		$ret.="</tr></table>";
		UseItem($itemno,1);
		delete $DT->{exp}{$itemno};
		main::DeleteSeaSub("$DT->{id}-abi$itemno");
		WriteLog(2,0,$DT->{shopname}.'的海盜船因為被海軍強烈攻擊，最終沉沒了。');
		return $ret;
		}
	$seaman=int($seaman * (40 + rand(30)) / 100);
	AddItem(@@ITEMNO "水手",$seaman);
	$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship1.png">|;
	$ret.=main::GetTagImgKao('提督','pir','align="left" ')."<SPAN>提督</SPAN>：我們已經回來。<br>";
	$ret.="因為遇上颱風及海軍，<br>只有$seaman位水手平安回來。<br>";

	if ($subdata[3])
		{
		$ret.="今次擊沉了不少探險的船。<br>";
		$ret.=main::GetTagImgItemType(51)."領取了 $subdata[3]枚金幣。<br>";
		AddItem(51,$subdata[3]);
		}
	if ($subdata[4])
		{
		$ret.="今次擊沉了不少貿易的船，<br>";
		$ret.=main::GetTagImgItemType($subdata[4]).$ITEM[$subdata[4]]->{name}."了 ";
		$ret.=$subdata[5].$ITEM[$subdata[4]]->{scale}."領取了啦。<br>";
		AddItem($subdata[4],$subdata[5]);
		}
	$ret.="為了下一次更多的金錢，我必須更早休息！";
	$ret.="</tr></table>";
	return $ret;
}

######################################################################
#★開始時??????
######################################################################
sub advice
{
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="570"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/harbor.png);" valign="top"><br><br>|;
	$ret.=main::GetTagImgKao('Hairedin','bal','align="left" ')."<SPAN>Hairedin</SPAN>：；那就好商量了。<br>";
	$ret.="用這個禮物券交換，<BIG>非常重大的選擇</BIG>。<br>";
	$ret.="那麼你便小心看看那一個職業對現時有利吧。<br><br>";
	$ret.="１．<BIG>造船家</BIG>適合初學者，太多<b>造船家</b>則不要做。<br>";
	$ret.="２．<BIG>貿易家</BIG>歐洲<b>海盜出現率</b>可是開始時很容易會無錢。<br>";
	$ret.="３．<BIG>探險家</BIG>歐洲<b>海盜出現率</b>若你去到<b>未走過領域</b>的話便發達了。<br>";
	$ret.="４．<BIG>海盜</BIG>歐洲<b>海軍偵察率</b>若太多海盜也不要做了。<br>";
	$ret.="５．<BIG>海軍</BIG>歐洲<b>海盜出現率</b>若海盜多的話就要做了。<br>";
	$ret.="<br>明白了嗎？不明白的話還可以到<SPAN>圖書館</SPAN>慢慢參考。";
	$ret.="</tr></table>";
	return $ret;
}

######################################################################
#★職業不足?飽和?況
######################################################################
sub jobwant
{
	my %jobwant;
	my $sum;
	foreach my $DT(@DT)
		{
		next if !$DT->{job};
		$jobwant{$DT->{job}}++;
		$sum++;
		}
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="570"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/harbor.png);" valign="top" align="center"><br><br>|;
	$ret.=$main::TB;

	my %jobneed=qw(shipb 10 explore 15 trader 55 pirate 10 pros 10);
	foreach("shipb","explore","trader","pirate","pros")
		{
		$ret.=$main::TR.$main::TDB.$main::JOBTYPE{$_};
		my $i=($sum) ? ($jobwant{$_} / $sum / $jobneed{$_} * 100 * 100) : 100;
		$ret.=$main::TD.main::GetMarketStatusGraph($i).$main::TRE;
		}
	$ret.="</tr></table></tr></table>";
	return $ret;
}

######################################################################
#★万引?
######################################################################
sub stole
{
	return '不能由別人的店舖偷竊，我偷竊失敗了。' if  ($DT->{id} eq $DTS->{id});
	my $ret="偷竊失敗了。賠款了\\500000。";
	if($DTS->{item}[@@ITEMNO"看門狗"-1])
	{
		$DT->{rank}-=int($DT->{rank}/4);
		$DTS->{money}+=500000;
		$DTS->{saletoday}+=500000;
		$DT->{money}-=500000;
		$DT->{paytoday}+=500000;
		WriteLog(3,0,$DT->{shopname}."曾經向".$DTS->{shopname}."進行偷竊，但被看門狗捉到了。");
		WriteLog(3,0,$DT->{shopname}."向".$DTS->{shopname}."賠款了\\500000。");
		WriteLog(0,$DT->{id},$ret);
		return $ret;
	}
	if(rand(1000)>900)
	{
		$DTS->{money}+=500000;
		$DTS->{saletoday}+=500000;
		$DT->{money}-=500000;
		$DT->{paytoday}+=500000;
		$DT->{rank}-=int($DT->{rank}/4);
		WriteLog(3,0,$DT->{shopname}."曾經向".$DTS->{shopname}."進行偷竊但失敗了。");
		WriteLog(3,0,$DT->{shopname}."向".$DTS->{shopname}."賠款了\\500000。");
		WriteLog(0,$DT->{id},$ret);
		return $ret;
	}
	$ret="偷竊成功了";
	my $manbiki_count=0;
	foreach my $idx (0..$DTS->{showcasecount}-1)
	{
		my $itemno=$DTS->{showcase}[$idx];
		if($itemno)
		{
			my $cnt=int($DTS->{item}[$itemno-1]*3/4);
			$cnt=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1] if $DT->{item}[$itemno-1]+$cnt>$ITEM[$itemno]->{limit};
			$DTS->{item}[$itemno-1]-=$cnt;
			$DT->{item}[$itemno-1]+=$cnt;
			$manbiki_count+=$cnt*$DTS->{price}[$idx];
		}
	}
	$main::STATE->{safety}=int($main::STATE->{safety} * 18 / 19);
	WriteLog(2,0,$DTS->{shopname}."總共\\$manbiki_count被偷竊了。") if $manbiki_count;
	WriteLog(2,0,$DTS->{shopname}."偷竊的犯人不知不覺的走了。") if !$manbiki_count;
	WriteLog(0,$DT->{id},$ret);
	return $ret;
}


@@FUNCUPDATE
sub UpdateResetBefore #決算直前??理(??名固定)
{
	UpdateTodayPrize();
	
	sub UpdateTodayPrize
	{
		#賞品授与
		my @TOP123=(
			[
				['禁止的邪惡聖經',	[[@@ITEMNO "禁止的邪惡聖經", 1],			],],
				['看門狗',	[[@@ITEMNO "看門狗", 1],			],],
				['方包',	[[@@ITEMNO "方包", 400],			],],
				['羊羔酒',	[[@@ITEMNO "羊羔酒", 200],			],],
				['廣告塑料袋',	[[@@ITEMNO "廣告塑料袋", 1],			],],
				['禮物券',	[[@@ITEMNO "禮物券", 5],			],],
				['抽獎券',	[[@@ITEMNO "抽獎券", 5],			],],
			],
			[
				['禁止的邪惡聖經',	[[@@ITEMNO "禁止的邪惡聖經", 1],			],],
				['方包',	[[@@ITEMNO "方包", 400],			],],
				['羊羔酒',	[[@@ITEMNO "羊羔酒", 200],			],],
				['廣告塑料袋',	[[@@ITEMNO "廣告塑料袋", 1],			],],
				['禮物券',	[[@@ITEMNO "禮物券", 4],			],],
				['抽獎券',	[[@@ITEMNO "抽獎券", 4],			],],
			],
			[
				['職業的秘密',	[[@@ITEMNO "職業的秘密", 1],			],],
				['方包',	[[@@ITEMNO "方包", 200],			],],
				['羊羔酒',	[[@@ITEMNO "羊羔酒", 100],			],],
				['廣告塑料袋',	[[@@ITEMNO "廣告塑料袋", 1],			],],
				['禮物券',	[[@@ITEMNO "禮物券", 3],			],],
				['抽獎券',	[[@@ITEMNO "抽獎券", 3],			],],
			],
			[
				['職業的秘密',	[[@@ITEMNO "職業的秘密", 1],			],],
				['方包',	[[@@ITEMNO "方包", 100],			],],
				['羊羔酒',	[[@@ITEMNO "羊羔酒", 50],			],],
				['禮物券',	[[@@ITEMNO "禮物券", 2],			],],
				['抽獎券',	[[@@ITEMNO "抽獎券", 2],			],],
			],
		);
		
		TopGetItem($DT[0],$TOP123[0],"今次優勝") if defined($DT[0]);
		TopGetItem($DT[1],$TOP123[1],"可惜2位差") if defined($DT[1]);
		TopGetItem($DT[2],$TOP123[2],"極限的地方得獎") if defined($DT[2]);
	
		for(my $i=9; $i<$#DT; $i+=10)
		{
			TopGetItem($DT[$i],$TOP123[3],"作為特別獎".($i+1)."位") if defined($DT[$i]);
		}
		
		sub TopGetItem
		{
			my($DT,$itemlist,$head)=@_;
			
			my @list=@{$itemlist};
			my @getitem=@{$list[int(rand($#list+1))]};
			
			my $msg=$head.$DT->{shopname}.$getitem[0]."被贈送了";
			WriteLog(0,0,0,$msg,1);
			foreach (@{$getitem[1]})
			{
				my @itemnocount=@{$_};
				
				my $cnt=AddItem($DT,$itemnocount[0],$itemnocount[1]);
				my $ITEM=$ITEM[$itemnocount[0]];
				WriteLog(0,$DT->{id},0,$head."作為獎品".$ITEM->{name}."了".$itemnocount[1].$ITEM->{scale}."獲得了",1);
				$cnt=$itemnocount[1]-$cnt;
				WriteLog(0,$DT->{id},0,"因為是最大所持數".$cnt.$ITEM->{scale}."廢棄了",1) if $cnt;
			}
		}
	}
}

sub UpdateResetAfter #決算直後??理(??名固定)
{
	foreach my $DT (@DT)
		{
		$DT->{profitstock}=5000000 if ($DT->{profitstock} > 5000000);
		$DT->{profitstock}=-1000000 if ($DT->{profitstock} < -1000000);
		if ($DT->{money} > 50000000)
			{
			$DT->{money} -= int( ($DT->{money} - 20000000)/2 );
			$DT->{rank} += int( (10000 - $DT->{rank})/2 );
			$DT->{rank}=10000 if $DT->{rank}>10000;
			PushLog(2,0,$DT->{shopname}.'慶祝會開始了。');
			}
		}
	main::RequireFile('inc-atlas.cgi');
}

@@FUNCNEW

# @@DEFINE Set NewShopMoney NewShopTime NewShopItem ??理
$DT->{money}=@@VALUE"NewShopMoney" if @@VALUE"NewShopMoney";
$DT->{time}=$NOW_TIME-eval(@@VALUE"NewShopTime") if @@VALUE"NewShopTime";
if(@@VALUE"NewShopItem")
{
	my %item=split /:/,@@VALUE"NewShopItem";
	while(my($key,$val)=each %item)
	{
		foreach my $item (@ITEM)
		{
			 $DT->{item}[$item->{no}-1]+=$val,last if $key eq $item->{code} or $key eq $item->{name};
		}
	}
}

# $DEFINE_FUNCNEW_NOLOG=1 ?設定???、????側?最近?出?事新?開店??????抑制???。
# $DEFINE_FUNCNEW_NOLOG=1;
# WriteLog(1,0,0,$DT->{shopname}."??????????",1);

# ??他、新?開店時??自??理?追加????。

@@FUNCSHOPIN

SetUserDataEx($DT,'_so_move_in',$NOW_TIME); # 移?時刻?記?
if($DT->{job} eq 'peddle')
{
	# 行商人(peddle)??移?消費時間?1/2?返還
	$DT->{_MoveTownTime}=int($DT->{_MoveTownTime}/2);
	EditTime($DT,$DT->{_MoveTownTime});
	WriteLog(0,$DT->{id},0,'移換時間一半'.GetTime2HMS($DT->{_MoveTownTime}).'好像結束了',1);
}
if(GetUserDataEx($DT,'_so_present_money'))
{
	WriteLog(0,$DT->{id},0,'從移換原來的街作為餞行\\'.GetUserDataEx($DT,'_so_present_money').'得到了',1);
	SetUserDataEx($DT,'_so_present_money','');
}

@@FUNCSHOPOUT

if(GetUserDataEx($DT,'_so_move_in'))
{
	my $present_money=int(($NOW_TIME-GetUserDataEx($DT,'_so_move_in'))/86400)*5000;
	EditMoney($DT,$present_money); # ?在期間1日?付?\5000?餞別???資金?
	SetUserDataEx($DT,'_so_present_money',$present_money);
	SetUserDataEx($DT,'_so_move_in',''); # $DT->{user}{_so_move_in} ?削除
}

@@FUNCBUY
# package item ??。
# 
# $item::BUY ?利用????。$item::BUY ?構造??????? @@ITEM funcb ???????。
# 商品???理? @@ITEM funcb ?利用??????。

if($BUY->{whole})
{
	if (rand(1000) > 990 && $BUY->{num} > 10)
	{
	$count=AddItemSub(@@ITEMNO"禮物券",1,$BUY->{dt});
	WriteLog(0,$BUY->{dt}{id},'用市場的抽籤禮物券'.$count.'枚得到。');
	$main::ret.='<br>用抽籤禮物券'.$count.'枚得到！';
	}
}

@@END #定義終了宣言(以降????扱?)

