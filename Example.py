import sublime
import sublime_plugin
import os
words_raw = '''
a art.一(个，件，...)
a.b. 文学士
a.d. 公元；(缩)公元
a.m  (缩)上午，午前；ad. 上午，由午夜至中午
a.m. (缩)上午
aback ad. 向后地,朝后地
abacus n.算盘
abandon vt.丢弃；放弃，抛弃
abandoned a. 被抛弃的；无约束的
abandonment n. 放弃,自暴自弃,放纵
abase v. 贬抑，使卑下
abasement n. 贬抑,屈辱,谦卑
abash v. 使局促不安；使羞愧，使窘迫
abashed adj.(在人前) 感觉羞愧的,局促不安的
abate v. 减轻，降低
abatement n. 减少,减轻,缓和
abbe n. 大修道院院长,僧侣,神父
abbess n. 女修道院院长,女庵主持
abbey n. 修道院
abbot n. 修道院院长,方丈,住持
abbreviate vt. 缩写,使...简略,缩短
abbreviation n.节略，缩写，缩短
abc asd
abdicate v. 让位，辞职，放弃
abdication n. 逊位,弃权,辞职
abdomen n. 腹，下腹（胸部到腿部的部份）
abdominal a. 腹部的,腹式呼吸,开腹手术
abduct v. 绑架，拐走
abe 艾贝(人名)
abeam ad. 向着船舷
abed ad. 在床上
aberrant adj. 脱离常轨的；越轨的，异常的
aberration n. 越轨,光行差,心理失常,色差
abet v. 教唆，协助（罪犯）
abettor n. 唆使者
abeyance n. 中止，暂搁
abhor v. 憎恨，嫌恶
abhorrence n. 痛恨
abhorrent adj. 可恨的，可厌的
abide vt.遵守 vt.忍受
abiding a.持久的，永久的
ability n.能力；能耐，本领
abject adj. 极可怜的，卑屈的
abjure v. 誓绝，弃绝
ablaze a. 着火的,闪亮的,激昂的
able adj.有能力的；能干的
ablution n. （宗教的）净礼，沐浴
ably ad. 能干地,巧妙地
abnegation n. 克己，自制
abnormal a.不正常的；变态的
abnormality n. 反常；变态
aboard adv.上船(飞机、车)
abode n. 住处，住所
abolish vt.废除，取消
abolition n. 废除，革除
abolitionist n. 废除主义者,废奴主义者
a-bomb 原子弹
abominable adj. 可厌的，天气极坏的
abominate v. 痛恨；痛恶
abomination n. 憎恨,痛恶,可憎的事物
aboriginal n. 原始居民，土著
aborigine n. 土著居民
aborigines n. 土人,原住民,土生生物
abort v. & n. 中断，故障
abortion n. 流产,堕胎,失败,夭折
abortive adj. 无结果的，失败的
abound v. 充满，富于
about prep.关于；在…周围
above prep.在…上面；高于
aboveboard ad. & a. 照直，公开的
above-mentioned adj. 上述的；以上提到的
abrade v. 磨损，擦伤
abrasion n. 表面，磨损
abreast ad. 并肩地,相并地
abridge v. 删减，缩短
Abridgment n. 删节，节本
abroad ad.(在)国外；到处
abrogate v. 废止，废除
abrogation n. 取消，废除
abrupt a. 突然的,唐突的,无礼的,不连贯的
abruptly adv. 突然地；突然；粗鲁地
abscess n. 脓疮,溃疡
abscond 潜逃，逃亡
absence n.缺席，不在场；缺乏
absent a.不在场的；缺乏的
absentee n. 缺席者,未上班者,不在者
absently ad. 心不在焉地
absent-minded adj. 心不在焉的
absolute a.绝对的；纯粹的
absolutely ad.完全地；绝对地
absolution n. 赦免，免除
absolve vt. 宣告...无罪,赦免,免除
absorb vt.吸收；使专心
absorbent a. 能吸收的
absorbing a. 吸引人的,非常有趣的
absorption n.吸收；专注
abstain v. 自动戒绝，抑制
abstemious adj. 有节制的，节俭的
abstinence n. 节制,禁欲,戒酒
abstract adj.抽象的；深奥的
abstracted adj. 心不在焉的
abstraction n. 抽象化,心不在焉,提炼,抽象派作品
abstruse adj. 难懂的，深奥的
absurd a.不合理的，荒唐的
absurdity n. 荒谬
absurdly ad. 荒诞地
abundance n.丰富，充裕
abundant a.丰富的；大量的
abuse vt.滥用；虐待 n.滥用
abusive a. 辱骂的,滥用的,陋习的
abut v. 接界，毗连
abysmal adj. 无底的；深渊的；极深的，糟透的
abyss n. 深渊，深坑
acacia n. 金合花
academic a.学院的；学术的
academy n.私立中学；专科院校
accede v. 应允，同意
accelerate vt.(使)加快；促进
acceleration n.加速；加速度
accelerator n. 加速者,加速器,油门
accent n.口音，腔调；重音
accentuate v. 着重，强调
accept vt.vi.接受；同意
acceptable a.可接受的，合意的
acceptance n.接受，验收；承认
acceptances 承兑汇票
acceptation n. 公认的意义,词义
accepted 已经接受的
access n.接近；通道，入口
accessary n. 同谋，从犯；附件
accessible adj. 易达到的，易受影响的
accession n. 到达,即位,增加,同意
accessory n.同谋 a.附属的
accident n.意外的；事故
accidental adj. 意外的，偶然的
accidentally adv. 意外地，偶然地；偶尔，附带
acclaim v. 欢呼，称赞
acclamation n. 欢呼
acclimate  v.使习惯于新环境；适应于新环境
acclimatize vt. 使适应新环境,使服水土
acclivity n. 向上的陡坡
accolade n. 推崇备至，赞扬
accommodate vt.容纳；供应，供给
accommodating adj. 乐于助人的
accommodation n.招待设备；预定铺位
accompaniment n. 自然的伴随物,陪伴物,伴奏
accompany vt.陪伴，陪同；伴随
accomplice n. 同谋者，帮凶
accomplish vt.达到(目的)；完成
accomplished a. 完成的,实现的,善社交的,有造诣的
accomplishment n. 技能；成就
accord vt.使一致；给予
accordance n.一致；和谐；授予
accordant 一致的
according ad. 根据
accordingly ad.因此，所以；照着
accordion n. 手风琴
accost vt. 招呼,搭讪,勾引
account n.记述；解释；帐目
accountable a. 有责任的,可说明的,可解释的
accountant n. 会计
accounting n. 会计学,清算帐目
accouter vt. 供以服装,供以军用品,装备
accoutre vt. 供以服装,供以军用品,装备
accoutrements n. (军服武器之外的)装备，配备
accra n. 阿克拉(加纳首都)
accredit vt. 信任,授权,归于,委任
accreditee 信用证受益人(即卖方)
accreditor 开信用证申请人(即买方)
accretion n. 自然的增加，增加物
accrue v. （利息等）增大，增多
accrued adj. 增值的，应计的
acculturation 文化移人，文化适应，文化交流
accumulate vt.积累 vi.堆积
accumulation n. 积累
accumulative adj. 积累的
accuracy n.准确(性)；准确度
accurate a.准确的，正确无误的
accurately adj. 准确地；ad. 准确地；精密地
accursed adj. 不幸的，倒霉的；被诅咒的；可憎的
accusation n. 指控
accuse vt.指责；归咎于
accuser n. 原告,控诉者,非难者
accustom vt.使习惯
accustomed a. 习惯了的
ace n. 幺点,好手,高手,少许
acephalous a. 无头的,群龙无首的
acerbic a. 尖刻的
acerbity n. 苦涩，刻薄
acetate n. 醋酸盐
acetic a. 醋的,酸的
acetylene n. 乙炔,电石气
acetylsalicylic adj. 乙酰水杨酸的
ache vi.痛；想念 n.疼痛
achieve vt.完成，实现；达到
achievement n.完成；成就，成绩
achillean a. 象阿基利斯一样健壮的；勇敢的
aching adj. 疼痛的
acid n.酸；酸的，酸性的
acid-base n. 酸-碱
acidity n. 酸味,酸性
acidulous adj. 有酸味的，刻薄的
acknowledge vt.承认；告知收到
acknowledgment n. 承认,承认书,感谢
acme n. 顶点，极点
acolyte n. (教士的)助手，侍僧
aconite n. 乌头,从乌头的根所提炼的强心止痛剂
acorn n. 橡实，橡子
acoustic adj. 听觉的，有关声音的
acoustics n. 声学
acquaint vt.使认识，使了解
acquaintance n.认识；了解；熟人
acquaintant adj. 熟悉的
acquiesce v. 勉强同意，默认
acquiescence n. 默许,默认,无可奈何的同意
acquiescent adj. 默认的；顺从的
acquire vt.取得；获得；学到
acquired adj. 后天免疫；后天习得的
acquirement n.取得,获得; 习得 (能力)
acquisition n. (有价值的)获得
acquisitive adj. 贪得的，物欲重的
acquit vt. 开释,释放,完成,表现
acquittal n. 宣告无罪，开释
acquittance 清偿；清偿债务的收据
acre n.英亩(=6.07亩)
acreage n. 英亩数,面积
acrid a. 苦味的,辛辣的,尖刻的
acrimonious adj. 尖刻的
acrimony n. 尖刻，刻薄
acrobat n. 特技演员，杂技演员
acrobatic a. 特技表演的,惊险表演的
acrobatics n. 杂技
acronym n. 首字母简略词，简称
acropolis n. 城堡,雅典的卫城
across prep.横过，穿过
act vi.行动；做，做事
acth (缩)肾上腺皮质激素
acting n. 演技；演戏；表演，a. 代理的
action n.行动；作用；功能
activate vt. & n. 使激活，驱动；vt.激活；使活动，使加速；起动；使活泼，开动
active a.活跃的；积极的
actively adv. 积极地，活跃地
activist n. 积极分子
activity n.活动，能动性
actor n.男演员；演剧的人
actress n.女演员
actual a.实际的；现行的
actuality n. 实际
actually adv.实际上
actuals n.现货
actuarial a. 保险统计师的,保险统计的
actuate vt. 开动,促使,激励
acumen n. 敏锐，明智
acupressure n. 针压法
acupuncture n. 针刺；针刺疗法
acute a.尖的，锐的；敏锐的
acuteness n. 锐利,敏锐,剧烈
ad n. (缩)广告
adadon vt. 抛弃，放弃
adage n. 格言，古训
adamant adj. 强硬的，固执的
adamantine a. 非常坚硬的,坚定不移
adapt vt.使适应；改编
adaptability n. 适应性
adaptable  adj. 有适应能力的，能运用的；适应性强的；可改编的
adaptation n. 适应
adapter n. 适配器，转换器
adcolumn 广告栏
add vt.加，增加
add...to 把…加到
addend n. 『数学』加数
adder n. 欧洲产的小毒蛇,北美产的无毒小蛇,
addict vt. 使沉溺,使上瘾
addiction n. 沉迷；热衷；沈溺，上瘾
addictive adj. (毒品等)使人上瘾的
adding 增加的
addition n.加，加法；附加物
additional a.附加的，追加的
additionally ad. 另外，又
additive adj. 附加的；n. 添加剂；附加物
addle v. 使腐坏，使昏乱
addled adj. 头脑混乱的
add-on 加码
address n.地址；演说；谈吐
addressee 收信人
addressing n. 寻址
adduce v. 给予（理由），举出
adenoids n. 腺状肿大,扁桃腺肥大
adenosine n. 腺苷，腺嘌呤核苷
adept adj. 老练的，精通的
adequacy n. 能力
adequate a.足够的；可以胜任的
adequately adv. 恰当地；足够地
adf sadf
adhere vi.粘附；追随；坚持
adherence n. 依附,固执
adherent n. 拥护者，党徒
adhesion n. 附着,粘着,固守,支持
adhesive a. 粘着的,有粘性的
adieu int. 再见,再会
adipose adj. 脂肪多的
adjacent a.毗连的；紧接着的
adjective n.形容词 a.形容词的
adjoin vt.贴近，毗连；靠近
adjourn vi. 延期,休会,换地方
adjournment n. 延期,休会,休会期间
adjudge vt. 宣判,判决,裁定给与
adjudicate v. 充当裁判，判决
adjunct n. 附属物,附件,修饰语
adjuration n. 严令,恳请,请愿
adjure v. 郑重敦促（恳请）
adjust vt.调整，调节；校正
adjustable adj. 可调整的；可校准的
adjustment n. 调节
adjutant n. （军队的）副官，助手
administer vt. 实施，掌管
administrate vt. 管理，经营，实施
administration n.局(或署、处等)
administrative a. 管理的,行政的
administrator n. 管理人,行政官
admirable a. 可钦佩的,优良的,令人惊奇的
admirably ad. 令人钦佩地；极妙地
admiral n. 舰队司令,海军上将,旗舰
admiralty n. 海军上将的地位或职权,海军部,
admiration n.羡慕，钦佩；赞赏
admire vt.钦佩；羡慕；赞美
admirer n. 钦佩者,仰慕者,求爱者
admissible 允许的，可采纳的
admission n.允许进入；承认
admit vt.&vi.承认
admittance n. 入场,入场权,准入
admittedly adv. 公认地；明白地
admixture n. 混合,混合物
admonish v. 训诫，警告
admonition n. 警告,劝告,训诫
admonitory adj. 警告的
ado n. 忙乱，骚扰
adobe n. 泥砖，土坯
adolescence n. 青春期
adolescent n. 青少年(此处是类比)
adopt vt.收养；采用；采取
adoption n.收养；采纳，采取
adorable adj. 迷人的，可爱的
adoration n. 爱慕，崇拜
adore vt.崇拜；很喜欢
adorn v. 装饰
adornment n. 装饰，装饰品
adrenal a. 肾上腺的；n. 肾上腺
adrenalin n. 肾上腺素
adrift ad. 漂流地
adroit adj. 熟练的，灵巧的
adulate v. 谄媚，奉承
adulation n. 谄媚,奉承,阿谀
adult n.成年人 a.成年的
adulterate v. 掺假
adulterated adj. 掺入次级品的
adulteration n. 掺杂,掺假的东西,冒充货
adulterer n. 奸夫
adulteress n. 奸妇
adulterous a. 通奸的,不贞的
adultery n. 通奸
adumbrate v. (对将来事件)预示
adumbration n. 轮廓,预示,阴影
adust a. 烘干的，烤焦的；忧郁的；阴沉的
advance vi.前进；提高 n.进展
advanced a.先进的；高级的
advancement n. 前进,进步
advancing (价格)上涨
advantage n.优点，优势；好处
advantageous a.有利的，有助的
advent n. 到来，来临
adventitious adj. 偶然的，外来的
adventure n.冒险，冒险活动
adventurer n. 冒险家,投机者
adventurous a. 喜欢冒险的,大胆的,惊险的
adverb n.副词
adverbial  adj. 状语的；副词的；n. 状语
adversary n. 对手，敌手
adverse a. 反面的，不友好的
adversity n. 不幸，灾难
advert vi. 注意,留意,言及
advertise vt.通知 vi.登广告
advertise/-ize vi. 登广告，做广告；vt. 为…做广告
advertisement n.广告；公告；登广告
advertiser n. 做广告的人
advertising adj. 广告的；广告，广告费n. (总称)广告；
advice n.劝告；忠告；意见
advisable n.明智的；可取的
advise vt. 忠告，劝告，建议；通知；告诉；通告
adviser n. 顾问,指导教授,劝告者
advisory adj. 劝告的
advocacy n. 拥护,支持,鼓吹
advocate n.辩护者 vt.拥护
aegean a. 爱琴海的
aegis n. 保护，庇护
aeon n. 永世,无数的年代
aerate v. 充气，让空气进入
aerial a.空气的；航空的
aerie n. 鹰巢,高处的房子,高处的城堡
aerodrome n.飞机场
aeronaut n. 气球驾驶员
aeronautics n. 航空学
aeroplane n. 飞机；(英)飞机
aerospace n. 航空和宇宙航行空间；太空，宇宙空间
aery n. 高巢,高处房子,高处的城堡
aesthete n. 审美家
aesthetic a. 美学的；审美的
aesthetics n. 美学
afar ad. 由远处,遥远地
afeared a. 恐惧的
affability n. 和蔼,殷勤,亲切
affable adj. 易于交谈的，和蔼的
affair n.事件；事情
affect vt.影响；感动
affectation n. 做作，虚假
affected adj. 不自然的，假装的
affection n.慈爱，爱；爱慕
affectionate adj. 挚爱的
affectionately adv. 充满深情地；热情地；体贴地；慈爱地
afferent a. 传入的,向心的
affiance n. 信托,婚约
affidavit n. 宣誓书
affiliate n. 分号(公司)；vt. 使…加入；使附于；合并，接纳；分支机构；附属公司；v. 加入联合
affiliation n. 入会，加入
affinity n. 密切关系，吸引力
affirm vt.断言，批准；证实
affirmation n. 肯定,断言,主张
affirmative adj. 赞成的，肯定的
affix vt. 使附于,署名,粘贴
afflatus n. 一阵风，（诗人等的）灵感
afflict vt. 使痛苦,折磨
afflicting 痛苦的
affliction n. 痛苦，折磨
affluence n. 富裕,富足,流入
affluent a. 丰富的,富裕的
afford vt.担负得起…；提供
affordable adj. 买得起的
affray n. 吵架,骚扰,滋事
affright vt. & n. (古)恐吓，恐惧
affront v. 侮辱，冒犯
Afghanistan n. 阿富汗
afield ad. 至野外,在田野,至远方
afire a. 着火的
afloat a. & ad. 漂浮着(的)
afoot a. 徒步的,在准备中,在进行中的
afore ad.prep. 在前
aforesaid a. 上述的,前述的
afraid adj.(表语)怕，害怕
afresh ad. 重新,再度
Africa n.非洲
African a.非洲的 n.非洲人
aft ad. 在船尾
after prep.在…以后；次于
after-dinner 饭后的；晚饭后的
aftermarket n.后继市场；零件市场
aftermath n. 不幸事件之后果，余波
afternoon n.下午，午后
after-service 售后服务
afterthought n. 事后才有的想法,追悔,再思
afterward ad.后来，以后
afterwards ad. 以后，后来，然后
again ad.又一次；而且
against prep.反对；对着
agape ad. 张口发呆地,目瞪口呆地
agate n. 玛瑙
age n.年龄；时代 vt.变老
aged a. 年老的,经过相当岁月的,有...岁的
age-group n.同龄的一群人
ageing n. 老化
agency n.经办；代理；代理处
agenda n. 议程
agent n.代理人，代理商
agglomerate v. 凝聚，结块
agglomeration n. 结块,凝聚,块
aggrandize v. 增大，扩张
aggravate v. 加重，恶化
aggravation n. 更恶化,加厉,恼怒
aggregate v. 集合，合计
aggregated a.聚合的，合计的
aggregation n. 聚集，总合
aggress v. (against)挑衅，攻击；侵略
aggression n. 进攻,侵略
aggressive a.侵略的；好斗的
aggressively ad.积极地
aggressor n. 侵略者,侵略国,攻击者
aggrieve vt. 使委屈,使苦恼,侵害
aggrieved adj. (因受伤害而)愤愤不平的，痛心的
aghast adj. 惊骇的，吓呆的
agile a. 敏捷的,灵活的,轻快的
agility n. 敏捷,灵活,轻快
aging n. 衰老，老化；分期；帐龄分期
agio n. 贴水
agiotage n. 汇兑业务，证券投机
agitate vi. 煽动；鼓动
agitated adj. 被鼓动的，不安的
agitation n.鼓动，煸动；搅动
agitator n. 煽动者
aglow a. 发红的,通红的
agnostic adj. 不可知论的
ago ad.以前
agog adj. 兴奋的，有强烈兴趣的
agonize vt. 使苦恼,折磨
agonizing adj. 使人坐卧不安的；使人痛苦的
agony n.极度痛苦
agrarian a. 有关土地的,耕地的
agree vt.&vi.同意，赞成
agreeable a.惬意的；同意的
agreeably adv. 欣然，依照
agreed adj. 商定的；已同意的
agreement n.协定，协议；同意
agricultural a. 农业的
agriculture n.农业，农艺；农学
agriculturist n.农学家
agronomist n. 农学家
aground ad. 搁浅地,地面上
ague n. 疟疾,打冷颤,发冷
ah interj.啊
aha interj.啊哈
ahead adv.在前面，在前头
ahoy int. 喂
aid n.帮助，救护；助手
aide-de-camp n. 副官,侍从武官
aide-memoire 备忘录
aids n. (缩)艾滋病
ail vt. 使苦恼
ailment n. （不严重的）疾病
aim n.瞄准；目标；目的
aimless adj. 无目的的；没有目标
ain't (同)are not，am not
air n.空气；空中；外观
airborne 起飞；adj. 空气传播的，(部队)空降的
airconditioning n.空气调节
air-conditioning n.空气调节系统
aircraft n.飞机，飞行器
aircrew 机组人员
airdrome n. 飞机场
Airedale  (C)  (又作 Airedale terrier) 爱尔得儿
air-fare 飞机票价
airfield n. 飞机场
air-filled adj. 充满空气的
air-flight n. 班机，航班
air-hostess n. 空中小姐；女乘务员
airing n.通风；讨论
airless adj. 缺少空气的；不通风的
airlift 空运
airline n.航空公司；航线
air-line n. 航空公司
airliner n. 定期班机,客机
airmail n. 航空邮件
airplane n.飞机
airport n.机场，航空站
air-raid n. 空袭
airship n. 飞艇,飞船
airsick 晕机
airsick,seasick,carsick 晕机、晕船、晕车
airtight adj. 密封的
air-tight a. 密封的
airway n. 航线
air-way n. 航空线；航空公司
airy a. 空气的,幻想的,轻快的
aisle n. 走廊,侧廊
ait n. 河中小岛
ajar a. 微开的,半开的,不和谐的
akimbo a. 两手叉腰的
akin a. 血族的,同族的,同种的
al n. 艾尔(男名)
alabama n. 亚拉巴马(州)(美国)
alabaster adj. 雪白的
alacrity n. 敏捷,轻快,乐意
alarm n.惊恐，忧虑；警报
alarming adj. 警告的；引起惊恐的
alas int.唉，哎呀
alaska n. 阿拉斯加(州)(美国)
albany n. 纽约州州城(美国)
albatross n. 信天翁
albeit conj. 纵令…,虽然…,虽则,即
albino n. 白公,白化病者,白化变种
album n.粘贴簿；相册；文选
albumen n. 蛋白,胚乳
albumin n. 蛋白质,蛋白素
alchemist n. 炼丹家
alchemy n. 炼金术
alcohol n.酒精，乙醇
alcoholic n. 酒鬼,酒精中毒的人
alcoholism n. 嗜酒者，酒鬼
alcove n. 凹室，壁龛
aldehyde n. 醛；乙醛
alder n. 赤杨
alderman n. 市府参事,市议员
aldosterone n. 醛固酮
ale n. 淡啤酒
alert a.警惕的；活跃的
alertness n. 警戒,机敏
alexandria n. 亚历山大(埃及港市)
alexandrine n. 亚历山大诗行,这种形式的诗
alfalfa n. 紫花苜蓿
alga n. 水藻
algebra n.代数学
algeria n. 阿尔及利亚
algerian a. 阿尔及利亚的
algiers n. 阿尔及尔
alias n. 化名，别名
alibi n. 不在场证明辩解,托辞
alice 艾莉丝(女名)
alien a.外国的 n.外国人
alienate vt. 使疏远,离间,让与
alienated adj. 疏远的，被隔开的
alienation n. 疏远,离间,割让
alienator 让渡人，转让人
alienee 受让人
alight vi. 落下,偶然发现
align v. & n. 定位，对准；vt. 排列；使成直线；使成一线；使结盟；校准，校直，结盟，合作，调节，调准；vi. 成一线，排成一行，(with)结盟
aligned a. 对准的，均衡的
alignment n.队列；结盟，联合
alike a.同样的，相同的
aliment n. 食物,滋养品
alimentary a. 食物的,滋养的
alimentation 营养
alimony n. 瞻养费
alive adj.活着
alkali n. 碱
alkaline a. 碱的,碱性的
alkalinity n. 碱浓度；碱性
alkaloid n. 生物碱,植物碱基
all adv.都
allan n. 艾伦(姓)
all-around a.全面的；综合性的
allay vt. 使镇静,使缓和
allegation n. （无证据的）指控
allege vt. 宣称,申述,主张,断言
allegiance n. 忠诚，拥护
allegorical a. 寓言的,寓意的,讽喻
allegory n. 寓意；寓言
allen 阿伦(男名)
allergic adj. 过敏性的；变态的；变应性的，对...讨厌的
allergy n. 反感，过敏；过敏性反应，过敏症；厌恶
alleviate v. 缓和，减轻
alley n. 小巷，小径
alliance n. 联盟,联合
allied a.联合的；联姻的
allies n. (一次大战)协约国
alligator n. 短吻鳄（一种鳄鱼）
all-in 全部的，包括一切的
alliteration n. 头韵
all-night a. 通霄的
allo a. 紧密相连的
allocate vt. 分派,分配
allocation n. 分配；配给物；拨款，拨款权，拨给
allonge (法)票据背书附条
allopathy n. (医)对抗疗法
allot vt. 分配,分摊指定
allotment n. 分配,配给的土地,命运
allow vt.允许，准许；任
allowable a. 可允许的,正当的,可承认的
allowance n津贴，补助费
allowed a. 容许的
alloy n.合金；(金属的)成色
all-round a. 全面的；综合性的
allspice n. 甜胡椒,由甜胡椒制成的香味料
allude v. 间接提到，暗指
allure v. 引诱，n. 诱惑力
allurement n. 诱惑物
alluring a. 诱惑的；迷人的
allusion n. 暗示
alluvial adj. 冲积的
ally n.同盟国；同盟者
almanac n. 年鉴,历书
almighty a. 万能的,全能的
almond n. 杏树，杏仁
almoner n. 施赈人员
almost ad.几乎，差不多
alms n. 施舍，捐献，救济金
almshouse n. 私立济贫院或养老院,公立救济院
aloft ad. 在高处,在上
alone a.单独的 ad.单独地
along prep.沿着 ad.向前
alongside prep.在…旁边
aloof a. 远离的；孤零的
aloud ad.出声地，大声地
alp n. 高山
alpaca n. 羊驼,羊驼毛,羊驼呢
alpha n. 希腊字母的第一个字母,最初,
alphabet n.字母表
alphabetical adj.依字母顺序的
alphabetically ad. 按字母表顺序
alpine a. 高山的,极高的
alpinist n. 登山运动员
alps n. (the-)阿尔卑斯山脉
already ad.早已，已经
alsace n. 阿尔萨斯(法国地名)
also ad.亦，也；而且，还
altar n. 祭坛，圣坛
alter vt.改变，变更；改做
alteration n.变更，改变；蚀变
altercation n. 争吵，争论
alternate vt.使交替 a.交替的
alternately ad. 交替地，轮流地
alternation n. 交互,轮流,隔一个
alternative n.替换物；取舍，抉择
alternatively adv. 交互地；交替地；另外，此外；两者择一
although conj.虽然
altitude n.高，高度；高处
alto n. 次高音,女低音,次高音歌手
altogether ad.完全；总而言之
altorf n. 阿尔托夫(瑞士城市)
altorfer n. 阿尔托夫人
altruism n. 利他主义；爱他主义；不自私；无私
altruistic a. 利他的,无私心的
alum n. 明矾
aluminium n.铝
aluminum n. 铝
alumni n. 男校友；男毕业生
alumnus 男校友
alveolus n. 肺泡
always adv.总是，一直
am n. (我)是；v. 是；be的第一人称单数
amaesthetic n.麻醉剂
amain ad. 全力地,全速地,急速地,突然
amalgam n. 混合物
amalgamate v. 合并，混合
amalgamation n. 与汞混合,融合,合并
amanuensis n. 笔记者,抄写员,书记
amaranth n. 不凋花,苋属植物,紫红色
amaranthine a. 不凋的,不死的,紫红的
amass v. 积聚
amateur a.业余的n.业余爱好者
amateurish adj. 业余爱好的，不熟练的
amatory a. 恋爱的,情人的
amaze vt.使惊奇，使惊愕
amazed 惊愕的
amazement n.惊异，诧异
amazing adj. 惊人的；惊奇的；令人惊异的
amazingly ad. 惊人地；惊奇地
amazon n. 女战士
ambassador n.大使，使节
amber n. 琥珀色
ambergris n. 龙涎香
amber-like a. 琥珀色的
ambidextrous adj. 十分灵巧的
ambient a.周围的，包围着的
ambiguity n. 模棱两可
ambiguous a.模棱两可的；分歧的
ambit n. 界限，范围，周围
ambition n.雄心，抱负，野心
ambitions a. 有雄心的，野心勃勃的
ambitious a.有雄心的；热望的
ambivalence n. 有两种相冲突的情感；矛盾心理
ambivalent adj. (对人或物)有矛盾看法的；有矛盾情绪的
amble n./v. 漫步，缓行
ambrosia n. 神仙食品，美味
ambrosial a. 特别美味的
ambulance n.救护车；野战医院
ambulatory adj. 步行的; 移步用的
ambuscade n. 埋伏,伏兵,埋伏处
ambush n./v. 埋伏，伏击
ameliorate vt. 改善；缓和
amelioration n. 改善,改良,改进
amen int. 阿门
amenable adj. 愿服从的，通情达理的
amend vt. 修正,改善,改良
amendment n. 改正，修正
amends n. 赔偿；赔罪
amenities n. 令人愉快之事物
amenity n. 愉快，适意
ament n. 智力缺陷者；精神错乱者
America n.美洲；美国
American a.美洲的 n.美国人
Americanism a. 美国所创,美国风俗,美国精神
Americanization n. 美国化
amerindian n. 美洲印第安人
amethyst n. 紫水晶
amiable adj. 和蔼的，亲切的
amicable adj. 友好的
amid prep. 在...中间
amidships ad. 在船中部,在船腹
amidst prep. 在...当中
amiss a. 有毛病的,出差错的
amity n. 友好,亲善关系
ammonia n. (化)氨
ammonite n. 菊石
ammonium n. 氨盐基,铵
ammunition n. 军火,弹药
amnesia n. 健忘症
amnesty n. 大赦，特赦
amoeba n. 阿米巴,变形虫
among prep.在…之中
amongst prep在…之中(=among)
amoral adj. 不知是非的
amorous adj. 容易动情的，情爱的
amorphous adj. 无定形的，散漫的
amortization  n. 亦作 amortizement
amortize v. 分期偿还
amory n. 艾默利(姓)
amount n.总数；数量；和
amour n. 奸情,恋情
ampere n.安培
ampersand n. &号(and)
amphibian a. 两栖类的,水陆两用的
amphibious a. 水陆两栖,两用的,陆海空军协同作战的
amphitheater n. 圆形剧场,斗技场,似圆形剧场的处所
ample a.足够的；宽敞的
amplification n. 扩大；加强
amplifier n. 放大器
amplify vt.放大，增强；扩大
amplitude n.广大；充足；振幅
amply ad. 充足地,详细地
amputate v. 切除
amputation n. 切断,切断手术
amsterdam n. 阿姆斯特丹(荷兰)
amuck ad. 狂乱地,杀气腾腾地
amulet n. 护身符
amuse vt.娱乐；逗...乐
amusement n.娱乐，消遣，乐趣
amusing adj. 令人感到有趣的；有趣的，逗人笑的；使人发笑的
amy 艾米(女名)
an  art. 一(个，件，…)；(不定冠词，在元音前)；每一；任何一人；一个（本…）
anabolism n. 组成代谢，合成代谢；同化作用
anachronism n. 时代错误；年代错误，落伍之物；落伍
anaemia n. 贫血,贫血症
anaesthesia 麻醉
anaesthetic n. 麻醉剂
analgesia n. 止痛法；无痛
analgesic n. 镇痛剂，adj. 止痛的
analogous adj. 类似的
analogue n. 类似物；同源语；模拟
analogy n.相似，类似；比拟
analyse vt.分析，分解，解析
analyse/-yze vt. 分析，分解
analysis n.分析，分解，解析
analyst n. 分析员
analytic a. 分析的,解析的
analytical a. 分析的,解析的
analyze vt. 分析,分解
anarch  n. 无政府主义者
anarchic adj. 无政府的
anarchist n. 无政府主义者
anarchy n. 无政府，混乱
anathema n. （基督教的）咒诅
anathematize vt.vi. 开除教籍,咒诅,咒逐
anatomical a. 解剖的,解剖学上的,构造上的
anatomically ad. 解剖学上，结构上
anatomist n. 解剖学家
anatomize vt. 解剖,仔细分析
anatomy n. 解剖
ancester n. 祖先
ancestor n.祖宗，祖先
ancestral a. 祖先的
ancestry n. 祖先,家系,门第
anchor n.锚 vi.抛锚，停泊
anchorage n. 下锚,停泊所,停泊税
anchorite n. 隐士
anchovy n. 鱼类
ancient a.古代的，古老的
ancillary adj. 辅助的，n. 助手
and conj.和；又
andesite 中性长石
andiron n. 柴架
andirons n. 铁制柴架
ane n. 烷
anecdote n. 短故事，轶事
anemia n. 贫血，贫血症
anemone n. 秋牡丹,海葵
anesthesia n. 麻醉
anesthesiologist n. 麻醉学家
anesthetic n. 麻醉剂；a. 麻醉的
anesthetist n. 麻醉医生
anesthetize vt. 使麻醉，使麻木
anew ad. 重新,再
angel n.天使，神差，安琪儿
angelic a. 天使的,似天使的
angelical a. 天使的,似天使的
anger n.发怒
angle n.角，角度
angler n.钓鱼者,钓鱼人
Anglo-Saxon n. 盎格鲁撒克逊人
angora n. 安哥拉猫,安哥拉呢,纯毛海
angrily adv.发怒地，愤怒地
angry adj.发怒的，生气的
anguish n. 极大痛苦
anguished adj. 很痛苦的
angular a. 有角的,消瘦的,有尖角的,生硬的
angularity n. 有角,成角状,生硬
animadversion n. 批评,非难
animadvert v. 苛责，非难
animal n.动物，兽 a.动物的
animate vt. 使有活力，激活；使有生气；激励；促使；赋于生命，鼓励，a. 有生命的，有生气的，生气勃勃的
animated adj. 活生生的；栩栩如生的；活跃的；生气勃勃的；有生气的，热烈的；n. 活生生的；能活动的
animatedly adj. 活生生地，热烈的
animating 鼓舞生气的，启发的
animation n. 兴奋，活跃
animosity n. 憎恶，仇恨
animus n. 憎恨
anise n. 大茴香
ankle n.踝，踝节部
annalist n. 纪年表编者,编年史作者
annals n. 纪年表,年鉴,年报
anneal n. 退火
annex vt. 并吞；附加
annexation n. 合并,附加,附加物
annie n. 妮(女名，ann的昵称)；安妮(女名)
annihilate v. 消灭
annihilation n. 歼灭,灭绝
anniversary n.周年纪念日
annotate v. 注解
annotation n. 注解
announce vt.宣布，宣告，发表
announcement n. 公告,发表,告知
announcer n.宣告者；播音员
annoy vt.使恼怒；打搅
annoyance n. 烦恼,可厌之事
annoying a. 恼人的，讨厌的；使人气恼的
annual a.每年的 n.年报
annually ad.一年一次,每年
annuitant 领年金者
annuity n. 年金,养老金,年金领受权
annul v. 宣告无效，取消
annum n.  年,岁
Annunciation n. 报喜,天使报喜节
anode n. 阳极，正极，板极
anodyne n. 止痛药；a. 解除痛苦的
anoint vt. 涂以油或软膏,施以涂油礼
anomalous adj. 反常的，不规则的
anomaly n. 异常、反常
anon ad. 不久,立刻,以后
anonymity  n. 无名，匿名
anonymous adj. 匿名的
anonymously adj. 匿名地
anorexia n. 厌食症
another adj.&pron.再一(个..)
anoxia n. 缺氧症
ansi n. 美国国家标准协会
answer vt.回答；响应；适应
answerable a. 可回答的
ant n.蚂蚁
antagonism n. 对抗，敌对
antagonist n. 敌手，对手
antagonistic a. 反对的,敌对的
antagonize vt. 使成敌人,敌对,反对
antarctic a.南极的 n.南极区
antarctica n. 南极洲；南极洲(与北极相对的地方)
antebellum adj. 战前的
antecedence n. 居先，在先
antecedent n. 前情,先行词
antechamber n. 前堂,前厅,接待室
antedate (在信，文件上)写上较早日期
antediluvian adj. 史前的，陈旧的
antelope n. 羚羊
antenna n.触角；天线
anterior adj. 较早的，以前的
anteroom n. 接待室,前房,休息室
anthem n. 圣歌，赞美歌
anther n. 雄蕊的花粉囊,花药
anthology n. 诗集，文选
anthracite n. 无烟煤
anthrax n. 炭疽热
anthropoid adj. 像人类的，类人猿的
anthropologist n. 人类学家
anthropology n. 人类学
anthropomorphic a. 神人同形同性论的
anti-aircraft n.高射兵器
antibacterial a. 抗菌的；n. 抗菌剂
antibiotic n. 抗生素，adj. 抗菌的
antibiotic-resistant a. 耐抗生素的
antibiotics n. 抗生素；抗菌素
antibody n. 抗体（身体中的抗病物质）
antic adj.古怪的，笨拙的
anticipate vt.预料，预期，期望
anticipation n.期望，预料；预期
anticipatory adj.预期的
anticlimax n. 渐降法,虎头蛇尾
anticoagulant adj. 抗凝的
anti-cowpox a. 抗牛痘的
antics n. 古怪滑稽的动作
antidote n. 解毒药
antigen  n. 抗原(注射于动物体内能使之产生抗体的物质)
antihistamine n. 抗组织胺
antimony n. 锑
antipathy n. 憎恶,反感
antipodes n. 相对极
antiquarian n. 古物研究者,收集古物者
antiquary n. 古物研究者,收集古物者,古董商人
antiquated adj.陈旧的，过时的，
antique a.古代的 n.古物
antiquity n. 古代；古人们
antisepsis n. 防腐法，抗菌法
antiseptic n. 杀菌剂，adj.防腐的
antiserum n. 抗血清
antislavery n. 反对奴隶制度
antisocial a. 反社会的
antithesis n. 对立，相对
antithetic adj. 对立的
antitoxin n. 抗毒素
antler n.鹿角的一枝
antonio n. 安东尼奥(男名)
antonym n. 反义字,反义语,对语
antonymous adj. 反义的
anus n. 肛门
anvil n. 铁砧
anxiety n.焦虑，忧虑；渴望
anxious adj.渴望的；忧虑的
anxiously adv. 焦急地，急切地；不安地；挂念地；渴望地；担心的
any adj.什么,一些,任何的
anybody n.重要人物
anyhow ad.无论如何
anyone pron.任何人
anything pron.任何事(物)
anytime adv. 在任何时候；无论什么时候
anyway ad.无论如何
anywhere ad.在什么地方
aorta n. 主动脉
ap n. (美国)联合通讯社，简称美联社(ap=associated press)
apace ad. 快速地,急速地
apanage n. 属地
apart adv.分别；相距
apartment n. 公寓；一套公寓房间；套房，(美)一套房间；房间，间；公寓住宅，套间
apathetic adj. 冷漠的，无动于衷的
apathy n. 漠然，冷淡
ape n. 猿
aperture n. 孔隙，窄的缺口
apex n. 顶点，最高点
aphasia n. 失语症
aphid n. 蚜虫
aphorism n. 格言
apiary n. 养蜂场
apiculture n. 养蜂业
apiece ad. 每人,每个,各
aplomb n. 沉着，镇静
apocalypse n. 启示,天启
apocalyptic adj. 启示的；天启的；预示灾祸的，预示大动乱
apocrypha n. 伪经，伪书
apocryphal adj.伪经的，假冒的
apogee n. 远地点（太阳等距离地球最远的点）
apolitical adj. 不关心政治的
apollo 阿波罗；n. (希神)阿波罗
apologetic adj.道歉的，歉意的
apologise v.道
apologist n. 辩护者,辩证者,护教论者
apologize vi.道歉，谢罪，认错
apologue n. 寓言,教训
apology n.道歉，认错，谢罪
apoplexy n. 中风
apostasy n. 背教，脱党
apostate n. 背教者，变节者
apostatize 背教，脱党
apostle n. 基督十二使徒之一,最初的传道者
apostolic adj.(十二) 使徒的; 使徒时代的
apostrophe n. 书写中撇号(')（表示省略或所有格）
apothecary n. 药剂师
apothegm n. 格言,箴言
apotheosis n. 神化，典范
appal v. 使惊骇，使恐怖
appall vt. 使胆寒,使惊骇
appalling  adj. 骇人的；令人震惊的；骇人听闻的；可怕的
appanage n.附属物，封地，世袭财产
apparatus n.器械，仪器；器官
apparel n. （精致的）衣服
apparent a.表面上的；明显的
apparently ad. 明显地；外表地；显然，表面上地；adj. 显然，似乎
apparition n. 幽灵，神奇的现象
appeal vi.&n.呼吁；申述
appealing adj. 有吸引力的；吸引人的，打动人心的；招人喜爱的，有感染力的，恳求的
appear vi.出现；显得；好象
appearance n.出现，来到；外观
appease v. 使平静，安抚
appeasement n. 平息，满足
appellant n. 上诉人
appellate a. 控诉的,上诉的
appellation n. 名称，称呼
append vt. 附加,添加,悬挂
appendage n. 附加物
appendectomy n. 阑尾切除术
appendicitis n. 阑尾炎,盲肠炎
appendix n.附录，附属物；阑尾
appertain vi. 附属,关系,适合
appetite n.食欲，胃口；欲望
appetizer n.开胃
appetizing adj.开胃的
applaud vt.喝彩；欢呼vi.欢呼
applause n.喝彩；夸奖，称赞
apple n.苹果
apples 苹果
appliance n.用具，器具，器械
applicable a.能应用的；适当的
applicant n. 申请者,请求者
application n.请求，申请；施用
applied a. 应用的；实用的，适用的，外加的
apply vt.应用，实施，使用
apply...to 把…应用于
appoint vt.任命，委任；约定
appointed 指定
appointment n.任命；约定，约会
apportion vt. 分配
apportionment n. 分配,分摊,分派
apposite adj. 适当的，恰切的.
appositive a. 同位的
appraisal n. 评估；估价
appraise vt. 评价,估价,鉴定
appreciable a.可估价的；可察觉的
appreciably adv. 相当大地
appreciate vt.感激；欣赏
appreciation n.欣赏；鉴别；感激
appreciative adj. 感谢的，赞赏的
apprehend v. 逮捕，恐惧
apprehension n. 焦虑，担忧
apprehensive adj. 恐惧的，担心的
apprentice vt. 使当学徒
apprenticeship n. 学徒的身分,学徒的年限
apprise v. 通知，告诉
approach vt.向…靠近 n.靠近
approachable adj. 可接近的，随和的
approbation n. 称赞，认可，
approbatory adj. 表示赞许的
appropriate a.适当的，恰当的
appropriately ad. 适当地
appropriation n. 拨款，挪用公款
appropriations 拨款
approval n.赞成，同意；批准
approve vt.赞成，称许；批准
approved 已批准的
approximate a.近似的 vt.近似
approximately  adv. 近乎，大约；近似地，几乎正确地；差不多
approximation n. 近似值
appurtenance n. 附属物,附件
appurtenances n. 附属物
apricot n. 杏子,杏色
April n.四月
apron n. 围裙
apropos adj. 适当地，中肯的
apse n. 教堂半圆形的后殿
apt a.恰当的；聪明的
aptitude n. 资质,才能,自然倾向
aptness n. 适合性,倾向,才能
aquamarine n. 海蓝宝石
aquaplane n. (小汽艇拖的)滑水板
aquarium n. 水族馆,养鱼池,玻璃缸
aquatic adj. 水生的，水中的
aqueduct n. 高架渠，渡槽
aqueous a. 水的,水成的
aquiline adj. 鹰的，似鹰的.
arab n. 阿拉伯人；n. & a. 阿拉伯人(的)
arabesque n. 蔓藤图饰
Arabia n. 阿拉伯
Arabian adj.阿拉伯的
Arabic n. 阿拉伯语
arable adj. 可耕的，适合种植的.
arbiter n. 权威人士，泰斗
arbitrage 套利，套汇；种裁，公断
arbitrament n. 仲裁,裁决,裁判
arbitrary a.随心所欲的；专断的
arbitrate v. 仲裁，公断
arbitration n. 仲裁,公断
arbitrator n. 公断人
arbitress n. 女仲裁人
arbor n. 藤架,树,心轴,凉亭
arboreal adj. 树木的
arboretum n. 植物园
arbour n. 藤架,凉亭
arc n.弧，弓形物；弧光
arcade n. 有拱廊的街道；骑楼
arcane adj. 神秘的，秘密的
arch n.拱门 vt.用拱连接
archaeological a. 考古学的,考古学上的
archaeologist n. 考古学家
archaeology n. 考古学
archaic a. 已废的,古老的,古代的
archbishop n. 大教主
archdeacon n. bishop 下一级的圣职者,副监督
archduke n. 大公
arched a. 弓形(结构)的
archer n. （运动或战争中的）弓箭手，射手
archery n. 箭术
archetype n. 原型，典型
archiepiscopal  adj. archbishop (之职位) 的
archipelago n. 群岛
architect n.建筑师
architectural a. 建筑上的
architecture n.建筑学；建筑式样
architrave n. 线脚,框缘,楣梁
archive vt. 归档
archives n. 档案
archway n. 拱门,拱道
arctic a.北极的 n.北极
ardent adj. 热心的，热烈的
ardor n. 热心；热情，狂热；激情
ardour n. 热心，热情
arduous adj. 费力的，艰难的
are  n. (你)是；公亩；v. 是；be的第二人称单复数；vi. 是
area n.地区
arena n. 竞技场
aren't 不是；(同)are not
argent n. 银
Argentina n. 阿根廷
Argentine n. 银,银色素,银色的工艺用材料
argo n. 南船星座
argon n. 氩
argosy n. 大商船
argot n. 隐语,暗语,暗号
arguable a. 可争辩的
argue vi.争论，争辩，辩论
arguement n. 争论，辩论，论据，论点
argument n.辩论；争论，论据
argumentative a. 好辩的,爱穷根究理的,争论的
aria n. 独唱曲，咏叹调
arid a. 干旱的
aright ad. 正确地
arightness 亮度
arise vi.出现；由…引起
arisen arise的过去分词
aristocracy n. 贵族,贵族社会,高级知识份子
aristocrat n. 贵族
aristocratic a. 贵族的,贵族政治的,贵族气派的
aristotle 亚里斯多德
arithmatic 算术
arithmetic n.算术
arithmetical a. 算术的,算术上的
arizona n. 亚利桑那(州)(美国)
ark n. 方舟，避难所
arkansas n. 阿肯色(州)(美国)
arm n.手臂，胳膊
armada n. 舰队
armament n. 军备,武器
armature n. 甲胄,防卫器官,盔甲,电枢
armchair n. 扶手椅子
armful n. 一抱之量
armhole n. 袖孔
armistice n. 休战，停战
armlet n. 臂环,臂钏,小海湾
armor n. 盔甲
armorer n. 兵器制造者,军械修护员
armorial a. 徽章的,家徽的
armory n. 纹章,纹章学,军械库,兵工厂
armour n. 盔甲，装甲；(同)armor，甲胄
armoured a. 穿戴盔甲的；装甲的
armourer n. 兵器制造者,军械修护员
armpit n. 腋窝
arms n. 武器
army n.军队
arnica n. 山金车花
aroma n. 芳香，香气
aromatic adj. 芳香的
arose arise的过去式
around prep.在...周围
arouse vt.唤醒；引起；激起
arraign v. 指责，传讯，弹劾
arraignment n. 提讯,传问,责难
arrange vt.整理，分类，排列
arrangement n.整理，排列；安排
arrant a. 声名狼藉的,极恶的
arras n. 花毯,挂毯
array vt.装扮 n.队列；排列
arrears n. 债，欠债
arrest vt.逮捕，拘留；阻止
arrestment 财产扣押，扣留
arrival n.到达；到来；到达者
arrive vi.到达；来临；达到
arrogance n. 傲慢，自大
arrogant adj. 傲慢的，自大的
arrogantly adv. 傲慢地
arrogate v. 冒称具有……权力
arrow n.箭；箭状物
arrowy a. 矢的,矢状的,矢般迅速的
arroyo n. 小河，小溪，枯干的河道
arsenal n. 军工厂
arsenate n.『化学』砷酸盐
arsenic n. 砒霜，砷
arson n. 纵火、放火
arsonist n. 纵火犯
art n.艺术；美术
arterial a. 动脉的,动脉状的
artery n. 动脉,主流,干道
artesian adj.自流的（井等）
artful a. 巧妙的,狡滑的
arthritis n. 关节炎
artichoke n. 朝鲜蓟
article n.文章，论文；冠词
article-mix 商品组合
articulate v. 清楚说话，接合
articulation n. 关节,接合,清晰发音
artifact n. 制造物；人工制品
artifacts n. 史前古器物
artifice n. 巧办法，诡计
artificer n. 工匠,巧匠
artificial a.人工的；娇揉造作的
artificially ad. 人工地；假地；人造地
artillery n. 大炮，炮兵
artisan n. 工匠；手工艺人
artist n.美术家；艺术家
artiste n. 艺人，技艺家
artistic a.艺术的；艺术家的
artistry n. 艺术才能
artless adj. 粗俗的，自然的
arts 文理科
as conj.因为，由于
as...as 与…一样；象…一样
as...as... 象，如同，与…一样
asbestos n. 石棉
ascend vi.攀登，登高；追溯
ascendancy n. 统治权，支配力量
ascendency n. 优势,优越,权势
ascending a. 增长的，向上的
ascension n. 上升,耶稣的升天
ascent n. 上升攀登
ascertain vt.查明，确定，弄清
ascetic adj. 禁欲的n. 苦行者
asceticism n. 禁欲主义
ascii n. 美国信息交换标准码
ascites n. 腹水
ascribe vt.把…归于
ascription n. 归属
asdf asdf
asean n. (缩)东盟
asepsis n. 无菌，无菌操作
aseptic adj. 无菌的，洁净的
asexually ad.无性地；无性器官地
asgard n. (北欧神话中)仙宫
ash n.灰；灰烬，灰堆
ashamed a.惭愧(的)；羞耻(的)
ashen a. 灰色的,苍白的
ashes n. 灰烬
ashore ad.在岸上，上岸
ashtray n. 烟灰缸
ashtry n.烟灰
ashy a. 灰的,覆盖着灰的,苍白的
Asia n.亚洲
Asian a.亚洲的 n.亚洲人
Asiatic  adj. 亚洲的; 亚洲人的
aside adv.在(到或向)旁边
asinine adj. 愚笨的
ask v.问
ask...for 询问；向…要
askance ad. 斜眼看
askew adj. 歪斜的v. 歪斜，弯曲
aslant ad. 倾斜地
asleep a.睡着的，睡熟的
asp n. 白杨,一种毒蛇
asparagus n. 芦笋（可作蔬菜）
aspect n.方面；样子，外表
aspen n. 白杨
asperity n. 粗鲁，艰苦
asperse 诽谤
aspersion n. 诽谤，中伤
asphalt n. 沥青
asphodel n. 日光兰,常春花,水仙
asphyxia n. 窒息
asphyxiate v. (使)无法呼吸，窒息而死
asphyxiation n. 窒息
aspic n. 肉冻
aspirant n. 有抱负者
aspiration n. 渴望，热望
aspire vi. 热望,立志
aspirin n. 阿斯匹林
ass n.驴；傻瓜，蠢笨的人
assail v. 抨击，猛攻
assailant n. 攻击者
assassin n. 暗杀者,刺客
assassinate vt.暗杀，行刺；中伤
assassination n. 暗杀
assassinator n. 暗杀者
assault vt.袭击；殴打 n.攻击
assay n. 化验,分析
assemblage n. 集合,集会,装配
assemble vt.集合，召集；装配
assembler n. 汇编程序
assembly n.集合；集会；装配
assent v. 同意，赞成
assert vt.断言，宣称；维护
assertion n. 断言,主张
assertive adj. 言语果断的，断言的
assess vt.对(财产等)估价
assessment n.估定；查定；估计数
assessor n. 辅佐人,顾问,估税员
asset n. 财产，可取之处
assets n. 财产，资产
asseverate v. 断言
asseveration n. 断言,誓言
assiduity n. 勤勉
assiduous adj. 勤勉的，专心的
assiduously ad. 勤奋地
assign vt.指派；分配；指定
assign...to 把…分配给
assigned a. 指定的，赋值的
assignment n.任务，指定的作业
assimilate v. 同化，吸收
assimilation n. 同化,同化作用,消化
assist vt.援助，帮助；搀扶
assistance n. 协助,援助
assistant n.助手，助理；助教
assistantship n.助手职
assize n.法令，条令，裁判
associate vi.交往 n.伙伴，同事
associated adj. 联合的；相联的adv. 副的
association n.协会，团体；联合
associative adj. 联想的
assort vt. 分类,配合
assorted  adj. 各种各样的
assortment n. 分类,配合,各色俱备之物
assuage v. 缓和，减轻
assume vt.假定；承担；呈现
assumed a. 假定的
assumption n. 假设
assurance n.保证；财产转让书
assure vt.使确信；向…保证
assured adj. 感到放心的；确实的；自信的，确定的n. 被保险人
assuredly ad. 确实地,无疑地,确信地
assyrian a. 亚述人的；n. 亚述人
aster n. 紫菀
asterisk n. 星号(*)
astern ad. 在船尾,向船尾
asteroid n. 小行星；流星
asthma n. 哮喘症
astigmatic adj. 散光的，乱视的
astigmatism n. 散光
astir a. 活动的,骚动的,起床
astonish vt.使惊讶
astonished 惊讶的；惊异的
astonishing a. 可惊异的
astonishment n.惊奇，惊讶
astound vt. 使惊骇,使大吃一惊
astral a. 星的,多星的,星界的
astray adj. 迷路的，误入歧途的
astride ad. 跨着
astringent adj. 止血的，收缩的n. 收缩剂，止血剂
astrolabe n. 星盘（古代星位观侧仪）
astrologer n. 占星家
astrological a. 占星的,占星术的
astrology n. 占星学，占星术
astronaut n.宇宙航行员
astronomer n. 天文学家
astronomical a. 天文学的,天文数字的,庞大的
astronomy n.天文学
astute adj. 机敏的，精明的
astuteness n. 机敏,精明
asunder adv. 分离，化为碎片
aswan n. 阿斯旺(埃及城市)
asylum n. 避难所，庇护所
asymmetric adj. 不对称的
asynchronous a. 异步的，非同步的
at prep.在
atavism n. 隔代遗传，祖型再现
ate eat 的过去式；eat(吃)的过去式
atelier n. 工作室,画室
atheism n. 无神论，不信神
atheist n. 无神论者
atheistic adj. 无神论者的
atheistical a.无神论的；不信神
athenian a. 雅典(人)的；n. 雅典人
athens n. 雅典(希腊首都)
atherosclerosis n. 动脉硬化
athirst a. 渴望的
athlete n.运动员；田径运动员
athletic a. 运动的
athletics n. 运动，体育
athwart ad. 横过地,斜地
atlanta n. 亚特兰大(美国城市)
Atlantic adj.大西洋的n.大西洋
atlas n. 地图集
atmosphere n.大气；空气；气氛
atmospheric a.大气的；大气层的
atom n.原子
atomic a.原子的；原子能的
atomizer n. 喷雾器,香水喷瓶
atomy n. 微小之物,原子,矮人
atonal adj. (音乐)无调的
at-once-payment 立即付款
atone v. 赎罪，补偿
atonement n. 赎罪，弥补
atop ad. 在顶上
atrium n. 中庭,心房
atrocious adj. 残忍的，凶恶的
atrociously ad. 残暴地
atrocity n. 残暴，暴行
atrophy n./v. 萎缩，衰退
attach vt.缚，系，贴；附加
attache n. 大使随员,大使馆馆员
attached a. 附加的
attachment n.连接物，附件；爱慕
attack vt.&vi.&n.攻击，进攻
attain vt.达到，获得，完成
attainable a. 可到达的,可得到的
attainder n. 剥夺公民权
attainment n. 完成，成就
attaint vt. 宣告剥夺财产权,损坏,玷污
attempt vt.尝试，试图 n.企图
attend vt.出席；照顾，护理
attendance n.到场；出席人数
attendant n.侍者；护理人员
attention n.注意，留心；注意力
attentive a.注意的；有礼貌的
attentively adv. 注意地；关心地；聚精会神地
attenuate v. 变薄，变弱
attest v. 证明
attestation n. 证明，证实；证据
attic n. 阁楼，顶楼
attire v. 穿着，装扮n. 衣服
attitude n.态度，看法；姿势
attorney n.代理人；辩护律师
attract vt.吸引；引起，诱惑
attraction n.吸引；吸引力；引力
attractive a.有吸引力的
attractively ad. 有吸引力地，诱人地
attributable a. 可归于...的
attribute vt.把…归因于 n.属性
attribution n. 归属
attributive adj. 定语的；属性的；n. 定语
attrition n. 消磨，磨损
attune "to	v. 使调和，习惯于"
atypical a. 非典型的
auburn n. 赤褐色
auction n. 拍卖
auctioneer n. 拍卖人
audacious adj. 大胆的，愚勇的
audacity n. 大胆，鲁莽
audible a. 听得见的
audience n.听众，观众，读者
audio a. 成音频率的,声音的
audit v. 审计，核对，旁听
auditing n.审计；查账；决算
audition n. (演员等)试唱
auditor n. 听者,收听者,稽核员
auditorium n. 观众席；礼堂
auditory adj. 听觉的
aug. 八月
auger n. 螺丝钻，钻孔机
aught n. 任何事物
augment v. 增大，增值
augmentation n. 增加
augur n. 占兆官,占卜师,相命者
augury n. 预言，征兆，占卜
August n.八月
aunt n.伯母，婶母，姑母
auntie n. 对；a. unt的亲热称呼
aupair a.国外来的(姑娘)帮助料理家务换取住宿的
aura n. 气味,气氛
aural a.耳的，听觉的
aureole n. 光轮,光环
aureomycin n. 金霉素
auricle n. 外耳
auricular adj. 耳的
aurora n. 极光(南北极夜晚所放彩光)
auroral adj. 北极光的
auscultation n. 听诊
auspice n. 前兆；赞助，主办
auspices n. 资助，赞助
auspicious adj. 幸运的，吉兆的
austere adj. 朴素的，(人)正经的
austerity n. 朴素，艰苦
Australia n.澳大利亚
australian n. 澳大利亚人；澳洲人，adj. 澳大利亚的；澳洲的
Austria n.奥地利
austrian adj. 奥地利的；n. 奥地利人
autarchy 自给自足，闭关自守；n. 独裁；专制
authentic adj. 真正的，原作的
authenticate v. 证明(某物)为真
authenticity n. 确实性,真实性
author n.创造者，创始人
authoritarian a. 要求服从权力的；权威主义的；权力主义的；专制的
authoritative adj. 权威性的，命令式的
authorities n. 当局，权力，权威
authority n.当局，官方；权力
authorization n. 授权，委任状
authorize v. 授权，批准
authorized 核准，认可；授权，委托
authorship n.作家之身分
auto n.(口语)汽车
autobiography n. 自传
autocracy n. 独裁政体
autocrat n. 独裁者
autocratic a. 独裁的,专制的
autograft n. 自体移植(物或术)
autograph n. 亲笔,自署,亲笔签名
autoindex n. 自动变址(数)
automat 自动售货机
automate vt. 使自动化；v. 自动化
automated 自动化的
automatic a.自动的；机械的
automatically ad. 自动地,机械地
automation n. 自动，自动化；自动学
automatism n. 无意识行动(如梦游)
automaton n. 自动机器,机器人
automobile n.汽车，机动车
autonomic adj. 自主的，自发的
autonomous adj. 自治的；自主的；自发；独立的
autonomously ad. 独立地
autonomy n. 自治,自主
autopsy n. 验尸，解剖
autumn n.秋，秋季
autumnal a. 秋的,秋天的
auxiliary a.辅助的；附属的
avail vt.有益于 n.效用
availability n. 有效(性)；可得性；可用性，可供货；可行性，利用率
available a.可利用的；通用的
avalanche n. 雪崩
avant-garde n. 先锋派(艺术流派之一)
avarice n. 贪财，贪婪
avaricious adj. 贪婪的，贪心的
avatar n. 天神下凡,神之化身,具体化
avaunt  int. ((古))去! 走开!
avenge v. 为…复仇，为…报仇
avenger n. 复仇者
avenging a. 报复的
avenue n.林荫道，道路；大街
aver v. 极力声明，断言
average n.平均数 a.平均的
averagely adv. 平均
averse adj. 厌恶的，反对的
aversion n. 嫌恶，憎恨
avert v. 避免,避开
aviary n. 大鸟笼，鸟舍
aviation n.航空，航空学
aviator n. 飞行员
avid adj. 渴望的，热心的
avidity n. 热望,贪婪
avocation n. 副业，嗜好
avoid vt.避免；回避，躲开
avoidable a.可避免的
avoidance n. 避免,避开,逃避
avoirdupois n. 常衡,体重,重量
avouch v. 主张，断言，承认
avow v. 承认，公开宣称
avowal n. 公开承认
avowedly ad. 公然地
avuncular adj. 伯(叔)父的
await vt.等候，期待
awake vt.唤醒 vi.醒
awaken vt.vi. 唤醒,醒来,唤起
awakening n. 唤醒,觉醒
award n.奖，奖品；判定
aware a.知道的，意识到的
awareness n. 意识
away ad.离开，远离；…去
awe v. 敬畏
aweary a. 疲倦的
awe-inspiring adj. 令人敬畏的
awesome adj. 可怕的
awe-struck a. 充满敬畏的
awful a.令人不愉快的
awfully ad.令人畏惧的；很
awhile ad. 片刻,一会儿
awkward a.笨拙的；尴尬的
awkwardly ad. 局促不安地，笨拙地；a. 笨拙地；棘手地
awkwardness n.笨拙，困窘
awl n. （钻皮革的）尖钻
awn n. 芒
awning n. 雨篷，遮阳篷
awoke awake的过去式(分词)
awry adj. 扭曲的，走样的.
ax n.斧子
axe 斧头
axial a.轴的；轴向的
axiom n. 公理，定理
axiomatic adj. 不需证明的，不言自明的
axis n.轴，轴线；第二颈椎
axle n.(轮)轴，车轴，心棒
ay n. 赞成票,投赞成票者
aye n. 赞成票,投赞成票者
azalea n. 杜鹃花
azores n. (pl.)亚速尔群岛
azure adj. 天蓝色的n. 碧空
b.c. 公元前(beforechrist)；(缩)公元前
b.m. 医学士
b/l n. (缩)提单
baa n. 羊叫声
babble v. 说蠢话，牙牙学语
babbler n. 爱唠叨的人
babe n. 小孩,缺乏经验的人
babel n. 巴别塔
baboon n. 狒狒
baby n.一家中年龄最小的人
babyhood n. 婴儿时代,婴儿,幼稚
Babylon n. 巴比伦,罪恶
Babylonian a. 巴比伦的,罪恶的
baby-sit vi. 担任临时保姆,照顾婴儿
baby-sitter n. 看顾小孩的人
bacchanal n. (行为放纵的)狂欢会
bacchanalian adj. 饮酒狂欢的；行为放纵的
bachelor n.未婚男子；学士
bacillus n. 杆状菌,细菌
back adv.回(原处)；向后
backbite vt. 背后诽谤
backbone n. 脊椎,志气,骨干,支柱
backdate v. 回溯
backgammon n. 西洋双陆棋戏
background n.背景，后景，经历
backing n. 衬背,后援,支持者
backlog n. 未交付的订货；储备积累
backs 假美钞
backslide vi.n. 堕落,退步,背离宗教
backspace v. 退格，回退
backtrack 向下顶替
backup n. 备份，后备，后援
backward a.向后的；倒的 ad.倒
backwardation 现货升水；交割延期费
backwardness n. 落后；落后(状态)
backwards ad. 向后
backwater n. 回水处，回水；死水
backwoods n. 未开垦地,边远地区的人
backwoodsman n. 住在边远地区的人
back-yard n. 后院
bacon n.咸猪肉，熏猪肉
bacteria n.细菌
bacterial a. 细菌的
bacteriologist n. 细菌学家
bacteriology n. 细菌学
bacterium n. 细菌；拳击迷
bad a.坏的，恶的；严重的
badge n.徽章，像章；标志
badger v. 一再烦扰，一再要求
badly adv.坏；恶劣地
badminton n.羽毛球
bad-mouth 说坏话
bad-tempered adj. 脾气坏的
baffing 令人迷惑的
baffle vt.使挫折 n.迷惑
baffling adj. 令人困惑的
bag n.提包，口袋，书包
baggage n.行李
baggy adj. 袋状的
baghdad n. 巴格达(伊拉克首都)
bagman 行商，推销员
bagpipe n. 风笛
bah int. 呸!
bail n. 保释,把手,栅栏,桶箍
bailee 受托人
bailer 委托人
bailiff n. 执行官,法庭监守,镇长
bailment 财物委托
bairn n. 小孩
bait n.饵；引诱物
baize n. 厚羊毛毯,粗呢
bake vt.烤，烘，焙；烧硬
baker n. 面包师
bakery n. 面包店
baking n. & a. 烘烤(的)
balance vt.使平衡；称 n.天平
balanced a. 均衡的
balcony n.阳台；楼厅，楼座
bald a.秃头的；无毛的
baldric n. 佩饰,肩带
bale n. 大包裹，灾祸，不幸
baleen n. 鲸须
baleful adj. 邪恶的，恶意的
balk v. 阻止，妨碍
ball n.球
ballad n. 歌谣，小曲
ballast n. (船等)压舱物
ballerina n. 芭蕾舞女演员
ballet n.芭蕾舞；舞剧
balloon n.气球
balloon-borne a. 气球运载的
ballooning n. 热气球飞行运动；股票上涨，非法操纵价格
ballot n. 投票,投票用纸,抽签
ball-pen n. 圆珠笔
ballroom n. 大舞厅
ball-shaped a. 球形的
bally 理货，点数
ballyhoo 招徕生意的广告
balm n. 香油，药膏
balmy adj. (气候)温和的，芳香的
baloon 气球
balsam n. 香油,产香油的树,香膏
baltic a. 波罗的海的
baltimore n. 巴尔的摩(美国城市)
balustrade n. 栏杆
bamboo n.竹；竹杆，竹棍
bamboo-shoot n. 竹笋
ban n. 禁令
banal adj. 陈腐的
banality n. 陈腐，平庸
banana n.香蕉
band n.乐队；带；波段
bandage n.绷带，包带
bandanna n. 印花大手帕
bandbook n. 手册，指南
bandit n.土匪，盗匪，歹徒
bandy a. 向外弯曲的
bane n. 祸根
baneful adj. 有害的，致祸的
bang n.巨响，枪声；猛击
banish v. 放逐，摒弃
banishment n. 放逐,驱逐
banister n. (楼梯的)栏杆
banjo n. 班卓琴
bank n.银行；库；岩，堤
bank-book 银行存折
banker n.银行家
banking n. 银行业
banknote n. 纸币；钞票
bankrupt a.破产的 vt.使破产
bankruptcy n. 破产
banner n.旗；旗帜
bannock n. 一种薄饼
banquet n.宴会，盛会，酒席
bantam n. 矮脚鸡
banter n./v. 嘲弄，戏谑
bantering adj. 嘲弄的
baptism n. 施洗,洗礼
baptismal a. 洗礼的
Baptist n. 施洗者约翰,施洗者,浸信会教友
baptistery n.洗礼所
baptize vt. 施洗礼,提炼,命名
bar n.酒吧间；条，杆；栅
barb n. （鱼钩的）倒钩
barbarian n. 野蛮人
barbaric a. 野蛮的,粗野的
barbarism n. 野蛮,未开化
barbarity n. 残忍，残暴
barbarous adj. 野蛮的，残暴的
barbecue n. 烤肉架，烤肉
barbed adj. 有倒钩的，讽剌的
barber n.理发师
barberry n. 伏牛花,伏牛花子
barcelona 巴塞罗纳(西班牙城市)
bard n. 古代的游吟诗人，护马甲
bare a.赤裸的；仅仅的
barefoot adv.&adj.赤脚(的)
barefooted ad. & a. 赤脚(的)
bareheaded a. 不戴帽子的
barely ad.仅仅，勉强
bareness n. 赤裸,裸露
bargain n.交易 vi.议价；成交
barge n.驳船；大型游船
bargemaster n. 驳船主
bark vi.吠叫
barley n.大麦
barn n.谷仓；牲口棚
barnacle n. 一种北极鹅,藤壶
barnyard n. 仓前，空前
barograph n. 自动记录式气压计
barometer n.气压计，睛雨表
barometer/-tre n. 晴雨表，气压表
baron n.男爵；贵族；巨商
baroness n. 男爵夫人,女性男爵
baronial a. 男爵的,适于男爵的,宏大的
barony n. 男爵的领地
baroque n./adj. (艺术、建筑等)高度装饰的，过份雕琢的
barrack n. 兵营；vt. 使驻兵营内
barracks n. 兵营
barrage n. 火力网，弹幕
barrel n.桶；圆筒；枪管
barrels 大桶
barrel-shaped adj. 筒状的
barren a.贫瘠的；不妊的
barrenness n. 不妊；不毛；无趣味
barrette n. 夹子的一种
barricade  n. 障碍物；栅栏 v. 设栅阻挡
barrier n.栅栏，屏障；障碍
barrio n. 大城市郊外
barrister n. 法庭律师,律师
barrow n. 搬运架,手推车,古墓
barter v. 以物易物，物物交换
barterer n. 交易商
barton n. (庄园中的)农场
basal a. 基础的,基本的
basalt n. 玄武岩
base n.基础；基地，根据地
baseball n.棒球；棒球运动
baseless a. 无根据的
basement n.地下室；地窖；底层
bashful adj. 害羞的，羞怯的
bashfulness n.羞怯
basic a.基本的，基础的
basically  adv. 基本上，主要地；事实上；基本地
basil n. 罗勒
basilica n. 长方形会堂,长方形教堂
basilisk n. 蛇怪
basin n.水盆，面盆
basis n.基础，根据
bask v. 晒太阳，取暖
basket n.篮，篓，筐
basketball n.篮球；篮球运动
basket-work n. 枝条编织物
bass n. 低音乐器；男低音
bassanio n. 巴萨尼奥(男名)
bassinet n. 摇篮,摇篮车
bassoon n. 低音管，巴松
basswood n. 椴木
bast n. 树的内皮,韧皮
bastard n. 私生子,劣货,庶子
baste v. 倒脂油于(烤肉上，以防烤干)
bastion n. 棱堡,阵地工事
bat n.蝙蝠
batch n. 一批，大量
bate v. 减少，降低，衰落
bath n.浴，洗澡；浴缸
bathe vt.给…洗澡；弄湿
bath-house n. 澡堂
bathrobe n. 浴衣
bathrom n.浴室；盥洗室
bathroom n.浴室；盥洗室
bathtub n. 浴缸
batiste n. 薄织的麻布
baton n. 指挥棒，警棍
battalion n. 营,军队,集团
batten n. 板条,木条
batter n. 内倾,击球手
battery n.炮兵连；兵器群
batting n. 打球,打击,棉絮
battle vi.战斗 vt.与…作战
battle-ax n. 战斧
battle-axe n. 战斧
battledore n. 羽毛球拍
battlefield n. 战场,沙场
battleground n. 战场,战地
battlement n. 城垛,防卫墙
battleship n. 战舰,主力舰
bauble n. 廉价珠宝
baulk n. 障碍,错误,失败
bauxite n. 铝土岩(产铝的矿土，石)
bawdy adj. 淫猥的、下流的
bawl v. 大叫，大喊
bay n.海湾
bayberry n. 月桂树的果实
bayonet n.(枪上的)刺刀
bayou n. 海湾,支流,河口
bazaar n. 集市，廉价商店；商店集中区
b-complex 复合维生素b
be aux.v.&vi.是，在，做
beach n.海滩，湖滩，河滩
beacon n. 信号灯，闪光灯
bead n.有孔小珠；露珠
beading n. 珠或制珠的材料
beagle n. 小猎犬,间谍,侦探
beak n. 鸟嘴
beaker n. 大酒杯，有倒口的烧杯
beam n.梁；横梁；束，柱
beaming a. 笑吟吟的
bean n.豆，蚕豆
beanstalk n. 豆茎
bear n.熊；粗鲁的人
beard n.胡须，络腮胡子
beardless a. 无须的,年轻的
bearer n. 搬运者
bearing n.支承；忍受；方位
bearish adj. 熊市的；卖空的，行情看跌的
beast n.兽，野兽；牲畜
beastly a. 如兽的,残忍的,令人不愉快的
beat vt.&vi.打，敲；打败
beaten a. 被打败了的,筋疲力竭的,敲平的,
beater n. 搅拌器
beatific adj. 祝福的，有福的
beating n. 打,挫败,搏动
beatitude n. 至福，十分幸福
beatles 披头士乐队
beau n. 花花公子，好打扮者
beauteous a. 美丽的
beautician n.美容师
beautifier n. 美化者
beautiful a.美的，美丽的
beautifully ad. 美丽地；优美地
beautify vt. 美化,变美,修饰
beauty n.美；美人
beaver n. 海狸
becalm vt. 使安静,因无风而使停航
became  become(变得，成为)的过去式
because conj.因为
beck n. 点头示意,招手,小河
beckon vt.vi. 招手,召唤
become vi.变成；成为，变得
becoming a. 合适的,适当的
bed n.床
bedaub v. 弄污，乱涂，过分的装饰
bedclothes n. 铺盖,床单被褥类
bedding n. 被褥,寝具,基础,床上用品
bedeck vt. 装饰,修饰
bedew vt. 沾湿
bedfellow n. 同床者,伙伴
bedford n. 贝德福德
bedim vt. 使模糊,使昏暗,使朦胧
bedizen vt. 俗丽地穿着
bedlam n. 疯人院，喧闹
bedraggle vt. (在泥水中)拖湿
bedraggled adj. （衣服、头发等）弄湿的，凌乱不堪的
bedridden a. 卧床不起的
bedrock n. 基岩
bedroom n.卧室
bedsheet n. 床单
bed-sheet n. 床单
bedside n. 床边
bed-sit n.卧室兼起居室
bedspread n. 床单,床罩
bedstead n. 床架
bedtime n.就寝时间
bee n.蜜蜂
beech n. 山毛榉,其木材
beechen a. 山毛榉制的
beef n.牛肉
beefsteak n. 牛排
beekeeper n. 养蜂人
been vi. be(是；在)的过去分词
beep n. 蜂鸣声，嘀嘀声
beeper n.给无人驾驶飞机发送信号的装
beer n.啤酒
beeswax n. 蜂蜡,蜜蜡
beet n. 甜菜
beethoven 贝多芬(德国大作曲家)
beetle n.甲虫；近视眼的人
beetling a. 突出的
beetroot n. 甜菜根
befall vt. 降临到…(指坏事)；发表(于)
befallen befall的过去分词
befell befall的过去式
befit vt. 适合,适宜,合适
before prep.在…以前；向…
beforehand ad.预先；提前地
befriend vt. 待人如友,帮助
befuddle 使昏乱
beg vt.&vi.请求，乞求
began begin的过去式；开始
beget v. 产生，引起
beggar n.乞丐，穷人
beggarly a. 象乞丐的,赤贫的
beggary n. 赤贫
begin vi.开始 vt.开始
beginner n.初学者，生手
beginning n.开始，开端；起源
begirt  v. begird 的过去式.过去分词
begone vi. 走开
begonia n. 秋海棠属的植物,秋海棠
begot beget的过去式(分词)
begrime vt. 弄脏
begrudge v.羡慕，嫉妒； 吝啬，勉强给
beguile v. 欺骗，诱骗
beguiling adj. 欺骗的，迷人的
begun begin 的过去分词；开始
behalf n.利益，维护，支持
behave vi.表现，举止；运转
behavior n.行为，举止，态度
behaviour n. 行为，举止；表现，(机器等的)运转达情况
behead vt. 斩首,砍头
beheld behold的过去式(分词)
behemoth n.巨兽
behest n. 命令，训喻
behind prep.在…后面
behindhand a. 迟的,落后的
behold v. 目睹，看见
beholden a. 负有义务的,有所亏欠的
beholder h. 目睹者
behoof n. 好处,利益
behoove v. 理应；有益于
behove vt. 理应,应该
behrman 贝尔曼(人名)
beijing n. 北京
being n.存在；生物；生命
beings n. 人
belabor vt. 痛打
belabour v. （过份冗长地）做或说，痛打 -> belabor
belated a. 迟来的
belch v. 打嗝，喷出
beleaguer v. 围攻
belfast n. 贝尔法斯特(英国)
belfry n. 钟楼,钟塔
belgian  n. 比利时人； a. 比利时的，比利时人的
belgium  n. 比利时(欧洲)
beliaiev 别利亚耶夫
belie v. 掩饰，证明为假
belief n.相信；信念；信仰
believe vt.相信；认为
believer n. 信徒
belike ad. 恐怕,或许
belittle v. 轻视，贬抑
bell n.铃，钟
belladonna n. 颠茄
belle n. 靓女
bellicose adj. 好战的，好斗的
belligerent adj. （国家等）交战的，挑斗的
bellman 为客人提行李的男服务员
bellow vi.vt. 怒吼
bellows n.风箱；减压舱
bell-shaped a. 铃状的
belly n. 腹部,食欲
belong vi.属于，附属
belongings n. 所有物，财产
beloved a.为…的爱的 n.爱人
below adv.在下面；向下
belt n.带，腰带；皮带；区
bemoan vt. 惋惜,认为遗憾,哀叹
ben n. (苏格兰)内室
bench n.长凳
bencher n. 坐凳子的人,法学院的老资格,
bend vt.使弯曲 vi.弯曲
beneath prep.在…下方
benedicite n.『基督教』万物颂
Benedictine n. 圣本铎修会的僧,一种甜酒
benediction n. 祝福，祈祷
benefaction n. 善行,恩惠,施舍
benefactor n. 行善者，捐助者
benefactress n. 女施主,女恩人
benefice n. 僧侣之禄,圣俸,有俸圣职
beneficence n. 仁慈,善行,赠物
beneficent a. 仁慈的,慈善的,善行的
beneficial a.有利的，有益的
beneficiary n. 受惠者，（遗产的）受益人
benefit n.利益；恩惠；津贴
benevolence n. 善心，仁心
benevolent adj. 慈善的，好意的
benficial a.有益的，有利的
bengal n. 孟加拉(亚洲)
benighted adj. 愚昧的
benign adj. 慈祥的
benignant a. 仁慈的,和蔼的,有益的
benignity n. 温和，仁慈
benison n. 祝福,祝祷
benjamin n. 男紧身大衣
bent a. 弯曲的,决心的
benumb vt. 使无感觉,使迟钝,使麻木
benumbed a.麻木
benzene n. 苯
benzol n.(粗制) 苯
bequeath v. 遗赠（留）
bequest n. 遗产，遗赠物
berate v. 猛烈责骂
bereave v. 丧亲，夺去
bereavement n. 丧失
bereft adj. 被剥夺的；bereave的过去分词
berg n. 冰山
berlin n.柏林(德国首都)
berore pren. 在…以前；ad. 以前，前面
berry n.浆果(如草莓等)
berserk adj. 狂怒的，疯狂的
berth v. （船）停泊
beryl n. 绿玉石,绿宝石
beseech v. 祈求，恳求
beseem vt.vi. 适合于
beset vt. 围攻,使苦恼,镶嵌
beshrew v. 诅咒
beside prep.在…旁边
besides prep.除...之外
besiege v. 围攻，困扰
besieger n. 围攻者,围攻军
besmear vt. 涂,弄脏
besmirch v. 诽谤，玷污
besought beseech过去式(分词)
bespangle vt. 以小亮片装饰
bespeak v. 显示，表示
besprent a. 撒满的
best adj. 最好的；最大的； adv. 最好地；最好；最佳；最好的人(东西等)；最，极；vt. 打败，战胜
bestial a. 似野兽的,残忍的,卑劣的
bestow vt.把…赠与
bestride vt. 跨骑,跨坐,跨过,控制
best-selling adj. 畅销的
bet vt.&vi.&n.打赌
beta 希腊文的第二个字母β
betake vt. 去,赴,致力于,使用
bethel n. 圣地,礼拜堂,非国教徒的礼拜堂
bethink vt. 想起；思考
bethune n. 白求恩
betide vt. 发生于
betimes ad. 早,及时,及早
betoken vt. 预示
betray vt.背叛；辜负；泄漏
betrayal n. 背叛,叛国
betroth vt. 订婚,许配
betrothal n. 婚约
better adj.较好的，(健康状况)好转的；更好的；adv. 更好地；较佳的；更多地；改进；较好；好些，更好些
betterment n. 改进,改善,涨价
better-off adj. 经济情况较好的
better-trained adj. 受过较好训练的
betty 贝蒂(女名)
between prep.在…中间
bevel n. 斜角,倾斜,斜角规
beverage n. （水，酒等之外的）饮料
bevy n. 一群（少女或鸟）
bewail vt.vi. 悲悼,哀泣,叹惜
beware vt.&vi.谨防，当心
bewilder vt.迷惑；弄糊涂
bewildering  adj. 令人无所适从的；使迷惑，使糊涂
bewilderment n. 困惑,迷乱
bewitch vt. 施魔法于,迷惑,使着迷
bewray v. 泄露，暴露
bey n. 州长,在土耳其对于要人的尊称,
beyond prep.在…的那边
biannual 一年两次的，半年一次的
bias n. 偏见,斜线
bib n. 围兜
Bible n.基督教《圣经》
biblical a. 圣经的
bibliography n. 文献学，
bibulous adj. 高度吸收的，嗜酒的
bicameral a. 两院制的,有两个议院的
bicarbonate n. 重碳酸盐
biceps n. 双头肌,筋力,强健的筋肉
bicker n./v. 争吵，口角
biculturalism a.双文化(生存或适应)能力
bicycle n.脚踏车，自行车
bid vt.命令 vi.报价
bidder 报价人，投标人
bidding n. 命令,邀请,出价
bide  vt. 等待 (wait)
biennial n. 二年生植物,二年一次的事
bier n. 棺材
bifurcate v. 分为二支，分叉
bifurcated adj. 分为两部分
big adj.大的
bigamy n. 重婚,重婚罪
bigger adj. 大一些的
bight n. 海湾,绳圈
bigness n. 大,伟大,重大
bigot n. （宗教，政治等的）盲信者，顽固者
bigoted a. 固执己见的,执迷的,顽固的
bigotry n. 顽固，偏狭
bike n.自行车
bilateral a. 有两面的,双边的,双方的
bile n. 胆汁
bilge v. 鼓账，突出，（船底）穿洞
biliary a. 胆的；胆汁的
bilingual adj. (能说)两种语言的
bilingualism n.熟谙两种语言(的能力)
bilious adj. 多胆汁的，坏脾气的
bill n.账单；招贴；票据
billboard n. 布告板,揭示栏,广告牌
billet n. 兵舍,军营,木柴块
billiards n. 台球
billingsgate n. 伦敦的鱼市场,粗暴话,骂人话
billion num.万亿(英)
billionth num. 第一万亿
billow n. 巨浪
billowy a. 巨浪似的,汹涌的
bin n. 箱柜
binary a. 二进位的,二元的
bind vt.捆，绑
binder n. 缚者,用以绑缚之物,夹器
binding a. 有约束力的；捆绑的；n. 装订； 捆绑(物)
bine n. 茎
binoculars n. 双眼望远镜
binomial a. 二项的,二项式的,二种名称的
biochemical a. 生物化学的，生化的
biochemistry n. 生物化学
biodegradable a. 能被生物分解成无害物的
bio-engineered a.通过生物工程加工的
biographer n. 传记作者
biographical a. 传记(体)的
biography n. 传记；志
biological a. 生物的
biologist n. 生物学家
biology n.生物学；生态学
bios n. 基本输入/输出系统
biosphere n. 生命层，生物圈
biotechnology n.生物技术
birch n. 桦树，赤杨
bird n.鸟，禽
birdcage n. 鸟笼
birdie n. (儿语)小鸟
birds n. 家禽
birmingham n. 伯明翰(英国城市)
birth n.分娩；诞生；出身
birthday n.生日
birthplace n. 诞生地
birthright n. 与生俱来的权力
biscuit n.(英)饼干；(美)软饼
bisect vt.vi. 切成两分,对分
bishop n.(基督教的)主教
bishopric n. 主教的职位,主教的辖区
bismuth n. 铋
bison n. 野牛
bit n.一点，一些
bitch n. 母狗,母狼,母狐
bite vt.咬，叮，螫；剌穿
biting a. 刺痛的,辛辣的
bits n. 小片，少许
bitten bite的过去分词
bitter a.痛苦的；严寒的
bitterly ad.苦苦地；悲痛地
bittern n. 鹭鸶,盐卤
bitterness n.苦味，辛酸，苦难
bitumen n. 沥青
bituminous a. (含)沥青的
bivalve n. 双壳贝
bivouac n. 露营，露宿
biz (美)商业(新闻组)
bizarre adj. 奇异的，古怪的
blab v. 泄密
black adj.黑色的
blackamoor n. 黑人,皮肤黑的人
blackberry n. 黑莓,悬钩子
blackbird n. 山鸟类
blackboard n.黑板
blacken vt. 使变黑,诽谤
blackened a. 熏黑了的，抹黑了的
blackguard n. 无赖,流氓
blackmail n./v. 敲诈，勒索
blackman n.黑人
blackness n. 黑,黑色,阴险
blackout n. 灯光转暗，变黑，灯火管制，一时的眩晕
Blackpool (英国城市名)黑潭
blacksmith n.铁匠
bladder n. 膀胱
blade n.刀刃，刀片；叶片
blame vt.责备，把…归咎于
blameless a. 无可责难的,无过失的,清白的
blanch v. 使变白，（脸色）变苍的
bland adj. （人）情绪平稳的，（食物）无味的
blandishment n. 甜言蜜语,谄媚,奉承
blandishments n. 甘言劝诱
blank a.空白的 n.空白
blanket n.毛毯，毯子，羊毛毯
blanknote 空白支票
blare v. 高声鸣叫
blarney n. 奉承话，谄媚
blase adj. 对享乐感到厌倦的，无动于衷的
blaspheme vt.vi. 亵渎
blasphemous adj. 对神不敬的
blasphemy n. 亵渎，渎神
blast n.管乐器的声音
blatant adj. 喧哗的，无耻的
blaze vt.使燃烧 vi.燃烧
blazon vt. 以家徽装饰,宣布
blckage n.阻塞，堵
bleach vt.漂白 vi.变白
bleachers n. （球场的）露天座位
bleak a. 荒凉的
blear a. 朦胧的,模糊的
bleat n. 羊的鸣声
bleed vi.出血，流血；泌脂
bleeding a. 流血的
blemish v. 损害，玷污n. 瑕疵，缺点
blench v. 退缩，畏缩，回避，使变白
blend vt.&vi.&n.混和
bless vt.保佑；降福
blessed a. 享福的；神圣的
blessedness n. 幸福
blessing n. 祝福
blest bless的过去式(分词)
blew blow的过去式；吹
blight n. 植物枯萎病v. 使…枯萎
blighted adj. 毁灭的
blind n.百叶窗；窗帘；遮帘
blindfold n. 眼罩,障眼物
blindly ad. 盲目地；没头脑地；轻率地
blindness n. 盲目,失明,愚昧
blinds n. 百页窗
blink vi. 眨眼睛
blinking n. 闪烁
bliss n. 福佑,天赐的福
blissful a. 充满喜悦的
blister n. 水泡
blithe adj. 快乐的，无忧无虑的
blithesome a. 愉快的,高兴的
blizzard n. 暴风雪
bloat vt. 使膨胀,腌制
bloated adj. 发胀的；肿胀的
bloc 集团
block n.阻塞；障碍物；炮闩
blockade n./v. 封锁
blockage n. 封锁；障碍
blockhead n. 笨蛋,傻子
blockhouse n. 碉堡,防舍
blocky adj. 短而粗的，浓淡不匀的
blond n.白肤金发碧眼的人
blonde a. n. 金发碧眼的（女子）
blood n.血
blooded 血的
bloodhound n. 侦探犬
bloodless a. 无血色的,不流血的,没精神的
bloodshed n. 流血
bloodshot a. 充血的
bloodstream n. 血流
bloodsucker n. 吸血动物,水蛭,剥削他人者
bloodthirsty a. 嗜杀的,残忍的
bloody a. 血腥的,嗜杀的,非常的,有血的
bloom vi.开花 n.花；开花
bloomer n.开花的植物
bloomers n. 灯笼裤
blooming a. 正开花的；妙龄的
blossom n.花，开花 vi.开花
blot n. 污点,墨水渍
blotch n. （皮肤上的）红斑点，（墨水等）斑点
blotter n. 吸墨纸,记事簿
blouse n.女衬衫；童衫；罩衫
blow vt.&vi.吹
blowhard n. 自吹自擂者
blowhole n. (海豚等)鼻孔
blown 吹
blowpipe n. 吹风管
blowtorch n. 吹管
blubber n. 鲸脂,哭泣
bludgeon n. 大头棒
blue adj. 蓝色的；伤心的；下流的；忧郁的；沮丧的，脸色发灰的n. 青色；蓝色
blueberry n. 越橘的一种
bluebird n. 知更鸟
bluebottle n. 绿头苍蝇
bluefish n. 竹荚鱼之类
blues n.布鲁斯乐曲 a.(非正式)伤感的
bluff n. 断崖,绝壁,吓唬
bluish a. 带蓝色的
blunder vi.犯大错 n.大错
blunderbuss n. 老式的大口径短炮,蠢材
blunt a. 钝的,坦率的,麻痹的
bluntly ad. 钝，迟钝地；直率地
bluntness n. 钝,率直,迟钝
blur n. 模糊不清的事物v. 使…模糊
blurred a. 模糊的
blurring n. 模糊
blurry adj. 视力模糊的
blurt vt. 冲口说出,突然说出
blush vi.脸红，害臊 n.脸红
blushy adj. 害羞的
bluster vt. 风狂吹,咆哮,汹涌
boa n. 蟒蛇,女用毛皮,羽毛围巾
boar n. 公猪,野猪
board n.木板；板
boarder n. 寄膳者,寄膳宿者
boarding n. 伙食
boast vi.自夸 vt.吹嘘
boastful a. 自夸的,自负,喜夸耀的
boat n.小船，艇；渔船
boathook n. 有钩的篙子
boathouse n. 船库,艇库
boating n. 划船(游玩)
boatman n. 出租船者,舟子,船夫
boatswain n. 水手长
bob 鲍勃(男名)
bobbin n. 线轴,缠线板,缠线管
bobby n. (英)警察；初生之犊
bobolink a. 食米鸟之类
bobtail n. 截短的
bobwhite n. 鹑的一种
bode v. 预示
bodice n. 女服的紧身衣
bodiless a. 无体的,无形的
bodily a. 身体的
bodkin n. 大眼粗针,锥子
body n.身体；主体；尸体
bodyguard n. 保镖，侍卫
bog n. 沼泽
boggle v. 畏缩不前，不敢想像
boggy a. 似沼泽的
bogus adj. 假装的，假的
boil vi.沸腾；汽化vt.煮沸
boiled 煮开的
boiler n.锅炉；热水贮槽
boiling  adj. 沸腾的
boiling-point n. 沸点
boisterous adj. 喧闹的，欢闹的
bold a.大胆的；冒失的
boldly ad. 大胆地，勇敢地；醒目地
boldness n. 大胆,勇敢,冒失
bole n. 树干
bolivia n. 玻利维亚(拉丁美洲)
boll n. 圆荚
Bolshevik n. 布尔什维克,激进分子
Bolshevism n. 布尔什维克的政策,思想,激进论
bolster n. 枕垫v. 支持，鼓励
bolt n.螺栓；插销 vt.闩门
bolted adj. 脱离的
bomb n. 炸弹；突发事件；高压喷雾器； vt. 投弹，轰炸；投弹于
bombard vt. 不断攻击；炮击
bombardment n. 炮击
bombast n. 高调，夸大之辞
bombastic adj. 唱高调的
bombay n. 孟买
bomber n. 轰炸机；投弹手；
bombshell n. 炸弹,突发而惊人的事物
bonanza n. 走运，发财
bonbon n. 小糖果
bond n.联结，联系；公债
bondage n. 奴役,束缚
bonded adj. 保税的；有担保的
bondman n. 奴隶
bondwoman n. 女奴隶
bone n.骨，骨骼
bonfire n. 大篝火,营火
bonito 鲣
bonnet n. 圆帽，扁平软帽
bonny adj. 健美的，漂亮的
bonus n. 奖金,红利
bony a. 多骨的；瘦的
boo vi.vt. 讥笑
booby n. 呆子,傻瓜
book n.书，书籍 vt.预定
book-binder n. 装订工人
bookcase n. 书架,书柜
booking adj. 定货；订货，末交定货；记帐
bookingform 预订单(表)
bookings 订货
bookish a. 好读书的,书呆子的
bookkeeper n. 簿记员
book-keeper n. 薄记员
bookkeeping n. 簿记
booklet n. 小册子
bookmaker n. 靴匠；制靴厂
bookmark n. 书签
bookmobile n. (设在车上到处巡回的) 流动
books 书
bookseller n.书商
bookshelf n. 书架
bookshop n. 书店
bookstall 书摊
bookstore n. 书店
boom n. 兴旺
boom-and-bust (市面)繁荣与萧条
boomer n.生育高峰中出生的人
boomerang n. 回飞棒,飞去来器
booming  adj. 兴旺的，轰响的；繁荣的
boon n. 恩惠
boor n. 举止粗野的人，乡下人
boorish adj. 粗野的
boost v. 往上推，增加，提高
booster n. 支持者
boot n.靴子，长统靴
booth n.货摊；公用电话亭
bootless a. 无用的,无益者
booty n. 战利品,获得之物
bopeep n. 藏猫游戏
borax n. 硼砂
border n.边，边缘；边界
borderland n. 边界地方,边陲,朦胧之境
bore vt.令(人)厌烦
boredom n. 烦恼，无聊；厌烦
boric a. 硼素的,含硼素的
boring n. 钻孔；adj. 讨厌的
born a.天生的；出生的
borough n. 享有自治权的市镇或区
borrow vt.借
borrower 借方，借主，借款人
borrowing n.借款，贷款
borrowings n. 借款
bosky a. 矮林丛生的,有丛林的,有树荫的
bosom n.胸，胸部；内心
boss n.老板，上司 vt.指挥
bossy adj. 发号施令的
boston n. 波士顿(美国城市)
bot 马蝇的幼虫
botanical adj. 植物（学）的
botanist n. 植物学家
botany n. 植物学
botch vt.vi. 拙笨地修补,糟蹋
both pron.两者(都)
both...and... …和…两者都；既…又…；不但…而且；两个都
bother vt.烦扰，迷惑 n.麻烦
bothersome a. 令人厌恶的；麻烦的
bottle n.瓶，酒瓶；一瓶
bottleneck 瓶左面关态；薄弱环节；难题
bottle-neck n. 影响…的环节
bottom n.底，底部，根基
bottomless adj. 无底的,深不可测的,极深的
bottom-line n. 末行数字，结果
bottomry 押船借款，冒险借款
boudoir n. （女人的）化妆室，闺房
bough n.树枝
bought (动词buy的过去时)；buy 的过去式(分词)；买
bouillon n.肉汤
boulder n. 巨石
boulevard n. 林荫大道
bounce vi.反跳，弹起；跳起
bound a.一定的；有义务的
boundary n.分界线，边界
boundless a. 无限的,无边无际的
bounteous adj. 慷慨的，丰富的
bountiful a. 慷慨的,宽大的
bounty n. 慷慨,宽大,恩惠
bouquet n. 花束
bourdon n. 嗡嗡的低音
bourgeois a.资产阶级的；平庸的
bourgeoisie 资产阶级
bourn n.小河，小溪,分界线
bourne n.小河，小溪，分界线
bourse 交易所，证券交易所
bout n. 一回合，一阵
boutique n.花束；酒香
bovine adj. (似)牛的，迟钝的；不易激动的
bow n.弓；蝴蝶结；鞠躬
bowdlerize v. 删除，任意删改
bowel n. 肠
bower n. 凉亭，树荫下凉快之处
bowery a. 有亭子的,象亭子的,有树荫的
bowl n.碗
bowling n. 保龄球
bowman n. 弓射手,持弓的兵,船首的划手
bowshot n. 箭可到达的距离,箭程
bowsprit n. 船首斜桅
bowstring n. 弓弦,绞索
box n.盒子
boxcar n. 有盖货车
boxer n. 拳师
boxes 盒子
boxing n. 拳击运动
boxing-day n. 节礼日
boxwood n. 黄杨木材,黄杨木
boy n.男孩，少年；家伙
boycott vt.&n.联合抵制
boyfriend n. 男朋友
boyhood n.少年时代
boyish a. 少年的；幼稚的
boys 男孩
brace n.支架；固定器(矫形)
bracelet n. 手镯
brachial adj. 臂的，上臂的
bracing adj. 振奋精神的n. 支柱，刺激
bracken n. 欧洲蕨
bracket n. 支架,括弧,托架
bracketed a. 加括号的
brackets n. 括号
brackish a. 有盐味的,可厌的
bract n. 苞叶,苞
brad n. 曲头钉
brae n. 斜坡,山坡
brag n. 吹牛
braggadocio n. 自夸,吹牛大王
braggart n. 吹牛
braid n. 辫子,穗带
braille n. 布莱叶盲文；点字法；vt. 用盲文印(或写)
brain n.脑(子)；脑力，智能
brainless a. 无头脑的,愚笨的
brains n. 脑力，智能
brainstorm vi.动脑筋，出主意，想办法，献计献策
brake n.闸，刹车 vi.制动
bramble n. 荆棘,悬钩子,树莓
bran n. 糠,麸
brancepeth 布朗土泼斯(地名)
branch n.枝条；支流；部门
brand n.商品；烙印 vt.铭刻
brandish vt. 挥,挥舞
brand-new a.崭新的，新制的
brandon 布兰敦(地名)
brandy n.白兰地酒
brant n. 黑雁
brashness n.莽撞，无礼，轻率
brasilia 巴西利亚(巴西首都)
brass n.黄铜；黄铜器
brassage 铸币费
brasses 铜管乐器
brassiere n. 奶罩
brat n. 乳臭未干的小孩,小子
bravado n. 故作勇敢，逞能
brave a.勇敢的，华丽的
bravely adv. 勇敢地；毅然
bravery n.勇敢，大胆
bravura n. 华丽而雄壮的表演
brawl n./v. 争吵，打架
brawn n. 筋肉,膂力,腕力,腌肉
brawny adj. （人）强壮的
bray n. 驴叫声,喇叭声
brazen adj. 无耻的，厚脸皮的
brazier n. 火盆,黄铜匠
brazil n.巴西(拉丁美洲)
brazilian a. 巴西人的，巴西的； n. 巴西的(人)
breach v. 毁坏，泄密n. 缺口
bread n.面包
bread-earner n. 挣钱养家的人
breadth n.宽度，幅度；幅面
breadwinner n. 养家活口的人
break n.(课间)休息时间
breakage n. 裂口
breakdown n. 崩溃，倒塌；失败；故障，损耗；病倒，垮台，破裂，(健康，精神等)衰竭，衰弱，(机器等)损坏
breaker n. 断路器
break-even n.保本的，不盈不亏的，得失相当的
breakfast n.早饭，早餐
breaking-down a. 毁坏的，分解的
breakthrough n. 突围；突破；冲垮
breakwater n. 防波堤
bream n. 鲤科食用鱼,铜盆鱼类
breast n.胸膛，胸部
breastplate n. 护胸甲,腹甲,胸革带
breastwork n. 赶工做成的防壁
breath n.呼吸；气息
breathe vi.&vt.呼吸
breathless a. 喘不过气来的,屏气的,死的,
breathlessly ad. 气喘吁吁地
breathlessness n. 屏息；气喘吁吁
breathtaking a.令人赞叹的
breath-taking a. 惊人的
bred breed的过去式(分词)
breech n. 屁股，炮尾
breeches n. 马裤
breed n.(动物)品种
breeder n. 繁殖的动物
breeding n. 教养,生育,饲养
breeze n.微风，和风
breezy a. 有微风的,通风好的,活泼的
breviary n. 每日祈祷书,摘要
brevity n. 短暂,简短
brew n. 酿造酒,酝酿
brewer n. 啤酒制造者,阴谋家
brewery n.  (啤酒) 酿造厂
briar n. 蔷薇属植物
bribe n.贿赂 vt.向…行贿
bribee 受贿人
briber 行贿人
bribery n. 贿赂行为,行贿,受贿
brick n.砖，砖块；砖状物
bricklayer n. 砖匠
brickwork n. 砌砖
bridal a. 新娘的,婚礼的
bride n. 新娘
bridegroom n.新郎
bridesmaid n. 女傧相
bridge n.桥，桥梁；桥牌
bridle n.笼子；束缚 vt.抑制
brief a.简短的；短暂的
briefcase n. 公文包
briefing n. 简要情况
briefly  adv. 简单地，简短地；短暂地；简略地；简要地
brier n. 蔷薇属植物
brig n. 旅,队,组
brigade n. 旅,队,组
brigadier n. 陆军准将,准将
brigand n. 土匪,盗贼
brigantine n. 双桅帆船的一种
bright a.明亮的；聪明的
brighten vt.使发光；使快活
brightly adv. 闪烁地；灿烂地；明亮地；聪明地
brightly-lit 灯光辉煌的
brightness n.明亮，辉煌，聪明
brilliance n. (声音的)清晰动人；光辉
brilliancy n. 卓越,光辉
brilliant a.光辉的；卓越的
brilliantly adv. 灿烂地；亮闪闪地；杰出地；鲜明地，辉煌地
brim n.边，边缘；帽沿
brimful adj.充满的、盈满的
brimstone n. 硫黄
brindled adj. 有斑纹的
brine n. 盐水，海水
bring vt.带来；引出；促使
bring...to 把…拿到/拿给
brings v. 带来(第三人称单数)
brink n. （峭壁的）边沿，边缘
brisk a.活泼的；清新的
brisket n. 胸部,胸肉
briskly ad. 轻快地；敏捷的；活泼地
briskness n. 敏捷,活泼
bristle n.短而硬的毛；鬃毛
bristling adj. 竖立的
bristly a. 短而硬的
Britain n.英国，不列颠
British adj.英国的
briton n. 布立吞人；英国人
brittle a.脆的；易损坏的
broach v. 开瓶，提出（题目）
broad adj.宽的；广阔的
broad-brush 粗略的，不完整的
broadcast n.广播，播音
broadcasting n. 广播节目
broadcloth n.宽幅的纺织品
broaden vt.&vi.放宽，变阔
broadly ad. 广，宽；明白；粗鲁
broadsheet n.(印在)大幅(纸张上的)广告
broadside n.『航海』 (水线上的) 舷侧
broadsword n. 阔刀,腰刀
broadway n. & a. 百老汇大街(的)
brocade n. 织锦
brochure n. 假订本,小册子,小册
brogue n. 土音,厚底皮鞋
broil n./v. 烤，烧，争吵，怒骂
broiled a.烤过的
broiler  n. 老爱吵架的人; 唆使他人争吵者
broke break的过去式；破；打破
brokee 破产者
broken a.被打碎的，骨折的
broker n. 掮客,经纪人
brokerage n.经纪人或掮客之业务
bromide n. 溴化物（镇静药用），平庸的人或物
bronchial  adj. 支气管的
bronchitis n. 支气管炎
bronchogenic adj. 支气管源的
bronchus n. 支气管
bronco n. 野马
bronze n.青铜色
brooch n. 胸针或领针；饰针
brood vt.沉思vi.郁闭地沉思
brooder n. 孵卵器,沉思的人,默想的人
brook n.小河，溪流
brooklet n. 细流,小河
broom n.扫帚
broomstick n. 帚柄
broth n. 肉汤
brother n.兄，弟
brotherhood n. 手足情谊,兄弟关系
brother-in-law n. 姊妹的丈夫
brotherly a. 兄弟的,亲兄弟似的,亲切的
brougham n. 有盖马车的一种
brought bring的过去式(分词)；带来
brow n.额；眉，眉毛
browbeat  vt.  (用神情、言词) 威吓
brown adj.褐色的，棕色的
brownie n. 核仁巧克力饼
brownish a. 呈褐色的
browse n./v. 吃嫩叶或草，浏览
bruce 布鲁斯(男名)
bruin n. 熊,熊先生
bruise n.青肿，伤痕；擦伤
bruit vt. 散播
brunette n. 浅黑肤色的人
bruno 布鲁诺(男名)
brunt n. （主要的）压力
brush n.刷子，毛刷；画笔
brushes 刷子，画笔
brushstroke n. 笔的一划
brushwood n. 柴,柴枝,草丛
brusque adj. 唐突的，鲁莽的
brussels n. 布鲁塞尔(比利时)
brutal adj. 残忍的，严酷的
brutality n. 残酷，兽行
brute n.禽兽，畜生
brutish adj. 如野兽
bubble n.泡 vi.冒泡，沸腾
bubonic  adj. 『医』横玄的, (患) 淋巴腺红肿的
buccaneer n. 海盗
buck n. 强烈反对，吹牛，雄鹿，美元
bucket n.水桶；吊桶；铲斗
bucketeer 买空卖空者，投机家
buckle n. 皮带扣环v. 扣紧
buckled adj. 鞋上有银环装饰的
buckler n. 小圆盾,防卫物,防卫
buckram  n. 胶硬的粗布
bucksaw n. 有框的锯
buckskin n. 鹿皮
buckwheat n. 乔麦,乔麦之种,乔麦粉
bucolic adj. 乡村的，牧羊的
bud n.芽，萌芽；蓓蕾
Buddha n. 佛
Buddhism n.佛教，释教
buddhist n. 佛教徒
buddy n. 伙伴，弟兄
budge v. 移动，让步n. 羔皮，革袋
budget n.预算，预算案
buff n. 浅黄色（软皮革），水牛
buffalo n.水牛；水陆坦克
buffer n. 缓冲,缓冲区
buffet n. 自助餐,小卖部,冲击,殴打,碗橱
buffoon n. 丑角，缺乏教养之人
buffoonery n. 打诨,滑稽
bug n.臭虫；(美)虫子
bugaboo n.鬼怪,妖怪,吓人的东西
bugbear n. (传说会吃掉坏孩子的) 鬼怪
buggy n. 轻型马车，婴儿车
bugle n.军号，喇叭
build vt.建筑；建立；创立
builder n. 建立者
building n.建筑物，大楼；建筑
building-up a. 组合的，合成的
built  vt. build(建设)的过去式和过去分词
built-in a. 嵌入的，内装的
bulb n.电灯泡；球状物
bulge n./v. 膨胀，突出
bulk n.物体，容积，大批
bulk-cheap 薄利多销
bulkhead n. 隔壁,防水壁,分壁
bulky a. 庞大的
bull n.买空的证券投机商
bull-bear 多头空头
bulldog n. 斗牛犬
bulldozer n. 推土机
bullet n.子弹，枪弹
bulletin n.公报；公告
bullfight n. 斗牛
bullfinch n. 红腹灰雀
bullion n. 金条，银条
bullionism 金银通货主义
bullish adj.股票行情看涨，物价上涨
bullock n. 阉牛
bully v. 欺负，威协
bulrush n. 芦苇,香蒲,纸草
bulwark n. 堡垒，保障
bum v. 流浪，乞讨，adj. 差劲的
bumble v. 说话含糊；语无伦次
bump vt.&vi.碰，撞；撞击
bumper n. 汽车前后的保险杆
bumpkin n. 粗人，乡巴佬
bumptious a. 瞎自夸的,瞎自大的,傲慢的
bumpy adj. 凹凸的，崎岖不平的，颠簸不平的
bun n. 小面包
bunch n.束，球，串；一群
bunco 诈骗，投机勾当
bund n. 堤岸，江边道路，码头
bundle n.捆，包，束；包袱
bungalow n. 平房,周围有阳台的木造小平房
bungle vt.vi. 拙劣地工作,粗制滥造,失败
bunion  (C) 拇趾粘液囊肿大,拇囊肿
bunk n. 铺位,废话,逃走
bunny n. 兔子
bunt n. 顶撞,推,短打
bunting n. 旗帜；白颊鸟
buoy n. 浮标，救生圈，v. 支持，鼓励
buoyancy n. 浮力
buoyant adj. 易浮的，快乐的.
burd n. 少女
burden n.担子，负担 vt.劳累
burdensome a. 难以负担的；沉重的
burdock n. 牛蒡
bureau n.局，司，处；社，所
bureaucracy n.官僚主义；官僚机构
bureaucratic adj. 官僚主义的
burgeon v. 迅速成长，发展
burgess ]伯奇士 (男子名)
burgh n. 自治都市
burgher n. 公民,市民
burglar n.夜盗，窃贼
burglary  n. 盗窃 (罪)
burgomaster n. 市长
burgoo n. 燕麦牛奶粥
burial n.安葬，埋葬，埋藏
burke vt. 秘密镇压
burlap n. 粗麻布（用于窗帘等）
burlesque n. 讽刺或滑稽的戏剧
burly a. 结实的,粗壮的,率直的
burn vi.&vt.燃烧
burner n.灯头，煤气头
burnish v. 擦亮，磨光
burns 烧伤
burnt adj. 烧焦的，烧坏的；burn的过去式(分词)；燃烧(burnt=burned)
burr n. 粗喉音；v. 粗喉音说
burro n. 驴子
burrow n. （兔子等）所掘的地洞，v. 挖洞
burst n.突然破裂；爆发
burton n. (机)复滑车
bury vt.埋葬，葬；埋藏
bus n. 公共汽车；总线，信息通路
bus-driver n. 公共汽车司机；公共汽车驾驶员
buses 公共汽车
bush n.灌木，灌木丛，矮树
bushel n.蒲式耳(容量单位)
bushing n. 轴衬,套管
bushmaster n.一种美洲产的大毒蛇(草丛之主)
bushy a. 灌木一样的,灌木茂密的,多毛的
busily ad. 忙碌地
business n.商业，生意；事务
businesslike a. 事务性的,有条理的,有效率的
businessman n. 商人，实业家
businesswoman n.女商人
buskin n.
busman n. 公共汽车上司机
buss n. 接吻,一种帆船
bus-stop n. 公共汽车站
bust n. 半身（雕）像
bustle n. 喧闹,裙撑
busy adj.忙的；繁忙的
but conj.但是，可是
butcher n.屠夫；屠杀者
butchery n. 肉食店
butler n. 仆役长
butlor n. (男)管家
butt n.大酒桶，桶
butte n. 孤立的丘
butter n.黄油；奶油
buttercup n. 毛茛,金凤花
butterfly n.蝴蝶
buttermilk n. 白脱牛奶,酪浆
butterscotch n. 奶油糖果
buttocks n. 臀部
button n.扣子；按钮 vt.扣紧
buttonhole n. 扭扣孔
buttress n. 扶墙，拱壁，v. 支持
buxom adj. 体态丰满的
buy vt.买
buyer n. 买主,买方
buying 购买
buzz vi.(蜂等)嗡嗡叫
buzzard n. 贪婪的人，肉食的秃鹰
buzzword n.流行词
by prep.被，由
by-business 副业，兼业
bye int. ((口语))再见
bye-bye interj. 再会
bye-bye! 再见！
by-effect 副作用
bye-law n.地方法规，章程
by-end 附带目的，私下目的
bygone adj. 过去的，昔日的
bylaw n. 地方法规；内部章程
by-law n.地方法规，章程
byline n. (列作者名字的)报刊文章首行
bypass n. 旁通管；分路；旁路；迂回的旁道，v. 规避，绕过；
by-pass 绕过，回避，忽视
byproduct n. 副产品
by-product n.副产品
byron 拜伦(英国诗人)
byte n. (二进制的)字节
byway n. 旁道,通道,间道
byword n. 谚语,格言,笑柄
by-work 副业
byzantine adj. 拜占延帝国的；错综复杂的，迷官似的
c/o v. (缩)请转交…
caac 中国民航
cab n. 计程车,出租汽车,出租单马车
cabal n. 徒党,秘密结社,(尤指政治上的)阴谋
cabbage n.洋白菜，卷心菜
cabin n.小屋；船舱，机舱
cabinet n.橱，柜；内阁
cable n.海底电报
cablegram n. 海底电报
caboose n. (载货火车最后一节的)守车,
cacao n. 可可子,可可树
cache v. 贮藏，隐藏，n. 藏物处
cackle n. 咯咯声,高笑声,饶舌,闲谈
cacophonous a. 刺耳的；不协调的
cacophony n. 刺耳的声音
cacti n. 仙人掌
cactus n. 仙人掌
cad n. 卑鄙的男人,下流人,无赖
cadaver n. 尸体
cadaverous adj. 像尸体的，（形容）枯槁的
cadence n. 韵律,抑扬,调子,节奏
cadet n. 军校或警官学校的学生
cadre n. 干部
caesar n. 凯撒；暴君；独裁者
caesura n. 休止
cafe n.咖啡馆；小餐厅
cafeteria n.自助食堂
caffeine n. 咖啡因,茶精(兴奋剂)
cage n.畜养禽、兽的笼子
cail v. 脱帽；低垂
cain n. 该隐；杀弟者，凶手
cairn n. 石堆纪念碑,石冢,堆石界标
cairo n. 开罗(埃及首都)
caitiff a. 卑劣的
cajole v. （以甜言蜜语）哄骗
cake n.蛋糕，饼，糕
cakes 蛋糕
calais n. 加来(法国港市)
calamitous adj. 造成灾祸的
calamity n. 大灾祸，不幸之事
calcify v. 使硬化，钙化
calcimine n. 墙粉(一种涂料)
calcine vt.vi. 烧成石灰,锻烧
calcium n. 钙
calculate vt.计算；估计；计划
calculated a. 精心制作的
calculating adj. 精于打算的；深谋远虑的，精明的
calculation n.计算，计算结果
calculator n.计算器，计算者
calculus n.微积分；结石
calcutta n. 加尔各答(印度)
caldron n. 大锅,大汽锅
calendar n.日历，历书；历法
calender n. 研光机
calf n. 小牛,小牛皮,腓,小腿
caliber n. 口径,才干,器量
calibrate vt. 使标准化，校准，标定，分度，测量…的口径
calibration n. 校准；标定，刻度；核定
calibre n. （枪等）口径，（人或事）品质，才能
calico n. 印花棉布,白洋布
calif n.哈利发,回教国国王
california  n. 加利福尼亚(美国)
californian a. 加利福尼亚州的
calipers n.pl. 弯脚器,测径器
caliph n. 哈利发,回教国国王
calk vt. 填...以防漏,使不漏水,装尖铁,
call vt.把…叫做；叫，喊
call-back 收回，招回加班
call-box n. 电话间
called a. 被称呼的
caller n. 访客,召集员,传唤员
calligraphy n. 书法
calling n. 职业,行业,邀请,召集
callipers n. 弯脚规,测径器
callous adj. 结硬块的，无情的
callow adj. （鸟）未生羽毛的，（人）未成熟的
callus n. 老茧，皮肤硬厚处
calm adj.平静的；沉着的
calmly adv. 平静地；沉着地；无风浪地；镇静地
calmness n. 平静,镇静,冷静
calomel n. 甘汞
calorie n. 卡路里
calorific adj. 生热的
calumniate v. 诽谤，中伤
calumnious  adj. 诽谤的,中伤的
calumny n. 诽谤，中伤
calves calf的复数
calyx n. 花萼
cam n. 凸轮
cambric n. 一种亚麻布或棉布
cambridge  剑桥大学；剑桥(英格兰东部一城市)
came vi.come(来)的过去式；come(来)的过去分词
camel n.骆驼
camellia n. 茶花,山茶
cameo n. 刻有浮雕的宝石或贝壳
camera n.照相机
cameraman 摄影师
camouflage n./v. 掩饰，伪装
camp n.野营，营地，兵营
campaign n.战役；运动
campaigner n. 从军者,出征者,竞选者
camper n. 露营者
camphor n. 樟树,樟脑
camping n. 野营
campsite n.露营场地 ,营地
campstool n. 折椅
campus n.校园，学校场地
camshaft n. 凸轮轴
can n.罐头，听头
canada n.加拿大(北美洲)
Canadian n.加拿大人
canal n.运河；沟渠；管
canard n. 虚报；谣言；假新闻
canary n. 金丝雀，女歌星
cancel vt.取消，撤消；删去
cancellation n. 取消,作废,注销戳
cancer n.癌，癌症，肿瘤
candelabrum n. 枝状大烛台
candid a. 坦白的,率直的,公正的
candidacy n. 候选人的地位,候选资格
candidate n. 候选人
candidature n. 候选人的，资格
candle n.蜡烛
candle-light  adj. 在烛光中进行的 <聚餐等>
candlestick n. 烛台
candor n. 坦白,直率
candour n.公正，坦率
candy n.糖果；砂糖结晶
cane n.手杖
canel n. 运河，沟渠
canine adj. 犬的，似犬的
canister n. 罐,筒,霰弹
canker n. 溃疡，弊害
canned a. 罐装的,录音的,被囚的,刻板的,
cannibal n. 食人者，食同类的动物
cannibalism n. 同类相食
canning n. 罐头制造
cannon n. 大炮；火炮；榴弹炮；(飞机上的)机关炮
cannonade n. 炮击
cannot can的否定式
cannot...too... 越…越好；怎么…也不会过分
canny a. 精明的,谨慎的
canoe n.独木舟，皮艇，划子
canon n. 经典，真作
canonical adj. 符合规定的，经典的
canonize vt. 封...死者为圣徒,使加入圣徒之列,
canopy n. 蚊帐，华盖
cant n. 斜坡，斜面，v. 使倾斜
can't v. & aux. 不能；(同)cannot不能
cantankerous adj. 脾气坏的，好争吵的
cantata n. 清唱剧
canteen n.小卖部；临时餐室
canter n. 慢跑,流浪汉
canticle n. 圣歌,颂歌,小歌曲
canto n. 篇章,旋律
canton n. 州,行政区
cantonment n. 宿营地
canvas n.粗帆布；一块油画布
canvass n. 细查,讨论,劝诱
canvasser 保险经纪人，推销员
canyon n. 峡谷
caoutchouc n. 弹性橡皮
cap n.帽子
capability n.能力，才能；性能
capable a.有能力的，有才能的
capacious adj. 容量大的，宽敞的，
capacitance n. 电容，电容量
capacitor n. 电容器
capacity n.容量；能力；能量
caparison n. 马衣,美服
capclothes 衣服
cape n.披肩，斗篷；海角
caper n./v. 雀跃，欢蹦
capillary n. 毛细管
capita n. 人
capital n.资本，资金；首都
capital-intensive adj. 资本密集型的
capitalism n. 资本主义,资本的集中
capitalist n. 资本家,资本主义者
capitalistic a. 资本主义的,资本家的
capitalization n. 资本化,资本总额,股本,大写
capitalize vt. 以大写字母写,使资本化,计算...的现价
capitalized a. 大写的
capital-output 资本产出
capitation n. 人头税，丁税
Capitol n. 国会大厦,州议会大厦,(古罗马的)主神殿
capitulate v. （有条件地）投降。
capitulation n. 投降
capon n. 阉鸡
caprice n. 反复无常,善变,任性
capricious adj. 变化无常的，任性的
capsize vi.n. 翻覆,倾覆
capstan n. 绞盘,起锚机
capsule n. 胶囊,蒴,瓶帽,太空舱
captain n.陆军上尉；队长
caption n. 说明,字幕,标题
captious adj. 吹毛求疵的
captivate v. 迷惑，吸引
captivation n. 吸引力，魅力
captive n.俘虏，被监禁的人
captivity n. 囚禁,被关
captor n. 捕捉者,逮捕者
capture vt.捕获，俘获；夺得
car n. 汽车；小卧车；(这里指)运货马车；轿车；电车；车，火车车厢
carafe n. 玻璃水瓶
caramel n. 焦糖,焦糖糖果
carapace n. (蟹或龟等的)甲壳
carat n. （宝石重量单位）克拉，（金子）开
caravan n. 旅行队,有篷顶的大车
caravansary n. 商队旅馆,大旅舍
caravel n. 轻快帆船
caraway n. 香菜
carbine n. 卡宾枪
carbohydrate n. 碳水化合物
carbolic a. 碳的,用煤焦油制成的
carbon n.碳
carbonate n. 碳酸盐
carbonic a. 碳的,由碳得到的
carboniferous n. 石炭纪,石炭层
carbuncle n. 粉刺,红玉,红水晶
carburetor n. 汽化器,  化油器
carcanet  n. 『罕』 (金质镶珠宝之) 项链; 项圈
carcase n. 尸体,架子
carcass n. 尸体
card n.卡片；名片
cardboard n. 厚纸板
cardiac  adj. 心脏的，心脏病的
cardiff n. 加的夫(英国港市)
cardigan n. 羊毛上衣，羊毛衫
cardinal a. 基本的；主要的
cardiologist n. 心脏病学家
cardiovascular a. 心血管的
care n.照料；保护；小心
careen v. 把船倾倒，倾倒，歪靠
career n.生涯，职业，经历
careful a.仔细的；细致的
carefully adv. 小心地；仔细地；注意地
carefulness n. 小心,仔细,慎重
careless adj.粗心的
carelessly adv. 粗心地；毫不在乎地；随便地，疏忽地
carelessness n.粗心，大意
caress n. 爱抚,拥抱
caret n. 加字符号（∨，∧）
caretaker n. 管理人,看管者,看守人
careworn a. 疲倦的,饱经忧患的
cargo n.船货，货物
cargo-cargo 回头货
cargo-owner 货主，托运人
caribbean n. & adj. 加勒比海(的)
caribou n. 北美驯鹿
caricature n. 讽刺画，滑稽模仿
carillon n. 钟乐器
carl 卡尔(男名)
carload n. 车辆所载的货物,货车的最低载重量
carmine n. 洋红色,深红色
carnage n. 大屠杀，残杀
carnal a. 肉体的,肉欲的
carnation n. 康乃馨（一种花）
carnet 货物通行证；执照，海关文件
carnival n. 狂欢节
carnivore n. 食肉动物
carnivorous adj. 食肉的。
carol n. 赞美诗，颂歌
carom v. 使弹开；使弹回
carousal n. 欢闹的酒宴
carouse n./v. 狂饮寻乐
carousel n. 圆盘传送带
carp n. 鲤鱼
carpenter n.木工，木匠
carpet n.毛毯；地毯
carping adj. 吹毛求疵的
carport n. 无墙车库,车棚
carriage n.客车厢；四轮马车
carrier n.运输工具；运载工具
carrion n. 腐肉
carrot n.胡罗卜
carry vt. 拿；搬；带；提；扛，挑，刊登；搬动；带去；运送，携带；运载；传送；领，抱背，传播，输送；手提，肩挑；举动；进位，担负；vi. 抬，扛，搬运
carrying-pole n. 扁担
cart n.二轮运货马车
carte n. 全权委任
carter n. 运货马车夫
cartilage n. 软骨
cart-load n. 一车之载量
cartographer n. 绘制地图者
carton n. 长形纸匣；纸箱；纸板盒
cartoon n.漫画，动画片
cartridge n.弹药筒，子弹；软片
carve vt.刻，雕刻；切开
carver n. 雕刻匠,雕工,切肉刀
carving n. 雕塑；雕刻(术)；雕刻品
caryatid n. 女像柱
cascade n. 小瀑布
cascara n. 鼠李,用其树皮制成的缓泻剂
case n.情况；事实；病例
casein n. 干酪素,酪蛋白
caseload 工作量
casement n. 窗
cases 箱；盒
cash n.现金，现款
cash-desk n. 收款台
casher n.出纳员
cashier n. 出纳；出纳员，收支员
cashmere n. 产于咯什米尔和西藏的一种羊毛
cash-out 现金不足
casing n. 箱,盖,套管,框,包装
casino n. 娱乐场,(供表演跳舞赌博的地点),
cask n. 桶,木桶
casket n. 首饰盒,小箱,匣子,棺材
casque n. 盔
cassava n. 木薯
casserole n. 餐桌上用有盖的焙盘,砂锅菜
cassette n.盒式录音带；盒子
cassia n. 肉桂
cassock n. 法衣,袈裟
cast vt.投，扔，抛；浇铸
castaway n. 被抛弃的人,坐船遇难者,漂流者
caste n. 社会等级，等级
castellate n. 城主之阶级、职位或辖区
caster n. 投手,(家具的)轮脚,调味瓶
castigate v. 惩治，严责
castigation n. 申斥，强烈反对
casting n. 投掷,铸成品,角色
cast-iron a. 用铸铁制的
castle n.城堡；巨大建筑物
castor n.蓖麻
casual a.偶然的；随便的
casualty n. 严重事故,伤亡,受害者
casuist n. 决疑者,诡辩家
cat n.猫，猫科，猫皮
catabolism n. 分解代谢
cataclysm n. 剧变，灾难（常指大洪水或地震）
catacomb n. 地下墓穴,茔窟
catalog n.目录，目录册
catalogue vt.为…编目录
catalpa n. 梓,梓属植物
catalysis n. 催化作用
catalyst n.催化剂；刺激因素
catapult n. 弹弩；发射机
cataract n. 大瀑布,奔流,洪水,白内障
catarrh n. 粘膜炎,感冒
catastrophe n. 大灾难,大祸
catbird n. 猫声鸟
catch vi.钩住；挂住；绊住
catcher n. 捕手,捕捉的人,捕捉的事物
catching a.传染性的
catch-penny 花哨而不值钱的商品
cate n. 佳肴,美食
catechism n. 教义问答书,问答集
categorical adj. 无条件的，绝对的；武断的
category n.种类，类目；范畴
cater vi.迎合，投合
catering 公共饮食业
caterpillar n. 毛虫，蝴蝶的幼虫
catfish n. 鲶鱼
catharsis n. 宣泄，净化
cathartic n. 泻药
cathedral n.总教堂；大教堂
cathode n. 阴极；负极
catholic a.天主教的n.天主教徒
catholicism 天主教
catholik 天主教徒
catnip n. 猫薄荷
catsup n. 酱,(如蕃茄酱之类)
catter n. 冰脚
cattle n.牛
Caucasian n. 高加索人,白种人
caucus n. 政党高层会议，核心人物
caudal adj. 尾的，尾部的，像尾部的
caught catch的过去式(分词)；提；捉
cauldron n. 大锅,大汽锅
cauliflower n. 花椰菜
caulk v. 填塞（隙缝）使不渗水
causative a. 引起…的
cause n.原因，理由；事业
causeless a. 无显著原因的,偶然的
causeway n. 堤道,铺道
caustic adj. 腐蚀性的，刻薄的
cauterize vt. 烧灼,使麻木不仁
caution n.小心；告诫 vt.警告
cautious a.小心的，谨慎的
cautiously ad.小心地；谨慎地
cavalcade n. 骑兵队
cavalier n. 骑士，武士
cavalry n. 骑兵部队
cavalryman n. 骑兵
cave n.山洞，洞穴，窑洞
caveat 停止支付通知
caveman n.(石器时代的) 穴居人
cavern n. 大洞穴
caviar n. 鱼子酱
caviare n. 鱼子酱
cavil v. 挑毛病，吹毛求疵
cavity n.洞，穴，空腔
caw v.(乌鸦等)呱呱地叫
cay n. 珊瑚礁，沙洲
cayenne n. 辣椒
cease vi.&vi.&n.停止，停息
ceaseless a. 不停的,不断的
cedar n. 西洋杉,香柏
cede v. 割让（土地，权利）
ceiling n.天花板；顶逢
celandine n. 白屈菜
celebrate vt.庆祝；歌颂，赞美
celebrated  adj. 有名的，著名的；知名的
celebration n.庆祝；庆祝会
celebrity n. 名人，知名人士
celerity n. 快速，迅速
celery n. 芹菜
celestial adj. 天体的，天上的
celibacy n. 独身（主义）
celibate n./adj. 独身者，不结婚的.
cell n.细胞；小房间
cellar n.地窑，地下室
cellular a. 细胞的
celluloid n. 赛璐珞
cellulose n. 纤维素
Celt n.凯尔特人
cement vt.粘结 vi.粘紧
cemetary n.公墓，墓地
cemetery n.公墓；墓地
cene a. (构词成分)表示"新的"，"最近的"
censer n. 香炉
censor vt.审查，检查
censorious adj. 吹毛求疵的，苛求的
censorship n. 检查（制度）
censure n./v. 责难，非难
census n. 统计数字；普查
cent n.分
centaur n. 人首马身的怪物,半人马座
centenary a./n.百年的；百年纪念
centennial n. 百年纪念
center n. 中心,中心点,中锋
centigrade a.百分度的
centigram n. 厘克
centime n. 生丁
centimeter n. 厘米
centimetre n.公分，厘米
centipede n. 蜈蚣
central a.中心的；主要的
centralization n. 集中,中央集权化
centralize vt. 使集权
centralized a. 中央集权的
centre n. 中心；中央；中枢；核心；vt. 集中；使集中，把…放在中部vi. 居中
centrifugal adj. 离心的
centripetal adj. 向心的
centurion n. 百夫长
century n.世纪；百年
cephalic adj. 头的，头部的
ceramic a.陶瓷的；陶器的
ceramics n. 陶器制，陶业
cere vt. 用蜡布包裹
cereal n.谷类，五谷，禾谷
cerebellum n. 小脑
cerebral adj. 大脑的，深思的
cerebration n. 用脑，思考
cerebrospinal a. 脑脊髓的
cerebrum n. 大脑
cerement n.裹尸布,寿衣
ceremonial a. 仪式的；礼节的
ceremonious a. 讲究仪式的,隆重的
ceremony n.典礼，仪式；礼节
certain a.确实的；肯定的
certainly ad.一定，必定；当然
certainty n.必然；肯定
certes ad. 的确,诚然
certificate n.证书，证件，执照
certification n. 证明
certifier 保证人，证明人
certify vt.vi. 证明,保证
cerulean a. 蔚蓝的
cess n. 运气；捐，税
cessation n. 中止，（短暂的）停止
cession n. 割让，转让
cesspool n. 污水坑,化粪池
cg 心(动)电图描记器(缩)
chafe vt. 擦伤；磨损
chaff n. 谷物的皮壳，米糠
chaffinch n. 鸟类,(一种欧洲鸣禽)
chaffing adj. 玩笑的；嘲弄的
chagrin n./v. 失望，懊恼
chagrined adj. 失望的，灰心的
chain n.链，链条，项圈
chair n. 椅子；大学的讲座；(会议的)主席；vt. 当…的主席，主持
chairman n.主席；议长，会长
chairmanship n. 主席的身分或资格
chairperson n. 主席(无性别之分)
chairwoman n. 女主席，女董事长
chaise n. 轻车马
chalet n. 瑞士山中的牧人小屋
chalice n. 杯,圣餐杯
chalk n.白垩；粉笔
chalk-mark n. 粉笔记号
chalky a. 白垩的
challenge n.挑战；要求，需要
challenger n. 挑战者
challenging adj. 具有挑战性的
cham n. 可汗
chamber n.会议室；房间；腔
chamberlain n. 侍从,管家,收款人
chambermaid n.  (旅馆等的) 房间女服务生,女仆
chameleon n. 变色龙，晰蜴
chamois n.羚羊
champ vt.vi. 使劲地嚼,格格地咬,咬响牙齿
champagne n. 香槟酒,香槟色
champaign n. 平野,平原
champion n.斗士；提倡者
championship n.冠军称号；锦标赛
chance n.机会
chancel n. 高坛
chancellor n.(财政) 大臣、司法官
chancery n. 大法官法庭
chancy a. 冒险的；危险的
chandelier n. 枝形吊灯（烛台）
change n.零钱；找头 vt.兑换
change...into 把…变成；转换成
changeable a. 可改变的
changeful a. 易变的,不安定的,富于变化的
changeless a. 不变的,固定不变的,固定的
changeling n. 调换儿,矮小丑陋的小孩,低能儿
channel n.海峡；渠道；频道
chanson n. 歌
chant vt. 不变地把歌反复唱；歌唱；诵经n. 单调的歌；咏唱；颂歌；圣歌
chanticleer n. 雄鸡，公鸡
chantry n.捐献,捐款
chaos n. 混乱
chaotic adj. 混乱的
chap v. （皮肤）变粗糙，皲裂
chapel n. 小礼拜堂,礼拜
chaperon v. 陪伴，伴随
chaplain n. 牧师
chaplet n.花冠,花圈
chapman n. 商人,负贩,叫卖小贩
chapter n.章，回，篇
char n. 家庭杂务,炭
character n.性格；特性；角色
characteristic a.特有的 n.特性
characteristical adj. 特征的
characterization n. 描述,人物之创造
characterize vt.表示…的特性
character-training 性格的培养；品质的培养
charactor-training n. 性格的培养，品质的培养
charades n. 用动作等表演的字谜游戏
charcoal n.炭；木炭
charge n. 主管；电荷；负责；责任；管理；费用；负荷；充电；使承担；看管；保管；代价；(pl. )费用，罪名；收费， vt. 罚款，指控；索价；控告；装满；职责；索费；使承担(任务，责任)；费用；充电；(pl. )费用，使充满，收费，冲向，冲锋
chargeable a. 应课税的
charger n. 充电器,袭击者,军马
chariot n. 二轮战车
charioteer n. 战车的御者
charisma n. （大众爱戴的）领袖气质，魅力
charismatic adj. 有魅力的
charitable adj. 仁慈的、宽厚的
charity n.施舍；慈善事业
charlatan n. 江湖郎中，骗子
charles 查尔斯·西门斯
charlie 查利(男名)
charlotte n. (法)水果奶油布丁
charm n.魅力；妩媚 vi.迷人
charmer n. 魔术师
charmeuse n. 缎子的一种
charming a.迷人的，可爱的
chart n.图，图表；海图
charter vt.租 n.宪章；契据
chartering 租船，租凭业务
chary adj. 小心的，审慎的
chase n.追逐，追赶，追求
chasm n. 深渊，大差别，代沟
chassis n. (汽车的)底盘
chaste adj. 贞洁的，朴实的
chasten v. (通过惩罚而使坏习惯等)改正、磨练
chastise v. 严厉惩罚，遣责
chastisement n. 惩罚
chastity n. 贞节，纯洁
chat  n. 聊天；闲谈； vi. 聊天；谈天；闲谈vt. 亲谈，
chateau n. 城堡，乡间别墅
chatelaine n. 腰带,大别墅的女主人,女城主
chattel n. 动产,奴隶
chatter vi.&n.喋喋不休
chatty a. 绕舌的,爱讲闲话的
chauffeur n. 司机
chauvinism n. 沙文主义，盲目爱国主义
chauvinist n. 沙文主义者,盲目的爱国主义者
cheap adj.廉价的，便宜的
cheaply  adv.廉价地；粗俗地；便宜地
cheat vt.骗取；哄 vi.行骗
cheating n. 欺骗行为
check n.支票
checker n.核对
checkerboard n. 国际象棋盘
checkered adj. 方格花样的; 有各种颜色的
check-out n. 结帐，离店时限
checkup n.检查，体格检查
check-up n. 核对，检查；体检
cheek n.面颊，脸蛋
cheeky adj. 胖乎乎的
cheep n. 吱吱的叫声
cheer vt.使振作；欢呼
cheerful adj.高兴的；爽快的
cheerfully ad. 高兴地；愉快地
cheerfulness n. 高兴,快活
cheerily adv. 兴高采烈地
cheerless a. 寡欢的
cheery a. 愉快的
cheese n.乳酪，干酪
cheese-maker n. 制造乳酪的人
cheetah n. 猎豹
chef n. 厨师
chemical adj.化学的
chemise n. 紧身衣一种,衬裙
chemist n.化学家；药剂师
chemistry n. 化学
chemotherapy n. 化学疗法(化疗)
chemo-treatment n.化疗
cheque n.支票
chequer v. 变化，沉浮
cherish vt.珍爱；怀有(感情)
cherry n.樱桃
cherub n. 小天使,胖娃娃
cherubim n. cherub的复数
chess n.棋；国际象棋
chest n.胸部
chestnut n.栗子
chevalier n. 骑士,爵士,见习武士
chew vt.咀嚼，嚼碎
chic adj. 漂亮的，俏式的
chicago 芝加哥(美国城市)
chicanery n. 欺诈，欺骗
chiche n.陈腐思想，陈词滥调
chick n.小鸡
chickadee n. 山雀
chicken n.鸡肉；小鸡
chickenpox n.水痘
chickweed n. 繁缕
chicory n. 菊苣
chide v. 叱责，指责
chief n.首长，头子
chiefly ad. 主要地
chieftain n. 酋长,首领
chiffon n. 一种透明的丝质薄纱,雪纺绸
chiffonier n. 西洋梳镜柜,小衣橱
chilblain n. 冻疮
child n.小孩
childbirth n. 分娩
childhood n.幼年(时代)，童年
childish a.孩子的；幼稚的
childless a. 无儿女的
childlike a. 孩子似的,天真烂漫的
children n. 小孩(复数)；(child的复数形式)；子女(复数)
chile n. 智利(拉丁美洲)
chili n.辣椒
chill vt.使变冷 n.寒冷
chilly a. 寒冷的
chimaera n. 神话怪物，梦幻
chime n. 鸣,钟,和谐
chimera n. 神话怪物，梦幻
chimerical adj. 荒诞不经的，梦幻的
chimney n.烟囱，烟筒；玻璃罩
chimpanzee n. 黑猩猩
chin n.颏，下巴
china n.中国
chinch n. 臭虫
chinchilla n.『动物』栗鼠
chine n. 山脊；幽谷
Chinese a.中国的 n.中国人
chink n. 隙缝，裂口n./v. 丁当作响，破裂
chintz n. 印花棉布
chip n.薄片，碎片
chipmunk n. 花粟鼠(象松鼠的美洲小动物)
chips n. (口语)炸土豆条(片)
chiromancy n. 手相术
chiropodist n. 手足病医生
chirp v. (鸟或虫)唧唧叫
chirrup n. 吱喳声
chisel n. 凿子
chivalrous adj. 武士精神的，侠义的
chivalry n. 骑士制度
chloral n. 三氯乙荃,三氯乙二醇
chloride n. 氯化物
chlorine n. 氯
chloroform n. 氯仿
chlorophyll n. 叶绿素
chocolate n.巧克力；巧克力糖
choice n.选择
choir n. (教堂的)歌唱队
choke vt.使窒息；塞满
choler n. 盛怒
cholera n. 霍乱
choleric adj. 易怒的，暴躁的
cholesterol n.胆固醇
chomp vi. 嚼
choose vt.&vi.选择
chop vt.&vi.砍，伐
chopper n. 切物之人,斧头,切肉大刀,伐木者
chopstick n. 筷子
chopsticks n. 筷子
choral a. 合唱队的
chord n.(乐器的)弦 vi.协调
chore n. 零工,家务
choreography n. 舞蹈，舞蹈编排
chorister n. 唱诗班歌手,唱诗队指挥
chortle v. & n. 开心地笑
chorus vt.&vi.合唱
chose choose的过去式；选择
chosen choose的过去分词；选择
chowder n.一种羹汤
christ n. 救世主(耶稣基督)； int. 天啊！
christen vt. 施洗,行施洗礼,命名
Christendom n. 基督教界
Christian n.基督教徒
Christianity n. 基督教,基督教精神
Christianize vt. 使成基督徒
Christmas n.圣诞节
chromatic adj. 彩色的，五彩的
chrome n. 铬合金
chromosome n. 染色体
chronic a. 慢性的,习惯性的
chronicle n. 年代记,记录,编年史
chronicler  n. 年代记编者,年代史家
chronological a. 按年月顺序的
chronology n.年代学
chronometer n. 精密计时器
chrysalis n. 蛹,茧,准备期
chrysanthemum n. 菊，菊花
chubby adj. 圆胖的，丰满的
chuck v. 放弃，离职
chuckle v. 轻声地笑
chug n. 轧轧声
chum n. 好朋友，同伴
chummy a. 亲密的,合得来的
chunk n. 短厚木头，大量
chunky adj. (人或动物)矮胖的
church n.教堂
churchgoer n. 经常去做礼拜的人
churchman n. 教士；牧师；国教教徒
churchwarden n. 教会委员,陶制的长烟斗
churchyard n.(教堂的)墓地
churl n. 粗鄙之人
churlish adj. 脾气暴躁的
churn vi. (波涛)翻腾；剧烈搅动
cicada n. 蝉
cickness n. 疾病
cide 表示"杀"；(构词成分)杀死
cider n. 苹果酒，苹果汁
cif n. (缩)到岸价
cigar n.雪茄烟，叶卷烟
cigaret  n. 香烟，纸烟，卷烟
cigarette n. 香烟,纸烟
cilia n. 纤毛；睫
ciliated adj. 有纤毛的
cilium n. 纤毛
cinch n. 容易做的事情，确定的事情
cinchona n. 金鸡纳树
cincinnati n. 辛辛那提(美国城市)
cincture n. 围绕物,带,边轮
cinder n. 余烬，矿渣
cinderella n. 灰姑娘(童话中人物)
cinema n.电影院；电影，影片
cinnamon n. 肉桂,肉桂树,肉桂色
cipher n. 零，无影响力的人，密码
circle vt.环绕，盘旋 n.圆
circlet n. 小圈,小的环,饰环
circuit n.电路；环行；巡行
circuitous adj. 迂回的，绕圈子的
circuity n. 曲折性，拐弯抹角的行动
circular a.圆的；循环的
circulate vt.使循环 vi.循环
circulating 流通的，循环的
circulation n.循环；(货币等)流通
circulatory a. 循环的
circumcise vt. 对<某人>行割礼
circumcision n. 割礼
circumference n.圆周，周长，圆周线
circumlocution n. 迂回累赘的陈述
circumnavigate vt. 环航
circumscribe v. 限制
circumspect adj. 慎重的，仔细的
circumspection n. 细心,慎重
circumstance n.情况，条件；境遇
circumstances n. 情况，环境，细节
circumstantial a. 依照情况的
circumvent v. 用计谋战胜，规避
circus n.马戏；马戏团
cirque n. 天然的圆形剧场,圆环,圈谷
cistern n. (抽水马桶的)贮水池
citadel n. 堡垒；避难所
citation n. 引用,引证,引用文
cite vt.引用，引证；举例
citizen n.公民；市民，居民
citizenship n.公民权；国籍
citron n. 香木缘,圆佛手柑,一种西瓜
citrus n. 柑橘类的植物
city n.城市，都市
city-state n. 城邦
civet n.麝猫香
civic a. 城市的；公民的
civil a.公民的；文职的
civilian n.平民 a.平民的
civilisation n. 文明，文化，开化，教化
civilise vt. 使文化，开化，教育；使文明，使开化
civility n. 彬彬有礼，斯文
civilization n.文明，文化；开化
civilize vt.使文明；教育
civilized adj. 文明的；先进的
clack v. 唠叨，发哔剥声
clad a. 穿衣的；被覆盖的
claim n.权利，所有权
claimant n. 提出要求者
clairvoyance n. 超人的，洞察力
clairvoyant a. 透视的,有透视力的
clam n. 蛤，蚶
clamber n. 攀登,爬上
clamor n. 喧闹,叫嚷,大声的要求
clamorous adj. 吵闹的，喧哗的
clamour n. 吵闹、喧哗
clamp n.夹子 vt.夹住，夹紧
clan n. 氏族,宗族,党派
clandestine adj. 秘密的，暗中从事的
clang n. 叮当声,铿锵声
clangor  n.
clank n. 铿然之声,叮当声
clannish adj. 排他的，门户之见的
clansman n. 同一氏族的人,族人,同宗的人
clap n.拍手喝采声；霹雳声
clapboard n. 护墙板,隔板,桶板
clapper n. 铃舌，响板
clara 克拉拉. 布拉恩特
claret n. 红葡萄酒,深紫红色
clarification n. 澄清；解释
clarify vt.澄清，阐明
clarinet n. 竖笛,单簧管,黑管
clarion n. 尖音号角
clarity n. 清楚
clarke 克拉克(姓)
clash n.碰撞声；抵触，冲突
clasp vt.扣住，扣紧，钩住
class n. (学校里的)班；课；阶级；同学们；班级；种类，等级；阶层；(一堂)课，门类，vt. 分类；班级，阶级；类别，把…分成等级
classic n.名著 a.不朽的
classical a.古典的；经典的
classification n.分类；分级；分类法
classify vt.把…分类
classmate n.同班同学
classmates 同班同学(复数)
classroom n.教室
clatter n.得得声，卡嗒声
clause n. 子句,条款
claustrophobia n. 幽闭恐怖症
clave vi. cleave(粘着)的过去式
clavichord n. (敲弦)古钢琴
clavicle n. 锁骨
claw n.爪，脚爪，螯
clay n.粘土；泥土
clean a.清洁的；纯洁的
cleaner n. 清洁工人,清洁剂
cleaning n. 扫除
cleanliness n.清洁
cleanly a. 爱清洁的,干净的,清洁的
cleanness n. 清洁,洁白
cleanse vt. 使清洁,净化,使纯洁
clear adj. 晴朗的；清楚的；清澈的；清晰的；vt. & vt. 清除；扫除；清出(空地)；越过，使清澈；使清楚
clearance n. 清除,解除,间隙,森林开拓
clearing n.(森林中的)空旷地
clearly adv. 清楚地；无疑地，清澈地；明白地，清晰地；明亮地
clearness n. 晴朗,明白
cleat n. 楔子，栓
cleavage n. 裂缝，分裂
cleave v. 劈开，分裂
cleaver n. 切肉刀
clef n. 音部记号
cleft n. 裂缝
clemency n. 仁慈，(气候)温和
clement adj. 仁慈的，温和的
clench vt.咬紧(牙关)
clergy n. (总称)教牧人员；神职人员
clergyman n. 牧师；教士
clerical n. 牧师
clerk n.办事员；秘书
clever adj.机灵的，聪明的
cleverness n. 聪明，机智；机灵
cliche n. 陈腔滥调,铅版
click n.卡嗒声
client n.顾客；诉讼委托人
clientele n. 顾客(总称)；(医生，律师的)顾客，(商店的)常客
cliff n.悬崖，峭壁
climactic a. 渐层法的,顶点的,高潮的
climate n.气候；风土，地带
climatic a. 气候上的
climax n.(兴趣的)顶点
climb v.爬；攀登
climber n. 登山者
clime n. (诗)地方，风土
clinch v. 钉牢，彻底决定
cline (构词成分)斜坡
cling vi.粘住；依附；坚持
clinic n.诊所，医务室；会诊
clinical a. 临床的,病房用的
clink n. 丁当声
clip vt.夹住 n.夹子，钳子
clipper n. 大剪刀,快速帆船修剪者
clipping n. 剪断,剪裁,剪下物,剪报
clique n. 朋党派系，小集团
cloak vt.掩盖，覆盖，掩饰
cloakroom n. 存放衣帽间
clock n.钟，仪表
clockwise a.&ad.顺时针方向转的
clockwork n. 钟表装置,发条装置
clod n. 土块
clog n. 障碍,重物
cloister n. 修道院
cloistered adj. 隐居的
clone v.克隆，无性繁殖
close v.关
closed adj. 关着的；关闭的，停业的；闭迹
closedown n.停业；倒闭
closely  adv. 细细地；紧密地，接近地；严密地；准确地；a. 精密地，仔细地
close-lying a. 紧巾看的
closeness n. 接近，紧密，严密
closet n.壁橱；小房间
closure n. 关闭，中山
clot n. 凝块，v. 使凝成块
cloth n.布；布料
clothe vt.给…穿衣服
clothes n.衣服，服装；被褥
clothier n. 呢绒商,衣商
clothing n.衣服，被褥
cloths 布
cloud n.云
cloudburst n. 大暴雨，豪雨
cloudless a. 晴朗的,无云的
cloudy adj.多云的，阴天的
clout n. 破布，碎片布
clove n. 丁香
clover n. 苜蓿
cloverleaf n. 四叶苜蓿形的立体道路交叉点
clown n.(马戏的)小丑，丑角
clownish a. 滑稽的
cloy n. (吃甜食)生腻，吃腻
cloying adj. 甜得发腻的
club n.俱乐部；社团
cluck n. 咯咯的叫声
clue n.线索，暗示，提示
clump n. 丛,块,笨重的脚步声
clumsily ad. 笨拙地，样子瞥脚地
clumsy adj.笨拙的；不灵活的
clung cling的过去式(分词)
cluster n.一串 vt.使成群
clutch vt.抓住 vi.掌握，攫
clutter n. 杂乱
co (前缀)共同，一起，相互
coach vt.辅导，指导，训练
coachman n. 马车夫
coadjutor n. 助手,副员,副主教
coagulant n. 凝结剂
coagulate v. 凝结，使凝结
coagulation n. 凝结,凝结物
coal n.煤，煤块
coalesce v. 联合，合并，结合
coalescence n. 聚结；凝聚
coalition n. 结合，联合
coarse a.粗的，粗糙的
coarseness n. 粗糙,劣等,粗
coast n.海岸，海滨(地区)
coastal a. 海岸的,沿海的,沿岸的
coaster n. 沿岸贸易船
coastline n. 海岸线
coat n.外套，上衣；表皮
coating n. 涂层
coax v. 哄诱，巧言诱哄
cob n. 圆块
cobalt n. 钴,钴类颜料,由钴制的深蓝色
cobble n. 圆石,鹅卵石,圆石子路
cobbler n. 补鞋匠
cobblestone n. 圆石,鹅卵石
cobble-stone n. (铺路的)鹅卵石
cobol 面向商业的语言
cobra n. 眼镜蛇
cobweb n. 蜘蛛网,蛛丝,混乱
cocaine  n. 『化学』古柯碱
cochineal n. 虫红,胭红,胭脂虫
cochlea n. 蜗
cock n.旋塞，开关，龙头
cockade n. 帽章
cockatoo n. 美冠鹦鹉
cockatrice n.  鸡头蛇身怪兽
cockerel n. 小公鸡,好斗的年轻人
cockle n. 海扇类,海扇壳,小舟,火炉,皱,
cockpit n. 驾驶员座舱,战场
cockroach n. 蟑螂
cocktail n. 鸡尾酒,开味菜
coco n. 椰子树,椰子,脑袋
cocoa n. 可可粉,可可饮料,可可色
coconut n. 椰子
cocoon n.蚕茧
cod n. 鳕
coddle vt. 娇养,溺爱,煮蛋
code n.准则；法典；代码
codex n. 古抄本,法律,规则,药典
codfish n. 鳕
codicil n. 遗嘱的附录，附加条款
codify v. 编码
codling n. 未熟的小苹果,幼鳕
coed n.男女同校的学生
coeducation n.男女同校
coefficient n.协同因素；系数，率
coenzyme n. 辅酶
coerce v. 强迫，压制
coercion n. 强迫,威压,高压政治
coercive a. 强制的,强压的,强迫的
coeval a. 同时代的
coexist vi. 共存
coffee n.咖啡
coffeepot n. 咖啡壶
coffer n. 保险箱
coffin n.棺材，柩
cog v./n. 诈骗，欺骗n. 齿轮的齿，轮牙
cogency n. 说服力，中肯
cogent adj. 有说服力的
cogitate v. 慎重思考，思索
cogitation n. 思考，苦思
cognac n. 白兰地酒的一种
cognate adj. 同词源的，同类的
cognition n. 认识,认识力,知觉
cognitive a.认识的
cognizance n. 认识,认定,审理
cognizant a. 已认识,既知道,晓得
cognomen n. 姓
cohabitation n. 同居
cohere vi. 附着,粘着,凝聚,符合
coherence n. 一致性
coherent adj. 有条理的，紧凑的；粘着的；条理清楚的；连贯的，一致的
cohesion n. 内聚力
cohesive adj. 有粘性的；凝聚的，凝结的
cohort n. 步兵大队,军队,一群
cohorts n. 军团
coil n.(一)卷；线圈 vt.卷
coin n.硬币；铸造(硬币)
coinage n. 造币
coincide vi.相符合；相巧合
coincidence n. 巧合(之事)
coincident a. 一致的,符合的,暗合的
coke n.焦炭 vt.&vi.炼焦
colander n. 滤器，漏勺
cold a.冷的；冷淡的 n.冷
cold-blooded adj. (动物)冷血的；无情的
coldly adv. 冷淡地；无情地
coldness n. 寒冷,冷,冷淡
cole n. 油菜,小菜
colic n. 绞痛,疝痛,疝气
coliseum n. 竞赛场
collaborate vi.协作，合作；协调
collaboration n. 合作；协作，通敌；勾结
collaborative a. 协作的，合作的
collage n. 拼贴画
collagen n. 胶原
collapse vi.倒坍；崩溃，瓦解
collar n.衣领，项圈
collate v. 对照，核对
collateral adj. 平行的，旁系的
collation n. 校勘，整理
colleague n.同事，同僚
collect vt.收集 vi.收款
collecting 集邮
collection n.搜集，收集；收藏品
collective a.集体的；集合性的
collectively ad. 集体地，共同
collector n. 收集家,收税员
college n.(综合大学中的)学院
collegiate a. 学院的
collide vi.碰撞；冲突，抵触
collie n. 牧羊狗
collier n. 矿工,煤船,煤船员
colliery n. 煤坑,煤矿,煤炭主意
collision n.碰撞；冲突
collocation n. 排列,安排,布置
collop n. 薄肉片，小肉骗，皮肤的皱折
colloquial a. 白话的,口语的,语体的
colloquium n. 学术讨论会
colloquy n. 谈话,会话,自由讨论
collude v. 串通，共谋
collusion n. 勾结，串通
cologne n. 科隆香水
colon n. 冒号,结肠
colonel n.陆军上校；中校
colonial a.殖民地的，殖民的
colonist n.移民；殖民地居民
colonization n. 开拓殖民地,殖民
colonize vt. 在...开拓殖民地
colonnade n. 柱廊
colony n.殖民地；侨居地
color n.颜色，彩色；颜料
colorado n. 科罗拉多(州)(美国)
coloration n. 着色,配色,彩色
color-blind adj. 色盲的
colored a. 染色的
colorful adj. 颜色丰富的；色彩丰富的
colorless a. 无色的
colossal adj. 巨大的，庞大的
colossus adj. 巨人，巨型雕像
colour n.颜色
colour-blind a. 色盲的
colour-blindness 色盲
coloured a.有色的，着色的
colourful adj. 绚丽多彩的，彩色的；艳丽的；吸引人的；颜色丰富的，多色的，引人入胜的
colouring n. 色彩；外貌；伪装
colourless a. 平庸的；苍白的；无趣味的，无特色的；无色的；不生动的
colt n. 小雄驹
coltish adj. 放浪不拘的，似小马的
columbia n. 哥伦比亚(美国城市)
columbine a. 鸽的,鸽似的,鸽色的
columbus n. 哥伦布(美国一地名)
column n.柱，支柱，圆柱
columnist n. 专栏作家
coma n. 昏迷状态
comatose adj. 昏睡的；无生气的；昏迷的；昏迷不醒的；不醒人事的
comb n.梳子
combat vt.跟…战斗 vi.格斗
combatant n. 争斗者,战斗员
combative a. 好战的,杀气腾腾的,斗志旺盛的
combe n.深谷
combination n.结合，联合；化合
combine vt.使结合；兼有
combing vi. & vt. 联合结合；n. 联合收割机
combo n. 二进位组合码
combust vi. 燃烧，消耗
combustible adj. 易燃的，易激动的
combustion n.燃烧；氧化；骚动
come vi.来，来到；出现
comedian n. 喜剧演员
comedy n.喜剧；喜剧场面
comeliness n. 清秀,美丽,合宜
comely adj. 动人的，美丽的
comer n. 来的人,新来者,有希望的人
comestible adj. 可吃的，可食用的
comestic a. 本国的
comet n. 彗星
comfit n. 糖果,酒馅的巧克力
comfort n.舒适；安慰 vt.安慰
comfortable a.舒适的，安慰的
comfortably adv. 舒适地
comforter n. 安慰的人,安慰者,圣灵
comforting a. 安慰的，安慰人的
comfortless a. 无安慰的,不舒服的,不自由的
comic n. 连环图画,喜剧演员,杂耍滑稽演员
comical a. 滑稽的，可笑的
coming n. 进来；a. 即将到来的；有指望的；来到；就要来的
comity n. 友谊,礼让
comma n. 逗点,逗号
command vt.命令，指挥；控制
commandant n. 司令官
commandeer vt. 征募,霸占
commander n.司令官，指挥员
commandment n. 戒律
commemorate vt. 纪念
commemoration n. 纪念,纪念节,庆典
commence vt.开始 vi.获得学位
commencement n. 开始，(大学的)毕业典礼
commend vt.称赞，表扬；推荐
commendable adj. 值得称赞的
commendation n. 赞赏,嘉奖,推荐
commensurate adj. 同样大小的，相称的
comment n.评论，意见；注释
commentary n. 注释,评论,批评
commentator n. 注解者
commerce n.商业，贸易；社交
commercial a.商业的；商品化的
commercialization n. 商品化
commingle vt.vi. 混合
commiserate v. 同情；慰问；怜悯
commiseration n. 怜悯,同情,追悼辞
commissar n. 政委
commissariat n. 军需部,粮食,粮食补给
commissary n. 代表,委员,物资供应所
commission n.委托，委任；委托状
commissioner n. 地方长官
commit vt.犯(错误);干(坏事)
commitment n. 约束；责任；承诺，约定
committee n.委员会；全体委员
commode n. 洗脸台,小橱,便桶
commodious adj. 宽敞的
commodity n.日用品，商品，物品
commodore n. 海军准将,船队队长
common adj.普通的，一般地
commonalty n. 平民,大众,民众团体
commoner n. 平民,自费学生,有共用权的人
commonly ad.普通地，一般地
commonplace a.平凡的 n.平常话
commonsense n. 常识；a. 有常识的，明明白白的
commonweal n. 公益
commonwealth n.共和国；联邦
commotion n. 骚动，动乱
communal a. 公有的
commune n. 恳谈,自治体,工社
communicable a. 可传达的,会传染的,爱说话的
communicate vi.&vt.通信；通话
communication n.通讯；传达；交通
communicative adj. 通讯的
communion n. 交流,恳谈,宗教团体
communism n.共产主义
communist adj.共产主义的
community n.社区；社会；公社
commutator n. 换向器,整流器
commute n. 承车上下班
commuter n.乘公交车辆上下班者
compact a.紧密的 vt.使紧凑
companion n.同伴；同事
companionable a. 适于做朋友的,好交往的
companionship n. 交谊,友谊,陪伴
company n.公司
comparable a.可比较的；类似的
comparative a.比较的，相对的
comparatively adv. 比较地；相当地；相对地
compare vt.比较，对照；比作
compare...to 比作…；比喻为…；与…相比较
comparison n.比较，对照；比似
compartment n. 间隔,个别室,小事,车厢
compass n.罗盘，指南针；圆规
compassion n. 同情，怜悯
compassionate adj. 有同情心的
compatibility n. 兼容性，适应性；和谐共处，不矛盾
compatible a.一致的；兼容制的
compatriot n. 同国人
compeer n. 地位相等的人,同辈,伙伴
compel vt.强迫，迫使屈服
compellation n. 姓名，头衔
compelling adj. 引起兴趣的
compels v. 强迫
compendious adj. 简洁的，简要的
compendium n. 简要，概略
compensate vt.&vi.补偿，赔偿
compensation n.补偿，赔偿，赔偿费
compete vi.比赛；竞争；对抗
competence n. 能力
competency n. 胜任,资格,能力
competent a.有能力的；应该做的
competition n.竞争，比赛
competitive a.竞争的，比赛的
competitivemechanism 竞争机制
competitiveness n. 竞争能力
competitor n.竞争者，敌手
compilation n. 编辑
compile vt.编辑，编制，搜集
compiler n. 编译程序(器)
complacence  n. 自满,自得; 自以为是
complacency n. 自满，自得
complacent adj. 自满的，得意的
complain vi.抱怨，拆苦；控告
complaining adj. 抱怨的，发牢骚的
complaint n.疾病，病痛；主诉
complaisance n. 迁就，奉承
complaisant adj. 顺从的，讨好的
complement vt.补充 n.补足(物)
complementary a. 互补的，补充的
complete adj.完全的，彻底的
completely adv.完全地，彻底地
completeness n. 完全
completion n.完成，结束，完满
complex a.结合的；复杂的
complexion n. 肤色，局面
complexity n.复杂(性)
compliance n. 服从，听从
compliant adj. 服从的，顺从的
complicate vt.使复杂；使陷入
complicated v. 使复杂化，使混乱；adj. 难懂的，难解的；复杂的
complication n.复杂，混乱；并发症
complicity n. 共谋,共犯,连累
compliment n.问候 vt.赞美，祝贺
complimentary adj. 赞赏的
comply vi.应允，遵照，照做
component n.组成部分；分；组件
componential adj. 成分的
components 零件
comport v. 举止，行为
comportment n. 举止
compose vt.创作(乐曲)vi.作曲
composed a. 镇静的,沉着的
composer n.作曲家
composite a.合成的 n.合成物
composition n.组成，构成，结构
compositive a. 合成的，综合的
compost n. 混合物,堆肥
composure n. 镇静，沉着，自若
compound n.化合物；复合词
comprador 买办
comprehend vt.了解，理解，领会
comprehension n.理解，理解力；领悟
comprehensive a.广泛的；理解的
compress vt.压紧，压缩
compressed a. 压缩的
compression n.压缩，压紧，浓缩
compressor n. 压缩机
comprise vt.包含，包括；构成
compromise n. 妥协，和解；折衷；v. 和解；危及；让步；妥协，危害；折衷
comptroller n. 审计官
compulsion n. 压力，难以抗拒的冲动
compulsive adj. 难以抑制的
compulsory a.强迫的，义务的
compunction n. 懊悔，良心不安
computation n. 计算
compute vt.&vi.计算
computer n.计算机，电脑
computergame n. 电子游戏
computerization n. 计算机化
computerize v. 使…计算机化
comrade n.同志，亲密的同伴
comradeship n. 同志关系；友谊
con v. ①熟读，精读 ②哄骗
concatenate v. 连结；连锁； 连接，串联，并置
concatenation n. 连结，一连串
concave adj. 凹的
concavity n. 中央凹陷,凹洼,凹状
conceal vt.把…隐藏起来
concealment n. 隐匿,隐蔽,躲藏
concede v. 承认（为正确），让步
conceit n.自负，自高自大
conceited adj. 自负的，自高自大的
conceivable adj. 想像得出的，可信的
conceive vt.设想，以为；怀孕
concentrate vt.&vi.浓缩，提浓
concentrated adj. 全神贯注的
concentration n.集中；专注；浓缩
concentric a. 同中心的,集中性的
concept n.概念，观念，设想
conception n.概念，观念，想法
conceptive adj. 概念的
concern n.关心，挂念；关系
concerned a. 关心的
concerning prep.关于
concert n.音乐会；演奏会
concerted adj. 齐心协力的；协定的，商议的
concerto n. 协奏曲
concess v. 让步
concession n.让步，迁就
conch n. 贝壳
conciliate v. 安抚，调和
conciliation n. 安慰，安抚
conciliatory a. 安抚的,怀柔的,融和的
concise adj. 简洁的
concision n. 简明，简洁
conclave n. 秘密会议,教皇选举会议,红衣主教团
conclude vt.&vi.推断出，断定
conclusion n.结论，推论；结尾
conclusive a. 决定性的,确实的,最后的
conclusively 最后地
concoct v. 调制，捏造
concoction n. 调配（物），谎言
concomitant adj. 伴随而来的
concord n. 和睦，公约
concordance n. 调和,一致,用语索引
concordant adj. 和谐的，一致的
concordat n. 协定；宗派间的协约
concourse n. 集合,合流,群众
concrete n.混凝土；具体物
concubine n. 妾,姘妇,第二夫人以下之妻
concur vi. 意见相同,一致,互助
concurrence n. 赞同,意见一致,协力
concurrent adj. 同时发生的，一致的
concurrently ad. 同时发生
concussion n. 脑震荡，震动
condemn vt.谴责，指责；判刑
condemnation n. 谴责，定罪
condemned a. 被判死刑的
condensation n. 压缩,凝缩,液化
condense vt.压缩，使缩短
condenser n. 凝结器,冷凝器,冷却器
condescend v. 屈尊，俯就
condescension n. 自以为高人一等，贬低（别人）
condign a. 相当的,适宜的
condiment n. 调味品，佐料
condiments n. 调味品
condition n.条件；状况
conditional a. 有条件的,假定的
conditioned a.受某种情况限制
condole "with	v. 向…吊慰"
condolence n. 吊唁，哀悼
condominium n.共
condone vt. 赦,宽恕
condor n. 秃鹰
conduce "to	v. 引起，有助于"
conducive adj. 有助于…的
conduct n.举止，行为；指导
conducter 售票员
conduction n. 传导
conductivity n. 导电率,传导率,传导度
conductor n.售票员；(乐队)指挥
conduit n. 导管,水管,沟渠
cone n. 圆锥体,球果
coney n. 兔毛
confabulate v. 闲谈，讨论
confection n. 甜食，糖果
confectioner n. 糖果制造人,糖果店
confectionery n. 糕饼,糕饼制造,制饼厂
confederacy n. 联盟
confederate n. 同盟者,同盟国
confederation n. 同盟,联盟,组织联盟
confer vt. 授予
conference n.会议，讨论会
confess vt.供认，承认；坦白
confession n. 自认,自白,招供
confessional a. 自白的,忏悔的
confessor n. 自白者
confidant n. 心腹朋友,知己
confide v. 吐露（心事）
confidence n.私房话，秘密，机密
confident n.确信的，自信的
confidential a.秘密的；亲信的
confidently ad. 自信地；有信心地
configuration n. 轮廓，结构
configure vt. 使成形；使具形体
confine vt.限制；禁闭
confinement n. 限制,禁闭,坐月子
confines n. 范围
confirm vt.证实，肯定；批准
confirmation n.证实，确定；确认
confiscate v. 没收，充公
confiscation n. 没收,充公,征发
conflagration n. 建筑物或森林大火
conflate v. 合并
conflict n.争论；冲突；斗争
confluence n. 合流，汇流
confluent a. 合流的,汇合的,融合性的
conflux n. 合流,合流点,集合,人群
conform vt.使遵守 vi.一致
conformable a. 适合的,一致的,调和的
conformity n. 一致
confound vt. 使混淆,使狼狈,挫败
confounded 惊慌失措的，困惑的
confraternity n. 团体,协会,帮会
confront vt.使面对；使对证
confrontation n. 面对，对峙；对抗
Confucius n.孔
confuse vt.使混乱，混淆
confusedly ad. 受困惑地,慌乱地,混乱地
confusion n.混乱；骚乱；混淆
confutation n. 驳倒,驳住
confute vt. 驳倒,驳住
congeal v. 凝结，凝固
congenial adj. 意气相投的，宜人的
congenital adj. （病等）先天的，天生的
conger n. 『鱼』 (欧洲) 康吉鳗
congest vt.密集；充血，使拥挤
congested a. 拥挤的
congestion n. 充血，拥挤
conglomerate v. 集聚，集团
conglomeration n. 聚集；凝聚
congo 刚果
congratulate vt.祝贺，向…道喜
congratulation n.祝贺，庆贺
congregate v. 聚集，集合
congregation n. 集合在一起的群众
congregational a. 会众的,公理教会的
congress n.大会；国会，议会
congressional a. 会议的,议会的,国会的
congressman n. 国会议员,众议院议员
congruence n. 适合,一致,相合性
congruent adj. 全等的
congruity n. 全等，一致
conical  adj. 圆锥 (体,形) 的
conifer n. 针叶树
conjecture n./v. 推测，臆测
conjoin vt.vi. (使)结合,(使)连结,(使)联合
conjugal adj. 婚姻的，夫妻的
conjugate vt. 结合,配合,使成对
conjugation n. 结合,配合,动词的变化
conjunct a. 联合的，连接的
conjunction n.接合，连接；连接词
conjunctive a. 连结的,结合的,联合的
conjuration  n. 符咒,咒语; 魔法
conjure v. 变魔术，变戏法
conjurer n. 魔术师
conjuring n. 魔术
connect vt.连接，连结；联系
connect...with... 把…连接起来；把…连结起来
connected adj. 连结的；有联系的；连接的
connection n.连接，联系；连贯性
connective a. 连接着,连接的
connectivity n. 连通性，联络性
connector n. 连结者,连结手,连结物
connexion n. 联系，连结
connivance n. 共谋，纵容
connive v. 默许，共谋
connoisseur n. 鉴赏家，行家
connotation n.(词等的)涵义
connotative adj. 有含意的，暗示的
connubial a. 结婚的,夫妇的,配偶的
conquer vt.征服
conqueror n.征服者，胜利者
conquest n.攻取，征服；克服
consanguinity n. 血亲，同家
conscience n.良心，道德心
conscientious a. 有责任心的,负责的,本着良心的
conscientiously adv. 认真地
conscious a.意识到的；有意的
consciousness n.意识，觉悟；知觉
conscript v. 征兵，征召
conscription n. 征募
consecrate vt. 供神用,奉献,使神圣
consecration n. 供献,奉献,神圣化
consecutive a. 连续的,联贯的,始终一贯的
consensus n. 一致,交感
consent n.同意，赞成 vi.同意
consequence n.结果，后果
consequent a.作为结果的；必然的
consequential adj. 产生后果的，重要的
consequently ad.因此，因而，所以
conservation n.保存，保护；守恒
conservationist n.自然资源保护论者
conservatism n. 保守主义
conservative a.保守的 n.保守的人
conservatory n. 温室，音乐学院
conserve n. 蜜饯,果酱
consider vt.考虑；把...看作
consider...as (把某人)看作…
considerable a.相当大的；重要的
considerably ad. 十分地；相当地
considerate a.考虑周到的；体谅的
consideration n. 考虑，思考；体贴；照顾；原因；体谅；研究，讨论；补偿，报酬；理由；需考虑到的事，关心
considered a. 考虑过的，被尊重的
considering prep. 就…而论
consign v. 托运，托人看管
consignee 收货人，承销人，受托人
consignment n. 托运，寄售
consignment-in 承销，承销品
consignor 寄销人，委托人，发货人
consist vi.由…组成；在于
consistence n. 坚固性,浓度
consistency n. 坚固性,浓度,一致性
consistent a.前后一致的，连贯的
consistently ad. 一致地；始终如一地
consistory n. 宗教法院,红衣教会议,监督法院
consitstent a. 一致的，符合的，坚持的，相容的
consolation n. 安慰，慰藉
consolatory a. 慰问的,可藉慰的
console n.悬臂，肘托；控制台
consolidate vt.巩固 vi.合并
consolidated adj. 加固的，统一的；固定的
consolidation n. 巩固,团结,合并,加强
consomme n. 清汤
consonance n. 一致,调和,和音
consonant n. 辅音
consort n. 配偶,夫妻
consortium n. 财团
conspectus n. 概要，大纲
conspicuous adj. 显著的，显而易见的
conspiracy n. 阴谋
conspirator n. 阴谋者，谋叛者
conspire v. 阴谋，谋叛
constable n. 治安官,警官,巡官
constancy n. 坚定不移,恒久不变
constant a.经常的；永恒的
constantinople n. 君士坦丁堡(土尔其)
constantly adv. 经常地；不断地；不变地，a. 经常地
constellation n. 星座，星群
consternation n. 大为吃惊，惊骇
constipation n. 便秘,秘结
constituency n. 选民,顾客,读者
constituent a.形成的 n.选民
constitute vt.构成，组成
constitution n.(人的)体格，素质
constitutional a. 宪法的；章程的
constitutive adj. 宪法的，章程的
constrain vt. 强迫；压制，抑制
constraint n.强迫，结束；强制力
constrict vt. 约事；收缩
constriction n. 压缩,收缩,紧压的感觉
constrictive a. 紧缩的,束紧的,压缩性的
construct vt.建造；建设；构筑
construction n. 建设(不可数名词)；建造；建筑；建筑物；结构；作图(法)；修建；解释，工程；构造
constructive a. 建设性的,构造上的,作图的
constructively ad. 积极地
construe v. 解释，翻译
consul n.领事
consular a. 领事的
consulate n. 领事馆
consulship n. 领事的职位,领事的任期
consult vt.查阅
consultancy 咨询服务
consultant n. 咨询顾问(公司)；顾问咨询商议者；(受人咨询的)顾问，会诊医生
consultation n. 请教,咨询,协议会
consumables 消费品
consume vt. 消耗，消费；消灭；耗尽；花费，毁灭，浪费；憔悴；vi.使用；消费掉，枯萎
consumer n.消费者，用户
consumerism 保护消费者利益主义
consummate adj. 完全的，完美的，v. 完成
consummation n. 达到极点，完成
consumption n.消费(量)，灭绝
consumptive a. 消费的,浪费的,消耗性的
contact vt.使接触；与…联系
contagion n. 传染（病）
contagious adj. 传染的，有感染力的
contain vt.包含，容纳；等于
container n.容器；集装箱
containerization n.集装箱化
containerize 用集装箱运
contaminate vt. 弄污,弄脏,毒害,传染,染污
contamination n. 污染,污物,混淆
contango 期货溢价；交易延期费
contemn vt. 侮辱,蔑视
contemplate v. 深思，（严肃）注视
contemplation n. 沉思，思考
contemplative a. 沉思的,爱默想的,冥想的
contemporaneous a. 同时期的,同时代的
contemporaries n. 同时代人
contemporary a.当代的，同时代的
contempt n. 轻视；轻蔑；藐视；受辱；不顾；鄙视；蔑视，丢脸
contemptible adj. 令人轻视的
contemptuous a. 轻蔑的,侮辱的,瞧不起人的
contemptuously ad. 蔑视地；傲慢地
contend  vt. 坚决主张；争斗；竞争；争夺，vi. 竞争，主张，争辩；斗争；争论
content n.内容，目录；容量
contented a. 满足的,心安的
contention n. 争论，论点
contentious adj. 好辩的，喜争吵的
contentment n. 满足
contents n. 容纳物，内容，目次；所装的东西；要旨
contest vt.争夺，争取；辩驳
contestant n. 参赛人
context n.上下文；来龙去脉
contextual adj. 上下文的，环境的
contiguity n. 邻近，接壤
contiguous adj. 接近的，接壤的
continence n. 节制、克制力
continent n.大陆；洲
continental a.大陆的，大陆性的
contingency n. 意外事件，可能性
contingent adj. 意外的，视情况条件而定的
continual a.不断的；连续的
continually adj. 不断地；连续地；频繁地
continuance n. 继续的期间,停留,持续
continuation n. 继续,续集,延长
continue vt.继续，连续；延伸
continued a. 继续的
continuity n. 连续性
continuous adj. 连续的；持续的；连续不断的，不断的；延长的；不间断的
continuously  adv.连续不断地；连续地，持续地
continuum n.连续的事
contort v. (使)扭曲
contortion n. 扭曲，弯曲
contortions n. 扭歪；弯曲
contour n. 轮廓
contra n. 对方帐户，抵清帐户(优指贷方)
contraband n. 走私，非法运输
contraceptive a.避孕
contract n.契约，合同；婚约
contracted adj. 合同所规定的；收缩了的；缩略的
contractile a. 会缩的,有收缩性的
contraction n. 收缩
contractionary 收缩性
contractor n. 立契约的人,承包商
contractual adj. 合同的，契约的
contradict vt.反驳，否认
contradiction n.矛盾，不一致；否认
contradictory a. 反驳的,反对的,抗辩的
contralto n. 最低的女低音,唱女低音的歌唱家
contrariety n. 反对,矛盾,相反物
contrariwise ad. 反之,顽固地
contrary n.相反；反面；对立面
contrast n. 对照；悬殊差别；对比；反差，对比度；vt. 使对比； 使与…对比；使与…对照 vi. 形成对比；对比(着重于相异处)
contravene v. 违背（法规，习俗等）
contravention n. 违法
contribute vt.捐献，捐助；投稿
contribute...to 向…贡献出
contribution n. 贡献
contributor n. 贡献者,捐助者,赠送者,投稿者
contrite adj. 悔罪的，痛悔的
contrition n. 悔罪，痛悔
contrivance n. 发明,发明的才能,想出的办法,
contrive v. 计划，设计
contrived adj. 不自然的，人造的
contriver n. 发明者,创制者,筹谋者
control vt.&n.控制；支配
controlled a. 受控制的，受操纵的
controller n. 控制器,管理者
controversial a. 有争论的
controversy n.争论，辩论，争吵
controvert v. 反驳，驳斥
contruct vt. 建造，构造
contruction n. 建造，建筑，建设
contumacious adj. 违抗的，不服从的
contumacy n. 抗命，不服从
contumelious adj. 无礼的，傲慢的
contumely n. 无礼，傲慢
contusion n. 殴打,打伤,挫伤
conundrum n. 谜语
convalesce v. (病)康复，复原
convalescence n. 病后康复期
convalescent a. 渐愈的;恢复期的
convene vt. 集合,召集,召唤
convenience n.便利，方便；厕所
convenient a.便利的；近便的
conveniently  adv.便利地；方便地；合宜地
convent n. 女修道会
conventicle n. 非国教徒的秘密聚会
convention  n. 习俗，惯例；公约，(换俘等)协定；会议；常规，契约
conventional a.普通的；习惯的
conventionality n. 陈规陋习，因袭传统
converge v. 会聚，集中于一点
convergence n. 集中,收敛
convergent a.汇合的；聚集
conversant adj. 精通的，熟知的
conversation n.会话，非正式会谈
converse vi. 交谈
conversely  adv. 相反地；反过来
conversion n.转变，转化；改变
convert v. 转变，改变，变换；使转变；使改变；变更；转换，改变信仰；n. 改变信仰者
convert...into 把…转化成
converted a. 转换的，变换的
convertible adj. 可转换的，n. 敞篷车
convex adj. 凸出的
convey vt. 传送；运送；传播；转让；传达；通报；v. 运输，传达
conveyance n. 运输,运输工具,财产让与
conveyor n. 传送机
convict v. 定罪，n. 罪犯
conviction n.确信，信服，深信
convince vt.使确信，使信服
convinced adj. 信服的
convincing a. 有说服力的；有力的
convivial adj. 欢乐的，狂欢的
convocation n. 召集，会议
convoke v. 召集会议
convoluted adj. 旋绕的，费解的
convolution n. 回旋,卷旋,盘旋
convoy v. 护航，护送
convulse v. 使震动，震惊
convulsion n. 骚动，痉挛
convulsive a. 摇撼的,抽搐的,骚动的
cony n. 兔子
coo vi.(鸽)咕咕地叫
cook vi.烹调，煮 n.厨师
cookbook n. 食谱；烹饪书
cooker n. 炊具,厨师
cookery n. 烹调法,烹调术
cookie n.小甜饼
cookies n.饼干
cooking n. 烹饪；烹调用的
cooky  n. = cookie 小甜饼
cool vi.&vt.(使)凉快,冷却
cooler n. 冷却器
coolie n. 苦力,小工
coolly ad. 冷(静地)，沉着地
coolness n. 冷,凉爽,冷静
coon n. 浣熊,狡滑兔,黑人
coop n. （鸡、）笼、栏
co-op n. 合作社
cooper n. 制桶工人
cooperate v. 合作，协作；配合
co-operate vi.合作
cooperation n. 合作，协作
co-operation n. 合作
cooperative  n. 合作社；adj. 合作的
co-operative adj.合作的
cooperatively adv. 合作地，抱合作态度地
cooperator 合作者
coordinate vt. 使协调，调节；使同等；协作，协调坐标的；同等的；(语法)并列的；并列的，协同的；同等者，同位；同等的人；n. 坐标；a. & n. 同等的
co-ordinate a.同等的，并列的 n.同等物（人）
coordination n. 协调
coot n. 黑鸭,笨人,傻瓜
cop n. 警察(slang俚语)
cope vi.对付，应付
copious adj. 丰富的，多产的
copper n.铜；铜币，铜制器
copperas n. 绿矾
coppice n. 矮林
coprocessor n. 协同处理器
copse n. 小灌木材,杂树林
copy vt.抄写 n.副本
copybook n. 习字帖；习字本
copyright n. 版权，著作权
coquetry n. 卖弄风情，媚态
coquette n. 卖弄风情的女人，狐狸精
coracle  n. 轻便小舟
coral 珊瑚, 珊瑚虫
cord n.细绳；(弓的)弦
cordage n.绳索
cordial a.真诚的，诚恳的
cordiality n. 诚实,郑重,恳挚
cordially adv. 亲切地；热诚地
cordillera  n. 山脉,山系
cordon n. 警戒线，哨兵线
corduroy n. 灯芯绒,用该布制的衣服,裤子
cordwood n. 锯成及堆成128立方英尺之柴薪
core n.果实的心，核心
Corinthian adj. (古代希腊的) 科林斯的
cork n. 软木塞,软木树,软木
corkscrew n. 拔塞钻,螺丝锥
cormorant n. 鸬鹚,贪婪的人
corn n. 谷物；(英)小麦；五谷；(美)玉米
cornea n. 角膜
corner n.角；(街道)拐角
cornerstone n. 奠基石,基础
cornet n. 短号. 圆锥形蛋卷（cone）
cornfield n. 稻田；麦田；玉米田
cornflower n. 矢车菊
cornice n. 壁带,柱带
cornucopia n. 象征丰收的羊角(羊角装饰器内装满花，果，谷物等以示富饶)
corny adj. 平谈无奇的，乡巴佬的
corolla n. 花冠
corollary n. 系,推论,必然的结果
corona n. 日冕（月球经过太阳前面时，太阳外围呈现的光环），
coronal n. 冠,花冠,冠状物
coronary adj. 冠状的
coronation n. 加冕，加冕礼
coroner n. 验尸官
coronet n. 冠,冠冕,冠状头饰
corparate a. 共同的，全体的
corpase n.尸体；被废弃的东西
corporal adj. 肉体的，身体的
corporate adj. 团体的，共同的
corporation n.公司，企业；社团
corporeal a. 肉体的,有形的,物质的
corps n. 队；团；特殊兵种
corpse n. 尸体
corpulence n. 肥胖，臃肿
corpulent adj. 肥胖的
corpus n. 全集，全部资料
corpuscle n. 血球，细胞
corral n. （牛、马等）畜栏
correct a.正确的 vt.纠正
correction n.改正，纠正，修改
corrective a. 纠正的,改正的,矫正的
correctly adv. 正确地；恰当地；adj. 正确地；恰当地
correlate n.互相关联的事物
correlation n.相互关系；对射
correlative a. 有相互关系的,相关的
correspond vi. 相当于；符合；通信(联系)；一致；(to)相当，相应；与…一致，相符合
correspondence n. 往来函件；通信；符合；相应，相当；信件，一致对应
correspondent n.通信者；通讯员
corresponding  adj. 相应的；符合的；通信的；相当的；一致的
correspondingly ad. 相应地
corridor n.走廊，回廊，通路
corroborate v. 支持或证实，强化
corroboration n. 证实，支持，证据
corrode vt. 使腐蚀,侵蚀,破坏
corrosion n. 腐蚀，侵蚀；锈
corrosive a. 腐蚀的,腐蚀性的,蚀坏的
corrugate v. （使）起波浪形，起皱纹
corrugation n. 波浪形状，起皱纹
corrupt adj. 腐败的，腐化的；收受贿赂的，不道德的，邪恶的，败坏的；v. 败坏；贿赂；使腐败，行贿收买
corruptible a. 易腐败的,易堕落的,易恶化的
corruption n. 腐败,堕落,贪污
corsage n. 胸部,胸衣,装饰的花束
corsair n. 海盗,海盗船,回教徒的私掠船
corselet n. 盔甲,胸衣
corset n. 紧身衣
corslet n. 盔甲,胸衣
cortege n. 行列,扈从,随从
cortex n. 外皮
cortical a. 外皮的
cortisone n. 肾上腺皮质激素
coruscate v. 闪亮，闪光
coryza n. 普通感冒，鼻炎
cosine n. 余弦
cosm (构词成分)宇宙，世界
cosmetic n. 化妆品；a. 化妆用的，美发的
cosmetics n. 化妆品
cosmic a.宇宙的；广大无边的
cosmogony n. 宇宙的产生,宇宙进化论
cosmopolitan a. 不限于国家或地区范围的；全世界的
cosmos n.宇宙；秩序，和谐
Cossack n.
cosset v. 宠爱，娇养
cost vi.值(多少钱) n.成本
costing n.成本会计，成本核算
costliness n. 高价,昂贵,奢侈
costly a.昂贵的；价值高的
costume n. 服装，剧装
costumer n.服装供应商
cosy  adj. = cozy a.舒适的,安逸的,惬意的
cosy,cozy adj. 温暖而舒适的
cot n. 小屋；吊床；v把…关进
cote n. 棚,窝,栏
coterie n. （有共同兴趣的）小团体，小圈子
coterminous adj. 毗连的，有共同边界的
cottage n.村舍，小屋
cottar n.住茅屋者
cotter n.住茅屋者
cotton n.棉；棉线；棉布
cottonwood  n. 『植物』三叶杨
cotton-wool n. 药棉，原棉
cotyledon n. 子叶,瓦松属
couch n.睡椅，长沙发椅
couchant a. 俯伏的,蹲着的,抬头伏卧状的
couchette n. (法)火车卧铺
cougar n. 美洲豹
cough n. & v. 咳嗽；咳
could aux.v.(can的过去式)
couldn't (同)could not
couldst can的第二人称单数
council n.理事会，委员会
councilor n.顾问,评议员
counsel n.商议；忠告；律师
counseling n.顾问服务
counsellor n. 顾问,辅导员,律师
counselor n. 顾问,参事,法律顾问
count vt.数；计数
countable adj. 可计算的
countdown n. 倒数
countenance n. 容貌，支持；面部表情；脸色；面容；鼓励，允许；表情；v. 支持，赞成
counter n.柜台
counteract v. 消除，抵消
counteraction n. 反作用
counterbalance vt. 使平衡
countercheck n. 阻挡,妨碍,对抗方法
counterfeit a. 伪造的；v. & n. 伪造；假冒，假货，伪造品；v. 伪造，仿造
counterfoil n. 存根，票根
countermand v. 撤回（命令），取消（订货）
countermeasure n. 对策
counterpane n. 床单,床罩
counterpart n. 对应的人(或物)
counterpoint n. 对位法,旋律配合,重复旋律
counterpoise vt. 平均,平衡,使平衡
counterrevolution n. 反革命
countershaft n. 对轴
countersign n. 口令,暗号,副印
countersignature n. 副署，会签
countersink vt. 钻孔装埋,打埋头孔于
countervail 对抗，抵销，补偿
countess n. 伯爵夫人,女伯爵
counting n计数
countless a. 数不尽的,无数的
countries 国家
country n.国家，国土；农村
countryman n. 乡下人,国民
countryside n.乡下，农村
countrywide a. 全国性的，全国范围的
countrywoman n.乡村妇女
county n.英国的郡，美国的县
coup n. 出乎意料的行动，政变
couple n.一对；夫妇
couplet n. 对句,对联
coupling n. 联结,结合,耦合
coupon n. 息票,赠券
courage n.勇气，胆量，胆识
courageous a.勇敢的，无畏的
courier n. 送快信的,急差,旅行从仆
course n.课程；过程；一道菜
courser n. 猎狗,打猎者,骏马
court n.法院，法庭；庭院
courteous a.有礼貌的，谦恭的
courteously ad. 有礼貌地；殷勤地
courtesy n.礼貌，谦恭，请安
courthouse n. 法院大楼
courtier n. 朝臣；奉承者
courtly a. 谦恭的,礼让的,恳挚的
court-martial n. 军事法庭
courtship n. 求爱,求婚,求爱时期
courtyard n. 庭院,天井
cousin n.堂(或表)兄弟(姐妹)
cove n. 山凹,小湾
covenant n. 契约，v. 立书保证
cover vt.盖，包括 n.盖子
coverage n. 覆盖率；保险类别险别总称；覆盖物，封面，掩护物，罩vt. 覆盖，涉及，包含，经过(一段路程)支付…费用
covered adj. 覆盖的
covering n. 覆盖(物)；套，罩；adj. 包括的
coverlet n. 床单,床罩
covert adj. 秘密的，隐密的
coverture n. 保护,掩护
covet v. 贪求，妄想
covetous adj. 贪婪的，贪心的
covey n. 群,一群,一队
cow n.母牛，奶牛
coward n.懦夫；胆怯者
cowardice n. 胆小，懦弱
cowardly a. 懦弱的,卑怯的,胆小的
cowboy n. 牛仔,牛郎,牧童
cower v. 畏缩，蜷缩
cowhide n. 牛皮,牛皮鞭
cowl n.(修道士的) 连头罩的斗篷
co-worker n. 合作者，同事；共同工作的人
cowpox n. 牛痘
cowslip n. 西洋樱草,猿猴草的一种
cox n. 舵手；v. 作舵手；驾驶
coxcomb n. 花花公子,好打扮的人,鸡冠花
coxswain n. 艇长,舵手
coy adj. 腼腆的，忸怩的
coyote n. 一种小狼,山狗
cozen v. 欺骗，瞒，骗取
cozenage n. 欺骗,瞒骗,哄骗
cozy a. 舒适的；谨慎小心的
cps 每秒周(波)数
cpu 控制处理部件
crab n. 蟹，蟹肉；螃蟹；牧童，牛仔vi. 捕蟹
crabbed adj. 暴躁的
crack n.裂缝，裂纹 vi.爆裂
cracked adj. 有裂缝的；碎的；粗哑
cracker n. 饼干,爆竹,胡桃钳
crackle n. 劈啪响,裂纹
cradle n.摇篮，发源地
craft n.工艺；手艺，行业
craftiness n. 狡猾,巧妙,熟练
craftsman n.工匠；名匠
craftsmanship n. 手艺
crafty adj. 狡诈的
crag n. 悬崖，峭壁
craggy adj. 有峭壁的，粗壮的
cram v. 填塞，塞满
cramp n. 铁箍，夹子
cramped  adj. 拥挤的；狭窄的，挤在一起的
cranberry n. 曼越橘,其果实
crane n.起重机，摄影升降机
cranial a. 头盖的,头盖形的
cranium n. 头盖，脑壳
crank n.曲柄 vi.转动曲柄
cranky adj. 怪癖的，不稳的
cranny n. 裂缝,裂隙
crap n. 废物，废话；谎言
crape n. 黑丧章,绉纱
crash n. (树倒下的)哗啦声；碰撞；坠毁；轰隆声，撞击声；起重机，鹤vi. 碰撞，坠落；撞坏，摔坏，砸碎；撞碎；v.破裂，爆裂；发出爆裂声；坠落，坠毁
crass a. 粗鲁的,愚钝的,粗糙的,非常的
cratch n. 饮料架；饲料架
crate n. 篓，板条箱
crater n. 火山口，弹坑
cravat n. 领巾，领结
crave vt. 渴求；请求，恳求；渴望；需要；热望
craven adj. 懦弱的，畏缩的
craving n. 强烈的欲望
crawfish n.『动物』 (淡水的) 小龙虾
crawl vi.爬，爬行
crawly a. 悚然的
crayfish n. 小龙虾
crayon n. 彩色笔、粉笔或其绘画
craze n. 狂热,大流行
craziness n. 疯狂
crazy a.疯狂的，荒唐的
creak vi.吱吱嘎嘎地作响
cream n.奶油，乳脂；奶油色
creamery n. 奶油干酪厂,奶油公司,牛奶
creamy a. 含乳脂的,乳脂状的,奶油色的
crease n. 折缝，皱痕
creat v. 创造，创作，引起，造成
create vt.创造；引起，产生
creation n. 创造，创造物；创作；作品
creationist n. 神灵论者，上帝论者
creative a.创造性的，创作的
creator n.创建者
creature n.生物，动物，家畜
credence n. 相信，信任
credential n. 生物，动物，人
credentials n. 信任状
credibility n. 可信用,确实性,可靠
credible a. 可信的,可靠的
credit n.信用贷款；信用
creditable adj. 值得称赞的，可信的
creditor n. 债权人
creditworthiness n. 商誉
creditworthy adj. 有信誉的
credo n. 信条
credulity n. 轻信，易信
credulous adj. 轻信的，易信的
creed n. 信条，教义
creek n. 小河；支流；小水湾；小湾，小溪；小川，小港
creel  n.  (钓鱼、捕鱼虾用的) 鱼篮,鱼篓
creep vi.爬行；缓慢地行进
creeper n. 爬行者
creepy a. 爬着走的,毛骨悚然的
cremate v.火葬；烧成
creole  n.
creosote n. 杂芬油,木馏油,碳酸
crepe n. 绉绸;假胡子
crept creep的过去式(分词)
crepuscular adj. 朦胧的，微明的
crescendo n. （音乐）渐强，高潮
crescent n. 新月,新月形之物
cress n. 水芹,水韭
cresset n. 灯号,标灯,油盏
crest n. 鸡冠；山顶；背突
crestfallen adj. 挫败的，失望的
crete n. 克里特岛(地中海)
cretonne n. 印花棉布
crevice n. 缺口，裂缝
crew n.全体船员
crib n. 婴儿小床,食槽,栅栏
cribbage n. 纸牌玩法之一
cricket n. 板球；蟋蟀
cried cry的过去式(分词)
crier n. 喊叫者,哭泣者,传布公告的
crime n.罪，罪行；犯罪
criminal n.犯人，罪犯，刑事犯
crimination n. 控告；定罪；责备
crimp v. 使卷曲，打褶
crimson adj. & n. 深红色(的)；a. & n. 深(紫)红(的)
cringe v. 畏缩，谄媚，奉承
cringing adj. & n. 谄媚(的)，奉承(的)
crinkle v. （使）变皱，n. 皱纹
crinoline  n.马鬃布
cripple vt. 使跛脚；使残疾；削价；使残废；n. 跛子；残废的人；罪犯；a. 犯罪的
crisis n.危机；存亡之际
crisis-export 转嫁危机
crisp a.脆的；卷曲的
crisscross a.交叉的；十字形
criterion n.标准，准则，尺度
critic n.批评家，爱挑剔的人
critical a.决定性的；批评的
critically adv. 批判的；吹毛求疵地；批评地，用鉴定的眼光；重要地
criticise v. 批评；批判；评论；非难
criticism n.批评；批判；评论
criticize vt.&vi.批评；责备
critique n. 批评,批评法,评论
croak n. 蛙鸣声
crochet n. 钩针织物v. 用钩针编织
crock n. 壶,罐,碎瓦片
crockery n. 陶瓦器
crocodile n.鳄鱼
crocus n. 番红花属,番红花,磨粉
croft n. （住宅附近的）小农场
crone n. 干瘪老太婆,老母羊
crony n. 密友,亲伴,好朋友
crook v. 使弯曲
crooked  adj. 弯曲的，歪的；弯的，畸形的；扭曲的
croon v. 低声歌唱，低吟
crop n.庄稼；收成
cropper n. 种植者,农作物
croquet n. 槌球戏,循环球戏
crosier n. 权杖
cross n.十字架 vt.&vi.穿过
crossbar n. 闩,横木,球门的横木
crossbow n. 石弓,弩
cross-breeding 杂交育种
cross-cultural a.跨文化的
crosscut adj.横锯的 <锯子>
cross-elasticity 交叉弹性
cross-examination 交互讯问
cross-eyed a. 斜视的,对视眼的
crossfire n. 交叉火力
crosshatch v. 交互配血
crossing n.交叉(点)；十字路口
cross-reference n. 前后参照
crossroad n. 交叉路,岔道,十字路口
cross-road 十字路口
crossroads n. 交叉路口，十字路
cross-section n. 剖面图
cross-sectional a. 截面的
cross-talk n. 相声
crosswise ad. 斜地,成十字状地,交叉地
crossword n. 纵横字迷
crotch n. 分叉处,丫叉
crotchet n. 怪念头，小钩，四分音符
crotchety a. 有怪想的,反复无常的,想入非非的
crouch v. 蹲伏、弯腰
croup n. (尤指马的) 臀部
crow n.鸦，乌鸦 vi.啼
crowbar n. 撬棍
crowd n.群；大众；一伙人
crowded adj. 拥挤；充(拥)满了的；拥挤的n. 拥挤的，密集的
crown n.王冠，冕；花冠
crucial a. 至关重要的
crucible n. 坩锅,严酷的考验
crucifix n. 十字架
crucifixion  n. 钉死于十字架上
crucify vt. 十字架上钉死
crude a.简陋的；天然的
crudity n. 粗糙，粗野
cruel a.残忍的，残酷的
cruelly ad. 残酷地；极，非常
cruelty n. 残忍，残酷行为；痛苦
cruet n. 调味瓶
cruise vi.巡航 vt.巡航于…
cruiser n. 巡洋舰,巡航飞机,警察巡逻车
cruller n. 油煎饼的一种
crumb n. 面包屑；一些；点滴；饼屑，小量
crumble v. 弄碎，崩毁
crumple v. 弄皱，扭弯
crunch n. 关键时刻，危境
crupper n. 屁股,马屁股
crusade n. 为维护理想，原则而进行的运动或斗争
crusader n. 十字军战士,改革者
cruse n. 壶
crush vt.压碎，碾碎；镇压
crust n. 硬皮；地壳；面包皮；硬的表面；硬壳；外壳，外层，厚脸皮；外皮，壳；干面包片v. 用外皮覆盖
crustacean n. 甲壳类动物
crutch n. 拐杖,支撑,帮助
crux n. 十字架形,关键,难题
cry vi.哭；叫喊
crypt n. 土窖,地穴,地下室
cryptic adj. 秘密的，神秘的
cryptogram n. 暗号，密码
cryptomeria 日木杉
crystal n. 结晶(体)；晶体；水晶，晶粒；水晶饰品；石英；a. 晶莹的，水晶的；水晶(制)的；透明的
crystalline a. 水晶的,透明的,结晶性的
crystallize vt. 使结晶,使具体化,做成蜜饯
cub n. 幼兽，年轻无经验的人
cuba n. 古巴
cuban n. & a. 古巴(人)的
cube n.立方形；立方
cubic a.立方体的；立方的
cubicle n. 小寝室
cubism n. 立体主义
cubit n. 腕尺
cuckoo n. 杜鹃，布谷鸟
cuckoo-bird adj. 布谷鸟，杜鹃
cucumber n.黄瓜
cud n. 反刍的食物
cuddle n./v. 搂抱，拥抱
cudgel n. 棍棒
cue n. 开端,线索,发辫,长队,开始
cuff n. 袖口；衣袖反折部分；护腕；v. 用手轻拍
cuirass n. 胸甲，护胸铁甲
cuirassier n. 穿着胸甲的骑兵,胸甲骑兵
cuisine n. 烹饪
culinary adj. 厨房的，烹调的
cull vt. 采,摘,拣
culminate vi. 到绝顶,达于极点,达到高潮
culmination n. 顶点,极点,最高点
culpable adj. 有罪的，该受谴责的
culprit n. 犯人,罪犯,刑事被告
cult n. 宗派，崇拜
cultivate vt.耕；种植；培养
cultivated a. 在耕作的；有教养的
cultivation n. 教化,培养,耕作
cultivator n. 耕者,栽培者,耕田机
cultural adj.文化上的；文化的
culture n.文化，文明；教养
cultured a.人工培养的；有教养的
culvert n. 暗渠,阴沟,电线用地下管路
cum (拉)和，与，附有；和与附有
cumber v. 拖累，妨碍
cumbersome adj. 笨重的
cumbrous a. 讨厌的,累赘的,成负担的
cumulate v. 积累，堆积
cumulative a. 累积的
cuneiform a. 楔形的,楔形文字的,楔状骨的
cunning a.狡猾的，狡诈的
cunningly ad. 狡猾地；精巧地
cup vt.使成杯形
cupboard n.碗柜，碗碟橱；食橱
cupful n. 一满杯
cupid n. (罗神)丘比特(爱神)
cupidity n. 贪婪
cupola n. 圆屋顶,圆顶篷,圆顶的塔
cur n. 杂种狗，坏种
curable a. 耐久的
curate n. 副牧师,助理牧师
curative a. 治病的
curator (博物馆等)馆长
curb  n. 马勒；勒马链条；路边；路的边栏；抑制物；v.束缚；抑制；控制，制止，抑制场外交易
curd n. 凝乳
curdle v. 使凝结，变稠
cure vt.医治；消除 n.治愈
cure...of 医好某人的病；纠正
cured 治愈的
curfew n. 晚钟,打晚钟时刻,晚钟,宵禁
curie 居里(姓)
curio n. 古玩，古董
curiosity n.好奇，好奇心；珍品
curious adj.稀奇的，奇妙的
curiously adv. 好奇地；稀奇古怪地
curl vt.&vi.卷曲 n.卷发
curly a.卷曲的；有卷毛的
curmudgeon n. 脾气暴躁之人
currant n. 葡萄干
currency n.通货；通用；市价
current a.当前的；通用的
currently  adv. 当前，广泛地；目前，普遍地；现在
curriculum n. 课程(设置)
currish adj. 下贱的，杂种的
curry n. 咖哩粉,咖哩饭菜
curse n.诅咒，咒骂；天谴
cursed a. 该咒诅的，可恶的
cursive adj. 草书的
cursor n. 光标；指针
cursory adj. 粗略的，草率的
curst v. curse(诅咒)的过去式和过去分词
curt adj. （言词、行为）简略而草率的
curtail vt. 缩减,剥夺,简略
curtain n.(窗、门)帘；幕
curtsey n. (妇女行的)屈膝礼
curtsy n. 屈膝礼
curvaceous adj. 婀娜多姿的，曲线的
curvature n. 屈曲,弯曲,曲率
curve n.曲线；弯 vt.弄弯
curvet n. 腾跃,嬉戏
cus-cus n. 岩兰草
cushion n.软垫子
cusp n. 尖头,尖端,尖头
cuspidor n. 痰盂
cuss v. 诅咒，咒骂
custard n. 软冻
custodian n. 管理员，监护人
custody n. 监管，保管
custom n.习惯，风俗；海关
customary a.通常的；照惯例的
customer n.顾客，主顾
customhouse n. 海关
customize vt. 定制，定做
customs a. 海关的；定做的(衣)；n. 海关；关税；关税进口税海关；进口税
cut vt.切；割；砍
cutback n. 计划中的削减；中止；减少
cute adj. 逗人喜爱的，漂亮的，伶俐的
cuticle n. 表皮
cutlass n.短刀
cutler n. 刀匠,制餐刀商
cutlery n.
cutlet n. 肉片,炸肉片,炸肉排
cutter n.用于切割的器械
cutthroat n. 凶手,谋杀者
cutting n. 切断,切下,开凿
cuttlefish n. 乌贼，墨鱼
cyanosis n. 紫绀
cyclamen 樱草属植物
cycle n自行车，循环
cyclecar n. 小型机动车
cyclic adj. 循环的; 周期性的
cycling 自行车
cyclist n. 骑脚踏车的
cyclone n. 旋风，飓风
cygnet n. 小天鹅
cylinder n.圆筒；柱(面)；汽缸
cylindrical a. 圆筒形的
cymbal n. 铙钹,高音音栓之一
cynic n. 愤世嫉俗者
cynical adj. 愤世嫉俗的
cynicism n. 愤世嫉俗，犬儒主义
cynosure n. 注意的焦点
cynthia n. 月亮女神
cypher n. 零,零的记号,密码索引书
cypress n. 柏树
cyst n. 包囊,膀胱,囊肿
cytology n. 细胞学
czar n. 皇帝,沙皇
d/a n. (缩)承兑交单
dab n. 湿而软的小块；轻拍
dabble v. 涉足，浅赏
dace n. 一种鱼
dacron n. 涤纶
dad n.(口语)爸爸，爹爹
daddy n. 爸爸
daffodil n. 水仙花
daft adj. 傻的，愚蠢的
dagger n. 匕首
daguerreotype n. (早期)银板照相
dahlia n. 大丽花
daily a.每日的 n.日报
dainty adj. 优雅，考究；秀丽的；娇美的，挑剔的n. 美味；精美食品
dairy n.牛奶场；乳制品
dairyman n. 酪农场的男工
dais n. 台,讲台
daisy n. 雏菊,一流的人物
dakota n. 达科他州(美)；n. & a. 达科他人(语)
dale n. 小谷,溪谷
dallas n. 达拉斯(美国)
dalliance n. 戏弄，玩弄
dally v. 闲荡，嬉戏
dam n. 水坝；水闸；水堤；障碍物；堤，水坝(闸)；v. 筑坝；vt. 筑坝
damage vt.损害，毁坏 n.损害
damaging a. 有害的
damask n. 缎子,斜纹布,大马士革钢铁
dame n. 夫人
damn vt.诅咒 n.诅咒；丝毫
damnable a. 可诅咒的,该死的
damnation n. 非难,被罚下地狱,诅咒
damned a. 该死的；ad. 非常，极
damp a.潮湿的，有湿气的
dampen v. （使）潮湿，使沮丧，泼凉水
damper n. 爱挑毛病的人,讥诮话,增湿器,
damsel n. 年轻女人，少女
damson n. 西洋李子,其树
dance vi.跳舞；摇晃 n.舞
dancer n.舞者; 舞女;  (专业的) 舞蹈家
dancing n. 舞蹈
dandelion n. 蒲公英
dandified adj. 打扮得像花花公子的
dandle vt. 抱着逗弄,宠,娇养
dandruff n. 头皮屑
dandy n. 花花公子，好打扮的人
Dane n. 丹麦人
danger n.危险
dangerous adj.危险的
dangerously ad. 危险地
dangle v. 悬挂，吊胃口
Danish n. 丹麦文
dank adj. 透水的，阴湿的
danube n. 多瑙河(欧洲)
daphne n. (植)瑞香
dapper adj. 衣冠楚楚的，干净的
dapple n. 斑纹,花马
dappled adj. 有斑点的，斑驳的
dare v.aux.敢；敢于
daredevil adj. & n. 胆大的(人)，冒失的(人)
daring a.大胆的，勇敢的
dark adj.黑暗的
darken v. 变黑，转暗；变暗
darkling ad. 在暗中
darkly adv. 暗，黑；暗中
darkness n.黑暗
darksome a. 微暗的,阴暗的,含糊的
darling n.亲爱的人；宠儿
darn v. 缝补，补缀
darnel n. 毒麦
dart n. 飞镖，v. 急驰，投射
darwin n. 达尔文(城市名)
dash n.猛冲；短跑
dashboard n. 仪表板
dashing adj. 有活力的，有朝气的
dastard adj. 懦夫，胆小的人
data n.数据; 资料
database n. 数据库
datal 按日计算工资
date n.日期
dateless adj. 没有日期的,年代
dating n. 约会
datum n. 资料；数据；已知数
daub v. 涂抹，乱画
dauber n. 涂抹者,拙劣的画匠,涂抹工具
daubster n. 拙劣的画家
daughter n.女儿
daughter-in-law n.儿媳
daunt v. 使胆怯，使畏缩
dauntless adj. 勇敢的，无畏的
dauphin n. 法国皇太子
davenport n. 一种书桌,兼做卧床的长椅
david 戴维(姓或男名)
davit n. 吊艇柱,吊柱
davy n. (律)供词；宣誓书
daw n. 穴鸟
dawdle v. 闲荡，虚度
dawn n.黎明；开端 vi.破晓
day n.(一)天，白昼，白天
daybreak n. 黎明,拂晓
daydream n. 白日梦
daylight n.白昼，日光；黎明
days 天，日
daytime n.白天，白昼
day-time n. 白天
daze vt. 使茫然,发昏,使眼花缭乱
dazzle vt.&vi.炫耀；迷惑
dazzling adj. 令人目眩的
de (前缀)离开；除去；否定；倒转
deacon n. 副主祭,执事,公会会长
deactivate vt. 释放，去活化
deactive 使不活动
dead adj.死的
deaden vt. 使减弱,消除
deadline n. 期限；最后付款期限；最后期限，截止交稿日期，监牢周围的死线
deadlock n. 僵局，僵持
deadly adj. 致死的；致命的；死一般的；非常，极度；危险的，极有害的；ad. 死一般地；死一样地，非常，很
deadweight n.(船的最大)载重量
deaf adj.聋的
deafen vt.使聋；使隔音
deafness n. 聋,不听
deal vi.做买卖；对付
dealer n. 商人；贩子；发牌者；经记人，证券商；商人贩子
dealing n. 行为,交易
dealt deal的过去式(分词)
dean n.(大学)院长，系主任
dear adj.昂贵的，高价的
dearly adv. 深爱地；热切地；亲爱地；深深地(爱等)；昂贵；极，非常，昂贵地
dearness n. 高价,亲爱
dearth n. 缺乏,粮食不足,饥谨
deary n. 可爱的,爱人
death n.死，死亡；灭亡
deathbed n. 临死所卧之床,临终之时
deathless  adj. 不死的,不灭的,永恒的
deathlike a. 死了一样的,象死人的
deathly a. 死一般的
debacle n. 解冻，崩溃.
debar vt. 排除,防止,禁止
debase v. 贬低，贬损
debasement  n.  (品格、地位、品质的) 降低;  (货币
debatable a. 可争论的,成问题的,未决定的
debate n.,vt.&vi.争论；辩论
debater n. 讨论家,讨论者
debauch v. 使放荡，堕落
debauchery n. 放荡，沉缅酒色
debenture n. 公司债,公司债券,退税证明书
debilitate v. 使衰弱
debility n. 衰弱，虚弱
debit n. 借方,借
debonair adj. 殷勤的，快活的，温雅的
debouch v. 流出，进入(开阔地区)
debrief v. 向...询问情况，汇报情况
debris n. 废墟，残骸
debt n.债，债务，欠债
debtee n.债权人
debtor n. 负债者
debt-redden n.负债累累
debug vt. 调试
debugger n. 调试程序
debunk v. 揭穿真相，暴露
debut n. 初次登台，初次露面
debutante n. 初次参加社交活动的少女
decade n.十年，十年期
decadence n. 衰落，颓废
decadent adj. 衰落的；颓废的，衰退的
decagon n. 十边形,十角形
decagram 十克
decameter 分米
decamp v. （士兵）离营，匆忙秘密地离开
decant vt. 轻轻倒出,移入其他容器
decanter n.  有塞子的玻璃瓶
decathlon n. 十项运动
decay vt.使腐朽，使腐烂
decease n. 死亡
deceased adj. 已死的
deceit n.欺骗，欺诈
deceitful a. 欺诈的
deceive vt.欺骗，蒙蔽，行骗
deceiver n. 欺人者,欺诈者
decelerate v. 使减速，降低速度；减速；减缓
December n.十二月
decency n. 得体,礼貌,正派
decent a.正派的；体面的
decentralization 分权管理
decentralize v.给予更多权
deception n. 欺骗
deceptive a. 迷惑的,虚伪的,欺诈的
decertifacation 否认代表资格
decibel n. 分贝(音量的单位)
decide vi.&vt.下决心；决定
decided a. 确定的,坚决的
decidedly ad.明确地，坚决地
deciduous adj. 脱落的，落叶的
decimal a.小数的，十进制的
decimate v. 毁掉大部分，大量杀死
decipher v. 解开（疑团），破译（密码）
decision n. 决定，决心；果断；判决，决议；判定，决策；决断
decision-making a. 决策的
decisive a.决定性的；果断的
deck n. 甲板，舱面；层面；覆盖物；复盖
deck-chair n. 帆布躺椅
declaim v. 高谈阔论，雄辩，大声说
declamation n. 高声说话，高调
declaration n.宣布，宣言；申诉
declare vt.断言；声明；表明
declared a. 承认的，申报的
declassify v. 撤销，保密
declension n. 词尾变化,格变化,倾斜,衰退
declination n. 倾斜，衰微
decline vt.下倾；偏斜；衰退
declining adj. 下降的，衰落的
declivity n. 倾斜面，斜坡
decode v. 译解(密码)；vt. 破译；译(电报)；解码，译码
decollete  adj. <女装> 露出颈部和肩部的,袒胸露
decompose vt.&vi.腐败；分解
decomposition n. 腐烂，崩溃
decorate vt.装饰，装璜，修饰
decoration n. 装饰,装饰品
decorative a.装饰的；可作装饰的
decorator n.装饰者
decorous adj. 符合礼节的，相称的
decorum n. 礼节，礼貌
decoy v. 欺骗，引诱
decrease v. 减少，降低，缩短；减小；减弱；n. 减少，减小
decreasing 递减
decree v. & n. (专制君主的)命令；vi. 规定；n. 法令，政令；教令；公告；天命；命令，v. 判决；颁布命令，公告；命令；法令 vt. 颁布(法令、政令)
decrement 减值，减量，赤字，贬值
decrepit adj. 衰老的，破旧的
decrepitude n. 衰老、破旧
decry v. 责难，贬低（价值）
dedicate vt.奉献；献身
dedicated a. 潜心的
dedication n. 奉献,致力,献辞
deduce vt.演绎，推论，推断
deducible a. 可推论的
deduct vt. 扣除,演绎
deduction n. 减除,扣除,减除额,推论
deed n.行为；事迹
deem vt.认为，相信 vi.想
deemphasize 降低重要性
deep adj.深的
deepen vt.加深 vi.深化
deeply adv. 深深地；深切地
deep-rooted a. 根深蒂固的
deep-set adj. (眼睛等)深陷的
deer n.鹿
deerskin n. 鹿皮,鹿皮制衣服
dee-toned adj. 音色深厚的
deface vt. 损伤外观
defalcate v. 侵吞公款
defalcation 挪用，盗
defamation n. 破坏名誉,中伤,诽谤
defamatory adj. 诽谤的
defame v. 诽谤，中伤
default n.&vi.不履行；缺席
defeat n.击败；失败
defeatist n. 失败主义者
defecation n. 通便，排粪
defect n.缺点，缺陷，欠缺
defection n. 脱党，变节
defective a. 有缺陷的,欠缺的
defector n. 背叛者,叛离者
defects n.不合格品
defence n.防御；防务；辩护
defenceless a.未设防的
defend vt.保卫，防守
defendant n. 被告
defender n.防御者
defense n. 防卫,防卫物
defenseless a. 无防备的
defensible a. 可防卫的,可拥护的,可辩护的
defensive a. 防卫的,防备用的,辩护的
defer vt. 拖延；推迟，vi. 服从；拖延，延期
deference n. 敬意，尊重
deferential a. 恭敬的
deferred a. 延期的，递延的
defferent a. 各种的，差异的
defferential a. 微分的
defiance n. 蔑视,挑衅
defiant a. 挑衅的,目中无人的
deficiency n.缺乏；不足之数
deficient adj. 缺乏的，欠缺的；不足的；(in)缺乏的
deficit n. 不足，赤字
defile v. 弄污，弄脏n. （山间）小道
defilement n. 弄脏,污秽,污辱
definable a. 可定义的，可确定的
define vt.给…下定义；限定
definite a.明确的；肯定的
definitely  adv. 一定，肯定地；一定地，明确地；绝对
definition n. 定义，解说；释义；定界；解释；限定；明确；确实，清晰度；界限；(轮廓等)清晰，规定
definitive n. 限定词
deflate v. 收缩，紧缩
deflated adj. 灰心丧气的
deflation n. 紧缩通货
deflator 减缩指数，消除通胀因素指数
deflect vt.&vi.(使)偏斜
deflection n. 偏斜，歪斜；偏差；偏转，转向
deforestation n.砍伐森林
deform vt.损坏…的形状
deformation n. 损坏；变形；畸形；毁坏
deformity n.畸形；残废
defraud vt. 欺骗
defray v. 支付，支出
deft adj. 灵巧的，熟练的(adeft)
deftly ad. 灵巧地，敏捷地
defunct adj. 死亡的，过时的
defy vt.向…挑战；蔑视
degeneracy n. 退步,退化,堕落
degenerate vi. 衰败；腐化，堕落；vt. 退步
degeneration n. 退化,恶化,堕落
degenerative a.(疾病)变性的
degradation n.降级；退化；衰变
degrade vt. 降低品格；堕落；使降给；使堕落；降级；使降级；使堕落；贬黜
degraded adj. 被贬低的；堕落的
degree n.程度；度；学位
dehumanize v. 使失掉人性
dehydrate v. 除去水份，脱水
deification n. 神化，崇拜
deify v. 奉为神，崇拜
deign v. 屈尊，惠允（做某事）
deist n. 自然神论信仰者
deition 版本
deity n. 神，神性
dejected  adj.垂头丧气的；沮丧的，失望的
dejection n. 沮丧，颓丧
del n. 保付
delay vt.推迟；耽搁；延误
delecate a. 微妙的，棘手的
delectable adj. 赏心悦目的，愉悦的
delectation n. 享受，愉快
delegate n.代表，委员，特派员
delegation n.代表团
delete vt.删除；擦掉
deleterious adj. （对身心）有害的，有毒的
deletion n. 删除；取消
deleville 德勒维尔(地名)
delft  n.  (荷兰) 戴夫特 (彩色) 陶器
deliberate a.深思熟虑的；审慎的
deliberately  adv.仔细考虑地，故意地；审慎地，慎重地；从容地；有意地
deliberation n. 熟虑,熟思,协议
delicacy n. 细软,精致,精美的食品,娇气,
delicate a.纤细的；易碎的
delicately ad. 精美地；微妙地
delicatessen n.熟食
delicious adj. 美味的；可口的；怡人的；精美的；美妙的
delight n.快乐
delighted adj. 大喜；高兴的，欣喜的；喜欢的
delightful a. 令人愉快的,可喜的
delightfully ad. 大喜，欣然
delimit vt. 定界，定义；v. 定界，划界
delimiter n. 定界符，分界符
delineate v. 描画
delineation n. 画轮廓,略图,图形
delinquency n. 失职，罪行
delinquent adj. 疏忽职务的，有过失的
deliquesce v. 融解；潮解
deliquescent a. 溶解的,溶解性的
delirious adj. 精神错乱的
delirium n. 精神错乱，发狂
deliver vt.投递，送交；发表
deliverance n. 救出,救助,释放,判决
deliverer n. 救助者,引渡人,交付者
delivery n. 投递；交付；分娩；递送，讲述；送交；交货；传送；交货，发送，传递
dell n. 小谷,小溪谷
della 德拉(女名)
Delphic adj.神谕(似)的; 暧昧的,含混的
delta n. （河流的）三角洲
delude v. 欺骗，哄骗
deluge  vt. 泛滥；n. 大洪水，豪雨；大水灾
delusion n. 欺骗，幻想
delusive a. 困惑的,迷惑的,欺瞒的
deluxe a.昂贵的；奢侈的
delve vt.vi.探究,查考n.坑,穴
demagogue n. 煽动者,群众煽动者
demand vt. 要求；需要；询问；查问；v. 请求；查问；需要；n. 需要；请求，需求
demanding adj. 对人要求严格的；过分要求的
demarcate v. 划分，划界
demarcation n. 定界线；分开
demean v. 贬抑，降低
demeanor n. 举止，行为
demeanour n. 行为,举止
demerit n. 缺点,短处,过失
demesne n. 领地，范围
demise n. 崩,薨,死亡
demobilize v. 遣散(军人)，复员
democracy n.民主，民主制
democrat n. 民主正体论者,民主主义者,民主党员
democratic a.民主的，民主政体的
demography n. 人口统计；人口学
demolish v. 摧毁，拆除
demolition n. 破坏，拆除
demon n. 魔鬼
demonetize 非货币化
demoniac a. 着魔的,恶魔的
demonstrable a. 可论证的
demonstrate vt.说明；论证；表露
demonstration n. 示范,实证
demonstrative a. 说明的,指示的
demonstrator n.示威
demoralization n. 道德颓废,堕落,士气沮丧
demote v. 降级，降职
demotic a. 人民的,民众的,通俗文体的
demur v. 表示异议，反对
demure adj. 严肃的，矜持的
demurrage n. 滞期费；滞期
den n.窝，兽穴
denial n.否定；拒绝相信
denigrate v. 污蔑，诽谤
denizen n. 居民，外籍居民
denmark  n. 丹麦(欧洲)
denominate v. 命名，取名
denomination n. 命名，（长度，币值的）单位
denominator n. 分母,命名者
denotation n.意义
denote vt.指示，意味着
denouement n. （小说的）结尾，结局
denounce vt.谴责，声讨；告发
dense adj. 稠密的，密集的；愚钝的；(烟等)浓厚的；(烟、雾等)浓密的
densely ad. 密集地；浓厚地
density n.密集，稠密；密度
dent n. 缺口，凹痕，v. 弄凹
dental a. 牙齿的
dentist n.牙科医生
dentistry n.牙医
denture n. 假牙
denude v. 脱去，剥蚀，剥夺
denunciation n. 谴责,告发
denver n. 丹佛(市)(美国)
deny vt.否定；拒绝相信
deoxygenate vt. 除去氧气
depart vi.离开，起程；出发
departed a. 已往的；已故的
department n.部，司，局，处，系
departure n.离开，出发，起程
depend vi.依靠
dependability n. 可依赖性；可靠性
dependable a. 可依靠的
dependant n. 受赡养者；侍从；依赖别人
dependence n. 依赖,依存,信赖
dependency n. 属国,保护地,从属物
dependent a.依靠的，依赖的
depict vt. 描写
depiction n. 描述
depilate vt. 拔毛,脱毛
deplete v. 倒空，耗尽
depletion n. 耗尽，枯竭
deplorable a. 可叹的,悲惨的,凄惨的
deplore vt. 悲悼,哀叹,悔恨
deploy vt.vi. 展开,配置
depopulate vt.vi. (使)人口减少
depopulation n. 人口减少
deport vt. 持,举止,驱逐
deportation n. 驱逐,放逐
deportment n. （尤指少女的）风度，举止
depose v. 免职，废黜
deposit vt.使沉淀；存放
deposition n.免职，罢免；口供
depositor 存款人，储户
depository n. 存储处,贮藏所,受托者
depot n. 货栈；仓库
deprave vt. 使堕落,使恶化,使腐败
depravity n. 堕落，恶习
deprecate vt. 声明不赞成,抨击,反对
deprecatory a. 不赞成的,反对的,恳求的
depreciate v. 贬低，贬值
depreciation n. 贬值；折旧；跌价
depredation n. 劫掠，蹂躏
depress vt.使沮丧；按下
depressed adj. 郁郁不乐；情绪低落的；消沉的；萧条的
depression n.沮丧；不景气，萧条
deprivation n. 剥夺，丧失
deprive vt.夺去；使(人)失去
depth n.深度；深厚；深处
deputation n. 代理任命,代表,代表团
depute v. 派…为代表或代理
deputy n.代理人 a.副的
derail vt. 使出轨
derange vt. 扰乱,使发狂
deranged adj. 疯狂的
derangement n. 精神错乱
deregulation n.撤消管制规定
derelict adj. 荒废的，被弃置的
dereliction n. 无主,抛弃物
deride v. 嘲弄，愚弄
derision n. 嘲笑
derisive adj. 嘲弄的
derivation n.引出；起源；衍生
derivative adj. 派生的，无创意的
derive vt. 取得；得到；来自；由来；(from)导出；起源于；追寻…的起源，派生，引出；vi. 起源；由来，衍生
derma n. 真皮,皮肤
dermatologist n. 皮肤学者,皮肤科医生
dermatology n. 皮肤(病)学
derogate v. 贬低，诽谤
derogation n. 毁损,减损,堕落
derogatory adj. 不敬的，诽谤的
derrick n. 铁架塔
dervish n. 回教的托钵僧
desalinize v. 除去盐份
descant n. 合唱，详述
descend vi.下来，下降；下倾
descendant n.子孙，后裔；弟子
descent n.下降；出身；斜坡
describe vt.形容；描写，描绘
described a. 被看到的，被发现的
description n.描写，形容；种类
descriptive a. 描述的,叙述的
descry v. 远远看到，望见
desecrate v. 玷辱，亵渎
desecration n. 亵渎神圣,污辱
desert vt.遗弃；擅离(职守)
deserted adj. 被人遗弃的；废弃的，荒无的；无人的；无人居住的
deserter n. 背弃者,脱党者,逃亡者
desertion n. 丢掉,遗弃,逃亡
deserve vt.应受，值得
deservedly ad. 应得报酬地,当然地
desiccant n. 干燥剂
desiccate v. （使）完全干涸，脱水。
desideratum n. 必需品，要求
design vt.设计 n.设计；图样
designate vt.指出，指示；指定
designated a. 指定的，特指的
designation n. 指定，名称，称呼
designedly ad. 故意地,有计划地,特意地
designer n. 设计家
designing n. 设计; 构思,图案
desirability n. 称心如意的人(东西)
desirable a.值得相望的；可取的
desire vt.相望；要求 n.愿望
desirous adj. 渴望的
desist v. 停止，中止
desk n.书桌，办公桌
desks 书桌
desktop a. 台式的
desolate  adj.荒凉的，荒芜的；孤独的；凄凉的；不幸的，被遗弃的；孤寂的vt. 使悲惨
desolation n. 荒芜,荒废,荒凉
despair n.绝望；失望
despairing a. 感到绝望的
despatch vt.vi.n. 派遣
desperado n. 亡命之徒
desperate adj. 什么也不顾的；拼死的；绝望的；不顾一切的；危急的；令人绝望的
desperately  adv.绝望地，孤注一掷地；拼命地；令人绝望地
desperation n. 绝望
despicable adj. 可鄙的，卑劣的
despise vt.鄙视，蔑视
despite prep. 尽管；不管，不顾；任凭；n. 轻蔑
despiteful a. 故意为难的,有恶意的
despoil v. 夺取，抢夺
despond vi. 沮丧,失去勇气
despondence n. 失去勇气,失望
despondency n. 失去勇气,失望
despondent adj. 失望的，意气消沉的
desposal n. 布置，安排；处理，处置
despot n. 专制君主,暴君
despotic adj. 专横的、暴虐的
despotism n. 专制，暴政
dessert n.甜点心
destination n.目的地，终点；目标
destine vt. 命定，注定；指定，(常用被动态)(to)预定，v. 注定，预定
destiny n.命运，天数
destitute adj. 贫乏的，穷困的
destitution n. 穷困,贫穷,缺乏
destroy vt.破坏；消灭；打破
destroyer n. 破坏者,驱除者,作破坏的事物,
destruct vi. 破坏
destruction n.破坏，毁灭，消灭
destructive a.破坏(性)的，危害的
desturbance n. 骚动，动乱；打扰，干扰
desuetude n. 废止，不用
desultory adj. 不连贯的，散漫的
detach vt.分开；派遣(军队)
detachable a. 可分离的
detached adj. 分开的，超然公平的
detachment n. 分离、超然、公平
detail n. 细节；枝节；零件；琐碎，小事；详细情况；元件，详情；详述；琐事vt. 详述，细说；详细说明
detailed  adj. 详细的，详尽的；说细的
details 细节
detain vt. 耽搁；扣押，拘留；使延迟，留住；阻止
detect vt.察觉，发觉；侦察
detectable adj. 可觉察的
detection n.察觉，发觉；侦察
detective n.侦探，密探
detector n.发觉者，探测器
detemination n. 决定
detention n. 挽留,延迟,拘留
deter v. 威慑，吓住
detergent adj. 净化的，n. 清洁剂
deteriorate v. （使）变坏，恶化
deterioration n. 恶化,降低,退化
determinant n. 判定
determinate a. 确定的,一定的,决定的
determination n.决心；决定；确定
determine vt.决定；查明；决心
determined adj. 坚决的，有决心的；确定的；毅然的
deterrent n. 制止物；adj. 威慑的，制止的
detest v. 深恶，憎恶
detestable a. 嫌恶的,可憎的,可厌恶的
detestation n. 憎恶,嫌恶,厌恶的人
dethrone vt. 废黜,废位赶出
dethronement  n. 废立,废位; 权威地位的推翻
detonate v. (使)爆炸，引爆
detonation n. 爆炸（声）
detour n. 弯路，绕行之路
detoxicate vt. 除毒，解毒
detoxify v. 除去…的毒物
detract vt.vi. 减去,贬低
detraction n.恶言,诽谤,贬低,降低
detractor v. 贬低者
detriment n. 损害，伤害
detrimental adj. 损害的，造成伤害的
detritus n. 岩屑，碎石
detroit n. 底特律(美国城市)
deuce n. 两点,平手,平分
devaluation n. 贬值
devalue v. 贬值
devastate v. 摧毁，破坏
devastating adj. 破坏性的
devastation n. 毁坏
develop vt.使(颜色等)显现
developer n. 开发者，显影剂
developing adj. 发展中的
development n. 发展；开发；生长；进展，显影；研制
deviant adj. 越出常规的，反常的
deviate vt.(使)背离，偏离
deviation n.背离，偏离；偏差数
device n.器械，装置；设计
devil n.魔鬼，恶魔
devilish adj.  如恶魔的
devious adj. 不正直的，弯曲的
devise vt.设计，发明
devoid adj. 缺乏的；无…的，缺…的；空的，缺少的
devoir n. 本分,义务,敬意
devolution n. 责任转移；权利下放；退化
devolve vt. 转移,传下,委托
devote vt.将…奉献，致力于
devoted adj. 忠实的；热心的；献身于…的
devotee n. 热爱家,献身者,皈依者
devotion n.献身；忠诚；专心
devotional a. 信仰的,虔诚的,祷告的
devour vt.吞食；吞灭，毁灭
devout a. 虔诚的,虔敬的,衷心的
dew n.露，露水
dewberry n. 悬钩子之类,其果实
dewdrop n.露珠,露滴
dewy a. 露湿的,带露水的,如露的
dexterity n. 纯熟、灵巧
dexterous adj. 灵巧的，熟练的
dia prefix. (接辅者)通过，横过；分离
diabetes n. 糖尿病
diabolic adj.恶魔 (一样) 的,魔鬼性格的
diabolical adj. 残酷的；恶毒的，狠毒的
diacid n. 二酸
diacritical a. 区分的，辩别的
diadem n. 王冠,带状头饰,王权
diagnose vt.诊断(疾病)
diagnosis n. 诊断
diagnostic a. 诊断的；特征的
diagonal a. 对角线的,斜的,斜纹的
diagonally ad. 斜(对)
diagram n.图解，图表，简图
dial n.钟面；拨号盘 vt.拨
dialect n.方言，土语，地方话
dialectic n. 辩证法；逻辑
dialog n.对话，对白
dialogue n. 对话
dialysis n. 透析
diameter n.直径
diametre n. 直径
diamond n.金钢石，钻石；菱形
diapason n. 和谐,调音,全协和音
diaper n. 尿布
diaphanous adj. （布）精致的，半透明的
diaphragm n. 横隔膜,控光装置
diarrhea n.腹
diarrhoea n. 腹泻
diary n.日记，日记簿
diastolic adj. 舒张的
diatribe n. （口头或书面猛烈的）抨击，抨击性演说
dibble n. 挖洞器
dice n. 骰子
dichotomy n. 二分、本质对立
dick 迪克(男名)
dickens n. (同)devil，魔鬼
dicker n. 十个,十张,小生意
dictate vt.&vi.口授；命令
dictation n.口授笔录，听写
dictator n.独裁者，专政者
dictatorial a.独裁
dictatorship n. 独裁政治；专政；独裁(权)
diction n. 措辞；用语
dictionary n.词典，字典
dictum n. 格言、声明
did  do(做)的过去式
didactic adj. 教诲的、说教的
didactics n. 教学法
didn't (同)did not
die vi.死
diehard n. 顽固派
diesel n. 柴油发动机，内燃机；柴油机；内烯机
diet n.饮食，食物
dietary a. 饭食的,饮食的
dietetic a. 饮食的,食物疗法的
dietetics n. 饮食学，营养学
dietitian n. 营养学家
differ vi.不同，相异
difference n.差别；差；分歧
different adj. 不同的
differential a. 差别的,特定的,微分的
differentiate v. 区别，分辨
differentiation n. 区别,分化,变异
differently adv. 不同地；有差别地
difficiency n. 缺乏，缺少，不足
difficient a. 缺乏的，缺少的，不足的
difficult a.困难的；难对付的
difficulty a.困难；难事；困境
diffidence n. 无自信,内向,羞怯
diffident a. 无自信的,客客气气的,羞怯的
diffuse vt.&vi.使(热)散开
diffusion n. 传播，散布
dig vt.掘，挖；采掘
digest vt.&vi.消化
digestible a. 可消化的,易消化的,可摘要的
digestion n. 消化
digestive a. 消化的,助消化的
digger n. 挖掘者
digit n. 数字,位数,指头
digital a.数字的，计数的
digitalis n. 洋地黄，毛地黄
dignified a. 有威严的,有品格的
dignify vt. 增威严,使高贵,故做显贵
dignitary n. 高贵的人,高官,高僧
dignity a.尊贵；(举止)庄严
digress v. 离题，把（话题）离开
digression n. 离题，枝节话
digressive  adj. 本题以外的,枝节的
dike n. 堤防
dilapidated adj. 破旧的，倒塌的
dilapidation n. 破旧、荒废
dilate v. （身体某部位）张大，扩大
dilation n.  扩大,张大
dilatory adj. 慢吞吞的，磨蹭的
dilemma n. 困境，左右为难
dilettante n. 半瓶醋，业余爱好者
diligence n. 勤奋
diligent a.勤勉的，勤奋的
diligently ad. 勤奋地
dill n. 时萝,时萝的果实
dilute v. 把（液体）弄稀、弄淡
dilution n. 稀释、渗水
dim a.昏暗的；朦胧的
dime n. 一角
dimension n.尺寸，尺度；面积
dimensional adj. 尺寸的；n. 尺寸的，…维的
dimensions n. 面积；大小
diminish vt.减少，减小，递减
diminishing 递减
diminuendo n. (音乐)渐弱
diminution n. 减少,缩小,减低
diminutive adj. 小巧可爱的
dimity n. 凸花条纹布
dimly ad. 不清楚地；暗淡，朦胧，模糊
dimple n. 酒涡，笑靥
din n. 喧闹声，嘈杂声
dine vi.吃饭 vt.宴请
ding vi. 响,连响,执拗地讲
dinghy n. 救生橡皮筏，小船；无篷小船，小艇
dinginess  n. 肮脏; 昏暗
dingle n. 小峡谷
dingy adj. 肮脏的，褪色的
dining 进餐
dining-room n. 餐室，食堂；餐厅
dinner n.正餐(午饭或晚饭)
dinner-party n. 宴会
dinosaur n. 恐龙
dint n. 凹痕,打
diocesan a. 主教管区的
dioxide n.二氧化物
dip vt.浸；蘸
dip...into... 把…浸入(液体)中
diphtheria n. 白喉
diphthong n. 双重母音,双母音字,连母音字
diploma n.毕业文凭，学位证书
diplomacy n. 外交; 外交手腕
diplomat n. 外交官,有外交手腕的人
diplomatic a.外交的；有策略的
dipper n. 使浸渍者,现影液容器,汲取的人
dipsomania n. 嗜酒狂
dipsomaniac n. 耽酒症患者
dire adj. 可怕的；悲惨的
direct vt.指导
direction n.方向，方位；指导
directive n. 命令，指令
directly ad.直接地；立即
directness n. 笔直,直接,率直
director n.指导者；理事；导演
director-general 总干事；理事长
directory n.姓名地址录；董事会
direful adj. 可怕的，可怖的
dirge n. 哀歌、凄凉之曲调
dirigible a. 可驾驶的
dirk n. 短剑，匕首
dirt n.尘，土；污物，污垢
dirty a.脏的；下流的
dirver 司机
disability n. 无力,无能,残疾
disable vt.使无能，使伤残
disabled adj. 残废的；禁止的，报废的；n. 残疾人
disabuse v. 打消（某人）的错误念头，纠正
disadvantage n.不利，不利地位
disadvantageous a. 不利的,不便的,诽谤的
disaffected adj. （政治上）不满的，叛离的
disaffection n. 政治上不满，叛离
disagree vi.意见不同；不一致
disagreeable adj. 讨厌的、乖戾的
disagreement n.不一致；争论
disallow vt. 不许,不准,驳回
disappear vi.消失，消散
disappearance n.消失，消散；失踪
disappoint vt.使失望，使受挫折
disappointed adj. 失望的；扫兴的
disappointing a. 令人失望的
disappointingly ad.使人失望地
disappointment n.失望；沮丧
disapprobation n. 不答应,不赞成,非难
disapproval n.不赞成；不满意
disapprove vt.vi. 不赞成
disarm vt. 解除武装,回复平常的编制,
disarmament n. 缴械；裁军
disarrange vt. 扰乱,搅乱,弄乱
disarray n. 混乱，漫无秩序
disaster n.灾难，祸害；天灾
disasterous a. 灾难性的，造成惨重损失的
disastrous a.灾难性的；悲惨的
disavow vt. 否认,否定,抵赖
disavowal n. 否认,否定,拒绝
disband v. 解散（团体）
disbar v. 取消律师资格
disbarment n. 取消律师资格
disbelief n. 不信仰,不信,怀疑
disbelieve vt.vi. 不信,怀疑
disburse v. 支付，支出
disbursement n. 支出，开支
disc n. 圆盘,唱片
discard vt.丢弃，抛弃，遗弃
discern vt.看出，辨出；辨别
discernible a. 看得清的；辨别得出的
discerning a. 有识别力的
discernment n. 眼光、洞察力
discharge vt.释放；排出 n.释放
discharged a. 被解散了的
disciple n. 信徒、弟子
disciplinarian n. 严行纪律的人，严师
disciplinary adj. 纪律的，学科的
discipline n.纪律；训练 vt.训练
disclaim v. 放弃权利，拒绝承认
disclose vt.揭开；揭发；揭露
disclosure n. 发觉,败露,败露的事情
disco n. 迪斯科舞厅
discolor  vt. 使…变
discoloration n.变色,褪色
discolour vt.（使）变色，褪色
discomfit v. 使懊恼、难堪
discomfiture n. 狼狈，难堪
discomfort n.不舒适；不安
discomfortable adj. 不舒服的
discommode 使为难
discompose v. 使失态，慌张；使不安，弄乱
discomposure n. 失态，慌张
disconcert vt. 使困惑,使仓皇失措,破坏
disconnect vt. 分离,不相连,拆开
disconsolate a. 郁郁不乐的
discontent n. 不满
discontented  adj.心怀不满的；不平的；不满的；不满足的，不满意的
discontinue vi. 搁下,中止,停止
discord n. 不调和,不和
discordant adj. 不一致的，不调和的
discount n.折扣；打折扣卖
discountenance vt. 使丢脸,使蒙羞,使慌张
discourage vt.使泄气
discouraged adj. 泄气的；失去信心的
discouragement n.失望; 气馁
discourse n.讲话，演说，讲道
discourteous adj. 不恭的，不敬的
discourtesy n. 无礼,无礼貌,粗卤的言行
discover vt.发现；暴露，显示
discoverer n.发现者
discovery n.发现；被发现的事物
discredit v. 怀疑，n. 丧失名誉
discreet adj. 言行谨慎的，小心的
discreetly  adv. 谨慎地；慎重地
discrepancy n. 不同，矛盾
discrete adj. 个别的，不连续的
discretion n. 谨慎，审慎
discretionary  adj.随意的,自由裁量的
discriminate vt.vi. 区别,差别待遇
discriminating adj. 有辨别能力的
discrimination n.辨别；识别力；歧视
discriminatory n. 歧视的，差别待遇的
discursive adj. 散漫的，无层次的
discuss vt.讨论，谈论；论述
discussion n.讨论，谈论；论述
disdain v. 轻视、鄙视
disdainful adj. 鄙视的
disease n.疾病
diseased a. 生病的；有病的
disease-producing a. 致病的
disembark vt.vi. (使)起岸,(使)登陆
disembodied adj. 无实体的，空洞的
disembody vt. 使由肉体脱离
disenchant vt. 使清醒
disencumber v. 排除（障碍），摆脱（负担）
disengage vt. 使自由,解放,解开
disengaged adj. 空闲的，无公务在身的
disentangle vi. 解开纠结,松开,解决
disequilibrium 不均衡
disesteem vt. 侮辱,轻视
disfavor n. 厌恶,不悦,失宠
disfigure  vt. 毁损…的外观,使…变丑; 破坏…的
disfranchise v. 剥夺…的权力（尤指选举权）
disgorge v. 呕出，（水）流走
disgrace n.失宠，耻辱，丢脸
disgraceful a. 可耻的,不名誉的
disgruntle vt. 使不高兴
disgruntled n. 不满的
disguise vi.隐瞒，掩埋 n.假装
disguise...as 把…假扮成；使…假装
disgust n.厌恶，憎恶
disgustful adj. 令人生厌的
disgusting a. 令人作呕的；使人讨厌的
dish n.盘，碟；一道菜
dishabille n. 便服,便装
dishearten v. 使沮丧，使失去勇气
disheartened adj. 灰心；失望的
disheveled adj. 凌乱的，不整洁的
dishevelled adj. 散乱的，蓬散的
dishonest a. 不诚实的
dishonesty n. 不诚实
dishonor n. 不名誉
dishonorable adj. 不名誉的
dishonour n.不光彩；丢脸的人
dishonourable adj. 不名誉的，可耻的
dishonoured a.不光彩的，不名誉的
disillusion n.觉醒 vt.使觉醒
disillusionment n. 幻灭感
disinclination n. 不起劲,不感兴趣,厌恶
disincline vt. 使讨厌,不感兴趣
disinclined adj. 不愿意的；不愿的
disinfect vt. 消毒
disinfectant n. 消毒剂
disinfection n. 消毒
disinflation 反通货膨胀
disingenuous adj. 不坦白的，不真诚的
disinherit  vt. 剥夺<孩子>的继承权
disintegrate v. 分裂成小片，瓦解
disintegration n. 瓦解
disinter v. 挖出，掘土
disinterested adj. 公正的，客观的
disintermediation 金融中介作用削弱
disinvestment 负投资
disjoin vt.vi. (使)分开,(使)分离
disjoint vt.vi. (使)脱节,(使)解体,(使)脱臼
disjointed adj. 脱节的；杂乱的
disk n.圆盘，唱片；磁盘
diskette n. 软磁盘，软盘片
dislike vt.&n.不喜爱，厌恶
dislocate v. 使脱臼，把…弄乱
dislocation 脱节，动乱
dislodge v. 逐出，取出
disloyal a. 不实的,不义的,不忠的
disloyalty n. 不忠实,不信,不义
dismal a. 阴沉的，忧郁的
dismantle vt. 拆除...的设备,分解,去除覆盖物
dismay n.惊慌，沮丧，灰心
dismayed adj. 惊愕
dismember vt. 割断手足,支解,分割
dismiss vt.打发走；开除
dismissal n. 免职,解雇
dismission n. 免职,解雇
dismount vt.vi. (使)下马
Disney n.迪斯尼
disobedience n. 不服从,不孝,违反
disobedient a. 不服从的,不孝的,违背
disobey vt.vi. 违反,不服从
disorder n.混乱，杂乱；骚乱
disordered a. 混乱的
disorderly a. 无秩序的,乱的,骚动的
disorganize vt. 破坏阻织,搅乱秩序的,使混乱,
disorientate v. 失去方向感，迷途
disown vt. 否认 <著作等> 是自己的作品
disparage v. 贬抑，轻蔑
disparagement n. 轻蔑,瞧不起,轻视
disparate adj. 迥然不同的，不可并论的
disparity n. 不同，差异
dispart vt.vi. 分,分离,分开
dispassionate adj. 平心静气的
dispatch vt.派遣；调度 n.急件
dispatcher n. 调度负责人
dispel v. 驱散，消除
dispensable adj. 不必要的，可有可无的；非必需的，省得了的
dispensary n. 施药所,施疗院,诊疗所
dispensation n. 分配,施与,配药
dispense vt. 分配
dispenser n. 药剂师,配药员,分配者
dispersal n. 分散；疏散
disperse vt.(使)分散；驱散
dispersion n. 散布
dispirit vt. 使沮丧,使气馁
dispirited adj. 沮丧的
displace vt.移置；取代；置换
displacement n.移置；免职；置换
display vt.陈列，展览；显示
displease vt.使不愉快，使生气
displeasure n.不愉快,不满; 不高兴,生气
disport v. 玩耍、嬉戏
disposal n.丢掉，处理，销毁
dispose vi.去掉，丢掉；销毁
disposed adj. 有…倾向的；愿意，打算，倾向于；想干
disposition n. 处理，天性、气质
dispossess vt. 剥夺,使失去,逐出
dispossessed adj. 被剥夺财产的
dispraise vt. 毁谤,贬损,谴责
disproportion n. 不均衡
disproportionate a. 不成比例
disprove vt. 证明...是不对的,提出...的反证,
disputable a. 有讨论余地的,真假可疑的
disputant n. 争执者，争论者
disputation n. 争论,议论,驳斥
disputatious adj. 好争辩的
dispute vi.争论，争执 n.争论
disqualification n. 剥夺资格,不合格,失格
disqualified 不合格的
disqualify vt. 使丧失资格
disquiet n./v. 担心，焦虑
disquietude n.不安 (状态) ,动摇,不平静
disquisition n. 长篇演讲，专题论文
disregard vt.不管，不顾 n.不管
disrelish n. 不喜爱，厌恶
disrepair n. 失修，损破(的状况)
disreputable adj. 品格不端的，见不得人的
disrepute n. 声誉坏,坏批评,不名誉
disrespect n. 不敬,失礼,无礼
disrespectful a. 失礼的,无礼的
disrobe vt. 脱去衣服,使脱光
disrupt a. 分裂的,分散的
disruption n. 分裂,崩溃,瓦解
disruptive adj. 引起分裂的
dissatisfaction n.不满，不平
dissatisfied a. 不满的；显出不满的
dissatisfy vi.使不满，使不平
dissaving 负储蓄
dissect vt.vi. 解剖,切细
dissection n. 解剖,切开
dissemble v. 隐藏、掩饰（感受，意图）
dissembler n. 伪君子,伪善者
disseminate v. 散布，传播
dissemination n. 散播,传播,普及
dissension n. 意见不合,纠纷,倾轧
dissent v. 不同意，持异议
dissenter n. 持异义者
dissertation n. 论文
dissever vt.vi. 割裂,分开
dissident n. 唱反调者
dissimilar a. 不同的,相异的
dissimulate v. 隐藏、掩饰
dissimulation n. 掩饰,装糊涂,虚伪
dissipate vt.驱散；浪费vi.消散
dissipated adj. 浪费的，放荡的
dissipation n. 消散,分散,浪费
dissolute adj. 放荡的，无节制的
dissolution n. 分解,溶解,解散,结束
dissolve vt.解除(婚约等)
dissonance n. 不和谐（的音调）
dissonant adj. 不和谐的，不协调的
dissuade v. 劝阻，阻止
dissuasion n. 劝阻,劝戒,谏诤
distaff n. 卷线杆,拉线棒,拉线部门
distance n.距离；远处
distant a.在远处的，疏远的
distaste n. 讨厌,嫌恶
distasteful a. 讨厌的；乏味的
distemper n. 大瘟热,病异状,不高兴
distend v. （使）膨胀，胀大
distension n. 膨胀
distich n. 对句,对联
distil v.蒸馏，（使）滴下
distill vt. 蒸馏
distillation n. 蒸馏
distilled 人蒸馏出的
distiller n. 蒸馏酒制造业者
distillery  n.(尤指威士忌、杜松子酒等的) 蒸馏
distinct a.独特的
distinction n.差别，不同，区分
distinctive a. 特别的；独具一格的
distinctly adv. 清楚地；清晰地；显然，明晰地
distinctness n. 不同,明显
distinguish vt.区别，辨别，认别
distinguish...from 区别于
distinguishable adj.可区别的; 可看出的,可听出的
distinguished adj. 著名的，卓越的
distort vt.歪曲，曲解，扭曲
distortion n.弄歪，歪曲；畸变
distract vt. 分散(心思)；打扰；分心，困恼；使分心v. 分神，迷惑；adj. 心不在焉的
distracted adj. 心烦意乱的，精神不集中
distraction n. 娱乐,分心的事物,分心
distrain n.为抵债而扣押
distrait  adj.  (因不安、痛心等而) 心神恍惚的,心
distraught adj. 心神狂乱的
distress n.忧虑，悲伤；不幸
distressed 痛苦的
distressful a. 使苦恼的,苦难重重的,不幸的
distressing adj. 使人痛苦的
distribute vt.分发，分送；分布
distribution n.分发，分配；分布
distributor n.分配者,分发者, (货物的) 配销商
distributorship n. 分销权
district n.区，行政区；地区
distrust n. 不信任
distrustful a. 不信用的,怀疑的,可疑的
disturb vt.打扰，扰乱；弄乱
disturbance n.动乱；干扰；侵犯
disturbing a. 令人不安的；令人担心的
disunite vt. 使分离,不和
disunited a. 分裂的
disuse n. 不被使用,废弃
disused vt. 废弃，不用
dit n. 小孔砂眼
ditch n.沟，沟渠，渠道
ditto n. 同上
ditty n. 小调,小曲
diuretic n. & adj. 利尿剂
diurnal adj. 白昼的，白天的
diva  n. 歌剧中之首席女角
divagate v. (文章或谈话)离题，漂泊
divan n.(常靠墙摆放的) 无靠背长沙发
dive vi.跳水；潜水；俯冲
dive-bomber n. 俯冲轰炸机
diver n. 潜水者
diverge vi.分岔；分歧
divergence n. 分歧，分开
divergent adj. 分歧的，差异的；有分歧的
divers  adj. = diverse a.不同的,变化多的
diverse a.不一样的，相异的
diversification 经营多样化
diversify vt. 使多样化
diversion n.转移；改道；娱乐
diversity n. 多样化；不同；杂多；差异；多样性；变化万千
divert vt.使转向 vi.转移
divest vt. 剥除,使脱去,夺去
divide vt.分；分配；分开
divide...into... 把…分成…
dividend n. （股份的）红利
dividers n.两脚规
divination n. 占卜,卜卦,预测
divine a.神的；敬神的
diviner n. 卜者，占卦者，预言者
diving n. 跳水
divinity n. 神,神性
divisible a. 可分的,可分割的,除得尽的
division n.分，分配；除法
divisor n. 除数,法,约数
divorce n.离婚，离异 vi.离婚
divorse vt. 使离婚；(from)使脱离；n. 离婚；脱离
divulge v. 泄露，透露
dizziness n. 头晕，眩晕
dizzy a.头晕眼花的，眩晕的
dizzying a.极快的，极高的
dna (生化)脱氧核糖核酸
do v.做
doat vi. 昏馈,溺爱
docile a. 容易教的,温顺的
docility n. 顺从,温顺
dock vt.把…引入船坞
docket n. 摘要,记事表
docking n.扣工资
dockyard n. 造船所,海军工厂
doctor n.医生，医师；博士
doctorate n.博士学
doctrinaire n. 空论家；adj. 教条的，迂腐的；教条主义的
doctrinal a. 教义的,教条的,学理上的
doctrine n.教义，主义；学说
document n.公文，文件；证件
documentary a.纪录的，文献的
documentation n. 提供文件；文件编制，文本
doddering adj. 老态龙锺
dodge v. 闪开、躲避
doe n. 母鹿,雌兔等
doer n. 行为者,实干家
does v. & aux. 第三人称助动词；v. do的第三人称单数
doesn't (同)does not
doff v. 脱掉（外衣，帽子）
dog n.狗
dogfish n. 角鲨鱼之一种
dogged a. 顽固的,顽强的
doggedly adv. 固执地；执拗地；顽固地；顽强地
doggerel n. 歪诗，打油诗
dogma n. 教条
dogmatic adj. 教条的，教义的
dogmatism n. 独断,独断主义,独断论,教条主义
dogwood n. 山茱萸
doily n. 小型装饰桌巾
doing 做
doings n. 行为,活动
doit n. 小硬币，无价值之物，琐事
do-it-yourself 自己动手
doldrums  n.经济毫无生气；(海洋上的)无风带，情绪低沉；忧郁；消沉
dole n. 施舍品,失业救济金,悲哀
doleful adj. 忧愁的，消沉的
dolesman 领救济金者
doll n.(玩具)洋娃娃
dollar n.元(美国货币单位)
dolly n. 洋娃娃,捣棒
dolorous adj. 悲哀的，忧愁的
dolphin n.海豚
dolt n. 笨蛋，傻瓜
doltish adj. 愚笨的
domain n. 领土，领域
dome n.圆屋顶，拱顶
domestic a.本国的；家庭的
domesticate v. 驯养（动物）
domestication n. 驯服,教化
domesticity n. (喜欢)家庭生活
domicile n. 住所,住宅
dominance n. 优势，最高位置
dominant a.统治的 n.主因
dominate vt.统治，支配，控制
domination n. 统治，支配；控制
domineer v. 擅权，作威作福
Dominican adj. （天主教）多明我会的
dominion n. 领土,主权,统治
domino n. 化装外衣,面具
don v. 穿衣，戴帽
donate vt.vi. 捐赠
donation n. 捐赠
done do的过去分词；a. 注定要完蛋的；煮熟了的；合乎礼俗的；做
donkey n.驴；笨蛋
donor n. 捐赠人
don't (同)do not
don'ts n. 禁止的事
doodle v. 乱字，乱画
doom n.命运，毁灭 vt.注定
doomed 命定的
doomsday n. 世界末日
door n.门
doorbell n. 门铃
door-bell n. 门铃
door-keeper n. 看门人
door-knob n. 门把
doorman n. 看门的人
doormat n. 门前的擦鞋棕垫
doorstep n. 门阶
doorway n.门口；出入口
door-way n. 门口
dooryard n. 庭院,前院
dope n.有毒的药物(如鸦片)
dorford 道福特(地名)
Doric adj. 多利斯 (Doris) 地方的; 多利斯人
Dorling (英国一地名)道灵
dorm n.宿舍
dormant adj. 冬眠的，静止的
dormer  n. 天窗,老虎窗
dormitory n.集体寝室；宿舍
dormouse n. 睡鼠
dorsal adj. 背部的，背脊的
dory n. 小平底渔船
dos 磁盘操作系统
do's n. 要求做到的事
dosage n.剂量
dose n.剂量，用量；一剂
dossier n. 卷宗，档案
dot n.点，圆点 vt.打点于
dotage n. 老年糊涂，溺爱
dotard n.  老耄者,年老昏愦的人,老糊涂
dote v. 溺爱，昏愦
doth do的第三人称单数
doting adj. 溺爱的
double adj.两倍的；双的
doublet n.紧身上衣
doubling n. 加倍，双倍
doubloon n. 从前的西班牙金币的名称
doubly ad. 二倍地,双重地,双摺地
doubt n.怀疑；疑虑 vt.怀疑
doubtful a.难以预测的；怀疑的
doubtfully ad. 怀疑地，可疑地
doubting a. 可疑的，令人怀疑的；不信的
doubtless ad.无疑地；很可能
dough n. 生面团
doughboy n. 团子,步兵
doughnut n. 油炸圈饼
doughty a. 强的,勇敢的,刚强的
dour a. 不爱讲话的,沉沉的,严厉的,
douse v. 把…浸入水中，用水泼
dove n.鸽子，斑鸠
dover n.多佛(英国港市名)
dowager n.『法律』 (王公的) 寡妇,孀居贵妇
dowdy adj. 不整洁的，过旧的
dower n. 嫁妆,天赋,从亡夫处得来的产业
down ad.向下，在下面
downcast adj. 意志消沉的，朝下的
downfall n. 衰败,大雨
downhearted adj. 消沉的，沮丧的
downhill ad. 下坡，降下；vt. 降低
downpayment 预付定金，分期付款
downpour n.倾盆大雨
downright a. 明白的,率直的,显明的
downstairs adv.往楼下adj.楼下的
downstream ad. 下游地
downtime 商业区
downtown n. 市中心区
downward adv.向下；...以下
downwards  adv. 向下，以下
downy a. 绒毛的,柔和的,高原的
dowry n. 嫁妆
dowse vt.vi. 探寻水源
doxology n. 上帝赞美诗,颂歌,颂荣
doze vi. 打瞌睡,假寐
dozen n.一打，十二个
dr. n. (同)doctor博士；医生
drab adj. 枯黄色的，无聊的
drabness n. 乏味
draft n.草稿；汇票 vt.起草
drag vt.拖，拉；拖曳
dragon n.龙；凶暴的人
dragonfly n. 蜻蜓
dragoon n. 龙骑兵,骑兵,暴徒
drain vt.排去；放水 n.耗竭
drain...of 耗尽；用完
drainage n.排水；下水道
drake n. 公鸭,蜉蝣类
dram n. 打兰,一杯,微量
drama n.一出戏剧，剧本
dramatic a.引人注目的，戏剧的
dramatically ad. 戏剧性地；显著地
dramatist n. 剧作家
dramatize vt. 改编成戏剧,编写剧本
drank drink的过去式；喝
drape vi. 呈褶状垂下
drapery n. 帏帐,布料
drastic a.激烈的；严厉的
drastically ad. 大幅度地
draught n. (药的)顿服量；通风(气)；吸出
draw v.拉, 曳, 牵, 画, 绘制, 拖曳
drawback n.退款；妨碍；弊端
drawbridge n. 吊桥
drawee n. 受票人，(汇票)付款人
drawer n.抽屉
drawing n.图画，素描；绘图
drawing-room n. 客厅
drawl v. 慢吞吞说，拉长腔调说
drawn draw的过去分词；拉
dray n. 运货马车,撬的一种
drayage 运费
drayman n. 运货马车车夫
dread n.畏惧；恐怖 vt.惧怕
dreaded a. 令人畏惧的
dreadful a.可怕的；令人敬畏的
dreadfully adv. 可怕地,恐怖地; 提心吊胆地
dream vt.&vi.做梦 n.梦想
dreamer n. 做梦的人,梦想者
dreamland n. 梦境,梦乡,睡觉
dreamy a. 空幻的,梦想的
drear a. 沉闷的
dreary adj. 沉闷的，乏味的
dredge v. 用挖泥机疏浚，疏通
dredger n. 挖泥船
dregs n. 渣滓，糟粕
drench vt. 使湿透,使充满
drenched adj. 湿透的
dress n.衣服；连衣裙
dresser n. 化妆台,化装师,碗柜
dressing n. 打扮，调味品；敷料；敷裹；装饰
dressing-table n. 梳妆台
dressmaker n. 裁缝
dressmaking n. 女装裁缝
drew draw的过去式；拉
dribble v. （液体）往下滴，淌
dried a. 弄干了的
drier n. 干燥机,干燥剂
drift vi.漂流，漂泊 n.漂流
drifting a. 飘忽的；弥漫的
driftwood n. 流木,浮木
drill n.;vi.&vt.(军事)操练
drily ad. 冷冰冰地，干燥地；干巴巴地，枯燥地
drink vt.饮 vi.喝 n.饮料
drinker n. 喝的人,酒徒
drip vi.滴下；漏水 n.水滴
drive vt.&vi.驱赶；驾驶
drive-in a.免下车的
drivel vi. 淌口水,说傻话
driven drive的过去分词；驱赶；驱，赶
driver n.驾驶员，司机
driveway n. 车道
driving-test n. 驾驶测验
drizzle n./v. 下毛毛雨，毛毛雨
drizzly adj. 毛毛细雨的(a drizzly day)
droll adj. 古怪的，好笑的
drollery n. 滑稽
dromedary n. 单峰骆驼
drone v. 嗡嗡地响，n. 单调的低音
droop vi.&vt.(使)垂下
drop vt.使落下；降低
droplet n. 微滴
dropout n. 中途退出者；退学者
dropsical  adj. 水肿的; 患水肿的
dropsy n.『医』水肿 (症)
dross n. 浮渣，糟粕
drought n.旱灾，干旱
drove drive 的过去式；n. 畜群，人群；驱赶；驱，赶
drover n. 把家畜赶到市集的人,家畜商人
drown vt.&vi.淹死
drowning 溺水
drowse v./n.瞌睡
drowsiness n. 睡意
drowsy a. 昏昏欲睡的
drub 棒打，强迫灌注
drudge v. 劳碌，做苦差事，n. 劳碌的人
drudgery n. 苦差事,苦工
drug n.药，药物，药材
drug-fast 抗药的，耐药的
druggist n. 药商,药材商,药剂师
drugstore n. (美国习俗)杂货店；零食店
drum n.鼓；鼓状物，圆桶
drummer n. 鼓手,旅行推销员
drunk a.醉的；陶醉的
drunkard n. 酒鬼
drunken a. 酒醉的
drunkenness n.醉酒
dry vt.使干 vi.变干
dryad n. 森林的精灵
dryer n. 干衣机,干燥剂
dryly ad. (同)drily
dual adj. 双重的
dub vt. 配音,轻点,授予称号,打击
dubious a. 怀疑的
dublin n. 都柏林(爱尔兰首都)
ducal a. 公爵的,象公爵的,公爵领地的
ducat n.曾在欧洲通用的金币
duchess n. 公爵夫人
duchy n. 公爵领地,公国,直辖领地
duck n.鸭，雌鸭；鸭肉
duct n. 管；输送管
ductile adj. 易拉长的，易变形的，可塑的
ductless a. 无输送管的
due a.预期的；应给的
duel n. 决斗
duenna n.少女的保姆
duet n. 二重唱
dug  dig(挖)的过去式和过去分词
duke n.公爵
dukedom n. 君主领土,公国,公爵的地位
dulcet adj. （声音）悦耳的，美妙的
dulcimer n. 一种以槌敲金属弦而发出声音的乐器
dull a.枯燥的；不鲜明的
dullness n.迟钝
dully ad. 迟钝地；阴郁地
duly ad. 的确,当然地,适当地,及时地
dumb a.哑的；无言的
dumbfound vt. 使(人)目瞪口呆
dummy n. 傀儡,假人,哑巴
dump vt.倾卸，倾倒；倾销
dumping n. 倾销
dumpling n. 饺子
dun n. 催促者,讨债者,催罗
dunce n. 蠢材，笨人
dune n. 沙丘
dung n. 粪
dungeon n. 地牢
dunghill n. 粪堆,堆肥,简陋的房屋
dunkirk n. 敦刻尔克(法国港市)
duodenum n. 十二指肠
dupe n. 受骗的人，上当者
duplex 计算机] 双方的
duplicate n.复制品 vt.复制
duplication 复制
duplicity n. 欺骗，口是心非
durability  n. 耐久性
durable a.耐久的，耐用的
durance n. 禁锢,监禁
duration n.持续，持久
duress n. 协迫
during prep.在...的期间
durst (古)dare的过去式
dusk n.薄暮，黄昏，幽暗
dusky adj. 微暗的,暗淡的; 阴暗的
dust n.垃圾，废品，灰烬
dustbin n. 垃圾箱；簸箕
duster n. 掸子,打扫灰尘的人
dustman n. 垃圾清运工；清洁工；清除垃圾的人
dustpan n. 盛尘土的簸箕
dusty a. 灰尘多的,无聊的,含糊的,粉末状的
Dutch n. 荷兰人,荷兰语
Dutchman n. 荷兰人
duteous a. 忠贞的,顺从的,贞节的
dutiable a. 应纳关税的,有税的
dutiful a. 忠实的,顺从的,守本分的
duty n.义务；责任
duty-free adj. 免税的
dwarf n.矮子，侏儒
dwarfish a. 象侏儒的,矮小的
dwell n.居住 vi.凝思，细想
dweller n. 居民
dwelling n.住处，寓所
dwelt dwell的过去式(分词)
dwindle v. 日渐减少，变小
dye vt.染，把...染上颜色
dyeing n. 染色；adj. 染色的
dyer n. 染房
dying a.垂死的；临终的
dyke n. 塘
dynamic a.有活力的；动力的
dynamics n. 力学，动力学
dynamite n.炸药
dynamo n.发电机
dynastic a. 王朝的
dynasty n.王朝；朝代
dyne n. 达因(力的单位)
dynic n.恨世嫉俗的人
dyslexia n. 阅读
dyspepsia n. 消化不良
dyspeptic a. 消化不良的,胃弱的,患胃病的
dyton 戴顿
e.g. ad. 举例来说
each pron.各，各自 a.各
eager a.渴望的，热切的
eagerly adv. 渴望地；热切地；急切地；热心地
eagerness n. 热心
eagle n.鹰
eaglet n. 小鹰
ear n.耳朵；听力，听觉
ear-ache n. 耳痛
earl n. 伯爵
earldom n. 伯爵的身分
early adv.早
earmark n. 耳上记号,特征,记号,标记
earn vt.赚得，挣得；获得
earner n.获得收入者
earnest a.认真的，诚恳的
earnestly adv. 热心地；认真地；急切地
earnestness n. 诚挚
earnings n.工资，收入；收益
earphone n. 耳机
earring n. 耳环，耳饰
ears 耳朵
earth n.地球
earthen a. 土制的,陶制的
earthenware n.陶器
earthly a. 地球的,俗世的,可能的
earthquake n.地震
earthwork n. 泥瓦匠
earthworm n. 蚯蚓
earthy a. 土的,土质的,土味的
ease n.安逸，熟练，轻易
easel n. 框，(画)架；黑板架
easier a. 更容易的，更舒松的
easily ad.容易地；舒适的
east n.东,东方 adj.东方的
eastbound a.东去
Easter n. 复活节
easterly a. 东的,向东的,从东的
eastern a.东方的；朝东的
eastward a.&ad.向东的，向东
eastwards ad. & a. 向东方(的)，朝东(的)；东部
easy adj.容易
easygoing a. 悠闲自在的；懒惰的
easy-going adj. 逍遥自在的
eat vt.吃，喝 vi.吃饭
eatable a. 可以吃的
eaten eat的过去分词；吃
eater n. 吃的人,常食者,侵蚀物
eaves n. 屋檐
eavesdrop v. 偷听，窃听
ebb v. 退潮、衰退
ebony n. 黑檀树,乌木
ebullience n. 兴高采烈，兴冲冲
ebullient adj. 兴冲冲的，热情奔放的
ebullition n. 沸腾,精神饱满
eccentric adj. 古怪的，反常的
eccentricity n. 反常，怪癖
ecclesiastic n. 神职者,牧师,教会
ecclesiastical a. 教会的,神职的,牧师的
ecdysis n. (动物)蜕皮，换羽毛
echo vt.反射(声音等)
echo-location n. 回声定位
echo-sounding n. 回声测深
eclat  n. 辉煌的成就; 喝采; 名声
eclectic adj. 折衷的，综合性的；选择的
eclecticism n. 折衷主义
eclipse n.(日，月)食
ecliptic n. 黄道
ecliptie a. 日食的，月食的
eclogue n. 田园诗，牧歌
ecologic a.生态的；生态学的
ecological a. 生态的，生态学的
ecology n.生态学；个体生态学
economic adj.经济的；经济学的
economical a.节约的；经济学的
economically  adv.节约地，在经济上
economics n. 经济学；经济
economist n. 经济学者,经济家
economize v. 节省（钱、时间等）
economy n.经济；节约，节省
ecosystem n. 生态系(统)
ecstasy n. 狂喜，心醉神怡
ecstatic adj. 狂喜的，心花怒放的
eddy n. 漩涡，涡流
Eden n. 伊甸园,乐园
edge n.边缘；边
edging n. 边缘,边饰
edible a. 可以吃的
edict n. 法令、命令
edification n. 陶冶、教诲
edifice n. 大厦，(喻)心中构思之物
edify v. 陶冶，启发
edinburgh n. 爱丁堡(英国城市)
edison n. 爱迪生(美国发明家)
edit vt.编辑，编纂；校订
edition n.版，版本，版次
editor n.编辑，编者，校订者
editorial n.社论，期刊的社论
editor-in-chief 总编辑
educate vt.教育；培养；训练
educated adj. 受过教育的
education n.教育；训导；教育学
educational a. 教育的,教育性的
educator n. 教育家
educe vt. 引出,唤起,使显出
eeg 脑(动)电图描记器(缩)
eel n. 鳗鱼,鳝鱼
e'er ad. (诗)(同)ever，曾；永远
eerie adj. 胆怯的，引起恐惧的
eery a. 怪诞的,可怕的,奇异的,不安的
efface v. 擦掉，抹去
effcient n. 有能力的，能胜任的
effect n.结果；影响；效果
effective a.有效的；有影响的
effectively adv. 有效地
effectiveness n. 成效；有效；效力；生效
effectual a. 有效果的,会应验的,有效的
effectually ad. 有效地
effectuate 使实现
effeminacy n. 柔弱,女人气
effeminate adj. 柔弱的，缺乏勇气的
efferent a. 传出的
effervesce  v. 冒泡；沸腾，兴奋；热情洋溢
effervescence n. 冒泡,沸腾,活泼
effete adj. 衰老的，虚弱的，精疲力尽的
efficacious a. 有效的,灵验的
efficacy n. 功效,效力
efficiency n.效率；功效，效能
efficient a.效率高的，有能力的
efficiently ad. 有效地；能胜任地
effigy n. 假人，模拟像
effloresce 开花
efflorescent a. 开花的,风化的,发疹性的
effluence n. 流出,流出物,射出
effluent n. 流出的污物
effluvium n. 臭气,恶臭,放出
effort n.努力；努力的成果
effortless adj. 不费力的
effortlessly a. 不费力地
effrontery n. 厚颜无耻
effulgence n. 灿烂的光，强光
effulgent adj. 光辉的，灿烂的
effuse 流出，散布
effusion n. 流出物,泻出
effusive adj. 流出的，感情奔放的
eft n. 水蜥,小蜥蜴
egalitarian adj. 主张人人平等的
egg n.蛋
eggplant n. 茄子
eglantine n. 野蔷薇之一种
ego n. 自我
egocentric adj. 自我中心的；利己的
egoism n. 自我主义,利己主义
egoist n. 自我主义者
egotism n. 自我中心癖,自负
egregious adj. (缺点等)过份的，惊人的
egress n. 出去，出口
egret n. 白鹭，鹭鸶
Egypt n.埃及
Egyptian a.埃及的 n.埃及人
eh interj.(惊奇)啊! 嗯!
eiderdown n. 鸭的绒毛,鸭绒被
eight num.八
eighteen num.十八，十八个
eighteenth a. 第十八的,第十八,第十八日
eighth num.第八 n.八分之一
eightieth a. 第八十的,第八十,八十分之一的
eighty num.八十，八十个
einstein n. 爱因斯坦(物理学家)
either conj.或者， 要么
either...or conj. 不是…就是；或…或…
either...or... 或者…或者…
ejaculate v. 突然叫出或说出，射出
ejaculation n. 突然大叫
eject vt.逐出，排斥；喷射
ejection n. 喷射
eke vt. 补充,增加
elaborate a.复杂的；精心制作的
elaboration n. 详细说明，细致的工作
elan n. 精力；干劲
elapse vi.(时间)过去，消逝
elapsed vi. & n. 经过
elastic n.松紧带 a.有弹性的
elasticity n. 弹性伸缩力
elate vt. 使兴高采烈的,使得意
elated adj. 得意洋洋的，振奋的
elation n. 得意扬扬；得意，振奋；兴高采烈
elbow vt.用肘挤，挤进
elder a.年龄较大的 n.长者
elderberry n. 接骨木之果实,接骨木
elderly a. 过了中年的,稍老的
eldest  adj.  (因兄弟等的血缘关系) 最年长的
elect vt.选举，推选；选择
election n.选举，选择权；当选
electioneer vi. 从事选举活动
elective a. 选举的,根据选举的,选任的
elector n. 有选举权的人,选举人
electoral a. 选举人的,选举的,选帝侯的
electorate n. (全体)选民
electric a.电的，电动的
electrical a.电的，电气科学的
electrician n.电工，电气技师
electricity n.电，电学；电流
electrify vt.使触电；使充电
electrocardiograph n. 心(动)电图描记器
electrocute vt. 触电而死
electrode n.电极；电焊条
electrolysis n.电
electrolyte n. 电解物,电解质,电解液
electromagnet n. 电磁石
electromagnetic adj. 电磁的
electrometer n. 静电计
electromotive a. 起电的
electron n.电子
electronic a.电子的
electronics n. 电子学
electrotype n. 电版
elegance n. 典雅；雅致
elegant a.(举止、服饰)雅致的
elegantly adv. 雅致地，漂亮地
elegent a. 雅致的，优美的
elegiacal adj. 挽歌的；哀悼的
elegy n. 哀歌、挽歌
element n.元素；要素；成分
elemental a.基本的；自然力的
elementary a.基本的；初级的
elements n. 自然力
elephant n.象
elephantine adj. 笨拙的，巨大的
elephent n. 象
elevate vt.提高(思想)；抬高
elevation n.高度；标高；隆肿
elevator n.电梯；升降机
eleven num.十一
eleven-plus a. 11岁以上的
eleventh num.第十一(个)
elf n. 小精灵，矮子，淘气鬼
elfin a. 小妖精的,象小妖精的
elfish a. 如小精灵的,好恶作剧的,小妖精的
elicit v. 引出探出
eligibility n. 适任,合格
eligible adj. 适合被选的，合格的
eliminate vt.消灭，消除，排除
elimination n.消灭，排除，消除
elite n. 精华，中坚；名流
elitism n. 精英论，优秀人士统治
elixir n. 长生不老药，仙丹妙药
Elizabethan a. 伊莉莎白一世时代的,伊莉莎白女王的
elk n. 麋鹿
ell 旧时的量布长度
ellipse n. 椭圆(形)
ellipsis n. 省略；
elliptic a. 椭圆(形)的
elliptical a.椭圆的；省略的
elm n. 榆树
elocution n. 演说术
elongate v. 延长，伸长
elongation n. 延伸
elope v. 私奔
eloquence n.雄辩；口才，修辞
eloquent adj. 雄辩的，演说动人的
else adj.别的 adv.另外
elsewhere ad.在别处，向别处
elucidate v. 阐明说明
elucidation n. 说明,阐明
elude v. 逃避，
elusive adj. 难懂的
elusory a. 难以捉摸的
elves elf的复数
Elysian a. 乐土的,象天堂的
emaciate v. 使瘦弱
emaciated adj. 瘦弱的
emaciation n. 瘦弱,憔悴,衰弱
email n.电子邮件
emanate vi. 发出；散发
emanation n. 散发,发出
emanative adj. 发散的
emancipate v. 解放，解除
emancipation n. 释放，解脱
emasculate v. 阉割，使…无力
embalm vt. 以药物防腐,铭记于心,使不朽
embankment n. 堤岸，路基
embargo n. 禁运令，封港令
embark vi. 乘船,着手,从事,上飞机
embarkation 装载
embarrass vt.使负债；使复杂化
embarrassed a. 窘迫，尴尬
embarrassing  adj. 令人为难的；令人尴尬的
embarrassment n. 困难,阻碍,困窘
embassy n.大使馆；大使的职务
embattled adj. 作好战斗准备的,摆好阵势的
embed v. 牢牢插于，嵌于
embellish v. 装饰润饰
embellishment n. 装饰,润色,修饰
ember n. 灰烬,余烬
embezzle v. 盗用，侵吞
embezzlement n. 贪污，侵吞
embezzler 盗用公款者
embitter v. 使痛苦，使难受
emblazon vt. 用纹章装饰,盛饰,颂扬
emblem n. 象征，标志
emblematic adj. 作为象征的
embodiment n. 化身，体现
embody vt.体现；包含，收录
embolden v. 鼓励，给…壮胆
embosom vt. 围绕,环绕,珍爱
emboss v. 加浮雕花纹于，使凸出
embower  vt. 以树叶遮盖; 使…隐于树叶中
embrace vt.包括，包含；包围
embrasure n. 枪眼,炮眼
embroider v. 刺绣，修饰
embroidered adj. 绣花的
embroidery n.绣花，刺绣；绣制品
embroil v. 牵连，卷入纠纷
embryo n. 胚胎
embryonic adj. 胚胎的，萌芽期的
emend v. 修正；校订；订正，vt. 修正，修订
emendation n. 订正，校订
emerald n. 祖母绿，翡翠adj. 翠绿色的
emerge vi.出现，涌现；冒出
emergence n. 出现
emergency n.紧急情况，突然事件
emergent n. 紧急的，突然出现的，必然发生的
emeritus a. 名誉退休的,退休的
emery n. 金刚砂
emetic n. 催吐药
emigrant n. 移民,侨民
emigrate vi.永久移居国外
emigration n. 移民,移居
eminence n. 卓越、杰出
eminent adj. 著名的、显著的
emir n. 酋长,王侯
emissary n. 密使，特使
emission n.散发；传播；发出物
emit vt.散发；发射；发表
emollient n. 润肤剂
emolument n. 报酬，薪水
emote v. 激动地，表达感情
emotion n.感情；情绪；激动
emotional a.感情的，情绪的
emotionally ad. 感情上
empathy n. 心意相通，(感情等)融为一体
emperical n. 经验主义的
emperor n.皇帝
emphasis n.强调，重点，重要性
emphasise vt. 加强…的语气，强调，着重
emphasize vt.强调，着重
emphatic a. 语调强的,用力的,强调了的
emphatically ad. 强调地；断然地
emphysema n. 肺气肿
empire n.帝国
empiric n. 经验主义者,江湖医生
empirical a.经验主义的
empirically ad. 经验主义地
empiricism n. 经验主义，经验论
employ vi.雇用；用；使忙于
employe vt. 使用，花费
employee n.受雇者，雇员，雇工
employer n.雇佣者，雇主
employment n.工业；雇用；使用
emporium n. 商场，商业中心
empower vt. 授予权力,允许,使能够
empress n. 皇后,女皇帝
emprical a. 经验主义的
emprise n.冒险事业; 侠义行为
emptiness n. 空虚,无知
empty a.空的；空洞的
empurpled ] adj. 变成紫色的
empyreal adj. 天空的(empyreal heights天空高处)
empyrean n. 天空、天神居处
emulate v. 努力赶上或超越
emulation n. 竞争，仿效
emulator n. 仿真器，仿真程序
emulous a. 竞争性的,富于竞争的,求声名的,
emulsify v. 使乳化
emulsion n. 乳状液,乳剂
enable vt.使能够，使可能
enact v. 制定(法律)，扮演(角色)
enactment n. 颁布，扮演
enamel n. 珐琅,瓷釉
enamor vt. 迷住,使迷恋
enamored adj. 倾心的；被迷住的
enamour vt. 迷住,使迷恋
enamoured adj. 珍爱的，喜爱的
encamp vi. 扎营,露营
encampment n. 露营,宿营
encapsulate v. 装入胶囊，压缩
encase vt. 围住，包起；把...装入箱内
encash 把…兑现兑现，取得现金
encephalitis n. 脑炎
enchain vt. 束缚,以铁练绑住
enchant vt.迷住；用魔法迷惑
enchanter n. 行妖术的人,魔法师
enchanting adj. 讨人喜欢的
enchantment n. 着魔，喜悦
enchantress n. 妖妇,女巫
encipher v. 译成密码
encircle vt. 环绕
enclave n. 被包围的领土
enclose vt.围住，圈起；附上
enclosed 附入包装，封入
enclosure n.围绕；围场，围栏
encls 附件，内封物(缩)
encode vt. 编码
encomiastic a. 赞颂的,阿谀的
encomium n. 赞颂，颂辞
encompass v. 包围，围绕
encore n. 再演唱的要求,经要求而再唱
encounter vt.遭遇，遇到 n.遭遇
encourage vt.鼓励，支持，助长
encouraged 被鼓励的
encouragement n. 鼓励,激励,奖励
encouragingly ad. 鼓励地
encroach v. 侵占，蚕食
encroaching a. 渐渐渗入的
encroachment n. 侵入，侵犯
encrust vt. 包外壳,镶嵌
encumber v. 妨害，阻碍
encumbrance n. 妨碍物，累赘
encunter v. 遭遇，遭到
encyclopaedia n.百科全书
encyclopaedic a. 广博的
encyclopedia n. 百科全书
encyclopedic adj. 广博的，知识渊博的
encyst vt. 把...包在囊内
end n.目标，目的
endanger vt.危及，危害
endear vt. 使受喜爱
endearing a. 引起亲昵感情的
endearment n. 亲爱的行为或话语
endeavor n. 努力,事业,vi. 试图；努力
endeavour vi.&n.努力，尽力
endemic adj. 地方性的
ending n.结尾，结局；死亡
endive n. 菊苣
endless a.无止境的
endlessly ad. 无尽地；不停地
endocrine a. 内分泌的；n. 内分泌
endorse vt. 支持,赞同,背书于,签
endorsee 被背书人，被转让人，受让人
endorsement n. 背书，赞同
endorser 背书人
endothelial a. 内皮的
endow vt.资助；赋予，授予
endowment n. 捐助,天赋,才能
endue vt. 授予,赋予,穿上
endurable a. 可忍受的,能忍耐的
endurance n.耐久力，持久力
endure vt.忍受；容忍
endures n. 最终用户
enduring a. 持久的
enemy n.敌人；仇敌；敌兵
energetic a.积极的；精力旺盛的
energetics n. 动能学
energize vt.给与…能量；电压
energy n.活力；精力；能
enervate v. 使虚弱，使无力
enfeeble vt. 使衰弱
enfold vt. 包进,拥抱
enforce vt.实施，执行；强制
enforceable  adj. 可强行的; 可实施的
enforced a. 强加的
enforcement n. 执行,强制
enfranchise v. 给予选举权，释放(奴隶)
enfranchisement n. 参政
eng. (同)england，english
engage vt.使从事于；聘用
engaged adj. 占用的，从事…的
engagement n.婚约；约会，债务
engaging adj. 迷人的，美丽动人的
engels 恩格斯
engender v. 产生，引起
engine n.发动机，引擎；机车
engineer n.工程师，技师
engineering n.工程，工程学
engine-room n. 机器房
enginery n. 机器,机械类,兵器
England n.英格兰；(泛指)英国
englander n. 英格兰人；英国人
English adj.英国的 n.英语
Englishman n.英国男子
englishmen n. englishman的复数
englishwoman n. 英国女人
engraft vt. 使牢记,灌输,嫁接
engrave vt. 刻上,雕刻,铭记
engraver n. 雕刻师,雕工
engraving n. 雕刻,镌版术,雕版
engross v. 全神贯注于
engrossed 全神贯注的
engrossing adj. 引人入胜的
engrossment 垄断产品，哄抬讪价
engulf v. 吞噬
enhance vt.提高，增加；夸张
enhanced a.加强的
enhancement n. 提高；增加
enigma n. 谜，谜一样的人或事
enigmatic adj. 神秘的，难解的
enigmatical a. 难解的,谜一般的,不可思议的
enjoin v. 命令，吩咐
enjoy vt.享受；欣赏，喜爱
enjoyable a. 可享受的,令人愉快的
enjoyment n.享乐；欣赏
enkindle v. 煽动，点燃(感情怒3气等)
enlarge vt.扩大，扩展；放大
enlargement n. 扩大
enlighten vt.启发，开导；启蒙
enlightened  adj.开明的；有知识的；有见识的
enlightening adj. 给人启发的
enlightenment n. 教化，启蒙
enlist v. (使)入伍从军，征募
enlistment n. 征兵
enliven vt. 使活泼,使生动
enmesh v. (通常被动)绊住，陷入网
enmity n. 敌意，仇恨
ennoble vt. 授予爵位,使高贵
ennui n. 倦怠,厌倦
enormious a. 巨大的，庞大的
enormity n. 极恶，暴行，巨大
enormous a.巨大的，庞大的
enormously ad. 巨大的，庞大的
enough adj.足够的adv.充分地
enplane 乘飞机
enpuire v. 打听，询问调查，查问(enpuire=inpuire)
enquire vi.vt. 询问
enquiry v. 询问
enrage vt. 激怒,使暴怒
enrapture v. 使狂喜，使高兴
enrich vt.使富裕；使丰富
enrichment n. 致富
enrol vt.登记，招收
enroll vt.登记，招收vi.参军
enrollment n. 登记,注册,入伍
enrolment n.登记,注册,入伍
ensanguine vt. 满身染血,血染,使成血红色
ensconce v. 藏匿；庇护；安置，安坐
ensemble n. (法)全体；合唱团；总体，集合体；大合唱
enshrine v. 奉为神圣，珍藏
enshroud vt. 掩盖,隐蔽
ensign n. 舰旗
ensilage n. 未干秣草之保藏,保藏于地窖中的未干秣草
enslave vt. 奴役,束缚,沉溺,征服
ensnare v. 诱入陷阱，进入罗网
ensue vi. 跟着发生,继起
ensure vt.保证；保护；赋予
ent 耳鼻喉科
entail vt. 使成为必要；必须包括
entangle v. 使纠缠，卷入
entanglement n. 纠缠，牵累
entente n. 协定,协约
enter vt.走进，进入；参加
enterprise n.艰巨的事业；事业心
enterprising adj. 有进取心的，有事业心的
entertain vt.使欢乐；招待
entertainer 表演者
entertaining a. 有趣的
entertainment n.招待，招待会
enthral vt. 迷惑,奴役,迷住
enthrall v. 迷惑，迷住
enthrone vt. 立...为王,使登极,任为主教,
enthusiasm n.热情，热心，热忱
enthusiast n. 热心家,狂热者,爱好者
enthusiastic a.热情的，热心的
enthusiastically ad. 热心地,狂热地
entice v. 纵恿，引诱
enticement n. 诱骗，诱人
entire a.全部的，整个的
entirely adv.完全地；彻底地
entirety n. 全部,完全
entitle vt.把…称作
entitled 有资格的
entity n. 实体，统一体
entomology n. 昆虫学
entrails n. 内脏，肠
entrance n.入口；进入；入场
entrap vt. 骗入,诱捕,使陷入
entreat vt.&vi.恳求
entreaty n. 恳求，哀求
entree n. 入场许可,主菜
entrench vt. 保证；确立
entrenched adj. (权力风俗等)确立的，确定的
entrenchment n. 掘壕沟,壕沟,防卫工事
entrepreneur n. 企业家，创业人
entrust v. 委托，付托
entry n.入口处；登记；进入
entwine v. 使缠绕，交织
enumerate v. 列举枚举
enumeration n. 计算,列举,细目
enunciate v. 发音，(清楚地)表达
enunciation n. 阐明，发表
envelop vt. 包封,遮盖,包围
envelope n.信封
envenom vt. 下毒,使恶毒,毒化
enviable a. 令人羡慕的,可羡慕的
envious a. 嫉妒的,羡慕的
enviously ad.羡慕地；妒忌地
environ vt. 包围,环绕
environment n.环境，外界；围绕
environmental  adj. 环境的；环境产生的；周围的
environs n. 郊外，郊区；城郊
envisage v. 正视，想象
envision vt. 预想；v. 展望，想象
envoy n. 使者，代表，跋词，后记
envy n.&vt.羡慕；忌妒
enwrap vt. 围绕,包围
enzyme n. 酵素，酶
eon n. 永世,无数的年代
epaulet n. 肩章，肩饰
ephedrine n. 麻黄碱；麻黄素
ephemeral adj. 朝生暮死的，生命短暂的
ephod n. 犹太教的大祭司的法衣
epic n. 史诗
epicenter n.中心
epicentre 震中
epicure n. 美食家
epicurean adj. 好享乐的享乐主义的
epidemic adj. 传染性的，流行性的
epidermis n. 表皮，外皮
epiglottis n. 会厌
epigram n. 警句，讽刺短诗
epigrammatic adj. 警句的
epilepsy n. 癫痫症
epileptic a. 癫痫的,癫痫性的
epilogue n. 收场白，尾声
Episcopal a. 主教的,主教制度的,英国国教的
episcopalian a. 主教制度的,主教派的
episode n.一段情节；插曲
epistemology n. 认识论(对知识本质的研究)
epistle n. (长而重要的)书信
epistolary a. 书信的,用书信的,书信体的
epitaph n. 墓志铭
epithelial a. 上皮的
epithet n. (贬低人的)短语或形容词
epitome n. 典型，梗概
epoch n.(新)时代；历元
epoch-making adj. 划时代的
equable adj. 稳定的，（脾气）温和的
equal a.相等的；平等的
equality n.等同，平等；相等
equalization n. 使均等,同等化,平等化
equalize vt. 使相等,补偿
equally adv. 相等地，相同地；同样；平等地；同样地
equanimity n. 镇定，沉着
equate v. 使相等；与...相提并论，视为同等；vt. (with)使相等，使等同
equation n.方程(式)；等式
equator n.赤道，天球赤道
equatorial a. 近赤道的,赤道的
equestrian a. 骑马的,马的,在马背上的
equidistant a. 距离相等的,等距的
equilibrium n.平衡，均衡；均衡论
equine adj. 马的，似马的
equinoctial n. 春分或秋分时的暴风雨
equinox n. 昼夜平分点,春分或秋分
equip vt.装备，配备
equipage n. 装备
equipment n.装备；设备
equipoise n. 平衡,均衡
equitable adj. 公平的，公正的
equitably 公平地
equitation n. 骑术
equity n. 公平，公正
equivalence n. 相等，等值；等价，等量
equivalent a.相等的；等量的
equivocal adj. 意义含糊的，不直率的
equivocate v. 模棱两可地说，支吾其词
equivocation n. 模棱两可的话,含糊话
er interj. 呃，啊，这；欧(说话犹豫等)
era n.时代，年代；纪元
eradicate v. 根除，扑灭
eradication n. 根除
erase v. 擦掉，抹去
eraser n. 橡皮擦；黑板擦
erasure n. 抹去；擦掉，擦痕
ere pron. & conj. 在…之前
erect vt.建造；使竖立
erection n. 直立,竖起,建筑物
eremite n. 隐士，遁世修行的人
erewhile ad. 片刻前,以前
ergo  adv. ((谑))因此,所以
eric 埃里克(男名)
ermine n. 貂,貂的白毛皮
erode v. 腐蚀，侵蚀
erosion n.腐蚀，侵蚀；糜烂
erotic adj. 性爱的，色情的(作品)
err vi. 犯错,做错,犯罪
errand n.差使，差事
errant adj. 错误的，脱离正途的
erratic adj. 反复无常的古怪的
erroneous a. 错误的,不正确的
error n.错误，谬误；差错
ersatz adj. 代用的，假的
erst ad. 以前,往昔的
erstwhile adj. 往日的，以前的
erudite adj. 博学的，饱学的
erudition n. 博学
erupt vt. 喷发，迸发；长牙；爆发，v. 喷发，爆发；喷出火焰；(火山等)进发
eruption n. 爆发
eruptive a. 暴发的,喷火的
erysipelas n. 丹毒
erythema 红斑
erythrocyte n. 红细胞
escalate v. (战争等)升级，扩大，上升
escalator n. 电动扶梯
escapade n. 异常出轨的行为
escape n.&vi.逃跑
escapist n. 会消遣的人
escarpment n. 悬崖,断崖,绝壁
eschew v. 避开，戒绝
escort n.&vt.护卫，护送
escrow 由第三者保存的契约或证书
escutcheon n. 饰有纹章的盾
Eskimo n. 爱斯基摩人
esophagus n. 食道
esoteric adj. 秘传的，神秘的
especial a. 特别的,特殊的
especially ad.特别，尤其，格外
esperanto n. 世界语
espionage n. 间谍活动
espousal n. 拥护，支持
espouse v. 支持，拥护
esprit  n. 精神; 机智,才智
espy v. (从远处等)突然看到
esquire n. 先生(信件用语)
essay n.短文，散文，小品文
essayist n. 随笔作家,评论家
essence n.本质，本体；精华
essential a.必要的，本质的
essentially  adj. 本质上，实质上；ad. 本质上，基本上；实质上，本来
establish vt.建立，设立；确立
established adj. 已建立的；既定的，确定的
establishment n.建立，设立，确立
estate n.房地产；财产，产业
esteem n. 尊敬,尊重
esthetic a. 审美的
estimable adj. 值得敬重的，可估计的
estimate vt.估计，评价 n.估计
estimation n. 判断,值计,尊重
estrange v. 使疏远
estranged adj. 疏远的,不和的
estrangement n. 疏远
estuary n. 河口，三角湾
etc. n. 等等
etch v. 蚀刻，铭刻
etching n. 蚀刻技术
eternal n.永久的；不朽的
eternally ad. 永久地；不朽地
eternity n. 永远,来世,不朽
ether n. 醚,大气,苍天,以太
ethereal adj. 太空的，轻巧的
ethic a. 伦理(等)的，道德的
ethical a. 伦理的,民族的,民族特有的
ethics n. 道德体系，行为准则
ethiopia n. 埃塞俄比亚
ethiopian adj. 埃塞俄比亚的
ethnic a. 种族的
ethnical a. 人种的；种族的
ethnography n. 人种学，人种论
ethnology n. 人种学
ethos n. (个人，团体或民族)道德风貌，思潮信仰
etiquette n. 礼仪礼节
etude n. 练习曲
etymology n. 语源学
eucalyptus n. 桉树
Eucharist n. 圣餐
eugenic adj. 优生(学)的
eulogistic adj. 颂扬的，歌功颂德的
eulogize v. 颂扬；赞美
eulogy n. 颂词，颂文
eunuch n. 太监,宦官,柔弱的男人
euphemism n. 婉言，委婉的说法
euphonious adj. 悦耳的
euphony n. 悦耳的语音
euphoria n. 幸福愉快感；心情愉快；情绪高涨
Eurasia n. 欧亚大陆
eurasian a. 欧亚的
eurhythmic adj. 匀称的，协调的
eurobank 欧洲银行
Europe n.欧洲
European a.欧洲的 n.欧洲人
euthanasia n. 无痛苦的死亡；安死乐
evacuate v. 撤退，撤离
evacuation n. 撤退,走开
evade v. 逃避，规避
evaluate vt. 评价，估…的价；估计；估价，评估；求…的值；估算，求值
evaluation n. 评估；估价，评价；赋值
evanescent adj. 短暂的，瞬息的
evangelical adj. 福音 (书) 的,福音传道的
evangelist n. 福音传道者,圣经新约福音书的作者
evans (姓)埃文斯；埃文斯(姓)
evaporate vt.使脱水vi.发散蒸气
evaporation n. 蒸发
evaporator  n. 蒸发器,干燥器
evasion n. 逃避,藉口
evasive adj. 逃避的
eve n.前夜，前夕，前一刻
even adv.甚至，即使
evening n.傍晚，晚上
evenly  adv.一致地，平静地；平坦地，均匀地
evens 埃文斯(姓)
event n.事件，大事；事变
even-tempered adj. 性情平和的，不易生气的
eventful a. 变故多的,多事的,重要的
eventide n. 黄昏,日暮
eventual a. 最后的,终于的,可能的
eventually ad.终于；最后
ever adv.曾经
ever-bubbling 不断涌出的
everest n. 珠穆朗玛峰
evergreen n. 常绿树,常绿植物
ever-increasing a. 不断增长的
everlasting a.永久的；持久的
evermore ad. 永远,经常,从此以后
ever-present a. 无时无刻不在的
every adj.每一，每个的
everybody pron.每人，人人
everyday a.每天的，日常的
everyone pron.每人，人人
everything pron.每件事,每样东西
everywhere adv.到处，无论哪里
evict v. (依法)驱逐
evidence n.根据；证据，证人
evident a.明显的，明白的
evidently adv. 明显地，显然
evil adj.邪恶的 n.罪恶
evince v. 表明，表示
eviscerate v. 取出肠及内脏
evitable adj. 可避免的；可心以避免的
evocative adj. 唤起的，激起的
evoke v. 引起，唤起
evolute a. (数学)渐屈线
evolution n.发展；演变
evolutionary adj. 进化论的
evolutionist n. 进化论者
evolve vt.使进化；使发展
ewe n. 母羊
ewer n. 大口水罐
ex prep. 在…交货；无不，末
exacerbate v. 加重，恶化
exact a.确切的；精确的
exacting a. 严格的；费力的；苛求的；要求严格的
exaction n. 强求，勒索
exactitude n. 正确,精密,严格,规规矩矩,精确
exactly adv.确切地，恰恰正是
exactness n. 正确,精确
exaggerate vt.&vi.夸大，夸张
exaggerated adj. 言过其辞的
exaggeration n. 夸张
exalt v. (高度)赞扬，歌颂
exaltation n. (成功带来的)得意，高兴
exalted adj. 高贵的，得意的
exam n. (口语)考试；检查，细查；(exam＝examination)考试
examination n.检查；考试
examine vt.检查；诊察
examiner n. 主考者
example n.例子；榜样
exasperate v. 激怒，使恼怒
exasperation n. 激怒
excavate v. 挖掘，挖出
excavation n. 挖掘，发掘，被挖掘之地
excavator n. 开凿者,打洞机,开凿机
exceed vt.超过，胜过；超出
exceeded a. 过度的，非常的
exceeding a. 超越的，非常的
exceedingly ad.极端地，非常
excel vt.胜过 vi.杰出
excellence n. 优秀,卓越,优点
Excellency n. 阁下,优点
excellent adj.极好的，优秀的
excelsior a. 不断向上的,精益求精的
except prep.除...之外
excepting  prep. 除了…以外
exception n.例外，除外
exceptionable adj. 引起反感的
exceptional a.例外的；优越的
exceptionally ad. 例外地；异常地；极，很
excerpt n. 摘录
excess n.超越；过量；过度
excesses n. 过份荒淫的行为
excessive a.过多的，极度的
excessively ad. 过分，极端地
exchange vt.交换；交流 n.交换
exchangeable a. 可交换的，可转换的
exchequer n. 国库，财源
excise v. 切除，删去
excision n. 切除，割除
excitable a. 易兴奋的,易怒的
excitation n. 刺激；激发，激励
excite vt.使兴奋；使激动
excited adj. 兴奋的；激昂的；激动的
excitedly adv. 兴奋地；激动地
excitement n. 刺激,兴奋
exciting adv. & adj. 激动人心的；adj. 令人兴奋的；令人激动的；使激动的；兴奋的；使人振奋的
exclaim vi.呼喊；惊叫
exclamation n.呼喊，惊叫；感叹
exclamatory a. 感叹的,惊叹的
exclude vt.把…排除在外
exclusion n. 拒绝，排斥
exclusive a.除外的；孤傲的
exclusively  adv.排外地；专门地；独占地；独有地
exclusivity n. 独家经营权
excogitate v. 想出，设计(计划，办法)
excommunicate vt. 逐出教会
excommunication n. 逐出教会
excoriate v. 撕去皮，严厉批评
excrement n. 排泄物,大便
excrescence n. 异常生长,瘤,赘生物
excreta n.排泄
excrete vt. 排泄,分泌
excretion n. 排泄,排泄物
excretory a. 排泄的,分泌的
exculpate v. 开脱，申明无罪
excursion n.离题
excursive a. 游览的,离题的,散漫的
excuse n.藉口；托辞
ex-dividend n.无股利，无股息
execrable adj.极坏的
execrate v. 憎恶，咒骂
execration n. 憎恶,诅咒,念咒
exective n. 总经理，董事，行政负
executable a. 可执行的
execute vt.将…处死；实施
execution n.实行，执行；处死刑
executioner n. 刽子手
executive n.总经理，董事
executor n. 遗嘱执行人
exegesis n. (对圣经等的)严肃解释，注释
exeggerate v. 夸大，夸张
exemplary a. 模范的
exemplification n. 例证,范例
exemplify vt. 举例证明(解释)；v. 举例说明
exempt adj. 被免除的，v. 使免除
exemption n. 免除
exercise n.练习
exercise-book n. 练习簿；练习本
exert vt.发挥(威力)，施加
exertion n. 努力，用力
exhalation n. 呼气,蒸发,发出物
exhale v. 呼出(气)
exhaust vt.使筋疲力尽；用尽
exhausted  adj. 精疲力竭的；耗尽的，筋疲力尽的
exhaustion n. 疲备，耗尽
exhaustive adj. 彻底的，无遗漏的
exhibit vt.显示；陈列，展览
exhibition n.展览
exhibitionism n. 风头主义
exhibitionist n. 喜欢出风头的人
exhibitor n. 展出人；展出单位
exhilarate v. 使高兴
exhilarating  adj.使人高兴的；使人兴奋的
exhilaration n. 令人高兴,愉快
exhort v. 力劝，勉励
exhortation n. 劝告，规劝
exhume v. 掘出，发掘
exigency n. 紧急,急迫,苛求,紧急事件
exigent a. 紧急的,迫切的,苛求的
exiguous adj. 稀少的，微小的
exile vt.流放 n.被流放者
eximbank 进出口银行
exist vi.存在；生存
existence n.存在，实在；生存
existent a. 存在的，实在的，现存的
existing adj. 现存的，已有的；现有的；现行的；目前的
exit n.出口；退场 vi.退出
exodus v. 大批离去，成群外出
exogamy n. 异族通婚
exogenous 外生的
exonerate v. 免除责任，确定无罪
exoneration n. 免罪，免除
exorbitant adj. 过份的，过度的
exorcise v. 驱邪；除怪
exorcism n. 驱鬼，伏魔
exorcize v. 驱魔，去除(坏念头等)
exotic adj. 珍奇的，来自异国的
expand vt.扩大；使膨胀
expanding a. 扩展的，扩充的
expanse n. 宽阔的区域,宽阔
expansile adj. (可)增大的
expansion n.扩大，扩充；扩张
expansionary 扩张性的
expansive a. 易膨胀的,易扩张的
expatiate vi. 详述,细说
expatriate v. 驱逐出国，脱离国籍
expect vt.料想，认为
expectable a. 可预想的；意料中的
expectancy n.期待; 期望
expectant n. 预期者,期待者
expectation n.期待，期望，预期
expected a. 预期的，期待的
expectorate vt. 咳出
expedience n. 权宜,方便,私利
expediency n. 方便，权宜之计
expedient n. 权宜之计,临时手段
expedite v. 使加速，促进
expediter 稽查员
expedition n.探险；探险队
expeditionary adj.远征的；探险的
expeditious adj. 迅速的，敏捷的
expeditiously adj. 迅速地；敏捷地
expel vt.驱逐，开除；排出
expend v. 花费，用光
expendable adj. 可耗尽的，可牺牲的；消耗品
expenditure n.(时间等)支出，消费
expense n.消费；花费
expensive adj.昂贵的
experience n.经验，感受；经历
experienced adj. 有经验的；老练的；熟练的
experiment n.实验；试验
experimental a.实验的，试验的
experimentally ad. 实验上，实验性地
experimentation n. 实验，试验；实验法；实验(工作，法)；研究
expert n.专家 a.熟练的
expertise n. 专家队伍(总称)；专技，专业知识；专门，知识，专长
expiate v. 赎罪，补偿
expiation n. 赎罪,补偿
expiration n. 期满，终止
expire vi.满期，到期；断气
expiry n. 逾期
explain vt.&vi.解释，说明
explaination n. 解释，说明
explanation n.解释，说明；辩解
explanatory a. 说明的,解释的,辩明的
expletive  adj. 仅作补充性的; 附加的
explicable adj. 可解释的
explicate v. 详细解说
explicit a.明晰的；直率的
explicitly adv. 清晰地；明显地，显然地
explode vt.使爆炸 vi.爆炸
exploit vt.剥削；利用；开拓
exploitation n. 开发,开采,自私的利用
exploration n.考察；勘探；探查
explore vt.&vi.探险，探索
explorer n. 探险家,探测者
explosion n.爆炸，爆发，炸裂
explosive n.炸药 a.爆炸的
exponent n. 说明者，支持者
exponential a. 指数的，幂的，阶的
exponentially ad.成倍地；指数地；幂地
export vt.输出，出口；运走
exportation n.输出,出口
exporter n. 出口商
expose vt.使暴露；揭露
exposed adj. 暴露在外的
exposition n.说明，解释；陈列
expositive a. 说明的；阐述的；评注的
expositor n. 说明者,解释者
expostulate v. (对人或行为的)抗议，告诫
expostulation n. 劝告,谏言
exposure n.暴露；揭露；曝光
expound v. 解释，阐述，提出
express vt.表示 n.快车，快递
expression n.词句；表达；表情
expressive a. 表达的
expressly adv. 清楚地，特意地
expressway n. 高速公路
exprivileges 无特权；不予优待
expropriate v. 充公，没收
expropriation 没收，征用
expulsion n. 驱逐，开除
expunge v. 删除
expurgate v. 净化，删去
exquisite adj. 精致的，近完美的
exquisitely ad. 精巧地，优美地
ex-soldier n. 退伍军人
extant adj. 现存的，传世的
extemporaneous a. 无准备的,即席的,临时的
extempore a. 即席的,当场的
extemporize v. 即席演说；即席发言
extend vt.延长；扩大；致
extended a. 伸长的；广大的
extension n.延长部分；伸展
extensive a.广阔的；广泛的
extensively adv. 广泛地；彻底地
extent n.广度；范围；程度
extenuate v. 掩饰(罪行)，减轻罪过
extenuation n. 酌情减轻,减轻
exterior a.外部的；对外的
exterminate v. 消灭，灭绝
extermination n. 消灭,根绝
exterminator n.以消灭老鼠(蟑螂、臭虫)为职业的人
external a.外部的，外面的
externality 外部效应
extinct a.绝种的；熄灭了的
extinction n. 熄灭，消灭
extinguish vt.熄灭，扑灭；消灭
extirpate 消灭，根除
extirpation n. 消灭,根除,毁灭
extol v. 赞美
extort v. 强索
extortion n. 强取
extortionist n. 勒索者，敲诈者
extra a.额外的 ad.特别地
extract vt.取出；榨取 n.摘录
extracting 选取
extraction n.抽出；提取法；摘要
extractor n. 拔取的人,抽出者,抽出器
extracurricular a.课外
extradite v. 引渡回国，拿获归案
extradition n. 引渡逃犯,将亡命者送还本国
extraneous adj. 外来的，无关的
extraordinarily ad.非常地，特别地
extraordinary a.非同寻常的，特别的
extrapolate v. 预测，推断，推知；推测
extravagance n. 奢侈,浪费,放肆的言行
extravagant a.奢侈的；过度的
extreme n.极端不同的性质
extremely ad.极端，极其，非常
extremist n.极端
extremity n. 极度，绝境
extricate v. 拯救，救出
extrinsic adj. 外在的，外部的
extrovert n. 性格外向者
extrude vt. 挤出,压出,逐出
exuberance n. 茂盛,健康,丰富
exuberant adj. 充满活力的,茂盛的
exude v. 使慢慢流出，四溢
exult v. 欢腾，喜悦
exultant adj. 愉悦的
exultation n. 狂喜,大悦,欢欣
eye n.眼睛；眼力；鉴赏力
eyeball n. 眼球
eyebrow n.眉毛
eye-exercises 眼保健操
eyeglass n. 眼镜
eyelash n. 睫毛
eyeless a. 盲目的
eyelet n. 小孔,孔眼,针眼,金属圈
eyelid n. 脸
eyesight n.视力
eyewitness 目击者
eyry n. 鹰巢,高处的房子,高处的城堡
Fabian a. 费边式的,拖延时间的,
fable n.寓言；虚构的故事
fabric n.织物，纺织品；结构
fabricate vt.制作，组合；捏造
fabrication n.制作，构成；捏造
fabulous adj. 难以置信的，寓言里的
facade n. 建筑物的正面，外表
face n.脸
faced adj. 脸的
faces 脸
facet n. 面；方面
facetious adj. 轻浮的，好开玩笑的
facial n. 美颜术,脸部按摩术
facile adj. 容易做的，肤浅的
facilitate vt. 促进；使容易；助长；使便利，有助于v. 使便利，使容易；帮助
facilities n. (使事情便利的)设备，工具
facility n.设备；容易；便利
facing n. 贴边,饰面
facsimile n. 复制本，摹本
fact n.事实；实际
faction n.派别，宗派，小集团
factious adj. 有派性的，偏见的
factitious adj. 人为的，不真实的
factor n.因素；因子，系数
factorage 代理业
factories 工厂
factoring 代理经营，代理融通；融资
factory n.工厂，制造厂
factotum n. 杂役，听差
factual a. 事实的，现实的；实际的，事实上的
facultative 任意的，临时的；临垢
faculty n.才能，能力；系，科
fad n. (流行一时的)狂热，时尚
faddish adj. 流行一时的，时尚的
fade vi.褪色；逐渐消失
faeces n. 粪；排泄物，渣滓
faery n. 仙子,仙境
fag v. 苦干n. 苦工
faggot n. 柴把,束薪
fagot n. 柴把,束薪
Fahrenheit n.华氏温度计
fail vi.失败
failing n. 失败,缺点,过失
failure n.失败；失败的人
fain adj. 欣然地；乐意地；ad. 宁愿；乐意的
faint adj.暗淡的；微弱的
faint-hearted a. 无勇气的,胆怯的
faintly ad. 微微地；不明显的；微弱地，软弱无力的
fair adj.(头发)金色的
fairly ad.相当；公平地
fairness n. 晴朗,光明正大,美丽
fairy adj.幻想中的，虚构的
fairyland n. 仙境
fait 证书，契据
faith n.信任，信心；信仰
faithful a.忠诚的；如实的
faithfully  adv. 忠诚地；诚恳地；忠实地
faithfulness n. 忠诚,诚实,正确
faithless a. 无信的,不忠实的
fake n.假货，膺品 a.假的
fakir n. 托钵僧，骗子
falchion n. 刀,剑
falcon n. 猎鹰
falconer n. 以鹰狩猎者,放鹰者,养鹰者
falconry n. 放鹰捕猎,养鹰术
fall n.&vi.落下；跌倒
fallacious adj. 欺骗的，谬误的
fallacy n. 谬误，错误
fallen fall 的过去分词；落下
fallible adj. 会犯错的，易犯错的
fallow n./adj. 休闲地，休闲的
false a.不真实的；伪造的
falsehood n. 谎言,虚假
falseness n. 虚伪,不正确,不忠实
falsification n. 窜改
falsify v. 窜改，说谎
falsity n. 虚伪,错误
falter vt. 支吾地说,迟疑
fame n.名声，名望
famed a. 著名的
familiar a.熟悉的；冒昧的
familiarity n. 精通，亲近，不拘礼仪
familiarize vt. 使熟悉,使熟知,使通俗化
family n.家，家庭
famine n.饥荒；严重的缺乏
famish v. 使饥饿
famished adj. 极饥饿的；非常饥饿的
famous adj.著名的
fan n.扇子
fanatic adj. 狂热的，盲信的n. 狂热者
fanatical a. 狂热的；入迷的
fanaticism n. 狂热盲信
fancied adj. 想象的；幻想的
fancier n. 爱好者
fanciful a. 奇怪的,稀奇的,想像的
fancy n.想象力；设想；爱好
fane n. 寺院,神庙
fanfare n. 夸耀，嘹亮的喇叭声
fang n. (毒蛇的)尖牙
fantasia n. 幻想曲，组合乐曲
fantastic a.空想的；奇异的
fantastical a. 幻想的，异想天开的(fantastical=fantastic)；奇异的，怪诞的
fantasy n. 幻想,白日梦
far adj.远的 adv.远地
faraday 法拉第
faraway adj. 遥远的；(时间等)遥远的；心不在焉的；adv. 遥远的
far-away a. 遥远的
farce n. 闹剧，胡闹
fare n.车费，船费，票价
farewell int.再会 n.告别
far-flung a.漫长的；辽阔的；遥远的
farm n.农场
farmer n.农民，农夫；农场主
farmhand n. 长工，雇工；农工，农场工人；农业工人
farmhouse n.农舍
farming n. 农事；耕作；农业，种植业；耕作；n. & a. 农业(的)
farmland n.农田
farmstead n. 农场及其建筑物
farmyard n. 农家庭院
far-off a. 遥远的,久隔的
farrago n. 混杂物；杂烩
far-reaching adj. 影响深远的
farrier n. 蹄铁匠,马医
farrow v. (母猪)生产n. 一窝小猪
far-sighted a. 远视的
farsightedness n. 远视眼
farther ad.更远地 a.更远的
farthest adj. 最远的；ad. 最远地
farthing n. 1/4便士,英国最小的钱币
fascia n. 饰带，(商店上挂的)招牌
fascinate vt.迷住 vi.迷人
fascinating  adj.迷人，使神魂颠倒的；迷人的；吸引人的；醉人的
fascinatingly ad. 迷人地
fascination n.强烈的爱好；迷惑
fascism n. 法西斯
fascist n. 法西斯分子；法西斯主义者
fashion n.样子，方式；风尚
fashionable a.流行的，时髦的
fast adv.快地 adj.快的
fastback n. 快速返回
fasten vt.&vi.扎牢；扣住
fastener n.扣件，钮扣，揿钮
fastening n. (门等)扣绊，拴扣物
faster 更快
fastidious adj. 难取悦的，挑剔的
fastness n. 要塞，城堡，坚固
fat adj.肥胖的
fatal a.致命的；命运的
fatalism n. 宿命论
fatality n. 宿命，致命性
fate n.命运，天数
fateful a. 宿命的,重大的,决定性的
father n.父亲
fatherhood n. 父亲的身分,父道
father-in-law n.岳父；公公
fatherland n. 祖国
fatherless a. 无父的
fatherly a. 父亲的,如父亲的,慈爱的
fathom n. 英寸（量水深，等于1.8米）v. 彻底明白，了解
fathomless adj. 深不可测的
fatigue n.疲劳，劳累
fatness n. 肥胖,油腻,肥沃
fatten vi. 养肥
fatty a. 脂肪的,含脂肪的,脂肪状的
fatuity n. 愚蠢，愚昧
fatuous adj. 愚昧而不自知的
faucet n. 水龙头
fault n.缺点；过失；故障
faultless a.无过失的；无缺点的
faulty a.有错误的，有缺点的
faun n. 半人半羊的农牧神
fauna n. 动物区系
favor n.好意；帮助；恩惠
favorable a. 称赞的
favorably adv. 有利地，顺利地
favored a.受到喜爱的；爱到优待的
favorite adj.最喜爱的(人或物)
favoritism n. 偏爱,不公平,偏袒
favour n.好感；赞同；恩惠
favourable a.有利的；赞成的
favourably ad. 有利地；善意地
favoured a. 受到偏爱的；有利的，喜爱的
favourite a.特别受喜爱的
fawn n. 未满周岁的小鹿，v. 巴结，奉承
fawning adj. 奉承的；乞怜的
fax n. 传真
fay n. 小仙子
fealty n. 效忠
fear n.害怕；担心 vt.害怕
fearful a.害怕的，可怕的
fearfully adv. 胆怯地
fearless adj. 不怕的，无畏的；大胆的；毫不畏惧的
feasibility n. 可行性；现实性；可行，可用
feasible a.可行的；可能的
feast n.盛宴，筵席；节日
feat n. 功绩，壮举
feather n.羽毛；翎毛；羽状物
featherbedding 额外雇工
feathered a. 有羽毛的；羽状的
feathery a. 羽状的
feature n.特征，特色；面貌
feb. (同)february，二月
febrile adj. 发烧的，热病的
February n.二月
feckless adj. 无目标无计划的；无气力的；无益的
fecund adj. 肥沃的，多产的
fecundity n. 多产,丰饶,肥沃
fed feed的过去式(分词)
federal a.联邦的；联盟的
federalist n. 联邦主义者
federate v. 结成同盟
federation n. 联邦,联合,联盟
fee n.费，酬金；赏金
feeble a.虚弱的；微弱的
feebleminded a. 精神薄弱的,低能的,意志薄弱的
feebleness n. 弱,微弱
feebly ad. 虚弱地；贫乏地
feed vt.喂(养) vi.吃饲料
feed...to 把…喂给
feedback n. 回授，反馈，反应；(信息的)反馈；反债
feeder n. 饲养者,供给者,奶瓶
feel vi.有知觉 vt.触，摸
feeler n.触角
feeling n.感情；感觉，知觉
feelings n. 感情
feet n. foot的复数；足，英尺；脚；(脚)的复数
feign v. 假装，伪装
feigned adj. 假装的，不真诚的
feint n./v. 佯攻，佯击
feldspar 长石
felicitate v. 祝贺，庆贺
felicitous adj. （话语等）适当的，得体的
felicity n. 幸福，适当的措辞
feline adj. 猫科的
fell vt.砍倒(树等)；砍伐
felloe n.(车轮外围之) 轮圈; 轮网
fellow n.人，家伙；伙伴
fellow-actor n. (唱戏时的)搭档
fellow-citizen n. 住在同一城市的人
fellow-guest n. 一同作客的人
fellowship n.伙伴关系；联谊会
felon n. 重罪犯
felonious adj. 罪恶的，凶恶的，重罪（犯）的
felony n. 重罪
felt n. 毛毯,毡
female n.雌性的动物；女子
feminine a.女性的；女子气的
feminist n. 女权运动者
femur n. 大腿骨,腿节
fen n. 沼泽,沼池
fence n.栅栏
fencer n. 剑客击，剑者
fencing n. 剑术，击剑法
fend vt. 挡开(与off连用)；保护，供给，抚养
fender n. 挡泥板，护舷的垫子等
fennel n. 茴香
feral adj. 野生的，凶猛的
ferment n./v. 使发酵，骚动
fermentation n. 发酵
fern n. 羊齿植物，蕨
ferocious adj. 凶猛的，残暴的
ferocity n. 凶猛，残暴
ferret n. 雪貂，v. 搜寻
ferrous  adj.铁的；亚铁的；含铁的
ferrule n. 金属手杖等的,金属环,套圈
ferrum n. 铁
ferry n.渡船；渡口 vt.运送
ferryboat n. 渡船
fertile a.肥沃的；多产的
fertility n. 肥沃，丰饶
fertilization n. 使肥沃,土地肥沃法,施肥
fertilize vt. 使受精
fertilizer n.肥料
ferule n.教鞭,戒尺
fervent adj. 热的，热烈的
fervently ad. 热情地；火热地，热烈地
fervid a. 热的,热心的
fervor n. 热诚，热心
fervour n.热烈，热情
festal adj. 节日的，欢乐的
fester vi. 溃烂,生脓,生脓
festival n.节日；音乐节
festive adj. 欢乐的
festivity n. 欢宴,欢庆
festoon n. 花彩
fetch vt.拿来；请来，接去
fete n. 庆祝,祭祀,节日
fetid adj. （水等）有恶臭的
fetish n. （崇拜的）神物
fetlock n. 丛毛,球节
fetter n. 脚镣，束缚
fettered adj. 被拘束的，没自由的
fettle n. 状态,情绪
fetus n. 胎儿
feud n. 宿怨，不和
feudal a. 封建制度的,封地的,领地的
feudalism n. 封建制度
feudatory a. 受有封地的,封地的,封臣的
fever n.发热，发烧；狂热
feverish adj.发烧的
few a.很少的；少数的
fewer a. 为数更少的
fewness n. 少,少数
fez n. 土耳其毯帽
fiance n. 未婚夫
fiancee n.未婚
fiasco n. 大失败，惨败
fiat n. 命令，决断
fib n. 小谎,一击,打
fiber n. 纤维
fibre n.纤维，纤维质
fibrin n. 纤维素,敷质
fibroma n. 纤维瘤
fibrous a. 纤维的,纤维性的
fickle adj. （爱情或友谊上）易变的，不坚定的
fickleness n. 易变
fiction n.小说；虚构，杜撰
fictional adj. 虚构的
fictitious adj. 假的、虚构的
fiddle n. 小提琴
fiddler n. 拉提琴,蟹的一种
fidelity n. 忠实，忠诚
fidget v. 坐立不安n. 烦躁之人
fidgety adj. 烦躁的，不安的.
fiducial 信托的，信用的
fiduciary a. 基于信用的,信托的,受信托的
fie int. 咄!呸!
fief n. 封地，活动范围
field n.地，田地
field-glasses 小型双筒望远镜
fiend n. 恶魔，魔鬼
fiendish adj. 极凶恶的
fierce a.凶猛的，狂热的
fiercely ad. 猛烈地；凶猛地，残忍地
fierceness n.凶猛，猛烈
fiery a. 炽热的,热烈的,暴躁的
fife n. 横笛,吹横笛
fifteen num.十五；十五个
fifteenth a. 第十五的,15
fifth num.第五 n.五分之一
fiftieth num.第五十(个)
fifty num.五十，五十个
fig n. 无花果，一点儿.
fight vi.&vt.打仗(架)
fighter n.战士
fightful adv. 可怕的，令人恐怖的
fighting a. 战斗的
figment n. 虚构的东西
figuration n. 定形，外形，轮廓
figurative adj. 比喻的，借喻的
figure n.数字；外形；人物
figurehead n. 名义领袖
figurine n. 小塑像，小雕像
filament n.细丝；长丝；灯丝
filbert n. 榛树,榛子
filch v. 偷（不贵重的东西）
file n.档案 vt.把…归档
filename n. 文件名
filet n. (网格状的) 花边
filial "piety	n. 孝心"
filibuster v. & n. 妨碍议事，阻挠
filigree n. 金银丝做的工艺品
filing n. 档案管理；(文件的)整理汇集
filings n. 锉屑
filipino n. 菲律宾人；a. 菲律宾人的
fill vt.装满，盛满；占满
fill...with 把…装满
fill...with... 把…装满…
filled adj. 充满的
filler n. 补白,装填物
fillet n. 头带,带子
filling n. 充填物,填料,填土
fillip n. 弹指,刺激
filly n. 小雌马,小姑娘
film n.电影
film-goer n. 电影爱好者
filmmaking n.制片
filmy a. 朦胧的；薄膜似的
filter vt.过滤 n.滤纸
filterable a. 可滤过的，可滤的
filth n.污秽，污物；淫猥
filthy adj. 龌龊的，污秽的
filtrate v.过
filtration n. 过滤,筛选
fin n. 鳍
finable adj. 应罚款的
final a.最后的；决定性的
finale n. 终曲，乐曲的最后部分
finality n. 最后,定局,终结
finalize v. 落实，定下来；定妥
finally ad.最后；不可更改的
finance vt.提供资金
financial a.财政的，金融的
financially ad. 经济上；在金融方面
financier n. 财政家,金融家
financing n. 金融业，财政学；金融为列车长，筹资，提供资金
finch n. 雀科鸣禽（如燕雀，金丝雀等）
find v.找到；发现
finder n. 发现者，探测器
finding n. 发现；调查的结果；发现物；判断；结果；(pl.)调查(或研究的)结果
fine adj.好的 adv.很好,妙
finely ad. 精细地，美好地
fineness n. 出色; 优良; 优秀
finesse n. 技巧、计谋、手段
finger n.手指
fingernail n. 指甲
fingerprint n. 手指印
finicky adj. 苛求的，过份讲究的
finish vt.完成，结束 n.结束
finished adj. 制成的；结束的；精致的；完成的
finisher n. 成品机
finite a.有限的；有尽的
finland n. 芬兰
finnish n. 芬兰语；a. 芬兰的
finny a. 有鳍的,鳍状的,鱼族的
fiord n.峡湾
fir n. 枞树,杉木
fire n.火；火灾 vi.开火
firealarm n.火警
firearm n. 火器,枪炮
fireball n. 火球,大流星,太阳
firebrand n. 火把,在燃烧的木柴,放火者
fire-brigade n. 消防队
firecracker n. 爆竹,鞭炮
fire-engine n. 消防车
fire-extinguisher n. 灭火器
firefighter n. 消防人员
firefly n. 萤火虫
fireless a. 没有火焰的
firelight n. 火光
fireman n.消防队员；司炉工
firemen n. 消防队员们
fireplace n.壁炉
fireproof a. 耐火的,防火的
fireside n. 炉边,家庭,一家团圆
firewood n. 木柴
firework n. 爆竹，花炮，烟火；焰火；(pl.)烟花，礼花
fireworks n. 烟火,激烈争论
firm n.商行，商号，公司
firmament n. 苍穹，天空
firman n. 昔时土耳其皇帝等的勒令
firmly adv. 紧紧地；坚定地；牢牢地；坚固地；稳定地；牢固地，断然地，固定地
firmness n.坚固，坚定，稳固
first num.第一
firstborn a. & n. 头生的(子女)
first-born n. 头踏
first-class a. 最好的,第一流的,优秀的
firstling n. 首批东西,初生物
first-rate a.第一流的，优秀的
firth n. 峡湾,河口
fiscal adj. 公款的，财政的
fish n.鱼肉；鱼
fishbowl n. 玻璃鱼缸
fisher n. 渔夫,食鱼动物,渔船
fisherman n.渔夫
fishery n. 渔场
fish-hook n. 鱼钩
fishing n. 钓鱼，捕鱼；渔场；渔业
fishing-boat n. 渔船
fissile adj. 易分裂的
fission n. 裂变；裂开；分裂生殖；分裂；(核)裂变
fissure n. 裂缝，裂隙
fist n.拳(头)
fistula n. 管,瘘管
fit vt.&vi.适合，合身
fit...into 使…适应于
fitch n. 臭猫,臭猫皮,臭猫毛
fitful adj. 不安的
fitness n.适当，恰当；健康
fitted a.按照实物尺寸做的；(大小)合适的
fitting  n. 配合；试衣；装备；(pl. )配件adj. 适当的；适合的，恰当的
five num.五
fives n. (sing.)一种墙手球
five-star adj. 第一流的，最高级的
fix vt.使固定；决定
fixation n. 定置,固定,定色
fixed  adj.坚决的；固定的，已确定的；确定了的；不变的
fixedly adv. 固定地；不变地
fixer 中间拉线人；n. 固定器，定影剂，维修工
fixing 定影
fixture n.固定；定期存款
fizzle n. 咝咝声，失败
fizzy a.起泡的；发嘶嘶声的
fjord n. 峡湾
flabby adj. （肌肉）松软的，意志薄弱的
flaccid adj. 松驰的，软弱的
flag n.旗
flagellate v. 鞭打，鞭笞
flagging n. 铺砌石板,铺石材料,石板路
flaggy adj. 枯萎的，松软无力的
flagitious a. 极恶的,残忍的,凶恶的
flagman n. 旗手,信号旗手,平交道看守
flagon n. 酒壶
flagpole n. 旗竿
flagrant adj. 臭的，恶名昭彰的
flagship n. 旗舰
flail n. 连枷（打谷工具）v. 打，打击
flair n. 天赋，本领，才华
flak n. 高射炮，指责
flake n.片，薄片；肌膈
flaky a. 薄片的,成片的,薄而易剥落的
flamboyance n. 艳丽，炫耀
flamboyant adj. 艳丽的，炫耀的
flame vi.发火焰 vt.点燃
flaming a. 熊熊燃烧的；热情的
flamingo n. 红鹤,火鹤
flammable adj. 易燃的
flange n. （火车车轮的）凸缘，轮缘
flank n.肋，肋腹；侧面
flannel n.法兰绒；法兰绒衣服
flannelette n.  (内衣用的) 棉织法兰绒
flap vt.&n.拍打 vi.拍动
flare vi.闪耀 vt.使闪亮
flaring adj. 火焰摇曳的，过份艳丽的
flash vi.(火焰等)一闪,闪亮
flashing n. & a. 闪光的，闪烁的
flashlight n.手电筒
flash-locks n. 闸门
flashy a. 闪光的,一瞬间的,浮华的
flask n.瓶；火药筒；砂箱
flat a.平的，扁平的
flatboat n. 平底船
flat-bottomed  adj. <船>平底的
flatcar n. 平台型铁路货车
flation 物价稳定
flatly ad. 平淡地；断然地
flatten vt.把…弄平；击倒
flatter vt.阿谀,奉承；使满意
flatterer n. 拍马屁的人,阿谀者,谄媚者
flattering a. 谄媚的；奉承的
flattery n. 谄媚,阿谀,巴结
flatulence n. 肠胃气胀
flaunt v. 炫耀，张扬
flavor n. 滋味,香料
flavour n.味，味道；风味
flavouring n. 香料，调味品
flaw n.缺点，瑕疵；裂隙
flawless adj. 完美的，无瑕疵的
flax n. 亚麻
flaxen a. 亚麻的,亚麻色的,淡黄色的
flay v. 剥皮，诈取，严厉指责
flea n. 跳蚤
flea-ridden a. 充满跳蚤的
fleck n. 斑点，微粒
flection n. 弯曲；词尾变化
fled flee的过去式(分词)
fledged adj. 羽毛长成的，成熟的
fledgling n. 刚学飞的幼鸟，无经验的人
flee vi.逃起 vt.避开
fleece n. 生羊皮，羊毛
fleecy a. 以羊毛盖上的,羊毛似的,蓬松的
fleet n.舰队；船队；车队
fleeting adj. 短暂的，飞逝的
fleetness n. 快速,无常
flesh n.肉；肉体
fleshly a. 肉体的,肉欲的,耽于声色的
fleshy a. 肉的,肉体的,丰满的
flew fly的过去式；飞
flex v. 屈曲(四肢)；流动；弯曲
flexibility n. 灵活性
flexible a.易弯曲的；灵活的
flick n./v. 轻打，轻弹
flicker v. 闪烁，摇曳
flier n. 飞行者,快船,快车
flight n.航班；飞行；逃跑
flighty adj. 轻浮的，反复无常的
flimsy adj. 轻而薄的，脆弱的
flinch v. 畏缩，退缩
fling vi.&vt.(用力)扔，抛
flint n. 打火石，燧石
flinty adj. 极坚硬的
flip vt. 掷,弹,轻击,空翻
flip-flop n. 正反器
flippancy n. 无礼，言语尖刻
flippant adj.无礼的，轻率的
flirt v. 不认真考虑，调戏，挑逗
flirtation n. 调情,挑逗,调戏
flirtatious adj. 调情的
flit v. 掠过，迅速飞过
flitch n. 腌的猪肋肉,大比目鱼的肉片,
float vi.漂浮 vt.使漂浮
floating a. 浮在水上的；浮动的，浮点的；流动；发行
flock n.羊群，群；大量
floe n. 大浮冰
flog vt. 鞭打,鞭策,迫使
flood n.洪水 vt.淹没
floodgate n. 水门,水闸,防潮水闸
flooding n. 洪水泛滥；泛滥
floor n.地板；楼层
floorboards n. (pl.)地板
flooring n. 地板,地板材料,铺地板
floorwalker n.巡视员
flop n. 砰然落下,拍击声,失败
floppy n. 软磁盘；adj. 松软的，衰弱的
flora n. （某地区或时代的）植物群
floral a. 花似的,花的,植物的
florence  n.佛罗伦萨(意大利城市)
florentine n. 佛罗伦萨人
florid adj. 华丽的，（脸）红润的
florida 佛罗里达(美国州名)
florin n. 一种货币
florist n. 花商，种花者
floss n. 丝棉,乱丝
flotilla n. 小舰队,小型船队
flotsam n. 浮货,废料,零碎
flounce n. 衣裙上的荷边装饰,挣扎,挣脱
flounder v. 挣扎，艰苦地移动
flour n.面粉，粉；粉状物质
flourish vi.繁荣，茂盛，兴旺
flout v. 蔑视，违抗
flow vi.流，流动
flowchart 流程图
flower n.花，花卉；开花
floweret n. 小花
flowerpot n. 花盆,花钵
flowery a. 多花的,绚丽的,华丽的
flowline 流水线
flown a. 刚出巢的；fly的过去分词；飞
flu n.流行性感冒
fluctuate vi.波动 vt.使波动
fluctuation n.波动；脉动；踌躇
flue n. 烟洞,烟道,蓬松的东西,渔网,
fluency n. 流畅,雄辩,善辩
fluent a.流利的，流畅的
fluff n. 软毛,柔毛,无价值的东西,错误,
fluffy adj. 有绒毛的，空洞的
fluid n.流体，液体
fluke n. 侥幸，偶然的机会
flume n. 水槽,水道
flung fling的过去式(分词)
flunk v. 考试不及格
fluorescence n.荧光；发荧
fluorescent adj. 荧光性的；萤光的，发光的
fluoroscopy n. 荧光检查；荧光学
flurry n. 疾风,飓风,慌张
flush n.兴奋，脸红；发烧
fluster v. 使困惑，慌乱
flute n. 笛子
fluted a. 笛声的,有凹槽的
flutter vi.(鸟)振翼；飘动
flux n.流；涨潮；流量
fly v.飞跑，逃跑，消失
flyer n. 飞鸟,飞行物,飞行员,飞跳,传单,
flyover n.公路上的陆桥
flywheel n. 调速轮
foal n. 驹
foam n.泡沫；泡沫塑料
foamy a. 全是泡沫的,起泡沫的,泡沫的
fob n. 表袋,短表链
focal a. 焦点的,在焦点上的
focus vi.聚焦，注视 n.焦点
focus...on 使眼睛注视，集中
fodder n. 草料
foe n. 仇敌,反对者,敌人
foeman n. 敌兵,敌人
foetid a.恶臭的
foetus n. 胎儿
fog n.雾
foggy adj.多雾的；模糊的
foghorn n. 雾角
fogy n. 守旧者,赶不上时代的人
foible n. 小缺点，小毛病
foil n. 钝剑，箔，锡箔纸
foist vt. 偷偷插入,使混入,硬卖给
fold vt.折叠；合拢 n.褶
folder n. 折叠人,折纸机,折叠式书本,
foliage n. 叶子（总称）
folio n. 对开的纸,页码或张数,(原稿的)一页
folk n.人们，家属，亲属
folklore n. 民俗学，民间传说
follicle n. 小囊,滤泡,骨突
follow vt.跟随;(时间等)接着
follower n.追随者；信徒
follow-evaluation 追踪考察
following adj. 接着的；以下的；下列的；其次的；在…以后n. 下一个
follow-up n. & adj. 后续(的)；接着的
folly n. 愚蠢
foment v. 煽动，助长（坏事）
fomentation n. 煽动，助长
fond adj.喜爱的；爱好的
fondle v. 抚弄，抚摸
fondly ad. 喜爱地；愚蠢地
fondness n.慈爱; 溺爱
font n. 字体,字形,洗礼盘,泉
food n.食物
foodstuff n. 食料，食品
fool vi.&vt.愚弄，欺骗
foolery n. 愚蠢的行为,愚事,愚蠢
foolhardy adj. 鲁莽的，有勇无谋的
foolish adj.愚蠢的，傻的
foolishly adv. 愚蠢地；荒谬地
foolishness n.愚蠢
foolproof adj. 错不了的，容易懂的
foolscap  n.大页书写纸
foot n. 足；脚；英尺；最下部；底部
football n.足球比赛；足球
footbrake n. 脚闸
footfall n. 脚声,踏步,脚步
foothold n. 立足点，根据地
footing n. 立足点,立场,关系
footle v. 胡闹，浪费(时间)
footloose adj. 自由自在的，无拘束的
footman n. 马夫,马丁,仆役
footmark n. 脚印，足迹
footnote n. (书中的)脚注；vt. 为…作脚注
foot-note 脚注，附注
footpath n.小路，人行道
footprint n.脚印，足迹
footsore a. 伤了脚的
footstep n.脚步；脚步声；足迹
footstool n. 脚台
fop n. （喜好精致服装的）花花公子.
foppery n. 打扮,矫饰,纨绔习气
foppish adj. 浮华的，俗丽的
for prep.为
for...sake 为了…的缘故(之好处)
forage n. （牛马的）饲料，粮草v. 搜寻，翻寻
forager n. 为动物寻找饲料的人
foray n./v. 突袭，偷袭
forbade forbid的过去式
forbear vt.vi. 忍耐,克制,容忍
forbearance n. 自制，忍耐
forbearing adj. 忍耐的，宽容的
forbid vt.禁止；不许
forbidden a. 被禁止的,严禁的
forbidding  adj.令人生畏的；(表情)冷峻的，形势险恶的
forcast vt./n.预测，预报
force vt.强迫，迫使
forced a. 强制的，强迫的；压力的
forceful a. 有力的,强烈的
forceps n. （医用）钳子，镊子
forces n. 军队
forcible a. 强制的,强迫的,有气力的
forcibly ad. 强行地，强烈地
ford n. 浅滩，水浅可涉处v. 涉水
fore ad.在前面 a.先前的
forearm n. 前臂
foreat n. 森林
forebode v. 预兆，凶兆
foreboding n. 预感，预兆
forecast n.预测，预报 vt.预示
forecaster n.气象预测员
forecastle n. 前甲板,前甲板下面的水手舱,
foreclose v. 排除，取消抵押品的赎回权
foreclosure 取消抵押品赎权
foredate 倒填日期
foredoom vt. 预定命运,注定
forefather n. (常用复数)祖先
forefathers n. 祖先
forefinger n. 食指
forefoot n. 前脚,龙骨的前端部
forefront n. 最前部,最前线
foregift 押租，定金
forego vt. 放弃,在...之前,居先
foregoing adj. 先行的，上述的；在前的，前述的
foregone a. 先前的,过去的,已知的
foreground n. 前景,最显著的位置
forehand n. 马体的前部,正打,正击
forehead n.额头，前部
foreign adj. 外国的；外来的；无关的；对外的；外国来的；(to)使联系的；异质的，陌生的
foreigner n.外国人
foreknow vt. 预知,预见
foreknowledge n. 预知,先见之明
foreland n. 沿海地区,海角,海岸地
foreleg n.(前物的)前腿
forelock n. 额发,额毛,栓,销
foreman n. 领班,工头,陪审长
foremost a.最初的；第一流的
forenoon n. 午前,上午
forensic adj. 法庭的，辩论的
forepart n. 前部,最前部
forerun vt. 预告,预报,预示,走在...之前
forerunner n. 预兆，前兆，先驱.
foresee vt.预见，预知，看穿
foreseen foresee的过去分词
foreshadow vt. 成为前兆,暗示,预示
foreshorten vt. 照远近法画,缩小深度而画
foreshow vt. 预示
foresight n. 远见
foreskin  n.  (阴茎的) 包皮
forest n.森林
forestall v. 先发制人，预先阻止
forester n.林务员
forestry n. 林产,森林地
foretaste v. 预示，迹象，先尝试
foretell vt. 预言；预告v. 预告，预言
forethought n. 考虑将来,深虑,先见
foretold foretell过去式(分词)
forever ad.永远，总是，老是
forewarm v.预先警
forewarn vt. 预先警告
forfeit v. 丧失，没收，n. 丧失物
forfeiture n. （名誉等）丧失
forge vt.打(铁等)，锻造
forger n. 伪造者，打铁匠
forgery n. 伪造（物）
forget vt.忘记，遗忘
forgetful a. 健忘的,易忘的
forgetfulness n.健忘症; 忘却
forget-me-not 勿忘草；勿忘我
forging n. 锻件；锻造(法)
forgive vt.原谅，饶恕，宽恕
forgiven forgive的过去分词
forgiveness n. 宽恕,宽仁之心
forgo v. 放弃，抛弃
forgot forget的过去式；忘记
forgotten forget 的过去分词；忘记
fork n.叉；餐叉
forlorn adj. 孤独的，凄凉的
form vt.(使)组成，建立
formal a.正式的；礼仪上的
formaldehyde n. 甲醛,蚁醛
formalin n. 福尔马林
formalism n. 拘泥形式,形式主义,虚礼
formality n. 礼节,程序,拘谨,正式手续
formally ad. 形式地，正式地；adj. 正式的
format n. 格式，样式；形式；版式，(计算机的)格式，编排；vt. 设计，(计算机上)将…格式化
formation n.形成；构成；形成物
formative adj. 形成的，影响发展的
formatted a. 有格式的
formatting n. 格式化
form-blind a. 形盲的
formed a. & n. 成形；(血液)有形成分
former a.在前的 n.前者
formerly ad.以前，从前
formidable a.可怕的；难对付的
formless a. 无定形的,形体不明的,没有形状的
formula n.公式，式
formulary n. 公式集,处方一览表,定式
formulate vt.用公式表示
formulation n.明确的表达
fornication n. 通奸,通奸,乱伦
forrign adj. 外国的
forsake vt.遗弃，抛弃，摒绝
forsaken forsake的过去分词
forsook forsake的过去式
forsooth ad. 实在,的确,真的
forswear v. 誓绝，放弃
fort n.要塞，堡垒
forte n. 长处，擅长，adj. （音乐）强音的
forth ad.向前；向外，往外
forthcoming a.即将到来的；现有的
forthwith ad. 立刻,不犹豫地,不延迟地
fortieth a. 第四十的,第四十个的,四十分之一的
fortification n. 防御工事,要塞,筑城
fortify vt. 增强
fortitude n. 坚毅，坚忍不拨
fortnight n.两星期，十四天
fortran 公式翻译程序
fortress n.堡垒，要塞
fortuitous adj. 偶然的，意外的
fortuity n. 偶然事件
fortunate a.幸运的，侥幸的
fortunately adv. 幸亏；幸运地；幸而；幸好
fortune n.命运，运气；财产
fortune-teller n. 占卜者，算命先生
forty num.四十，第四十
forty-two n. 四十二
forum n.论坛，讨论会
forward adv.向前，前进
forwarder 代运人，转运公司，运输代理
forwarding 发运的
forwardness n. 大胆，鲁莽
forwards ad，向前
fosse n. 护城河
fossil n.化石 a.化石的
foster vt.养育，抚养；培养
fought fight的过去式(分词)；战斗
foul a.肮脏的；丑恶的
foulard n. 一种薄软的绸,用该布制的手帕
found vt.创立，创办；建立
foundation n.地基
founder n.创立者，奠基者
foundry n. 铸造,铸造场,铸造类
fount n. 泉,墨水缸
fountain n.泉水，喷泉；源泉
fountainhead n. 水源,源,本源
four num.四
four-poster n. 有四柱的床
fourscore a. 八十的,八十个的
foursquare a. 正方形的,直爽的,坚定的
fourteen num.十四
fourteenth num. 第十四
fourth num.第四 n.第四日
fowl n.家禽；禽肉
fowler n. 捕鸟者
fox n.狐狸
foxglove n. 指顶花
foyer n. 门厅，休息室
fracas n. 喧嚷，吵闹
fraction n.小部分；片断；分数
fractional adj. 微小的，极小的
fractious adj. （脾气）易怒的，好争吵的
fracture n.破裂；裂痕 vi.破裂
fragile a.脆的；体质弱的
fragility n. 易碎，脆性
fragment n.碎片，破片，碎块
fragmentary adj. 零碎的，不完整的
fragrance n. 香味
fragrant a.香的，芬芳的
frail a.脆弱的；意志薄弱的
frailty n. 脆弱，弱点
frame n.框架，框子；构架
framed a. 遭到陷害的
frame-up n. 陷害，虚构的罪名
framework n.框架，构架，结构
franc n. 法郎(法国货币单位)
France n.法国
franchise n. 公民权,特权,免赔额
franchisee n.特许经营权
franchiser n.给别人经营联营特许权的公司或制造厂
franchising 出卖产销权
Franciscan a. St.Francis 的,圣芳济修会的
francisco n. 弗朗西斯科(男名)
frank a.坦白的，直率的
frankincense n. 乳香
frankly  adv.坦率地说；坦率地；直率地；慷慨地
frankness n. 率直,坦白
frantic adj. 疯狂的，狂乱的
frantically ad. 狂乱地；狂暴地，疯狂地
franz 弗朗兹(人名)
fraternal adj. 兄弟的，友善的
fraternity n. 同行，友爱
fraternize vi. 结有深交,友善
frau n. (德)太太，夫人
fraud n. 欺诈，欺骗，骗子
fraudulent adj. 欺骗的，不诚实的
fraught adj. 充满
fray n. 吵架，打斗v. 磨破，恼火
freak n. 怪物，奇事adj. 反常的，奇特的
freakish a. 朝三暮四的,见异思迁的,珍奇的
freckle n. 雀斑，斑点
freckled a. 有雀斑的，有斑点的
free a.自由的；空闲的
freebooter n. 海盗
freedman n. 自由民,被解放的奴隶
freedom n.自由；自主
freedom-loving adj. 热爱自由的
freelancer n.自由职业者
freely ad.自由地；直率地
freeman n. 自由民,公民,正会员
Freemason n. 互济会会员
freesia 鸢尾科之植物
freeway n. 高速公路
freeze vi.冻；结冻vt.使结冰
freezer n. 冰库,冰箱,冷冻库
freezing adj. 极冷的，冻结的；迸发结的
freight n.货运；货物；运费
freighter 货轮；托运人，承运人
freight-in 运入运费，进货运费
freight-out 运出运费，销货运费
French a.法国的 n.法国人
Frenchman n.法国人
frenetic adj. 狂乱的，发狂的
frenzied a. 狂热的,狂乱的,激怒的
frenzy n. 狂暴,狂怒
frequency n.屡次；次数；频率
frequent a.时常发生的；经常的
frequently ad.时常，常常
fresco n. 壁画
fresh adj.新鲜的
freshen vt.使显得新鲜
freshet n. (流入海中的淡水) 河流
fresh-faced adj. 面带稚气的
freshly ad. 新近，刚才
freshman n.新生,一年级学生
freshness n. 新,新鲜,精神饱满
freshwater n. 淡水
fret vt.&vi.(使)烦恼
fretful adj. 烦躁的
fretwork n. 格子细工（在木头上雕出各种图案，格子的工艺）
friable adj. 易碎的
friar n. 修道士
fricassee n. 烧鸡肉或小牛肉成肉丁浇汁者
friction n.擦热皮肤
Friday n.星期五
fridge n. 电冰箱
fried adj. 油煎的；油炸的
friend n.朋友
friendless a. 没有朋友的,无依无靠的
friendliness n. 友谊,亲切,亲密
friendly adj.友好的
friendship n.友谊，友好
frieze n. （在墙顶与天花板间起装饰作用的）横条，饰带
frigate n. 护航舰，大型驱逐舰
fright n.惊吓，恐怖
frighten vt.吓唬
frightened adj. 受惊的，害怕的；受惊吓的
frightening adj. 令人害怕的
frightful adj. 可怕的；丑的；讨厌的；不愉快的；令人恐怖的
frightfully ad. 可怕地；非常
frigid a. 死板的；呆板的，寒冷的
frigidity n. 寒冷，冷淡，性冷淡
frill n. 衣饰上的皱边,皱边纸饰
fringe n.穗，毛边；边缘
frippery n. 低俗，俗艳
frisbee n. 飞盘(塑料玩具)
frisk n./v. 蹦跳，娱乐
frisky adj. 活泼的，快活的
fritter vt. 浪费,细切,剁碎
fritz n. 德国佬
frivolity n. 轻浮
frivolous adj. 轻泛的，轻佻的
frizzle n. 卷发,卷毛,吱吱响声
fro ad. 往，去，回，向后；向那边；(to and fro)来来回回地；adj. 回，离开
frock n.(女)上衣，罩衫
frog n.蛙
frolic n./v. 嬉戏，雀跃.
frolicsome adj. 快活的，欢乐的
from prep.从；从...起；由
from...to... 从…到…
frond n. （羊齿（fern），棕榈等的）叶子
front a.前面的 n.前部
frontage n. 房子的正面,朝向
frontal a. 前面的,正面的,额的
frontier n.边境；边疆；新领域
frontiersman  n. 边疆居民,边境的开拓者
frontispiece n.主立面；(书籍的)卷首插画
frontlet n. 附于额前之物
frost n.冰冻，严寒；霜
frosty a. 下霜的,严寒的,冷淡的
froth n. 泡,泡沫,琐物
froward a. 顽固的,固执的,刚愎的
frown vi.皱眉，蹙额
frowzy adj. 不整洁的，污秽的
froze freeze的过去式；冻结
frozen freeze的过去分词；a. 冷冻的；冻结
fructify v. 结果实，成功
frugal a. 节俭的,朴素的
frugality n. 节约，节俭
fruit n.水果
fruitage n. 果实,水果,结果实
fruiterer n. 水果商
fruitful a.多产的；肥沃的
fruition n. 结果实,成就,实现
fruitless a. 无结果的
frustrate vt.挫败；使无效
frustration n. 打破,挫折,顿挫
fry vt.油煎，油炸，油炒
frying 煎的
frying-pan n. 长柄平锅，煎锅
fuchsia n. 晚樱科植物
fuddle vt. 灌醉,使烂醉,使迷糊
fuddled 醉的
fudge n. 梦话,胡话,纸中另版插印记事
fuel n.燃料 vt.给…加燃料
fugitive adj. 逃亡的，易逝的n. 逃犯，逃亡者
fugue n. 赋格曲,朦胧状态,记忆丧失症
fulcrum n. 杠杆支点，支柱
fulfil vt. 达到(目的)，实现；满足；完成；执行；履行(诺言、责任等)，执行(命令等)，完成(计划、任务等)，达到(目的) v. 完成，满足要求
fulfill vt. 实践,履行,实行,满足,结束
fulfillment n.履行，完成，实现
fulfilment n.履行，完成，实现
fulgent a. 光辉的,灿烂的
full adj.满
full-bodied adj. (味道等)浓郁而强烈的
fuller n. 漂洗工
full-fledged adj. 羽毛丰满的，成熟的
full-length a. 全身的
fullness n. 满,充满,丰富
full-scale 齐备的；a. 全部的
full-service 经营全部业务
full-time adj. 专职的；全部工作时间的
fully ad. 十分地,完全地
fully-armed a. 全副武装的
fulminate v. 猛烈抨击，严厉谴责
fulmination n. 抨击，谴责
fulsome adj. 虚情假意的，丰满的
fulsomeness n. 虚情，谄媚
fumble v. 摸索，搜寻
fume n./v. 愤怒，冒烟
fumes n. (强烈而刺激的)气味，气体
fumigate v. 以烟熏消毒
fumigation 烟熏，熏仓
fun n.有趣的事，玩笑
function n.功能；职务；函数
functional a. 功能的
functionally ad. 功能上，机能上
functionary n. 小官，低级公务员
fund n.资金；基金；存款
fundament n. 基础，基本原理
fundamental a.基础的，基本的
funds 基金，资金，经费，专款
funeral n.葬礼，丧礼，丧葬
funereal a. 送葬的,适合葬礼的,悲哀的
funfair n.儿童乐园；游乐场
fungicide n. 杀真菌剂
fungous a. 草的,草似的,海绵状的
fungus n. 真菌
funk n. 恐惧，恐怖
funnel n. 漏斗；漏斗形物，vt. 传送；运送
funny adj.滑稽可笑的
funny-looking adj. 样子好笑的；样子古怪的
fur n.(兽类的)软毛；皮毛
furbish v. 磨光，刷新
furious a.狂暴的；强烈的
furiously ad. 狂怒地；有力地
furl vt. 卷收,叠,收下
furlong n. 英国长度单位
furlough n. 休假
furnace n.炉子，熔炉；鼓风炉
furnish vt.供应，提供；装备
furnished a.带家具的
furnishings 设备，陈设品
furniture n.家具；装置，设备
furor n. 激怒,感动,狂热
furred a. 毛皮的；毛皮做的
furrier n. 毛皮商,毛皮衣制作工
furrow n. 犁沟，皱纹
furry a. 毛皮的,盖着毛皮的,似毛皮的
further vt.增进
furtherance n. 助长,助成,促进
furthermore ad.而且，此外
furthest adj. & adv. 最远；a. 最远的；ad. 最远地
furtive adj. 偷偷的，秘密的
fury n.狂怒，暴怒；猛烈
furze n. 金雀花
fuse n.保险丝，导火线
fusillade n. （枪炮）齐射，连发
fusion n. 熔合物,结合,熔合
fuss n.忙乱；吹捧 vi.忙乱
fussy adj. 爱挑剔的
fustian n. 空洞的话，无意义的高调
futile a. 无用的,琐细的,无效果的
futility n. 无用，无益
future n.将来，未来
futures n. 期货；期货(比率)
futurity n. 未来,将来; 来世,后世
fuzz n. 细毛,绒毛,警员
fuzzy adj. 模糊的，有绒毛的
gabardine n. 一种斜纹防水布料,华达呢,一种宽松的长袍
gabble v. 急促而不清楚地说
gaberdine n. 工作服,华达呢
gable n. 山形墙,人字板
gad vi. 闲逛,游荡,蔓延
gadfly n. 虻，牛虻
gadget n. 小工具，小机械
gaff n. 鱼叉,斜桁,鸡脚上的铁爪
gaffe n. (社交上令人不快的)失言，失态
gag n. 箝口物,箝制言论,讨论终结
gage n. 抵押品,挑战
gaggle n. 鹅群
gaiety n. 欢乐，快活
gaily ad. 华丽地,欢乐地
gain vt.&vi.获得 n.利益
gainful a. 有利益的,唯利是图的
gainless 无利益的
gains n. 收益
gainsay v. 否认
gait n. 步法,步态
gaiter n. 绑腿,长统橡胶靴
gala n. 祭日,节日,祝贺
galactic adj. 星系的，银河系的
galaxy n. （银河）星群，显赫的人群.
gale n. 狂风，一阵（笑声）
galena  n. 方铅矿
galileo 伽利略
gall n. 胆汁（bile），怨恨（hatred）
gallant adj. 勇敢的，（向女人）献殷勤的
gallantry n. 勇敢，殷勤
gallbladder n. 胆囊
galleon n. 西班牙或地中海的大帆船
gallery n.长廊，游廊；画廊
galley n. 船上的厨房
gallon n.加仑
gallop n./v. （马）飞奔，疾驰
gallows n. 绞刑架，绞台
galore n. 丰富adv. 丰富地
galvanic a. 流电的,以流电所产的,抽搐的
galvanism n. 流电,流电学,电疗法
galvanize v. 电镀，通电，激励
gambit n. (常指带风险的)策略；弃兵局(指国际象棋开局让棋法)
gamble n.赌博 vt.冒…的险
gambler n. 赌博的人,赌徒
gambling n. 赌博
gambol n. 雀跃，嬉戏
game n.游戏，运动，比赛
gamekeeper n. 猎场看守人
games 运动员
gamesome  adj. 好戏谑的,好玩的,好作乐的
gamester n. 赌博者,赌徒
gammon n. 腌猪后腿,胡说
gamut n. 全音阶，（一领域的）全部知识
gander n. 雄鹅v. 闲逛
gang n.一帮，一伙
gangling adj. 细长的，不结实的
ganglion n. 神经节,神经中枢,腱鞘瘤
gangrene n. 坏疽,脱疽,腐败堕落的根源
gangster n.匪徒，歹徒，暴徒
gangway n. （上下船的）跳板
gaol n. 监狱；监禁；vt. 使…坐牢
gaoler n. 监狱看守
gap n.空隙；缺口
gape n. 裂口,张嘴,打哈欠
garage n.汽车间(或库)
garb n. 装束
garbage n.垃圾，污物，废料
garble v. 曲解，窜改
garbled adj. 篡改的；曲解的
garden n.花园，菜园；公园
gardener n.园丁，花匠
gardenia n. 栀子花
gardening n. 园艺(学)
gargantuan adj. 巨大的，庞大的
gargle vt. 漱
gargoyle n. （雕刻成怪兽状的）滴水嘴，面貌丑恶的人
garish adj. 俗丽的，过于艳丽的
garland n. （作为胜利标志的）花环，奖品
garlic n.蒜，大蒜
garment n.衣服；服装，衣着
garner v. 收藏，积累
garnet n. 石榴石,深红色
garnish v. 装饰（于食品上）
garnishee 扣押财产
garnishment 扣发，扣押金
garniture n. 附属品,添加物,服装
garret n. 阁楼，顶楼
garrison n. 守备队,驻军,要塞
garrulity n. 唠叨，饶舌.
garrulous adj. 唠叨的，多话的
garter n. 袜带
gary 加里(男名)
gas n.煤气；气体；汽油
gasconade n. 吹牛，夸口
gaseous a.气体的，气态的
gash n. 深长的伤口，裂缝
gasolene n.汽油
gasoline n.(美)汽油
gasp vi.喘息；喘气
gastric adj. 胃的，胃部的
gastritis n. 胃炎
gastrointestinal a. 胃肠的
gastronomy n. 美食法，美食学
gastrostomy n. 胃造口术
gate n.大门
gatekeeper n. 看门人；门警；门卫；守门人
gateway n.门口，入口；关口
gather vt.推测，推断
gathering n.集会，聚会，聚集
gauche adj. 笨拙的，不会社交的
gaucherie n. 笨拙
gaud n. 俗丽,俗丽的装饰,俗丽的仪式
gaudy adj. 俗丽的
gauge vt.量，测量 n.量器
gaunt adj. 憔悴的，瘦削的
gauntlet n. 铁手套,长手套,手腕,交叉射击
gauze n. 沙布，薄纱
gave  v. give(给)的过去分词；过去式
gavel  n.拍卖槌；年贡，税；(法官所用的)槌，小木槌
gay a.快乐的；鲜明的
gaze vi.凝视，盯，注视
gazelle n. 瞪羚
gazer  (C) 凝视者
gazette n. 报,公报,报纸
gazetteer n. 地名词典，地名表
gear n.齿轮，传动装置
gearbox n. 齿轮箱
gee n. 马,家伙
geese n. 鹅(复数)；goose的复数
gel n. 凝胶
gelatin n.明胶
gelatine n.明胶
gelatinous a. 凝胶状的
gem n. 宝石，珠宝
gen 表示"产生"，"生长"
gendarme  n.  (法国等之) 警官,宪兵
gender n. 性别
gene n. 基因；遗传因了
genealogical a. 宗谱的,家系的,系谱的
genealogy n. 系谱,宗谱,家系
general a.总的；一般的n.将军
generalise vt. 使一般化，归纳出，概括；vi. 形成概念，笼统地讲/写
generality n. 概论,概说,大要
generalization n.一般化；概括，综合
generalize vt.概括出vi.形成概念
generally ad.一般地；通常地
generate vt.发生；引起；生殖
generating adj. 发生的
generation n.一代，一代人；产生
generative a. 生殖的,生产的,有生殖力的
generator n.发电机；发生者
generic adj. 种类的、类属的
generosity n.慷慨，宽宏大量
generous a.慷慨的；宽厚的
generously 宽大地；ad. 慷慨地
genesis n. 创始，起源
genetic adj. 遗传的，起源的
genetically ad.遗传(基因)方面
genetics n. 遗传学
geneva  n. 日内瓦(瑞士城市)
genial adj. 愉快的，脾气好的.
geniality n. 和蔼，温和
genie n.妖怪
genitive a. 属格的
genius n.天才；天才人物
genoa n. 热那亚(意大利城市)
genome n. 基因组，染色体组
genre n. （文艺的）类型
gent n. 假绅士；家伙
genteel a. 有教养的,上流的,优雅的
gentian n. 龙胆属的植物,龙胆根
gentile n. 非犹太人,异邦人,异教徒
gentility n. 高贵的出身
gentle adj.柔和的
gentlefolk ]出身名门
gentleman n.绅士；有教养的人
gentlemen n. 男厕所
gentleness n. 温顺,柔和,亲切
gentlewoman n. 良家妇女,淑女,贵妇人
gently adv.温柔地；柔和地
gentry n. 贵族们
genuflect v. 曲膝半跪（以示敬意），屈从.
genuine a.真的；真正的
genuinely ad. 由衷地
genus n. 种,类
geographer n. 地理学者
geographical a.地理的；地区(性)的
geography n.地理，地理学
geological a. 地质学的,地质的
geologically ad. 从地质上来说
geologist n. 地质学家
geology n.地质学
geometric a. 几何的，几何形状的
geometrical a.几何学的
geometry n.几何，几何学
georgette n. 一种极薄的透明细纱,乔其纱
georgia n. 乔治亚(美国州名)
geranium n. 天竺葵
germ n.细菌
German adj.德国的 n.德国人
germane adj. 有密切关系的，贴切的
Germanic a. 德国的,条顿民族的,条顿语的
Germany n.德意志，德国
germinate v. 发芽，发展
germination n. 发芽,萌芽,发生
gerontologist n. 老年医学家
gerontology n. 老人病学
gerrymander vt. 为自党利益改划选举区分
gerund n. 动名词
gessler n. 盖斯勒(男名)
gestate vt. 怀孕; 孕育
gestation n. 怀孕，孕育时期
gesticulate v. 做手势表达
gesticulation n. 姿势,手势,做姿势传达
gesture n.姿势，手势；姿态
get v.取
get-together n. 聚集；集会；聚会，“联欢会”
gewgaw n. 便宜货
geyser n. 天然热喷泉
ghastly a. 可怕的,惊人的,惨白的
ghetto n.穷人或少数民族聚居
ghost n.鬼，灵魂；鬼魂
ghostly a. 幽灵的,影子似的,朦胧的
ghoul n. 食尸鬼,饿鬼,盗墓者
giant n.巨人；巨物
gibber vi. 急促而不连贯地说
gibbet n. 枭首台,绞首台,绞刑
gibbon n. 长臂猿
gibe n./v. 嘲弄，讥笑
giblets n. 鸡;鹅等的内脏;残余物
giddiness n. 眼花,轻率
giddy a. 眼花的,头晕的
gift n.礼物，赠品；天赋
gifted adj. 有天赋的；有才华的
gig n. 旋转物,轻便双轮马车,赛艇,
gigantic a.巨大的；巨人似的
giggle vi.vt. 吃吃地笑,格格地笑
gild vt. 镀金,虚饰,装饰,使有钱
gilded adj. 镀金的，富有的
gill n.鳃
gilt n. 镀金,表面的装饰,小母猪
gilt-edged 金边的，优良的，上等的
gimcrack 花哨不值钱的东西
gimlet n. 螺丝锥
gimmick n. 吸引人的花招，噱头
gin n. 杜松子酒,陷阱,轧棉机
ginger n.姜，生姜
gingerbread n. 姜饼,华而不实的东西
gingham a. 花格方布的
gipsy vi. 流浪
giraffe n. 长颈鹿,鹿豹座
gird n. 讥诮
girder n. 大梁
girdle n. 腰带，转绕物v. 环绕
girl n. 女孩；姑娘；女孩子，女儿；少女，女人；女职员
girlfriend n. 女朋友
girlish a. 少女的,少女似的,适于女子的
girls 女孩
giro 转帐；直接转帐
giroback n.转账支票
girocheck 转帐支票
girth n. 腰身,周长,肚带
gist n. 要点，要旨
git v. 获得；收到，(同)get
give vt.做，作；送给
given give的过去分词；给
giver n. 送礼者
giving n. 礼物，给予物
gizzard n. 砂囊,胃
glacial a. 冰的
glacier n.冰河，冰川
glad a.高兴的；乐意的
gladden vt. 使喜悦
glade n. 林中的空地
gladiator n. 角斗士，与野兽博斗者
gladiolus n. 剑兰,唐菖蒲
gladly ad. 愉快地，高兴地
gladness n. 欢乐,欢喜,喜悦
gladsome a. 高兴的,快乐的,愉快的
glamor n. 迷人的美,魔法
glamorous adj. 迷人的，富有魅力的
glamour n. 魅力，魔力
glance vi.看一下 n.一瞥
gland n. 腺
glandular a. 腺的
glare vi.瞪眼 n.瞪眼
glaring adj. 耀眼的；瞪眼的；怒目而视的；刺目的
glasgow n. 格拉斯哥(英国城市)
glass n.玻璃；玻璃杯
glasses (pl.) & n. 眼镜
glassful n. 一杯的容量
glasshouse n.温室，暖房
glass-topped adj. 玻璃罩的
glassware n. 玻璃器具类
glassy a. 玻璃质的,玻璃状的,如镜的
glaze n. 釉
gleam n.微光 vi.发微光
gleaming a. 闪闪发光的
glean v. 拾落穗，收集（材料等）
gleaner n. 拾落穗的人
gleanings n. 所拾得的落穗
glebe n. 土,土地,旱田
glee n. 欢喜，高兴
gleeful adj. 欢乐的，欣喜的
glen n. 峡谷,幽谷
glib adj. 流利圆滑的，善辩的
glide vi.滑动；消逝 n.滑行
glider n.滑翔机；滑翔导弹
gliltter v.闪烁；闪耀；闪闪发
glimmer v. 发微光，n. 摇曳的微光
glimpse vt.瞥见 n.一瞥，一看
glint n. 闪烁
glisten v. 闪烁，闪耀.
glitter vi.闪闪发光 n.闪光
gloaming n. 黄昏，薄暮
gloat v. 幸灾乐祸地看，窃喜
global  adj.球面的；全球的；全世界的，总的；世界的；地球的，环球的，全局的n. 全局，全程，全局符
globalization n. 全球化
globalize v. 使…全球化
globe n.球；球状物；地球
globular a. 球状的,小球状的,由小球形成的
globule n.  (尤指液体的) 小球体; 小滴
gloom n.黑暗；忧愁
gloomily adv. 忧郁的
gloomy a.黑暗的；令人沮丧的
glorify vt.赞美(上帝)；颂扬
glorious a.光荣的；壮丽的
gloriously ad. 光荣地，辉煌地
glory n.光荣；荣誉的事
gloss n. 光泽，注解
glossary n.词汇表；术语汇编
glossy adj. 光泽的，光滑的
glove n.手套
glow n.白热光 vi.发白热光
glower v. 怒目而视
glowing a. 灼热的
glow-worm n.萤火虫
gloze vt. 似有道理地说明,掩饰
glucose n. 葡萄糖
glue n.胶，胶水 vt.胶合
glum adj. 闷闷不乐的，阴郁的，
glut n./v. 供过于求，过多
gluten n. 麸质
glutinous adj. 粘的，胶状的
glutton n. 贪吃者
gluttonous a. 暴食的,贪吃的,饕餮的
gluttony n. 暴饮暴食
glycerin n.甘油
glycerine n.甘油
glycogen n. 肝糖，动物淀粉
gnarl n. 节,瘤
gnarled adj. （树木）多节的，粗糙的
gnash vt.vi. 咬牙切齿
gnat n. 对小事斤斤计较，琐事
gnaw vt.啃，咬断 vi.啮
gnawing adj. 痛苦的，折磨人的
gneiss n. 片麻岩（一种艰硬的岩石）
gnome n. 地下宝藏的守护神，地精，格言
gnomic adj. 格言的，精辟的
gnosis n. 灵知，神秘的直觉
gnp 国民总生产；n. (缩)国民总收入
gnu n. 角马
go v.去
goad n. 赶牛棒n./v. 刺激，激励
goal n.球门；得分；目的
goal-shy a.射门不果断的
goat n.山羊
goatherd n. 牧羊人
goatskin n. 山羊皮
gobble v. 贪婪地吃，吞没
gobbler n. 雄火鸡
goblet n. 高脚酒杯
goblin n. 顽皮的丑小鬼,小妖精
go-cart n. 学走器,乳母车,推车
god n.神，神像；上帝
goddess n.女神；绝世美女
godfather n. 教父
godhead n.神格,神性
godless a. 不信神的,无神论者的,不敬神的
godlike a. 神似的,庄严的,与神相称的
godliness n. 虔诚,敬神,信仰
godly a. 敬神的,虔诚的,神的
godmother n. 教母,名义上母亲
goggle n. 眼睛睁视,护目镜
going go的现在分词；n. 行走；离去；进行情况；a. 进行中的
gold n. 金子；黄金；金黄色；金色；金；钱财，金币，财富；a. 金的；黄金的；金制的；金质；黄金，含金的
golden adj.金(黄)色的
goldenrod n. 秋麒麟草属植物
goldfinch n. 金翅雀
goldfish n. 金鱼
gold-fish n. 金鱼
gold-ring n. 金戒指
goldsmith n. 金匠
gold-smith n.金匠
golf n.高尔夫球
gollop v. & n. 大口吞咽
gonad n. 性腺，生殖腺
gondola n. 狭长小船,两头尖的平底船,无盖货车
gondolier n. 操 gondola 的船夫
gone vi. (go的过去分词)；a. 已去的；过去的；垂死；入迷的
gong n. 铜锣,盘形钟
good adj.好的
goodby int.再见
goodbye int. 再见
good-bye interj.再见
good-humouredly ad. 和气地
goodliness n. 美丽,美貌,美好
good-looking adj. 相貌好看的；好看的；漂亮的，美貌的
goodly adj.漂亮的,可观的
good-natured  adj. 性情好
goodness n.优良，德性，仁慈
goodnight int. 晚安，再见
goods n.商品；货物
goodself n. 你方
good-tempered a. 脾气好的
goodwife n. 女主人,女子的敬称
goodwill n.善意,亲切; 亲善
good-will 商誉，信誉，营业权
goody n. 身分低微之老妇,媪,糖果
goose n.鹅，雌鹅
gooseberry n. 醋栗树,醋栗,醋栗酒
gopher 服务器名称
gore n. 凝血，血块
gorge n. 峡谷v. 贪婪地吃
gorgeous a.绚丽的；极好的
gorgon n. 丑陋女人，蛇发女怪
gorgot 忘记
gorilla n.大猩猩；暴徒，打手
gormandize v. 拼命吃，贪吃
gorse n. 金雀花
gory adj. 满是血的，血污的
gosh int. 天哪！啊呀！
gosling n. 小鹅，年轻无知的人
gospel n. 教义，信条
gossamer n. 蛛丝，薄纱，adj. 轻而薄的
gossip n.闲谈；碎嘴子；漫笔
got vt. get(得到)的过去式和过去分词
Goth n. 哥特人,野蛮人,粗野的人
Gothic n. 哥特式
gotten get的过去分词
gouge n. 半圆凿，v. 挖出，敲竹杠
gourd n. 葫芦，脑瓜
gourmand n. 嗜食者
gourmet n. 美食家
gout n. 味,趣味,嗜好,一团,一滴
gouty a. 痛风的,患了痛风的,易患痛风的
govern vt.统治，治理；支配
governance n. 统治，支配
governer 统治者，管辖者，地方长官
governess n. 女家庭教师
government n.政府；治理；政治
governmental a. 政治的,统治上的,政府的
governor n.统治者；总督
gown n.长袍，长外衣
grab vt.&vi.急抓；抢
grace 格雷斯(女名)
graceful a.优美的，优雅的
gracefully ad. 优美地，斯文地
graceless a. 不知礼的,不知耻的,粗野的
gracious a.谦和的
graciously adv. 文雅地；仁慈地，和蔼庄重地
gradation n. (颜色等的)层次
grade n.年级
gradener 园丁
grader n.…年级学生
gradient n. 斜坡；梯度，倾斜度；坡度a. 倾斜的；倾斜度
grading 分级
gradual a.逐渐的；渐进的
gradualism n.渐进主义
gradually adv. 逐渐地；逐步地
graduate n.毕业生 vi.大学毕业
graduation n.毕业
graft v. 嫁接，移植，n. 贪污
graham a. 用末精制之面粉的;全麦的
grain n.谷物，谷类；谷粒
gram n. 克,绿豆
gramercy int. 多谢! 不得了!
grammar n.语法；语法书
grammarian n. 文法家,文法学者,文法教师
grammatical adj.语法的
gramme n.克(重量单位)
gramophone n. 留声机；唱机
granary n. 谷仓，主要来源
grand adj.庄严的；伟大的
grandchild n. 孙子; 孙女; 外孙; 外孙女
granddaughter n.孙女，外孙女
grandee n. 贵族,大公,显贵之人
grandeur n. 壮丽，伟大
grandfather n.祖父；外祖父
grandiloquent adj.（语言等）夸张的，夸大的
grandiose adj. 浮夸的，夸大的
grandma n.(口语)奶奶，外婆
grandmother n.祖母，外祖母
grandpa n.(口语)爷爷，外公
grandparent n. 祖父或祖母,祖父母
grandparents n. 祖父母；外祖父母
grandsire n. 老人；祖先
grandson n.孙子，外孙子
grandstand n. 正面看台，哗众取宠的表演
grange n. 农庄
granite a.花岗岩，花岗石
granny n. 老奶奶；祖母；外婆；奶奶；老婆婆，外祖母
grant n.授予物，拨款
granted conj. 即使
grantee 受让人，受补贴人
grant-in-aid n.财政补贴
granular adj. 粒状的，含颗粒的
granulate v. 使成颗粒
granule n. 小粒，微粒.
grape n.葡萄；葡萄藤
grapefruit n. 柚子,柚子树
graph n.(曲线)图，图表
graphic adj. 图表的，生动的
graphically ad. 用图表表示
graphics n.制图法；图解计算法
graphite n.石墨，石墨电极
graphy (构词成分)图示法；画法；记；志
grapnel n. 小锚,抓钩
grapple vt.vi. 抓住,掌握
grasp vt.抓住；领会；掌握
grasping adj. 贪心的，贪婪的
grass n.草；草地
grasshoper n.蚱
grasshopper n.蚱蜢，蝗虫，蚂蚱
grassland n. 牧场；草地；草原
grass-seed 草籽
grassy a.草多的；草似的
grate v. 磨碎，使人烦燥
grateful a.可喜的，令人愉快的
gratefully ad. 感激地
grater n. 擦菜板
gratiano n. 葛莱西安诺(男名)
gratification n. 满足，喜悦
gratify v. 使高兴，使满足
gratifying adj. 可喜的
grating adj. （声音）刺耳的，恼人的
gratis adj. 免费的
gratitude a.感激，感谢，感恩
gratuitous adj. 无缘无故的，免费的
gratuity n. 赏钱，小费
grave n.坟墓 a.严重的
gravel n.砂跞；砂砾层；结石
gravely ad. 庄重地，严肃地
graveness n. 重大,严重,认真
graveyard n. 墓地
gravitation n. 引力,重力,沉下
gravitational a. 引力的
gravity n.重力，引力；严重性
gravy n. 肉汁,肉汤,不法利润
gray a.灰色的 n.灰色
gray-headed adj. 白发的
grayling n. 河尊,褐色蝶类
graze vi.喂草；放牧(牲畜)
grease n.动物脂，脂肪
greaseproof-paper 防油纸
greasy a. 油腻的,滑溜溜的,泥泞的
great adj.伟大的；重大的
greater a. 更大的，更伟大的
greatly ad.大大地，非常
greatness n.伟大；巨大
grecian a. 古希腊的；n. 希腊人
Greece n.希腊
greed n.贪心，贪婪
greedily ad. 贪婪地
greediness n. 贪吃,嘴馋,贪欲
greedy a.贪吃的；贪婪的
Greek a.希腊的 n.希腊人
green adj.绿色的
greenback n. 美钞,背部为绿色之动物
greengrocer n. 卖蔬菜及水果的商人
greenhorn n. 初学者，容易受骗的人
greenhouse n.温室，玻璃暖房
greenish a. 呈绿色的
greenness n. 绿色,新鲜,未熟
greensward n. 草皮
greenwich 格林威治
greenwood n. 绿磷,未枯干的树
greet vt.问候
greeting n.问候，招呼，致敬
greetings n. 问候
gregarious adj. 群居的，爱社交的
grenadier n.手榴弹兵,掷弹兵
grew grow的过去式；生长
grey adj.灰色的
greyhound n. 灰狗,快速船
greyish a. 淡灰色的
grid n. 格子,栅极
griddle n. 筛子，大孔筛
gridiron n. 烤架，橄榄球场
grief n.悲哀，悲痛，悲伤
grief-stricken a.充满悲伤的，极度悲痛的
grievance n. 委屈，抱怨
grieve vt.使悲痛 vi.悲痛
grieved 伤心的
grievous adj. 严重伤害的，引起痛苦的
grill v. 烤，烤问，n. 烤架
grille n. (银行，邮局柜台上的)铁栅
grim a.冷酷无情的，严厉的
grimace v. 做鬼脸，面部歪扭
grime n. 尘垢,煤尘,污点
grimly ad. 可怖地；严厉地；坚强地
grimy adj. 污秽的，肮脏的
grin vi.咧着嘴笑
grind vt.磨(碎)；磨快
grinder n. 研磨者
grinding a. 嘎嘎响的；难熬的，折磨人的，难以忍受的
grindstone n. 磨刀石
grip vt.握紧，抓牢 n.紧握
gripe v. 发牢骚，抱怨；紧握
gripes n.肚子痛
grippe n. 流行性感冒
gripping adj. 引起注意的
grisly adj. 恐怖的，可怕的
grist n. 大量，许多
gristle n. 软骨结构，软骨
gristmill n. 磨粉厂
grit n. 沙粒，决心，勇气v. 下定决心，咬紧牙关
grizzled a. 灰色的,头发斑白的
grizzly a. 略为灰色的,呈灰色的
groan vi.哼，呻吟 n.呻吟
groat n. 昔日英国的四便士银币,些许,
grocer n.食品商；杂货商
groceries n. 食品(店)；杂货(店)
grocer's 杂货店
grocery n.食品杂货店
grog n. 掺水烈酒
groggy adj. 体弱的，不稳的
groin n.腹股沟
groom n. 马夫，新郎
groove n.槽 vt.开槽于
grope vi.(暗中)摸索，探索
gropingly adv. 不确定的，摸索
gross a.(语言、举止)粗俗的
grossness n. 肥满,粗杂,粗劣
grot n. (美丽的)洞穴;巢穴
grotesque adj. 怪诞的，古怪的
grotto n. 洞穴，洞室
grouch n. 牢骚，不满
grouchy a. 不高兴的,不平的
ground n.地；场地；根据
groundless  adj. 无根据的; 无理由的; 无缘由的
grounds n. 理由
groundwork n. 地基,基础,根据
group n.小组，群 vi.聚集
groupage n. 合并装运
grouse n. 松鸡v. 牢骚，诉苦
grove n.林子，小树林，园林
grovel v. 摇尾乞怜，奴颜婢膝
groveler n. 乞怜者
grow vi.生长；变得；增长
grower n. 栽培者,生长物
growing n. 分类，分组，成群
growl vi.(狗等)嗥叫；咆哮
grown adj. 已长成的；grow的过去分词；生长
grown-up a. 已经成人的
growth n.增长；增长量；生长
grrr interj. (老虎的)吼叫声
grub n. 幼虫,穷文人
grudge v. 吝啬，不满.
grudging adj. 勉强的，吝啬的
gruel n. 稀粥
grueling adj. 令人筋疲力竭的；繁重而累人的
gruesome adj. 令人毛骨悚然的，恶心的
gruff adj. 粗暴的
gruffly ad. 粗暴地
grumble vi.抱怨，发牢骚
grumpy adj. 脾气暴躁的
grunt vi.作呼噜声；咕哝
guarantee n.保证；担保物
guarantees 保证人，票据担保人
guarantor 保票，担保，保证书，保证金
guaranty n. 保证品,抵押
guard n.哨兵，警卫员
guarded adj. 谨慎的，提防的
guardian n. 保护人；监护人
guardianship n. 监护,保护,守护
guardsman n. 卫兵,近卫兵,州辖预备役部队的人员
guerdon n. 报酬,奖赏
guerrilla n.游击队
guess v.猜
guest n.客人
guesthouse n. 宾馆
guest-room n. 客房
guffaw n./v. 哄笑，大笑
guidance n.引导，指导，领导
guide n.向导，导游者
guidebook 旅行指南
guideline n. 指南，方针
guidelines 指导性指标
guidepost n. 路标,路牌
guild n. 公会,协会,行业协会
guilder n. 基尔德,基尔德银币,旧荷兰
guile n. 狡猾,狡计
guileless a. 不狡猾的,诚实的
guillotine n. 断头台
guilt n.有罪，犯罪；内疚
guiltily ad. 内疚地
guiltiness n. 有罪,罪的自觉
guiltless a. 无罪的；不熟悉…的；无经验的
guilty a.内疚的；有罪的
guinea n. 英国往昔的金币
guise n. 外观,伪装
guitar n.吉他，六弦琴
gulch n. 峡谷；深谷
gules n. 红色
gulf n.海湾；鸿沟
gull n. 海鸥，v. 欺骗
gullet n. 食道,咽喉,海峡
gullible adj. 易受骗的
gully n. 小峡谷,排水沟
gulp v. 吞食，咽下
gum n.口香糖；树胶
gummy a. 树胶的,粘的
gun n.枪，炮，手枪
gunboat n. 炮舰；炮艇
gun-deck n. 炮台
gunman n. 枪手,持枪的歹徒,制造枪械者
gunner n. 炮手,炮长,带枪猎人
gunnery n. 炮术,射击,炮击
gun-port n. 炮眼
gunpowder n.黑色火药；有烟火药
gun-powder n. 火药
gunshot n. 火炮的单发射击
gunwale n. 『航海』舷缘,舷侧上缘
gurgle n. 汩汩声
guru n.领袖；古鲁(指印度教等宗教的宗师或领袖)
gush v. 涌出，滔滔不绝地说
gusher n. 滔滔不绝的说话者，喷油井
gust n.阵风，一阵狂风
gustation n. 品尝，味觉
gustatory a. 尝味的,味觉的
gusto n. 爱好，兴致勃勃
gusty a. 阵阵猛急的,突发的
gut n. 勇气,剧情,内容,海峡,肚子,
gutenberg n. 古腾堡
gutless adj. 没有勇气的，懦怯的
gutter n.沟，边沟；檐槽
guttle v. 狼吞虎咽
guttural adj. 喉的，咽喉的
guy n. （铁塔等的）支索，牵索
guzzle v. 大吃大喝
gym n. ((口语))体育馆，健身房
gymnasium n.体育馆，健身房
gymnast n. 体操运动员
gymnastics n. 体操
gynecocracy n. 妇人政治
gynecoid adj. 妇女的，有女性特征的
gypsum n. 石膏
gypsy n. 吉布赛人,吉布赛语,
gyrate adj. 旋转的；v. 旋转
gyve n. 脚镣,手铐
ha interj.哈；嘿(惊异)
haberdashery 服饰用品，服饰店
habergeon  n. 亦作haubergeon
habiliments n. 服装；衣着
habit n.习惯；习性
habitable a. 可居住的
habitant n. 居住者
habitat n. 自然环境，栖息地
habitation n. 居住,住所
habitual a.习惯性的，惯常的
habitually adv. 习惯地
habituate v. 使习惯于
habitus n. 状态
hack v. 乱劈，乱砍，n. 驽马
hackles n. 狗颈部之毛
hackney n.乘用马,出租马车,操贱役的人
hackneyed adj. 陈腐的，平常的
had  have(有的过去式和过去分词)
haddock n. 鳕的一种
Hades n. 冥府,阎王,地狱
hadn't (同)had not
haemophilia n. 血友病，出血不止
haemorrhage n. 出血(尤指大出血)
haemostat n. 止血器，止血剂
haft n. 柄，把柄
hag n. 女巫,丑老太婆,砍伐,沼地
haggard adj. 憔悴的，消瘦的
haggle v. 争论，讨价还价
hague n. 海牙(荷兰城市)
hail vt.向…欢呼 vi.招呼
hailstone n. 冰雹
hair n.头发
haircut n.理发
hairdo n. 发型
hairdress n. 美发
hairdresser n. 理发师，美容师
hairless a. 无毛的
hairlike a. 毛发似的
hair-oil n. 头发油
hairpin n. 簪,束发夹,夹发针
hairy adj. 毛发的，多毛的
haiti n. 海地
hake n. 无须鳕
halberd n. 戟
halcyon adj. 平静的，愉快的
hale a. 强壮的,健壮的
half n.半，一半
half-finished 半成品
half-hearted a.不热心的，不积极的
half-hibernate vi. (动物)半冬眠
half-hour 半小时；n. & a. (每)三十分钟的
halfpenny n. 半便士
halfway adv. 半途；不彻底地；a. 中途的，不彻底的；半途中的
half-way n. 中途
halibut n. 大比目鱼
hall n.会堂，大厅，礼堂
hallmark n. 标志；检验印记；金银的纯度
halloo int. 一种喊声
hallow v. 把…视为神圣，尊敬
hallowed adj. 神圣的；崇高的
hallucinate v. 产生幻觉
hallucination n. 幻觉,幻想
hallway n. 走廊
halo n. （日月等）晕，神像之光环
halt vi.停止；立定 n.停住
halter n. 缰绳,笼头
halting adj. 踌躇的，吞吞吐吐的
halve vt.对分；平摊
ham n.火腿；(兽类的)后踝
hamburg n. 汉堡(德国港市)
hamburger n.汉堡包，牛肉饼
hamlet n. 小村,部落
hammer n.锤，榔头 vt.锤击
hammock n. 吊床,小丘
hamper vt. 妨碍；阻碍，牵制；v. 妨碍，牵制；阻挠；阻扰；n. 有盖提篮
hamster n. 东欧或亚洲产的大颊的鼠类
han n. 汉，汉人，汉族
hand n.手
handbag n. 手提包
handball n. 手球,那种球,手球
handbill n. 传单,招贴
handbook n. 手册，便览，指南
handcart n. 手推车
handcuffs n. 手铐
hand-filling 人工包装
handful n.一把；少数，一小撮
handicap vt.妨碍，使不利
handicapped adj. 有残疾的
handicraft n. 手工艺,手艺,技巧
handiwork n. 手工,手工艺,手工
handkerchief n.手帕
handle n.柄，把手 vt.拿，触
handler n. 处理程序
handling n. 用特别方式使用；处理，管理；操纵
hand-made adj.手工制的
handmaid n. 女仆; 婢女
hand-money 预会款
handout n. 施舍物，救济品；分发物(印刷品等)；散发的文字材料
hand-picked 第一流的，精选的
hands 手
handshake n. 握手
handsome adj.漂亮的，清秀的
hands-on a.亲身实践的
handtruck n. 手推运货车
hand-washing n. 洗手
handwriting n.笔迹，手迹，书法
handy a.手边的；便于使用的
handyman n. 受雇做杂事的男人,手巧的人,
hang vt.挂，悬；吊死
hangar n. 飞机库
hanger n. 衣架，挂衣钩
hanging n. 绞刑；a. 悬挂着的
hangman n. 绞刑吏,刽子手
hangover n. 宿醉，残存物
hank n. 一束,一卷,一仔
hanker v. 渴望，追求
hanover n. 汉诺威(德国城市)
hap  n. 运气；机遇，幸运；机会vi.偶然发生之事
haphazard n. 偶然,偶然事件
hapless adj. 不幸的
haply ad. 或许
happen vi.(偶然)发生
happening n. 事件；偶然发生的事
happily ad. 幸福地,快乐地,幸好
happiness n.幸福，幸运；快乐
happy adj.高兴的，幸福的
harangue n. 大声疾呼的演说；长篇演说
harangur n. vi. 长篇演说
harass v. 烦扰
harassment n. 烦扰(的行为)
harbin n. 哈尔滨
harbinger n. 先驱，先兆.
harbor n. 港，避难所v. 包庇，隐匿
harborage  n.避难,保护
harbour vt.隐匿，窝藏；怀着
hard adj.困难的；硬的
hard-bitten adj. 不屈的，顽强的
hard-boiled a.煮透的
harden vt.使变硬 vi.变硬
hardened a. 老练的
hardheaded adj. 实际的，脚踏实地的；(商业上)现实的，精明的
hard-headed a. 头脑冷静的
hard-hearted adj. 心肠硬
hardihood n.胆大无敌,刚毅,厚颜
hardiness n. 强壮; 结实; 耐劳
hardly ad.几乎不，简直不
hardly...before 刚一就
hardly...when 刚一就
hardly...when... 刚…就…
hardness n. 坚硬,困难,严厉,勇气
hardpan 底价
hardship n.艰难，困苦
hardware n.五金器具；硬件
hardwood n. 硬木,硬木材,落叶树
hardworking a. 勤奋的；勤劳的
hard-working adj. 努力工作的；勤劳的
hardy a.强壮的，耐劳的
hare n.野兔
harebell n. 山小菜,蓝铃花
harem n. 由一群雄性动物支配的，一群雌性动物
hark vi. 倾听
harlequin n. 丑角
harlot n. 妓女
harm n.伤害，损害 vt.损害
harmful a.有害的
harmless adj.无害的
harmonic a. 调和的,音乐般的,和声的
harmonica n. 口琴,玻璃或金属片的敲打乐器
harmonious a.和谐的，协调的
harmonize v. 使调和，使一致
harmony n.调合，协调，和谐
harness vt.治理 n.马具，挽具
harp n.竖琴；天琴座
harper 哈柏(姓)
harping n. 反复述说
harpoon n. （捕鲸的）鱼叉
harpsichord n. 键琴（钢琴前身）
harpy n. 残酷贪婪的人,鸟身女妖
harridan n. 凶恶的老妇，老巫婆
harrow n. 耙
harrowing adj. 悲痛的，难受的
harry v. 掠夺，骚扰
harsh a.粗糙的；严厉的
harshly ad. 粗糙地，冷酷地
harshness n. 粗糙的事物,刺耳,严肃
hart n. 雄赤鹿,雄鹿
harvard n. 哈佛大学(美国)
harvest n.收获，收成 vt.收割
harvester n.收获者,收割工人 (reaper)
harvesting n. 收割
harvest-time n. 收获季节
has v.有(第三人称单数)；vt. 有
hash n. 无用信息,杂乱信号,杂烩,复述
hashish n. 以印度大麻提练的麻药
hasn't (同)have not
hasp n. 铁扣,一束纱或线,纺绽
hassle n. 激烈的辩论
hassock n. 当座凳用的厚垫子,跪垫,草丛
hast have的第二人称单数
haste n.急速，急忙；草率
hasten vt.催促 vi.赶紧
hastily ad. 匆忙地,急速地,慌张地
hasty a.急速的；仓促的
hat n.帽子
hatch vt.孵出 vi.(蛋)孵化
hatchery n. 育种站
hatchet n.斧头
hatchment n. 方形黑框中所画的死者菱形绞章
hatchway n. 舱口,地板,天花板之出入口
hate vt.恨，憎恨；不喜欢
hateful a.可恨的，可恶的
hater n.
hatred n.憎恶，憎恨，仇恨
hatter n. 帽子制造者,帽商
hauberk n. 锁子甲
haughtily ad. 傲慢地，高傲地
haughtiness n. 傲慢
haughty a.傲慢的，轻蔑的
haul vt.拖曳；拖运
haunch n. 腰,臀部,腰部
haunt vt.常去 vi.经常出没
haunted a. 闹鬼的，反复出现的；常出现鬼的
haunting adj. 不易忘怀的
hause v. 给房子住
hauteur n. 傲慢
havana n. 哈瓦那(古巴首都)
have v.有
haven n. 安息所，避难所
haven't 没有；(同)have not没有
haversack n. 肩背包，干粮袋
havoc n. 大破坏，混乱
haw n. 山楂,吆喝牲畜左转,呃,瞬膜
hawaii n. 夏威夷(州)(美国)
hawk n.鹰，隼
hawker n. 沿街叫卖之小贩
hawk-eyed a. 目光锐利的
hawser n. 粗绳，大钢索
hawthorn n. 山楂
hay n.干草
haycock n. 圆锥形的干草堆
haydn 海顿(奥地利作曲家)
hayloft n. 干草棚,干草仓
haystack n. 干草堆
hazard n.危险；公害
hazardous adj. 有危险的
haze n. 薄雾,阴霾,疑惑
hazel n. 榛子,淡褐色
hazelnut n. 榛实
hazy a. 朦胧的,模糊的,烟雾弥漫的
h-bomb 氢弹
he pron.(主格)他
head n.头
headache n.头痛；头痛的事
header n. 首领,队长,收割台
heading n.标题，题词，题名
headland n. 向水中突出的陆地,畦头未耕的一条地
headless a. 无头的,无领导者的,无知的
headlight n. 前灯,桅灯
headline n.大字标题；新闻提要
headlong a.&ad.头向前的(地)
headmaster n.校长
headmistress n. 中小学女校长
headnurse n. 护士长
headpiece n.头盔; 帽子
headquarters n.司令部；总部
headsman n. 刽子手,捕鲸船的指挥者,坑内运煤工人
headstone n. 墓石,基石
headstrong a. 顽固的,刚愎的,任性的
headteacher n. 中小学班主任
headwaiter 服务员领班
headway n. 前进,航行速度,进展
heady a. 顽固的,任性的,性急的,猛烈的
heal vt.治愈；使和解
health n.健康，健康状况
healthful a. 有益健康的,使人健康的,卫生的
healthy adj.健康的
heap n.(一)堆；大量；许多
hear v.听见，听
heard hear的过去式(分词)；听
hearer n. 听者,听众
hearing n.听；听力
hearken v. 倾听
hearsay n. 谣传，道听途说
hearse n. 灵车
heart n.心(脏)
heartbeat n. 心脏跳动
heartbreaking adj. 令人心碎的
heart-broken a. 伤心的
heartburn n. (消化不良)胃灼热感
hearted 心的
hearten vt. 鼓起勇气,激励
heartfelt a. 衷心的,真心真意的
hearth n.壁炉地面；炉边
hearth-rug n. 炉前地毯
hearthstone n. 炉底石,砌炉的石块,家庭
heartily ad. 衷心地,真实地,热心地
heartiness n. 诚实,热心
heartland n.心脏地带，中心地带
heartless a. 无情的,无勇气的
heartsick a. 悲痛的,苦恼的
hearty a.衷心的；丰盛的
heaser n.出租人
heat n.热，炎热 vi.变热
heated adj.激烈地；兴奋的
heater n.加热的人，加热器
heath n. 荒地
heathen n. 异教徒，不信教的人
heathenish a. 异教的,异教徒的,非基督教的
heather n. 石南花
heating n.加热，供暖
heat-regulating a. 调节热的
heat-wave n. 热浪(意即炎热)
heave vt.(用力地)举起；抛
heaven n.天堂；天，天空
heavenly a. 天上的,神圣的,天国似的
heavenward ad. 朝向天空地,朝向天国地
heavily ad.重重地；大量地
heaviness n.重; 沉重
heavy adj.重的
heavy-duty a.重型的
heavy-handed adj. 笨手笨脚的
Hebrew n. 希伯来人,希伯来语,犹太人
hecatomb n. 大屠杀，百牛大祭
heckle v. 诘问，困扰
heckler n. 诘问别人之人
hectare n. 公倾(合十五市亩)
hectic adj. 兴奋的，繁忙的
hector v. 凌辱，威吓
he'd (同)he had；he would
hedge n.篱笆，树篱；障碍物
hedgehog n. 刺猬
hedge-row n.一排树篱
hedonism n. 享乐主义，享乐
hedonistic adj. 享乐的
heed v. 注意到，关心
heedless a. 不注意的,不留心的,不谨慎的
heel n.脚后跟，踵，后跟
hegemony n. 霸权领导权
hegira n. 逃亡
heifer n. 小母牛
height n.高，高度；高处
heighten vt.加高，提高；增加
heinous adj. 可憎的，十恶不赦的
heir n.后嗣，继承人
heiress n. 女继承人
heirloom n. 传家宝,相传动产
heirship 继承权
held hold的过去式(分词)；抓住
helicopter n.直升机
heliotrope n. 向阳植物
helium n. 氦
hell n.地狱；极大的痛苦
he'll (同)he will；he shall
hellebore n. 『植物』菟葵
hellish a. 地狱的,凶恶的,令人毛骨悚然的
hello " interj.喂，你好；
helmet n.头盔，钢盔
helmsman n. 舵手
helot n. 奴隶，受人轻视之人
help v.帮助，帮忙
help...with 帮助(某人做某事)
helper n. 帮忙者,助手
helpful a.给予帮助的；有用的
helping n. 一份或一客食物
helpless a.无助的；无能的
helplessly ad. 无能为力地
helplessness n. 无能为力
helpmate n. 助手,伴侣,配偶
helter-skelter n. 慌张,狼狈
helve n. 斧柄
hem n. （衣服或裙子的）褶边
hematologist n. 血液学家
hemisphere n.半球；半球地图
hemlock n. 铁杉；常青树
hemoglobin n. 血色素
hemorrhage n. 出血
hemp n. 麻,大麻,纤维
hempen a. 大麻制的,大麻的
hemstitch n. 抽丝做成的花边装饰,垂迹
hen n.母鸡
hence ad.因此，所以；今后
henceforth ad.今后，从今以后
henceforward  adv.ad. 自此以后,今后
henchman n. 亲信，心腹
henhouse n. 鸡舍
henna n. 指甲花,指甲花染料,红褐色
henpecked adj. 顺从妻子的，惧内的
henry 亨利(男名)；亨利. 贝西默
hepatic a. 肝的
hepatitis n. 肝炎
heptagon n. 七角形,七边形
her pron.她的
herald ad.传令官；通报者
heraldic a. 纹章学的,纹章的,传令官的
heraldry n. 纹章学,纹章,家徽
herb n.草本植物；香草
herbaceous adj. 草本植物的
herbage n. 草本,草,草的柔软部分
herbal adj. 草药的；草本植物的
herbivore n. 草食动物
herbivorous a. 食草的
herculean a. 非常大的；大力神的
hercules n. (希，罗神)大力神；大力士
herd n.(动物)一群
herder  n. 牧人; 牧者
herdsman n. 牧人
here adv.这儿
hereafter n. 将来,来世
hereby ad. 因此,据此
hereditary a. 世袭的,遗传的
heredity n. 遗传,形质遗传
herein ad. 在此处,如此,鉴于
hereinafter adv. 以下
hereof ad. 于此,关于此点
here's (同)here is
heresy n. 异端邪说
heretic n. 异教徒
heretical adj. 异端邪说的
hereto adv. 对此；附此
heretofore ad. 直到此时,此时以前,迄今
herewith ad. 同此,因此
heritage n. 遗产，继承物
hermetic adj. 密封的，炼金术的
hermetically adv. 密封的；不透气的
hermit n. 隐士，修道者
hermitage n. 隐居处
hero n.男主角；英雄；勇士
heroic a.英雄的；英勇的
heroics n. 史诗；咬文嚼字；装腔作势的演说或行为
heroin n. 海洛因,吗啡
heroine n.女主角；女英雄
heroism n. 英勇,勇敢的事迹,豪侠的行为
heron n. 苍鹭的巢
herr n. (德)先生
herring n. 青鱼,鲱
hers pron.她的(所有物)
herself pron.她自己；她亲自
Hertford (地名)赫特福德
he's (同)he is；he has
hesitant adj. 犹豫的
hesitantly ad. 犹豫地
hesitate vi.踌躇；犹豫
hesitation n. 暂停,犹豫,口吃,含糊,踌躇
heterodox adj. 异端的，非正统的
heterodoxy n. 异端邪说
heterogeneous adj. 异类的，不同的
heterograft n. 异种移植(物或术)
hew v. 砍伐
hewer n. 砍伐者,煤矿工
hex a. & n. 六角形的
hexadecimal a. 十六进制的
hexagon n. 六角形，六边形
hexameter n. 六步格,六步格的诗
hey interj.嗨
heyday n. 全盛时期，青春期
hi  interj.你好；喂(问候等)；嗨(表示问候等)
hiatus n. 空隙，裂缝
hibernal a. 冬天的,寒冷的
hibernate vi.(动物)冬眠
hibernation n.冬眠
hibiscus n. 芙蓉，木槿
hick n. 乡下人；农夫；土头土脑的人
hickory n. 山胡桃树,山胡桃木
hid hide的过去式(分词)；藏
hidalgo n. 西班牙的下级贵族,西班牙的绅士
hidden vbl. hide的过去分词
hide n.生皮，兽皮，皮革
hide-and-seek n. 捉迷藏
hidebound adj. 顽固的，心胸狭窄的
hideous adj. 讨厌的，丑恶的
hideout n. 隐匿处
hiding adj. 隐藏的；躲藏的；n. 躲藏
hiding-place n. 躲藏处；储藏处
hidrogen n. 氢
hie vt. 急忙,疾走,催促
hierarchical a. 分级的，分层的
hierarchy n. 阶层，等级制度
hieroglyph n. 象形文字，图画文字
hieroglyphic adj. 象形文字 (式) 的,图画文字的
high adv.高高地 adj.高的
highborn a. 出身名门的
highbrow n. 自以为文化修养很高的人
high-caliber a.高质量的
higher a. 较高的
highest a. 最高的
high-flown adj. 夸张的，好高骛远的
high-frequency a. 高频的
high-handed a. 专横的
highjack  v. = hijack 抢劫,劫持,揩油
high-jacker 动机者
highland n. 高地,丘陵地带
Highlander n. 高地的人,苏格兰高地地区的人
highlight n. 增强亮度，提示区；最重要的部分，最精彩的场面；vt. 使显著，使突出，着重
highlighter n.亮光笔
highly adv. 高度地；非常；很，十分，赞许地
highly-academic a. 注重书本知识的
highness n. 高,高度,殿下
high-pitched adj. 尖声的，高声的
high-spirited a. 勇敢的,精神充沛的,热血男儿的
hight a. (古，诗)被称为…的
high-technology n.(=high-tech)高科技
highway n.公路；大路
highwayman n. 路劫,拦路强盗
hijack vt. 抢劫,劫持,揩油
hijacker n. 栏路抢劫者
hijacking 劫持飞机
hike vi.作长途徒步旅行
hilarious adj. 高兴的，热闹的；充满欢乐的，引起大笑的
hilarity n. 欢乐，热闹
hill n.小山
hillock n. 小丘,小高处,土堆
hillside n.(小山)山腰，山坡
hilltop n. 小山顶
hilly a. 多丘陵的,多山岗的,险峻的
hilt n. （剑或刀之）柄
him pron.他(宾格)
himalaya n. 喜玛拉雅山
himself pron.他自己；他亲自
hin n. 欣(液体计量单位)
hind adj.后面的，后部的
hinder v. 阻碍，妨碍
hinderance n. (to)妨碍，障碍
hindmost a. 最后面的,最后部的
hindrance n.障碍，妨碍
Hindu n.信奉印度教的印度人
hinge n.合页，折叶，铰链
hinged a. 用(有)铰链的
hint n.暗示，示意；建议
hinterland n. 内地；穷乡僻壤
hip n.臀部，髋；屋脊
hippodrome n. 竞技场
hippopotamus n. 河马
hire vt.租借 n.租用，雇用
hireling n.佣工
hirsute adj. 多毛的
his pron.他的
hiss n.嘶嘶声 vi.嘶嘶作声
hist int. (唤人注意,禁止作声等场合用的字)嘘!
histology n. 组织学(研究细胞之学科)
historian n.历史学家；编史家
historic adj.有历史意义的
historical  adj.有关历史的；历史(上)的；根据历史上的发展叙述的
history n.历史，历史学
histrionic adj. 演戏的，剧院的
histrionics n. 演戏，表演
hit vt.打；击中；撞
hitch v. 搭便车，套住
hitchhike v. 搭车旅行；vt. 免费搭便车
hitch-hike vi. 搭便车
hither a. 这边的,在这边的
hitherto ad.迄今，到目前为止
hitler n. 希特勒(纳粹头目)
hitorical a. 历史的，有关历史的
hive n.蜂房；蜂箱
hives n. 麻疹,假膜性喉头炎
hmm interj. 哼！(踌躇等)
ho int. 引人注意,表示惊讶,满足
hoar a. 白的,灰色的,发白的
hoard n./v. 贮藏，秘藏
hoarding n. 收藏，贮藏
hoarfrost n. 霜,白霜
hoarse adj.发音嘶哑的
hoarsely ad. 嘶哑地
hoary adj. （头发）灰白的，古老的
hoax n./v. 骗局，欺骗
hobble v. 蹒跚，跛行
hobby n.业余爱好，癖好
hobgoblin n. 妖魔，恶鬼，怪物
hobnail n. 鞋钉,穿上钉鞋的人,乡下佬
hock n. 踝关节,德国产白葡萄酒,服刑所
hockey n. 曲棍球
hocus-pocus n. 戏法,奇术,变戏法的咒文
hod n. 木制容器,煤斗,装木炭容器
hodge 豪奇(男名)
hodgepodge n. 混杂物；大杂烩
hoe vt.&vi.锄地
hog n. 猪,贪婪者,象猪般的人
hogshead n.大桶
hoist vt.升起 vi.扯起来
hold vt.抓住；抑制
hold...against 记恨
hold...back 阻止
hold-all 手提旅行包
holder n. 持有人,所有人,支持物
holding n. 把持,支持,保持
holdup n. 拦劫行人的强盗行为,劫盗,停顿,
hold-up n. 停顿，耽误
hole n.洞；孔眼，裂开处
holiday n.假日，节日；假期
holiness n. 神圣,纯洁,洁白
holistic a.全盘的；整体的
Holland n.荷兰(欧洲)
hollow a.空的；空洞的
holly n. 冬青树
hollyhock n. 蜀葵
hollywood  n. 好莱坞(美影业中心)
holm n. (河，湖中的)小岛
holocaust n. 焚毁；大屠杀，浩劫
holograph n. 亲笔信
holp...back 阻止
holster n. 手枪皮套
holy a.神圣的；圣洁的
homage n. 效忠，崇敬
home adv.回家，在家 n.家
home-appliance 家庭用具
home-freight 回头运费，回程运费
homeland n. 祖国
homeless a. 无家的,无养主的
homelike a. 在自己家似的,舒适的,自在的
homely a.家庭的；家常的
homemade a. 自制的，本国制的；国产的；家庭制的
home-made a. 自制的
homemaker n. 持家的妇女，主妇
homeopathy n. 顺势疗法
homeostasis  n. 体内环境恒定
homer n. 荷马(希腊诗人)
homesick a. 思家的,思乡病的
homesickness  n. 乡愁,怀乡病
homespun adj. <布>手织的
homestay n.在当地居民家居住
homestead n. 家园,田产
hometown n. 家乡
homeward a. 在归途上的,向家的
homewards ad. & a. 回家(的)
homework n.家庭作业
homicide n. 杀人,杀人者
homiletics n. 讲道术，说教术
homily n. 说教,训诫
hominy n. 玉米粥
homo n. 『分类』人属
homogeneous a.同类的；均匀的
homogenize v. 使均匀，使一致
homogenous adj. 同质的，同类的
homograft n. 同种移植(物或术)
homograph n. 同形异义字
homonym n. 同音异义字,同名异物
hone n. 细磨刀石，v. 磨刀
honest a.诚实的；可敬的
honestly ad. 诚实地；老实地
honesty n.诚实，正直
honey n.蜂蜜；蜜
honeybee n.蜜蜂
honeycomb n.蜂窝
honeydew n.甘汁；蜜露
honeyed a. 多蜜的；甜如蜜的
honeymoon n.蜜月
honeysuckle n. 忍冬,金银花
honk n. 汽车喇叭声，雁叫声
honor n.荣誉；尊敬；敬意
honorable a. 值得尊敬的,荣耀的,高贵的
honorably ad. 光荣地；光明正大地
honorarium n. 酬劳金，谢礼
honorary a. 荣誉的,名誉的,道义上的
honored 已承兑或付款的
honour vt.给...以荣誉
honourable a. 诚实的；光荣的；荣誉的；正直的
honours n. 勋位，优等成绩
hood n. 头巾，兜帽
hooded adj. 戴头巾的
hoodwink v. 蒙混，欺骗
hoof n. （牛马的）蹄
hook vt.用钩连接，用钩挂
hooked  adj. 钩状的；上瘾的；钩形的，着迷的
hookworm n. 十二指肠虫,十二指肠病
hooligan n. 流氓，歹徒
hoop n. （桶之）箍，铁环
hooray interj. 好哇！
hoot n. 叫嚣,嘲骂声,鸣响
hop vi.跳舞；(人)单足跳
hope n.&vt.&vi.希望
hopeful  adj.有希望的；激励人的；怀有希望的，抱有希望的
hopefully adv. 可以指望；抱着希望地
hopeless a.没有希望的，绝望的
hopelessly ad. 无希望地，绝望地
hopper n. 单足跳者
horde n. 群众，一大群
horizon n.地平线；眼界，见识
horizontal a.地平的；水平的
horizontally ad. 水平地
hormone n. 激素，荷尔蒙；内分泌
horn n.喇叭
hornet n. 大黄蜂类,难缠的人物
hornless  adj. 无角的
hornpipe n. 角笛号管
horny a. 角的,角状的,角质的,老茧的
horology n. 测时法，钟表制造术
horoscope n.  (占星用的) 天宫图,十二宫图
horrendous adj. 可怕的，令人惊惧的
horrible adj.可怕的；极讨厌的
horribly ad. 恐怖地
horrid a. 可怕的,极可厌的,毛骨悚然的
horrify vt. 吓,使战悚,惊骇
horror n.恐怖；厌恶
horse n.马
horseback n. 马背
horsehair n.马毛
horseless a. 无马的
horseman n. 骑马者,马术师,养马者
horsemanship n. 马术
horsepower n.马力
horse-power n. 马力
horse-riding 骑马
horseshoe n. 马蹄铁
hortative adj. 激励的
hortatory  adj. 劝告的; 忠告的; 激励的
horticultural a. 园艺的
horticulture n. 园艺学
hose n.长筒袜；软管
hosepipe n. 水管；v. 以水管浇洗
hosiery n.袜子，针织衣物
hospice n. 旅客住宿处,收容所
hospitable a. 宜人的，有利的；好客的
hospital n.医院
hospitality n.好客，殷勤；宜人
hospitalize vt. 把…送入医院治疗
host n.主人；东道主
hostage n.人质，抵押品
hostel n. 宿舍,旅店
hostelry n. 旅社,客栈
hostess n.女主人；空姐
hostile a.敌方的；不友善的
hostility n. 敌对状态，敌意
hot a.热的；刺激的；辣的
hotbed n. 温床，滋长地
hotdog n. 热狗(面包)
hotel n.旅馆
hotelling n. 旅馆业
hothouse n. 温室,温床,干燥室
hotline n.热线
hotly ad. 发怒地；热烈地
hound n.狗；角鲨；卑鄙的人
hour n.小时；时间，时刻
houri n. 天堂女神,迷人的美女
hourly a. 每小时的,以小时计的,频繁的
house n.房屋，住宅；商号
household n.家庭，户；家务
householder n. 一家之主,家长,户长
housekeeper n. 主妇,女管家
housekeeping n. 家事,家政,持家
housemaid n. 女佣
housetop n. 屋顶
housewife n.家庭主妇
housewifery n. 家政,家事
housework n.家务劳动
housing n. 住房供给,住房建筑,马衣,装饰
houston n. 休斯顿(美国港市)
hovel n. 茅舍，肮脏的小屋
hover vi.徘徊；傍徨；翱翔
hovercraft n. 气垫船
hover-ferry n.气垫渡船
hovertrain n. 气垫火车
how ad.怎么；怎样；多少
howbeit ad. 然而,仍然
howe 豪(姓)
however adv.可是，不过
howitzer n. 榴弹炮
howl n.嚎叫；哀号 vi.吠
howler n. 嚎叫的人或动物，滑稽可笑的错误
howsoever adv. 无论如何
hoyden n. 粗野的女孩，野丫头
hub n. 轴心，中心
hubbub n. 嘈杂，喧哗
hubris n. 过份自傲，目中无人
huckleberry n. 越橘类
huckster n. 叫卖小贩，零售商
huddle v. 挤成一堆n. 一堆人（杂物）
hudson n. 哈得孙河(美国)
hue n. 色彩，色泽
huff vt. 吹胀,提高价格,激怒,发怒
huffy adj. 愤怒的，暴躁的
hug vt.搂 n.紧紧拥抱
huge adj.巨大的
hugo n. 雨果(法国小说家)
huh 哼
hulk n. 废船，笨重之人或物
hulking adj. 笨重的
hull n.外壳，豆荚；薄膜
hullo int. 喂
hum n.嗡嗡声 vt.哼曲子
human n.人 adj.人的,人类的
humane adj. 人道的，慈悲的
humanism n. 人道主义
humanist n. 人类学者,人道主义者,人文学者
humanitarian a.博爱的 n.慈善家
humanity n.人类；人性，人情
humanize vt. 赋予人性,教化,使通人情
humankind n. 人类
humble a.谦逊的；地位低下的
humbleness n. 谦逊,卑贱,粗鄙
humbler a. 较低级的
humbly ad. 恭顺地，谦卑地
humbug vt. 欺骗,欺诈,瞒骗
humdrum adj. 单调的，乏味的
humid  adj.湿的，湿气重的；潮湿的
humidify vt. 使湿润
humidity n.湿气；湿度
humiliate v. 使屈辱，使丢脸
humiliating adj. 叫人丢脸的
humiliation n. 耻辱,丢脸,谦卑
humility n. 谦逊，谦恭
huminity 湿度
humming a.发出嗡嗡声的
hummingbird n. 蜂鸟
hummock n. 小园丘
humor n. 幽默,诙谐,心情
humorist n. 有幽默感的人
humorous a.富于幽默的，诙谐的
humour n. 幽默；诙谐，滑稽；情绪；幽默感；v. 纵容，迁就
humourous a. 幽默的，诙谐的
hump n.驼峰；驼背 vi.隆起
humpback n. 驼背,座头鲸,小鲑鱼
humph int. 哼
humus n. 腐殖质
hunch n. 直觉，预感
hundred num.百，百个 n.许多
hundredth a. 第一百的
hundredweight  n. 英担
hung hang的过去式(分词)；挂；挂(hung=hanged)
Hungarian adj.匈牙利的
Hungary n. 匈牙利
hunger n.饿，饥饿；渴望
hungry a.饥饿的；渴望的
hunk n. 大块（食物）
hunt vi.打猎
hunter (姓)亨特
hunting n. 打猎；狩猎
huntress n. 女猎师
huntsman n. 猎人,管猎犬者
hurdle n. 跳栏，障碍
hurl vt.猛投 vi.猛冲
hurly-burly n. 喧闹，骚动
huron n. (北美)休伦族
hurrah int.好哇，万岁，乌拉
hurricane n.飓风，十二级风
hurried a. 仓促的，慌忙的
hurriedly  adv. 匆促地,慌忙地
hurry vi.赶紧 vt.催促
hurt vt.使受伤；使痛心
hurtful a. 造成损害的,有害的,伤害的
hurtle vi. 碰撞,突进
husband n.丈夫
husbandman n. 农夫,百姓
husbandry n. 耕种，务农
hush n.沉默 int.嘘！
husk n. 外壳，皮，荚
husking n. 农家碾米会
husky adj. 声音沙哑的
hussar n. 轻骑兵
hussy n. 轻佻的女子
hustings n. 竞选演员，讲坛
hustle n. 急速活动,挤,推,拥挤喧嚷
hustler n. 非常活跃之人
hut n.小屋；棚屋；茅屋
hutch n. 箱,厨,笼,小屋
huxley 赫胥黎(英国生物学家)
huzza int. 万岁!好啊!
hyacinth n. 风信子,橘红色,风信子石
hybrid n. 杂种，混血人
hybridization n. 杂交,配种,杂种培殖
hydra n. 水螅
hydrangea n. 八仙花属
hydrant n. 水龙头，消防栓
hydrate n. 水化物
hydraulic a.水力的；水力学的
hydraulics 水力学
hydrocarbon n. 烃，碳氢化合物；碳水化合物
hydrochloric  adj. 『化学』氯化氢的
hydroelectric a. 水力电气的
hydrogen n.氢
hydrophobia n. 恐水病,狂犬病
hydroplane n. 水上飞机,水上滑艇,水平舵
hydrosphere n. 水圈,水界,水气
hyena n. 土狼，鬣狗
hygiene n. 卫生学，卫生的
hygienic adj.卫生学的
hygienically 卫生地
hygrometer n. 湿度表
hymeneal a. 婚姻的
hymn n.赞美诗，圣歌；赞歌
hyperactive a.极度活跃的
hyperbole n. 夸张法
hyperbolic adj. 夸张的
hyperborean a. 极北的,严寒的
hypercritical adj. 苛求的，吹毛求疵的（
hyperinflation n.恶性通货膨胀
hypermarket n.特大百货商场，特大超级商场
hypersensitive adj. 过份敏感的
hyphen n. 连字号，即“-”
hypnosis n. 催眠状态
hypnotic adj. 催眠的
hypnotize vt. 施催眠术,使恍惚,使着迷
hypochondria n. 忧郁症，臆想病
hypochondriac n. 忧郁症患者的
hypocrisy n. 伪善，造作
hypocrite n. 伪君子,伪善者
hypocritical a. 伪善的,伪善者的
hypodermic adj. 皮下注射的
hypotenuse n. （直角三角形的）斜边
hypothalamic adj. 视丘下的
hypothecate vt. 抵押,担保
hypothecation n.抵押
hypothesis n.假设；前提
hypothetical adj. 假说的，臆说的
hypoxia n. 氧过少，低氧
hyssop n. 牛膝草
hysteria n. 歇斯底里症，过度兴奋
hysteric adj. 亢奋的
hysterical adj. 歇斯底里的，情绪激动的
hysterically adv. 歇斯底里地
I pron.(主格)我
i.e. (等于that is)那就是，即；(缩)即，也就是；即，就是(i.e.=that is)
iambic 『诗学』
ibidem ad. 在同书；在同处
ibis n. 朱鹭
ice n.冰
iceberg n. 冰山；流冰
ice-bound adj. 冰封的
ice-box n. 冰箱
icebreaker n. 碎冰船,破冰设备
icecream n.冰激淋
ice-cream n.冰淇淋
iceland n. 冰岛(欧洲)
ice-skate vi. 在冰上溜冰
ichneumon n. 姬蜂
icicle n. 冰柱，冰垂
icing n. 糖衣，糖霜
ick v. 踢；n. 踢
icon n. 图符，象征；圣像，偶像
iconoclast n. 攻击传统观念或风俗的人
iconoclastic adj. 破坏偶像的
icterus n. 黄疸
icy a.冰冷的；冷冰冰的
idaho n. 爱达荷
idea n.主意，念头，思想
ideal a.理想的；观念的
idealism n.唯心主义；理想主义
idealist n. 理想主义者,唯心主义者
idealize vt. 使理想化
ideally ad. 理想地；理论上
idears 主意
identical a.同一的；恒等的
identically ad. 相等，恒等
identification n.认出，鉴定；身份证
identify vt.认出，识别，鉴定
identity n. 同一性；特性
ideological a.意识形态
ideology n. 意识，意识形态
idiocy n. 愚蠢
idiom n.习语，成语
idiomatic a. 惯用的,通顺的
idiosyncrasy n. 个人心理上的特点；习性；癖性；特殊癖性或行为
idiosyncratic a. 特质的,异质的,特殊的
idiot n.白痴；傻子
idiotic a. 白痴的,愚蠢的,呆头呆脑的
idle a.空闲的；懒散的
idleness n.懒惰；赋闲无事
idler n. 懒惰者,游手好闲的人,惰轮
idly ad. 懒散地；漫不经心地
idol n. 神像、偶像
idolater n. 偶像崇拜者
idolatrous adj. 偶像崇拜的
idolatry n. 偶像崇拜,邪神崇拜,盲目的崇拜
idolize vt. 偶像化,极端崇拜,醉心于
idyl n.田园诗；牧
idyll n. 田园生活，田园诗
idyllic a. 田园诗的
if conj.假如，如果
iff conj. (数学)；if and only if当且仅当
igloo n. 冰屋
igneous adj. 火的，火绒的
ignite vt.引燃 vi.着火
ignition n. 点火,点燃,点火
ignoble adj. 卑鄙的，下流的
ignominious adj. 可耻的，屈辱的
ignominy n. 羞耻，屈辱
ignoramus n. 无知者，笨蛋
ignorance n.无知，无学，愚昧
ignorant a.不知道的；无知的
ignore vt.不顾，不理，忽视
ill adj.病的
i'll (同)i shall；i will
ill-educated a. 缺乏教育的
illegal a.不合法的，非法的
illegality n. 非法，违法
illegally adj. 非法地
illegible adj. 难读的，难认的
illegitimate adj. 不合法的，私生的
illiberal adj. 气量狭窄的，吝啬的
illicit adj. 违法的，违禁的
illimitable a. 无限的,无边际的
illinois n. 伊利诺斯(美国州名)
illiteracy n. 文盲
illiterate a.文盲的 n.文盲
ill-mannered a. 举止粗鲁的；无礼貌的；粗野的
illness n.病，疾病
illogical a. 不合逻辑的,不合理的
illotycin n. 红霉素
ill-treat vt.虐待,不友好地对待
ill-treatment  n. 虐待,苛待
illume vt. 照明,点亮,启发
illuminate vt.照明，照亮；阐明
illuminating adj. 启示性的，启发的
illumination n. 照明，古书上的图案、装饰
illumine vt. 照明,点亮,启发
illusion n.幻想；错觉；假象
illusive a. 幻影的,错觉的,迷惑人的
illusory adj. 虚幻的
illustrate vt.(用图等)说明
illustration n.说明，图解；例证
illustrative a. 说明的,解说的,做例证的
illustrator n. 插图画家
illustrious adj. 著名的，显赫的
i'm (同)i am
image n.像；形象；映象
imagery n. 肖像,比喻,雕刻
imaginable a. 可想象的,可能的
imaginary a.想象中的，假想的
imagination n.想象；想象力；空想
imaginative a. 想象的,虚构的
imagine vt.想象；设想
imbalance 失调，不平衡
imbecile n. 心智能力极低的人
imbecility n. 低能，愚蠢
imbibe v. 饮，吸入
imbroglio n. 纠纷，纠葛
imbrue vt. 涂,弄脏,染
imbue "with	v. 灌输（某人）强烈的情感或意见"
imitate vt.模仿，仿效；仿制
imitation n.仿制品，伪制物
imitative a. 喜模仿的,伪造的,摹拟的
imitator  (C) 模仿
immaculate adj. 洁净的，无瑕的
immanent adj. 普遍存在的，内在的
immaterial adj. 无关紧要的，非实体的
immature a. 不成熟的,未完全发展的
immeasurable a. 不可测量的,无限的,广大无边的
immediacy n. 立即，刻不容缓
immediate a.立即的；直接的
immediately adv. 立即；直接地；立刻，马上；紧挨着地；即刻；立即地
immemorial adj. 太古的，极古的
immense a.巨大的；极好的
immensely ad. 极大地，无限地
immensity n. 巨大之物，无限
immerse vt.沉浸；给…施洗礼
immersion n. 沉入，浸入
immigrant n.移民 a.移民的
immigrate vt.(使)移居入境
immigration n. 外来的移民,移居入境
imminence n. 急迫，危急
imminent adj. 即将发生的，逼近的
immiscible a. 不能混合的
immobility n. 不动性,不动,固定
immobilize v.使不能
immoderate adj. 无节制的，过度的
immodest a. 不谦虚的,冒失的
immodesty 无礼
immolate v. 牺牲，焚祭
immolation n. 牺牲品
immoral adj. 不道德的，淫荡的
immorality n.不道德; 品行不端正,淫荡
immortal a.不朽的；永生的
immortality n. 不朽,不朽的声名
immortalize vt. 使不灭,使不朽
immovable a. 固定的,不动的
immune adj. 免疫的，免除的
immunity n. 免疫，豁免
immunization n. 免疫
immunize vt. 使免疫，使免除；v. 使免疫
immunoglobulin n. 免疫球蛋白
immunosuppressive a. 抑制免疫反应的
immure v. 监禁
immutable adj. 不变的
imp n. 小鬼，顽童
impact n.影响，作用；冲击
impair v. 损害，使弱
impairment 减损，亏损
impale v. 刺穿，刺住
impalpable adj. 无法触及的，不易理解的
impart vt.给予，传递；告诉
impartial a.公正的，无偏见的
impartiality n. 公平,无私,不偏
impassable a. 不能通行的,无路可通的
impasse n. 僵局，死路
impassible a. 不觉痛苦的,无感觉的,无感情的
impassioned adj. 慷慨激昂的
impassive adj. 无动于衷的，冷漠的
impatience n. 性急,难耐,渴望,急躁,焦急
impatient a.不耐烦的，急躁的
impatiently ad. 不耐烦地，急躁地
impeach v. 指摘，弹劾
impeachment n.『法律』弹劾
impeccable adj. 无瑕疵的
impecunious adj. 不名一文的，贫困的
impede v. 妨碍
impediment n. 妨碍、阻碍物
impedimenta n. 随身携带物，行李
impel v. 推进，驱使
impend vi. 迫近,逼迫,悬挂
impending adj. 行将发生的，逼近的
impenetrable adj. 不能穿透的，不可理解的
impenitent adj. 不悔悟的
imperative adj. 急需的，必要的
imperceptible adj. 觉察不到的
imperfect a. 有缺点的,半完成的,减弱的,
imperfection n. 不完全,不完备,缺点
imperial a. 帝王的,至尊的,壮丽的
imperialism n.帝国主义
imperialist n.帝国主义者
imperil v. 使陷于危险中，危及
imperious adj. 傲慢的，专横的
imperishable a. 不灭的,不朽的
impermeable adj. 不可渗透的，不透水的
imperscriptible 没有文件证明的，非正式的
impersonal a. 客观的,和个人无关的,非人称的
impersonate v. 模仿，扮演
impertinence n. 鲁莽,无礼,不恰当
impertinent adj. 不恰当的，粗鲁的
imperturbability n. 沉着,冷静,自若
imperturbable adj. 冷静的，沉着的
impervious adj. 不能渗透的，不为所动的
impetuosity n. 激烈,猛烈,性急
impetuous adj. 冲动的，鲁莽的
impetus n. 推动力，刺激
impiety n. 无信仰,无信心,不虔诚,不孝
impinge vi. 撞击,紧密接触,侵犯
impious a. 无信仰的,不敬神的,不虔诚的,
implacable a.难宽恕的,难和解的,执拗的
implant v. 注入，灌输
implement n.工具，服装 vt.贯彻
implementation n. 实行，执行；实现履行执行程序，实施
implicate v. 牵连（于罪行中）
implication n.含义，暗示，暗指
implicit adj. 含蓄的，不言而喻的
implied adj. 暗含的，暗示的
implode v. 内爆，剧减
implore vt.乞求，恳求，哀求
implosion n. 向内破裂，内爆
imployer 雇主
imply vt.暗示，意指
impolite a. 无礼的,粗鲁的
impolitic adj. 不智的，失策的
imponderable adj. （重要性）无法衡量的
import vt.&n.输入，进口
importance n.重要；重要性
important a.重要的；有势力的
importation n. 进口,输入品
importer n. 输入者,进口商
imports 进口商品
importunate adj. 不断要求的，急切的
importune v. 强求，不断请求
importunity n. 硬要,强求
impose vi.利用；欺骗
imposing  adj.壮丽的，堂皇的；雄伟的；难忘的，外表强大的，体积巨大的
imposition n. 征收,课税,税款,欺骗
impossibility n. 不可能之事,不可能
impossible a.不可能的，办不到的
impost n. 税款,关税
imposter 冒名顶替者
impostor n.冒名顶替者，骗子
imposture n. 冒名顶替，欺骗
impotence n. 无力,虚弱,无效,阳萎
impotent adj. 无能的
impound 收押
impoverish v. 使成赤贫
impracticable a. 不能实施的,难办的,做不到的
impractical v. 不可行的
imprecate v. 祈求降祸，诅咒
imprecation n. 咒语，诅咒
imprecise adj. 不正确的
impregnable adj. 攻不破的，征服不了的
impregnate v. 怀孕，使充满
impregnation n. 受胎,受精,注入
impresario n. （剧院或乐团等）经理人，主办者
impress vt.印;留下极深的印象
impression n.印；印象；印记
impressionable adj. 易受影响的
impressionism 印象派
impressive a.给人印象深刻的
impressively 令人难忘地
impressiveness n. 感人
imprimatur n. 出版许可；赞许
imprint v. 盖印，刻印
imprison vt.关押，监禁；限制
imprisonment n. 关押；监禁
improbable a. 未必然的,不象发生的,似不可信的
impromptu adj. 即席的，即兴的
improper a.不适当的；不合理的
impropriety n. 不正当（的行为）
improve vt.使更好 vi.改善
improvement n.改进，改善；改进处
improvidence n. 无先见之明,浅见,浪费
improvident adj. 不顾将来的，不节俭的
improvisation n. 即席创作
improvise v. 即席而作
imprudent a. 轻率的,鲁莽的
impudence n. 厚脸皮,厚颜,无耻
impudent adj. 鲁莽的，冒失的，无礼的
impugn v. 指责，对…表示怀疑
impulse n.推动，冲力；冲动
impulsion n. 冲动,冲击,原动力,推动
impulsive adj. 易冲动的，感情用事的
impunity n. 免除惩罚
impure a. 不纯的,肮脏的,掺杂的,混合的
impurity n.不纯；杂质；不道德
imputation n. 归咎，归罪
impute "to	v. 归咎于"
in prep.在...里面
in...way 以…方式
inability n. 无能,无力
inaccessible a.达不到的，难接近的
inaccuracy n. 错误
inaccurate a.不精密的，不准确的
inaction n. 不活动,无为,怠惰,迟钝
inactivate vt. 使不活动
inactive a. 不活动的,停止的,怠惰的
inactivity n. 迟钝
inadequacy n. 不适当,不十分,不完全
inadequate a.不充足的，不适当的
inadequately ad. 不充分地
inadmissible a. 不可许可的,难承认的
inadvertence n.不注意,粗心
inadvertent adj. 不注意的，疏忽的
inadvisable a. 不受劝告的,不聪明的,不得体的,
inalienable adj. 不可剥夺的
inane adj. 无意义的，空洞的
inanimate adj. 无生命的
inanition n. （因无食物和水而）身体虚弱，死气沉沉
inanity n. 无意义，无聊
inapplicable a. 不适用的
inappreciation n.不欣赏；不正确
inappropriate a. 不适当的,不相称的
inapt a.不适当的，不合适的
inarticulate a. 口齿不清的,说不出的,不善于表达的
inasmuch ad.因为，由于
inattention n. 不注意,粗心,疏忽
inattentive a. 不注意的,怠慢的,疏忽的
inaudible a. 听不见的,不可闻的
inaugural a. 就任的,就职的,开始的
inaugurate vt.开始；使就职
inauguration n. 就任,就职
inauspicious a. 不吉的,凶兆的,恶运的
inborn adj. 天生的，天赋的
inbound 归航，入境
inbred a. 天生的,生来的,同系繁殖的
incalculable a. 无法计数的,无数的,无数量的
incandescent adj. 白热的，热烈的
incantation n. 咒语
incapable a.无能力的；无资格的
incapacitate vt. 使无能力,使不能胜任,使不适当
incapacity n. 缺乏能力
incarcerate v. 下狱，监禁
incarnadine a. 肉色的,深红色的
incarnate adj. 具有肉体的，化身的
incarnation n. 具体化，化身
incautious a. 不小心的,轻率的,不注意的
incendiary adj. 放火的，纵火的
incense n.香，熏香；香气
incentive n. 刺激，鼓励
inception n. 开端，开始，取得学位；发端
incertitude n. 疑惑，不确定
incessant adj. 无间断的，连续的
incessantly ad. 不断地，不停地
incest n. 近亲相奸,乱伦
incestuous a. 近亲相奸的,乱伦的
inch n.英寸
inchoate adj. 刚开始的，未发展的
incidence n.发生，影响；入射
incident n.小事件；插曲；事变
incidental a. 附带的,偶然的,容易发生的
incidentally adv.顺便说一下；附带地；顺便提及；偶然地，另外；附带提及地，顺便地
incinerate v. 焚化，毁弃；烧成灰；烧尽
incipience n. 初期
incipient adj. 初期的，刚出现的
incise v. 切，切割
incision n. 切口，切割
incisive adj. 一针见血的
incisor n. 门牙
incite v. 激发，刺激
incitement n.刺激,鼓舞,煽动
incivility n. 无礼，粗鲁
inclemency n. 险恶,严酷
inclement adj. （天气）严酷的，严厉的
inclination n.倾斜，点头；斜坡
incline n.斜坡 vt.使倾斜
inclined  adj. 倾斜的；倾向于…的；倾向于，赞成的
inclose vt. 围起来,附上
inclosure n. 围笼,附件
include vt.包括，包含
included 已包括的
including prep. 包括；包含
inclusion n. 包含,内含物
inclusive a.包围住的；包括的
incognito n./adj. 隐姓埋名的，化名
incoherent adj. （思想文字）不连贯的
incombustible a. 不燃性的
income n.收入；收益；进款
incommensurate adj. 不成比例的，不相称的
incommodious adj. 不方便的，狭小的
incommunicable a. 不能传达的
incommunicado adj. 被单独监禁的
incommunicative adj. 不爱交际的，沉默寡言的
incomparable a. 无比的,无双的,不能比较的
incompatibility n. 不兼容
incompatible a.不相容的
incompetence  n. 无能力; 不能胜任; 无资格
incompetent adj. 无能力的不能胜任的
incomplete a.不完全的，未完成的
incomprehensible a. 不能理解,费解的,无限的
incompressible a. 不能压缩的
inconceivable adj. 难以想象的，不可能的
incongruity n. 不一致
incongruous adj. 不调和的，不相称的
inconsequential adj. 不重要的，微不足道的
inconsiderable a. 不足取的,琐屑的
inconsiderate adj. 不体谅别人的
inconsistency n. 不一致,不调和,矛盾
inconsistent a. 不一致的,不合理的,矛盾的
inconsolable adj. 无所慰籍的，极度沮丧的
inconspicuous a. 不显眼的,不引人注意的
inconstancy n. 易变,不定性,无节操,反复无常
inconstant adj. 多变的，无常的
incontestable adj. 无可争辩的，明确的
incontinence n. 无节制,失禁
incontinent adj. 无力控制（自己）的，纵欲的
incontrovertible a. 无争论余地的,无疑的,明白的
inconvenience n. 不便,困难
inconvenient adj. 不方便的
inconvertibility 不可兑换
incorporate vt.结合，合并，收编
incorporated adj. 有限的
incorporation n. 结合,编入,团体组织
incorporator 公司创办人；社团成员
incorporeal adj. 无形体的，非物质的
incorrect a.不正确的，错误的
incorrigible adj. 积习难改的，不可救药的
incorruptible a. 不腐败的,不能收买的,清廉的
incoterms n. (缩)国际贸易术语
incovenient adj. 不方便的
increase vt.&vi.&n.增加
increasing adj. 不断增长的；递增的
increasingly ad.日益，越来越多地
incredible a.难以置信的，惊人的
incredibly adv. 难以置信地；惊人地
incredulity n. 不易相信,深疑,怀疑心
incredulous a. 怀疑的,不轻信的
increment n. 增值，增加
incriminate v. 连累，牵连
incubate vt. 抱,孵,培养,使发展
incubation n. 潜伏；酝酿；孵卵期，潜伏期
incubator n. 孵卵器，早产婴儿保育箱
incubus n. 恶梦，负担
inculcate v. 灌输，谆谆教诲
incumbency n职责，义务
incumbent n. 在职者，现任者
incur v. 招惹
incurable adj. 无可救药的
incursion n. 侵犯，入侵
indebted adj. 感激的，感恩的
indebtedness n.受恩; 负债
indecent a. 下流的,不妥当的
indecipherable adj. 不可破译的
indecision n. 优柔寡断
indecisive a. 非决定性的,犹豫不决的,不明确的
indecorous a. 无体的,不合礼节的
indeed adv.的确；真正地
indefatigable adj. 不知疲倦的
indefeasible a. 难使无效的,不能废弃的
indefinable a. 不可名状的
indefinite a.无限期的
indefinitely adv. 不明确地；模糊地；无限期地；无限地，无穷地
indelible adj. 擦试不掉的，不可磨灭的
indemnification n. 赔偿，赔偿金；给予赔偿补偿
indemnify v. 赔偿，偿付
indemnity n. 赔偿,补偿,保护
indent v. 切割成锯齿状
indentation n. 锯齿状，缺口
indented adj. 锯齿状的
indentor n.国外订货商
indentors 国外订货商
indenture n. 契约，合同
independence n.独立，自主，自立
independent a.独立的；自主的
independently adv. 独立地；自由地；独自地，单独地；a. 独立地
indescribable adj. （美得）无法形容的
indespensability n. 不可少，必需
indestructible a. 不能破坏的,不可毁灭的
indeterminate a. 不确的,不确定的,含混的
index n.索引；指数；指标
indexing n. 变址，标引，加下标
India n.印度
Indian adj.印度的 n.印度人
indiana n. 印第安纳(州)(美国)
indicate vt.标示，表示；表明
indication n.指示；表示；表明
indicative a.指示的；陈述的
indicator n. 指示者，指示物
indict v. 控诉，起诉
indictment n. 起诉,控告,起诉状
indictor 指标
indies n. 东(西)印度群岛
indifference n. 冷淡，不关心；无足轻重；无差别，中性
indifferent a.冷漠的；不积极的
indifferently ad. 不在乎地；不关心地；冷淡地
indigence n. 贫乏,穷困
indigenous adj. 土产的，本地的
indigent adj. 贫穷的，贫困的
indigestible a. 不消化的,难消化的,难理解的
indigestion n. 消化不良
indignant a.愤慨的，义愤的
indignantly ad. 愤慨地，义愤地
indignation n.愤怒，愤慨，义愤
indignity n. 侮辱
indigo n. 靛篮，深蓝
indirect a.间接的；不坦率的
indirectly adj. 间接地；迂回地
indiscernible adj. 看不清的
indiscreet adj. 不谨慎的，无礼的
indiscretion n. 不谨慎的、鲁莽的
indiscriminate adj. 不加选择的
indispensable a.必不可少的，必需的
indisposed adj. 不愿意的，身体不适的
indisposition n. 小毛病,厌恶
indisputable a. 无争论之余地的,明白的
indissoluble a. 不能溶解的,不能分解的,坚固的
indistinct a. 不明了的,朦胧的
indistinguishable a.不能辨别的，难区分的
indite v. 作诗，写作
individual a.特殊的
individualism n. 个人主义
individuality n. 个性
individually adv. 个别地；单独地
individuate vt. 使个体化，使具个性
indivisible adj. 不可分割的，不可分裂的
indocile adj. 不听话的，难顺服的
indoctrinate v. 灌输思想
indolence n. 怠惰,不痛
indolent adj. 懒惰的，懒洋洋的
indomitable adj. 坚强不屈的
indonesia n. 印度尼西亚
indoor adj. 室内的；室内进行的；屋里的
indoors adv.在屋里；进入室内
indorse 背书
indubitable adj. 不容置疑的
indubitably adj. 无疑地
induce vt.劝诱；引起；感应
induced 劝诱
inducement n. 引诱物
induct v. 使就职，使入伍
induction n.就职；归纳推理
inductive a. 归纳的,动人的,感应的
indulge vt.放纵(感情)vi.纵情
indulgence n. 沉溺,放纵,嗜好
indulgent a. 纵容的,任性的,放纵的
industrial a.工业的；产业的
industrialist n. 实业家
industrialization n. 工业化
industrialize v. 使工业化
industrialized adj. 工业化的
industrious a.勤劳的，勤奋的
industry n.工业，产业；勤劳
inebriate v. 使醉，n. 酒鬼，酒徒
inebriety n. 醉,陶醉
ineffable adj. 妙不可言的，说不出的
ineffaceable adj. 抹不掉的，不能消除的
ineffective a. 无效的
ineffectiveness n. 低效率
ineffectivesupply 无效供应
ineffectual a. 无效的,无益的,白费的
inefficiency n. 无效率,无能
inefficient a.效率低的，无能的
inelastic 无弹
ineligible adj. 无资格的，不适当的；没资格的，不妥当的
ineluctable adj. 难免的，不能逃避的
inept adj. 无能的，不适当的
ineptitude n. 愚蠢无能；无能，不称职
inequality n. 不平等,不同,不平均
inert adj. 惰性的，行动迟钝的
inertia n.惯性，惯量；无力
inertial a. 惯性的，惯量的
inessentials 非必需品
inestimable a. 无价的,无法估计的
inevitability n. 不可避免，必然性
inevitable a.不可避免的，必然的
inevitably ad. 必然地；不可避免地；不可避免的
inexact a. 不准确的，不精确的
inexcusable a. 没法辩解的,不可宽赦的
inexhaustible adj. 用不完的，取之不竭的
inexorable adj. 不为所动的，坚决不变的
inexpedient adj. 不适当的，不明智的
inexpensive a.花费不多的，廉价的
inexperience n. 无经验,不熟练,未熟
inexperienced a. 无经验的,不熟练的
inexpert a. 不熟练的
inexpiable adj. 不能补偿的
inexplicable adj. 无法解释的，难理解的
inexpressible a. 不能用语言表达的,不可言传的,
inextinguishable a. 不能消灭的,压不住的
inextricable adj. 无法摆脱的，纠缠的
infallibility n. 绝对可靠
infallible adj. 绝不会错的，绝对可靠的
infamous adj. 恶名昭彰的，邪恶的
infamy n. 恶名昭彰
infancy n. 幼年,初期,幼儿期
infant n.婴儿 a.婴儿的
infanticide n. 杀婴
infantile adj. 幼稚的，幼儿的
infantine a. 小孩似的
infantry n. 步兵
infatuate vt. 使迷恋,使糊涂
infatuated adj. 迷恋(人)的
infatuation n. 迷恋
infeacible a. 不能实行的，不可能的
infeasible 不可行，非适宜
infect vt.使受影响
infection n. 传染,影响,传染病
infectious a.传染的；感染性的
infective a. 易传染的，传染性的
infelicitous adj. 不妥当的，不得体的
infer vt.推论，推断；猜想
inference n.推论；推断的结果
inferior n.下级；晚辈，次品
inferiority n. 自卑感
infernal adj. 地狱的，可恶的
inferno n. 火海，地狱般的场所
infertile adj. 无法生殖的，不毛的；不肥活的；不结果实的
infest v. 骚扰，扰乱
infidel n. 不信教者，异教徒
infidelity n. 不忠实，不贞
infiltrate v. 渗透，渗入
infiltration n. 浸润；渗入
infinite n.无限；无穷(大)
infinitely adj. 极大地；adv. 无限地；无边地
infinitesimal adj. 极微小的
infinitive n. 不定词
infinitude n. 无限,无穷,无量
infinity n.大量，大宗；无穷大
infirm a. 弱的,虚弱的,柔弱的
infirmary n. 医院,医务室
infirmity n. 虚弱
inflame v. 使燃烧，激怒（某人）
inflamed adj. 发炎的，红肿的
inflammable adj. 可燃的，易激怒的
inflammation n. 怒火,发火,燃烧,发炎
inflammatory a. 激动的,煽动的,炎症性的
inflatable a. 可膨胀的，充气的
inflate v. 使膨胀；使得意；使充气，使物价上涨
inflated adj. 涨大的；充气的，骄傲的
inflatee 通货膨胀受害人
inflation n.通货膨胀，物价飞涨
inflection n. 屈曲,变调,音调变化
inflexible a. 不屈曲的,不屈挠的,顽固的
inflict vt. 施以,加害,科以,使承受
infliction n. （强加于人身的）痛苦，刑罚
inflow 流入
influence n.势力，权势
influential a.有影响的；有权势的
influenza n. 流行性感冒
influx n. 涌入
inform vt.通知，向…报告
informal a. 非正式的,不拘礼的,通俗的
informant 填报者
information n.消息，信息；通知
informative adj. 提供资料的
informer n. 告发者，告密者
infraction n. 违法
infrared a. 红外线的；红外区的；红处的
infra-red a. 红外线的
infrastructure n.基础结
infrequent a. 稀少的,珍贵的,罕见的
infrequently adv. 不经常地；少有
infringe v. 违反，侵害
infringement n. 违反，侵害
infuriate v. 使（人）极为愤怒
infuse v. 灌输，使…充满
infusion n. 灌输。激励
ingenious a.机灵的；精巧制成的
ingenue n.天真无邪
ingenuity n.机灵；设计新颖
ingenuous adj. 纯朴的，单纯的
ingest v. 摄取；吸收；咽下；吞下
ingestion n. 咽下；吸收
ingle n. 壁炉；火焰
inglorious a. 不名誉的,不体面的,可耻的,
ingot n. 锭,铸块
ingrain vt. 生染,就原料染色,使根深蒂固
ingrained adj. 根深蒂固的
ingrate n. 忘恩负义的人
ingratiate v. 逢迎，讨好
ingratiating adj. 讨好的，谄媚的
ingratitude n. 忘恩负义
ingredient n.配料，成分
ingress n. 进入
inhabit vt.居住于，栖息于
inhabitant n.居民，住户
inhalation n. 吸入
inhale v. 吸气
inharmonious a. 不合谐的,不和睦的
inhere vi. (in)本质上即属于；生来即存在于
inherent a.固有的，生来的
inherit vt.继承(传统等)
inheritance n. 遗传,遗产
inheritor n. (遗产) 继承人
inhibit vt. 禁止,抑制
inhibit...from 禁止...做某事
inhibited adj. 拘谨的，拘束的
inhibition n. 禁止,禁制,压抑
inhospitable a. 冷淡的,不和气的,不亲切的
inhuman adj. 残忍的
inhumane adj不近人情的
inhumanity n. 不人道,残暴
inimical adj. 为敌的，不友善的
inimitable adj. 无法仿效的，不可比拟的
iniquitous adj. 邪恶的，不公正的
iniquity n. 邪恶，不公正
initial a.词首的
initialize v. 初始化
initially adv. 最初，开始；开头
initiate vt.开始，创始；启蒙
initiation n. 开始,起蒙,入会
initiative a.创始的 n.第一步
inject vt.注射；注满；喷射
injection n.注射，注入；充满
injudicious a. 欠思考的,不聪明的,浅薄的
injunction n. 命令，强制令
injure vt.伤害，损害，损伤
injurious a. 有害的
injury n.损害，伤害；受伤处
injustice n. 不公正，非正义
ink n.墨水，油墨
inkhorn n. 墨水壶
inkling n. 暗示，细微的迹象
inkstand n. 墨水瓶
inkstone n. 砚
ink-well n.墨水池
inky a. 墨水的,给墨水弄污的,漆黑的
inland a.国内的；内地的
inlay vt. 嵌入,镶嵌,插入
inlet n.进口，水湾 vt.引进
inly ad. 在内,在心中,衷心地
inmate n. 同住者,居民
inmost a. 心底的,秘密的
inn n.小旅馆，客栈
innate adj. 生来的，天赋的
inner a.内部的；内心的
innermost a. 内心的,秘密的,最深处的
inning n. 一局,发展的机会,好时机,围垦
innkeeper n. 小旅馆 (inn) 的主人,客栈老板
inn-keeper n. 客栈老板，酒店主
innocence n. 无罪,无知,天真无邪
innocent a.清白的，幼稚的
innocently ad. 天真地，单纯地
innocuous adj. （行为，言论等）无害的
innovate v. 革新，变革，创始；创新，改革
innovation n.创新，改革，新设施
innovative 标新立异
innovator n. 发明者
innuendo n. 含沙射影，暗讽
innumerable a.无数的，数不清的
inoculate v. 预防注射
inoculation n. 接种，灌输
inoffensive a. 无害的,没恶意的,不讨厌的
inoperative a. 不活动的,无效力的,不发生效力的
inopportune 不凑巧，不合时宜
inordinate adj. 过度的，过份的
inorganic a.无生物的；无机的
inpatient 住院病人
in-patient n. 住院病人
input vt.输入 n.输入
inquest n. 审讯,讯问,验尸
inquietude n. 焦虑，不安
inquire vt.打听，询问；调查
inquirer n. 询问者,探究者,调查者
inquiringly adv. 好奇地
inquiry n.询问，打听；调查
inquisition n. 调查,探究,审理,宗教裁判所
inquisitive adj. 过份好问的，好奇的
inroad n. 侵袭，减少
inrush n. 水的涌入
insane adj. 疯狂的
insanity n. 疯狂，愚昧
insatiable a. 不知足的,贪求无厌的
inscribe vt. 登记,铭记于,题写,雕刻
inscribed 刻；写；记；写记
inscribing 注册；买或卖股票；登记
inscription n. 铭刻，题献
inscriptions 批注
inscrutable adj. 高深莫测的，神秘的
insect n.昆虫，虫
insect-eating a. 吃昆虫的
insecticide n. 杀虫剂
insecure a. 不安全的,不牢靠的,不坚固的,
insecurity n. 不安全,不安全感
inseminate v.使受孕；人工授
insensate a. 无感觉的,迟钝的,无生命的,
insensibility n. 无感觉,不在乎,不关心
insensible a. 不知的,昏迷的,无知觉的,冷淡的
inseparable a. 不能分的
insert vt.插入; 嵌入; 登载
insertion n. 插入，插入物
inside prep.在…里面 n.内部
insider n. 局内人，圈内人
insiders 内部人员
insidious adj. 祸害隐伏的
insight n.洞察力，洞悉，见识
insignia n. 徽章，袖章
insignificant a.无意义的；低微的
insincere a. 不诚实的,无诚意的,伪善的
insincerity n. 不诚实,无诚意,伪善
insinuate v. 暗指，暗示
insinuation n. 暗示,暗讽
insipid adj. 乏味的，枯燥的
insist vi.坚持；坚持要求
insistence n. 坚持，强求
insistent a.坚持的；逼人注意的
insofar adv. 在…范围内
insolate v. 使曝晒
insole n. 鞋内底,鞋垫
insolence n. 傲慢,无礼,傲慢的态度
insolent adj. 粗野的，无礼的
insoluble a. 不能溶解的,不能解决的
insolvable 破产，无力偿还债务
insolvency n. 无力偿还,破产
insolvent adj. 无钱还债的
insomnia n. 失眠症
insomuch ad. 由于,就此程度而言
insouciance n. 漠不关心
insouciant  adj. 漫不经心的; 无忧无虑的
inspect vt.检查，审查；检阅
inspection n.检查，审查；检阅
inspector n.检查员；巡官
inspiration n.鼓舞；激动人心的人
inspire vt.鼓舞；给…以灵感
inspired adj. 有创见的，有灵感的
inspiring adj. 鼓舞人心的
inspirit vt. 激励,精神,赋予元气,使振奋
instability n.不稳定性；不坚决
instable adj. 不稳定的；不固定的
install vt.安装，设置
installation n.安装；装置；设施
installment n.分期付款
installments n. 分期付款
instalment n. 就职,装设,分期付款
instalments 分期付款
instance n.例子，实例，事例
instant n.瞬间 a.立即的
instantaneous a.瞬间的，即刻的
instantaneously ad. 即刻地
instantly ad.立即，即刻
instead adv.代替，顶替
instep n. 脚背,背部,脚背形的东西
instigate v. 发起，煽动
instigation n. 煽动，刺激
instill v. 滴注，逐渐灌输
instinct n.本能；直觉；生性
instinctive a. 本能的
instinctively ad. 本能地
institute n.研究所；学院
institution n.协会；制度，习俗
instruct vt.教；指示；通知
instruction n.命令；教学；教训
instructive adj.有教育意义的
instructor n.指导者，教员
instrument n.仪器；工具；乐器
instrumental a.仪器的；有帮助的
instrumentality n. 帮助,媒介,手段
insubordinate adj. 不服从的，反抗的
insubstantial a. 脆弱的,无实体的,非实质的
insufferable adj. 无法忍受的
insufficiency n. 缺乏，不足之处
insufficient adj.不足的；不适当的；不充足的；无能的；不当；(for)不够的
insuficient a.不足的，不够的
insular adj. 岛屿的，心胸狭窄的
insularity n. 偏狭；心胸狭窄
insulate vt.使绝缘，使绝热
insulation n. 隔热
insulator n.隔离者；绝缘体
insulin n. 胰岛素
insult vt.&n.侮辱，凌辱
insuperable adj. 难以克服的
insupportable a. 忍耐不住的,不能忍受的
insurable 可保险的
insurance n.保险；保险费
insure vt.给…保险；确保
insured 被保险人；被保险的
insurer 保险人，保险业者
insurgent adj. 叛乱的，起事的n. 叛乱分子
insurmountable a. 不能克服的,不能超越的
insurrection n. 造反，叛乱
intact adj. 完整的，未动过的
intake n.吸入；输入能量
intangible adj. 不可捉摸的
intangibles 无形物
integer n. 完整的事物,整体,整数
integral a.组成的；整的
integrate vt.使结合，使并入
integrate...with... 使…与…结合
integrated adj. 全面的，统一的；整合的，完整的
integration n. 综合,完成,集成
integrative 综合的，一体化的
integrity n.诚实，正直
integument n. （水果等)外壳，包在外面的皮.
intellect n.理智，智力，才智
intellectual n.知识分子 a.智力的
intelligence n.智力；理解力；情报
intelligent a.聪明的；理智的
intelligently ad. 聪明地；理智地
intelligentsia n. 知识界
intelligible adj. 可了解的，清晰的
intemperance n. 不节制,过度,酗酒
intemperate adj. 无节制的，放纵的
intend vt.想要，打算；意指
intendant n. 监督官,管理者
intended 预测的
intense a.强烈的；紧张的
intensely ad. 强烈地；激烈地；热切地
intensify vt. 加强
intensity n.强烈，剧烈；强度
intensive a.加强的；精耕细作的
intent a.目不转睛的，热切的
intention n.意图，意向，目的
intentional a.故意的，有意识的
intently adv. 专心地
inter v. 埋葬
interact v. 相互影响；相互作用；n. 相互相作，相互影响
interaction n.相互作用；干扰
interactive a. 交互式，交互的
inter-bank 银行间的
inter-branch 分行往来
intercede v. 说好话，代求情
intercept v. 中途拦截，截取
intercession n. 仲裁,调解,说项
intercessor n. 仲裁者,调解人
interchange n. 立体交叉道,互换
interchangeable adj. 可互换的
inter-coast (美)国内沿海航行
intercolonial a. 殖民地间的
inter-communication 相互往来，交际，通路
intercompany 公司间的
inter-company 公司间的
interconnect v. 使互相联系；相互联系
interconnection n. 相互联系
interconnections n. 相互连接，彼此连系
inter-country 国际项目
intercourse n.交际，往来，交流
interdependence n. 互相依赖
interdependent a. 相互依赖的,互助的
interdict v. 禁止，切断（补给线）
interdiction n. 禁止,停止,禁止产宣告
interdisciplinary 各学科间的
interest vt.使发生兴趣 n.兴趣
interested adj. 感兴趣的；关心的；有兴趣；关注的
interest-free a.无息的
interesting a.有趣的，引人入胜的
interface n. 交界，接口；分界面；相交处；界面
interfere vi.干涉，干预；妨碍
interference n.干涉，干预；阻碍
interferon n. 干扰素
interfuse vt.vi. (使)混入,(使)混合
interim n. 过渡时期adj. 暂时的
interior n.内部 a.内部的
interject v.插
interjection n. 感欢词,插入之语词
interlace v. 编织，交错
interline 在…(承运人)之间；在之间
interlock v. 连锁，连串
interlocking a.相互扣连的
interlocutor n. 对话者，谈话者
interlocutory a. 对话的,对话体的,中间的
interloper n. (非法) 闯入者
interlude n. (活动间的)暂时休息
interlunar a. 看不见月亮期间的
intermarriage n. 通婚,异族结婚,近亲结婚
intermarry vi. 通婚,近亲结婚
intermeddle vi. 干涉,管闲事,多嘴
intermediary adj. 媒介的n. 中间人，媒介物
intermediate a.中间的；中级的
intermediator 仲裁人，居间者
interment n. 埋葬,土葬
interminable adj. 无尽头的
interminably ad. 没完没了地
intermingle v. 混合，搀杂
intermission n. 暂停，间歇
intermit vi. 暂时停止,中断
intermittent adj. 断断续续的，间歇的
intermix vt.vi. (使)混和,(使)混杂
intermixture n. 混合,混合物
intermodal 联运方式
intern v. 拘禁，软禁；拘留；扣留 n. 实习生
internal a.内的；国内的
internally ad. 在内(部)
international a.国际的，世界(性)的
internationalist ,"n. 国际主义者；adj. 国际主义的
internationalization n. 国际化
internationalize vt. 使国际化,置于国际管理下
internecine adj. 内讧的，两败俱伤的
internet n.国际互连网
internment n. 拘禁
interplay n. 相互影响
interpolate v. 加入(额外的事)，窜改
interpolation n. 插入，窜改
interpool n.国际联营
interpose v. 置于…之间，使介入
interposition n. 插入，干涉
interpret vt.解释，说明；口译
interpretability n. 配合动作性
interpretable a. 彼此协作的
interpretation n.解释；口译
interpreter n.译员，口译者
interregnum n. 无王时期，
interrelate v.(使)相互联系；互相关连，相关
interrogate v. 审问，审讯
interrogation n. 审问,问号
interrogative adj. 疑问的
interrupt vt.打断(讲话)；打扰
interrupted 受阴
interruption n.中断，打断；障碍物
intersect v. 横截，横断
intersection n. 横断，十字路口
intersperse v. 散布，点缀
interstate a. 州际的
interstellar a. 星际的
interstice n. 细裂缝，空隙
interstitial a. 组织间隙的，间质的
intertwine v. 纠缠，缠绕
intertwist vt.vi. (使)绞合,(使)搓合
interurban a. 都市间的
interval n.间隔；休息；间距
intervene vi.干涉，干预；播进
intervention n. 干涉
interview vt.采访
interviewee n.被访问者；被面谈者；被面试者
interweave v. 交织，编结
intestate adj. 未留遗嘱的
intestinal adj. 肠的
intestine n. 肠
intimacy n. 亲密，亲密的言行
intimate a.亲密的；个人的
intimately ad. 密切地；熟悉地
intimation n. 暗示,讽示,通知
intimidate v. 恐吓，协迫
intimidation n. 恐吓
into prep.进，入；进入到
intolerable a. 无法忍受的,难耐的
intolerably ad. 不能忍受的
intolerance n. 不宽容,偏狭,不容许相反的言论
intolerant adj.不容异已的
intonation n.语调，声调；发声
intone vt.vi. 吟咏
intoxicant adj. 醉人的
intoxicate v. 使醉，陶醉
intoxicating adj. 令人陶醉的
intoxication n. 使醉,沉醉状态,梦中
intracellular a. 细胞内的
intractable adj. 倔强的，难管的
intransigence n. 不妥协，不让步
intransigent adj. 不妥协的，固执的
intransitive n. 不及物动词
intra-trade 区域内贸易
intravenously ad. 静脉注射地
intrepid adj. 无畏的，刚毅的
intrepidity n. 无畏
intricacy n. 错综复杂
intricate adj. 复杂难懂的
intrigue v. 密谋，引起极大兴趣
intriguing adj. 引起极大兴趣的
intrinsic adj. 固有的，内在的
introduce vt.提出(议案等)
introduction n.介绍；引进；引言
introductory a. 介绍的,引导的,开端的
introspection n. 内省，反省
introspective adj. 反省的
introvert v. 内向的人
intrude v. 闯入，强行引入
intruder n. 侵入者,干扰者,妨碍者
intrusion n. 私闯，干扰
intrusive a. 打扰的,插入的
intrust vt. 信赖,信托,交托
intuition n. 直觉,直觉的知识
intuitive adj. 有直觉力的，直觉到的
intumescence n. 肿大，肿胀
inundate v. 淹没，泛滥
inundation n. 淹没
inure vt. 使习惯
inured adj. 习惯的
invade vt.入侵，侵略；侵袭
invader n. 侵略者
invalid n.病人 a.有病的
invalidate v. 使无效力，证明无效
invaluable a. 无价的,价值无法衡量的
invariable a. 不变的，永恒的
invariably adv.常常，总是；不变地，永恒地；adj. 不变地，总是
invasion n.入侵，侵略；侵犯
invation n. 侵入，侵略，侵犯
invective n. 猛烈抨击，痛骂
inveigh vi. 痛骂,漫骂,臭骂
inveigle v. 诱骗，诱使
invent vt.发明，创造
invention n.发明，创造
inventive a. 善于创造的,发明的
inventor n.发明者；发明家
inventory n. 详细目录，存货清单
inverse adj. 相反的，倒转的
inversely adv. 相反地
inversion n. 倒转,否定,倒置
invert v. 上下倒置，相反放置
invertebrate n./adj. 无脊椎的（动物）
invest vt.投资；投入
investee 接受投资者
investigate vt.&vi.调查
investigation n.调查，调查研究
investigator n. 研究者,调查者,审查者
investiture n. 任职仪式，授权仪式
investment n.投资，投资额，投入
investor n. 投资者
inveterate adj. 积习已深的
invidious adj. 惹人反感的，招人嫉妒的
invigilate v. 监考
invigorate v. 鼓舞，激励
invincible adj.战无不胜的
inviolability n. 神圣
inviolable adj. 不可侵犯的，不可亵渎的.
inviolate adj. 未受侵犯的，纯洁的
invisible a.看不见的，无形的
invitation n.请帖；邀请
invite vt.邀请，聘请；招待
inviting adj. 动人的；诱人的，引人入胜的；吸引人的
invocation n. 祈祷
invoice n.发票，发货清单
invoke v. 祈求，恳求，（法律的）实施生效.
involuntarily adv. 不自觉地
involuntary a. 自然而然的,无意识的,不随意的,
involve vt.使卷入；牵涉
involved adj. 涉及的，复杂的；有关的；有密切关系的
involvement n. 卷入，涉足
invulnerable adj. 无法伤害的
inward a.里面的 ad.向内
inwardly ad. 内向；独自地
inwards adv. 向内的
inwrought a. 织入的,刺绣的,嵌入的
iodide n. 碘化物
iodine n. 碘，碘酒
ion n. 离子
Ionic a. 离子的
ionosphere n. 电离层
iota n. 极小量，极少
IOU (=I owe you)n.借据
iowa n. 爱荷华(美国州名)
iran n. n. 伊朗(亚洲)
iranian n. 伊朗人；a. 伊朗的
iraq n. 伊拉克(亚洲)
iraqi n. 伊拉克人；a. 伊拉克的
irascible adj. 易发怒的.
irate n. 发怒的
ire n. 忿怒
ireful adj. 愤怒的
Ireland n.爱尔兰
iridescent adj. 闪光的，现晕光的
iris n. 虹膜，彩虹
Irish adj.爱尔兰的
Irishman n. 爱尔兰人
irk v. 使苦恼，厌烦.
irksome adj. 令人苦恼的，讨厌的
iron n.铁；铁制品
ironclad adj. 坚固的，装铁甲的
ironic adj. 挖苦的，出乎意料的；讽刺的，冷嘲的
ironical a. 讽刺的,用反语的
ironically ad. 讽刺地；易人啼笑皆非地
ironsides n. 铁甲军, 勇敢果断的人
ironworker n.钢铁工人
ironworks n. (用单或复)钢铁厂
irony n. 反话，出人意料的事情或情况
irradiate v. 使明亮，生辉
irradiation n.照
irrational a. 不合情理的
irreconcilable adj. 不能妥协的，不能和解的
irrecoverable a. 不能收回的,不能挽回的,不能复原的
irrecusable 法律上不可拒绝的
irrefragable a. 不能反驳的,不能否定的,不可争辩的
irrefutable adj. 不可辩驳的
irregular a.不规则的；不整齐的
irregularity n.不规则；不整齐
irregulars 等外品
irrelevant a. 不恰当的,无关系的,不相干的
irremediable a. 不能治疗的,不治的,不能挽回的
irreparable adj. 无法修复的，不能挽回的
irrepressible a. 镇压不住的,抑制不住的
irreproachable adj. 不可指责的，无过失的
irresistible adj. 无法抗拒的，无法抵抗的
irresolute a. 无决断的,优柔寡断的,踌躇不定的
irresolution n. 无决断,优柔寡断,无定见
irrespective a.不考虑的，不顾的
irresponsible a. 不负责任的,不可靠的
irretrievable a. 不能挽回的,不能复原的
irreverence n. 不敬,非礼,不敬的行为
irreverent adj. 不尊敬的
irrevocable adj. 不能改变的，无法取消的
irrigate vt.灌溉 vi.进行灌溉
irrigation n.灌溉；冲洗法
irritability n. 易怒,过敏性,兴奋性
irritable adj. 易怒的，易受刺激的
irritate vt.激怒；引起不愉快
irritating a. 气人的
irritation n. 刺激,烦恼,刺激物
irruption  n. 突然冲入,入侵,闯入
is n. 是；v. 是；be的第三人称单数；vi. 是
isinglass n. 鱼胶,明胶,云母
Islam n.伊斯兰教，回教
island n.岛；岛状物
islander n. 岛人,岛民
isle n.岛；小岛
islet n. 小岛
isn't 不是；(同)is not(口)不是
isolate vt. 使隔离，使孤立；隔开，绝缘
isolation n. 隔绝,孤立,隔离
isosceles a. 二等边的
isotherm n. 等温线
isotope n. 同位素
Israel n. 以色列,以色列的后裔,犹太人
issuance 发给，发行，开具
issue n.问题；发行 vt.发行
istanboul n. 伊斯坦布尔
isthmus n. 地峡
it pron.它
Italian adj.意大利的
italic adj. 斜体的
italicize vt. 用斜体字印刷
italics n. 斜体字
Italy n.意大利
itch n. 痒,渴望,疥癣
item n.条，条款；一条
itemize vt. 分条缕述,详细列举
iterate v. 重做，反复重申
iteration n. 重复,反复,复诵
iterative a. 迭代的
itinerant adj. 巡回的，流动的
itinerary n. 行程表，旅行路线
its pron.它的
it's (同)it is；it has
itself pron.它自己；自身
i've (同)i have
ivory n.象牙；牙质；乳白色
ivy n. 常春藤
jab vt.vi. 刺,戳,猛击
jabber v. 快而不清楚地说
jabot n. 胸部装饰
jack n.起重器；传动装置
jackal n. 狐狼,帮凶,走狗
jackass n. 公驴,愚蠢的人,傻瓜
jackdaw n. 寒鸦
jacket n.短上衣，茄克衫
jackie 杰基(男名)
jade n. 疲惫的老马，玉，翡翠
jaded adj. 疲惫的，厌倦的
jag n. 缺口,突出端,小量负荷,小伙子
jagged adj. 锯齿状的，不整齐的
jaguar n. 美洲虎
jail n. 监狱；看守所vi. 监禁；vt. 监禁
jailer n. 看守监狱的人,狱卒
jailor n. 看守监狱的人,狱卒
jam n.堵塞 vt.使…堵塞
jamb n. 门窗的侧柱
jamboree n. 快乐，喧闹的集会
james n. 詹姆斯(男名)
jan. n. 一月
jane n. 简(女名)
jangle vi.vt. 吵架,(使)发出刺耳声
janitor n. 管理员，管门人
January n.一月
Japan n.日本，日本国
Japanese a.日本的 n.日本人
jar n.坛子；罐子；缸
jargon n. 行话
jasmine n. 茉莉,淡黄色
jasper n. 碧玉,绿色装饰用宝石
jaundice n. 黄疸,偏见,乖僻
jaundiced adj. 有偏见的
jaunt v. 短程旅游
jaunty adj. 愉快的，满足的
javelin n. 标枪
jaw n.颚；上下颚，口部
jawbone 信用；赊买借贷
jawboning 劝说
jaws n. 危险的境遇
jay n. 鸟,喋喋不休的人,傻瓜
jaywalk vi. 擅自穿越马路
jazz n.爵士音乐，爵士舞曲
jazzy adj. 吸引人的，花哨的
jealous a.妒忌的；猜疑的
jealousy n.妒忌，嫉妒，猜忌
jean n.斜纹布，牛仔裤
jeanne 让娜(女名)
jeans n. 斜纹布裤子，牛仔裤；斜纹布，(pl.)工装裤
jeep n. 吉普车；小型越野汽车
jeer v. 嘲笑
jejune adj. 空洞的，不成熟的
jell v.凝结；成
jelly n.冻，果子冻；胶状物
jellyfish n. 海蜇
jenkins 詹金斯(姓)
jennet n. 西班牙种小马
jenny (女名)詹妮
jeopardise vt.使受危害，使陷险境
jeopardize v. 危及，危害
jeopardy n. 危险
jeremiad n. 长篇声讨文字，哀叹
jerk vt.猛地一拉 vi.急拉
jerkily adv. 颠簸地
jerkin n. 男用无袖短上衣,短上衣
jerky a. 急动的
jerque 检查
jersey n. 毛织运动衫；毛线衫
Jerusalem n. 耶路撒冷
jest n./v. 说笑，玩笑
jester n. 讲笑话的人,小丑
jesting adj. 滑稽的，好笑的
Jesus n.耶稣
jet n.喷射；喷气发动机
jettison v. 向外抛弃，n. 抛弃的货物
jetty n. 突堤,防波堤,码头
Jew n.犹太人
jewel n.宝石；宝石饰物
jeweler n. 宝石商
jewelery n.珠宝
jeweller n.珠宝商
jewellery n.珠宝，珠宝饰物
jewelry n. (总称)珠宝；(集合词)珠宝(饰物)
Jewish a.犹太人的
jib v. 踌躇不前
jibe n. 奚落；v. 与...一致，符合
jiffy  n. 亦作jiff.『俗』顷刻; 瞬间; 刹那
jig n. 快步舞,快步舞曲,带锤子的钓钩,
jiggle vt. & vi. 轻轻摇晃
jill n. 少女；情人
jilt v. 抛弃，遗弃（情人或恋人）
jim 吉姆(男名)
jingle vt.&vi.(使)丁当响
jingo n. 侵略主义,沙文主义
jingoism n. 沙文主义，侵略主义
joan 琼(女名)
job n.工作
jobber n. 批发商,股票经纪人
jobbery 假公济私
jobholder n.有固定职业者；公务员，政府雇员
job-hop 经常转换职业
job-hunter 求职者
jobless adj. 失业的
jobs 工作
jockey n. 赛马的骑师,停车,操作工
jocose adj. 开玩笑的，引人发笑的
jocular a. 诙谐的
jocularity n.滑稽,诙谐
jocund adj. 快乐的，高兴的
joe 乔(男名)
jog vt.使(马等)缓步行进
jogging n.慢跑
john n. 约翰(男名)
johnson 约翰逊(姓)
johnsy n. 约翰西(人名)
join vt.加入
join...to... 把…和…连接起来
joiner n. 结合者
joint n.接头，接缝；关节
joint...to... 把…和…连结起来
joist n. 托梁,桁
joke n.笑话 vi.说笑话
jollity n. 快乐，欢乐
jolly a.快活的；令人高兴的
jolt n. 颠簸，震摇
jordan n. 约旦(亚洲)
jostle vt. 挤，推；搅扰；同...竞争
jot n. 少量,少额,稍许
journal n.日报，杂志；日志
journalism n. 新闻业,报章杂志
journalist n.记者，新闻工作者
journey n.旅行，旅程，路程
journeyman n. (学徒期满而熟练的) 工人
joust v. 马上长枪比武，竞争
jove n. (罗神)(同)jupiter
jovial adj. 快活的
jowl  (C)
joy n.欢乐；高兴
joyance n. 喜悦
joyful a.十分喜悦的，快乐的
joyfully ad. 高兴地，快乐地
joyless a. 不高兴的,不快乐的
joyous a. 充满快乐的
joyously ad. 快乐地，高兴地
jubilant adj. 喜悦的，欢呼的
jubilation n. 喜悦，欢呼
jubilee n.周年纪念; 庆典; 佳节
Judaism n. 犹太教,犹太教徒,犹太主义
Judas 犹大
judge n.法官
judgement n.意见；审判；判断
judgment n. 判断
judicial adj. 法庭的，法官的
judiciary a. 司法的,法院的,法官的
judicious adj. 有判断力的，明智的
judo n. 柔道
jug n.大壶
juggernaut n. 摧毁一切的，强大力量
juggle vt. 变戏法
juggler n. 变戏法者,行骗者
juice n.(水果等)汁，液
juicy a. 多汁液的,生动的,多水分的
July n.七月
jumble n./v. 揉杂，混杂
jumbo a.巨大
jump vi.跳；暴涨 vt.跳过
jumper n. 跳跃者,工作服
jumping a. 跳跃的
jumpy ad. 激动而紧张的；adj. 神经过敏的
junction n.连接；接头；中继线
juncture n. 接合,连接,接缝
June n.六月
jungle n.丛林，密林
junior n.年少者；晚辈
juniper n. 杜松属
junk n.废弃的旧物；旧货
junket vi. 用公费游山玩水,设宴
juno n. (罗神)朱诺
junta n. 秘密结社；私党
junto n. 私党,秘密结社,阴谋团体
jupiter n. 木星；(罗神)朱庇特
jurisdiction n. 司法权,审判权,管辖权
jurisprudence n. 法律学，法学
jurist n. 法学家,法理学者,法律著作家
juror n. 陪审员
jury n.陪审团；评奖团
juryman n. 陪审团
jus (拉)法；废物，破料货
just adv.正好，恰好
justice n.正义，公正；司法
justifiable adj. 有理由的，无可非议的
justifiably ad. 无可非议地
justification n. 辩护,证明正当,释罪
justified a. 正当的，合理的
justify vt.证明…是正当的
justle n. 推挤,冲撞vi. 推挤,冲撞
justly ad. 应得地；公正地；正当地
jut v. 突出，伸出
jute n. 朱特人,朱特族,黄麻
juvenile adj. 少年的，似少年的
juxtapose v. 并排，并置
juxtaposition n. 并排
kail n.甘蓝类蔬菜
Kaiser n. 皇帝
kale n. 无头甘蓝类,甘蓝类蔬菜,甘蓝汤
kaleidoscope n. 万花筒
kaleidoscopic adj. 千变万化的
kangaroo n. 袋鼠
kansas n. 堪萨斯(州)(美国)
karate n. 空手道
kate 凯特(女名)
kate's 凯特的
kathy (女名)凯茜
katydid n. 纺织娘
kay 凯(姓)
kayak n. 爱斯基摩独木舟，小船
keel n. 龙骨,平底船
keen a.热心的；激烈的
keenly ad. 敏锐地；强烈地
keenness n. 锐利,尖锐,敏感
keep vi.保持；坚持
keep...from 使…不
keep...from... v. 阻止；避开
keep...out 不让…进来
keeper n.看护人；饲养员
keeping n. 保管,供养,一致
keepsake n. 纪念品
keg n. 小桶
ken n. 知识，眼界
kennel n. 狗舍，狗窝
kent 肯特(英格兰一郡)
kentucky n. 肯塔基(美国州名)
Kenyan a.肯尼亚的；肯尼亚人的
kept keep的过去式(分词)；保持
kerb 非正常交易所，场外
kerchief n. 头巾,围巾,手帕
kern 计算机] 紧排
kernel n.(果实的)核；谷粒
kerosene n.煤油
ketch n. 一种双桅船；一种双轮船
ketone n. 酮
kettle n.水壶，水锅
kettledrum n. 半球形铜鼓,午后茶会
key n.钥匙
keyboard n.键盘
keycard 钥匙牌
keyed a. 键控的
keyhole n. 键孔,栓孔,锁眼
keynote n. 主调音,基音,基调
keypad n. 小键盘
keys 钥匙
keystone n. 拱心石,楔石,重点
keyword n. 关键字(词)
khaki a. 卡其色的,土黄色的
khan n. 可汗,商队的宿店
kibe n. 冻疮,蹦裂
kick vi.&vt.&n.踢
kick...out 把…踢出去
kickback 回扣，佣金
kicking 捐助
kickoff 解雇，撤职
kickshaw n.精致的开胃菜肴
kid n.小孩，儿童，少年
kidd 吻
kidnap vt.绑架,诱拐,拐骗
kidnaper n. 绑架者
kidnapper n. 拐子，绑架者
kidney n.肾，腰子；性格
kill vt.杀死
killer n. 杀生者,杀人者; 职业杀手
killing 赚大钱
kiln n. 窑，窑房
kilo n. 公斤公里之略
kilobyte n. 千字节(kb)
kilocalorie n. 千卡，大卡
kilogram n.千克，公斤
kilogramme n.千克，公斤
kilolitre 千升
kilometer n. 公里
kilometre n.千米，公里
kilovolt n. 千伏
kilowatt n.千瓦(特)
kilt n. 苏格兰式短裙
kimono n. 和服,妇女穿着的宽大晨衣
kin n. 亲戚,同族,血缘关系,家族
kind adj.仁慈的；和蔼的
kindergarten n. 幼稚园
kind-hearted adj. 好心的
kindle vt.点燃 vi.着火
kindliness n. 亲切,慈爱,亲切的行为
kindling n. 引火物
kindly a. 和蔼的,温和的,爽快的
kindness n.仁慈，好意
kindred n. 家族,相似,亲戚关系
kinds 种类
kinescope n. 显像管
kinetic a.动力(学)的；活动的
kinetics n. 动力学
king n.国王，君主
kingdom n.王国；领域，界
kingfisher n. 鱼狗,翠鸟
kingly a. 国王的,高贵的,威严的
kingship n. 君主身分,王位,王权
kink n. 纽结,蜷缩,颈
kinsfolk ]亲戚,血族
kinship n. 血族关系
kinsman n. 男亲属
kiosk n. 售货亭，电话亭
kip 旅店
kirk n. 教会,苏格兰教会
kirtle n. (女用) 长袍,短裙 ,男用短上衣
kismet n. 命运，命定
kiss n.&vt.吻 vi.接吻
kit n.成套工具；用具包
kitchen n.厨房，灶间
kite n.风筝
kite-flyer n.开空头支票者
kith n.朋友,熟人
kiting 开空头支票
kitten n. 小猫
kitty n. 小猫,全部赌注
klarke 克拉克(男名)
kleptomania n. 盗窃癖
kleptomaniac n. 有窃盗癖的人
knack n. 决窍；技巧；习惯；特殊能力，窍门
knapsack n. 背包
knave n. 不诚实的人，无赖
knavery n. 恶棍的行为,欺诈,恶行
knavish adj. (像) 恶棍的,无赖的,狡诈的
knead vt. 揉,按摩,捏制
knee n.膝，膝盖，膝关节
kneel vi.跪着；跪下
knell n. 丧钟声,哀伤的声音,凶兆
knelt kneel的过去式(分词)
knew know 的过去式；知道
knickerbockers  n. pl. 灯笼裤
knife n.小刀
knight n.骑士，武士；爵士
knighthood n. 骑士身分,骑士气质,骑士团
knightly a. 骑士的,勇敢的,侠义的
knit vt.把…编结 vi.编织
knitter n. 编织者,针织工
knitting n. 编织(物)；接合；联合
knives 刀子(复数)；knife的复数；小刀
knob n.门把，拉手；旋纽
knock vi.敲；击，打
knock...into... 把…插进；把…敲进
knocker n. 敲击的人，门环
knoll n. 小圆丘
knot n.(绳的)结，(树的)节
knotty adj. 有节疤的，困难的
know vt.知道；认识；通晓
know-all n. 自称无所不知的人
know-how n. 专项技术，诀窍
knowing a. 博学的,聪颖的,精明的
knowingly ad. 狡黠地，机警地
knowledge n.知识，学识；知道
knowledgeable adj有见识的；博学的；有丰富知识的，知识渊博的
known know过去分词；知道；了解；知名的；已知的；大家知道的
knuckle n.指节,蹄爪,膝关节
kodak n. 柯达
kohlrabi n. 大头菜
kont v. 打结；节(海时／小时)
Koran n. 可兰经
kudos n. 荣誉，称赞(单复数同)；名声
l/c n. (缩)信用证
la n. 第六音；a音的唱名
lab n.研究室；(缩)实验室
label n.标签；标记，符号
labeled a. 有标号的
labial a. 唇的,嘴唇的,唇音的
labile adj. 易变的，不稳定的
labor n. 劳动,努力,分娩,劳工,工作
laboratory n.实验室
laborer n. 劳动者,劳工
labor-intensive adj. 劳动密集型的
laborious adj. 费力的，吃力的
labour n.劳动
laboured adj. 吃力的，(文体)不自然的
labrador n. 拉布拉多猎狗
labrary 图书馆
lab-technician n. 化验员；技术员
laburnum n. 金链花
labyrinth n. 迷宫
labyrinthine adj. 迷宫的; 迷宫似的
lace n.鞋带，系带；花边
lacerate v. 撕裂，伤害
laceration n. 撕裂，裂口
lacework n. 网状物
lachrymal a. 泪的,流泪的,啜泣的,泪腺的
lachrymose adj. 好流泪的，引人落泪的
lack n.,vi.&vt.缺乏，没有
lackadaisical adj. 无精打采的，无兴趣的
lackey n. 卑躬屈膝者，走卒
lacking a. 缺少的，没有的
lacklustre adj. 无光泽的呆滞的
laconic adj. （用字）简洁的
lacquer n. 漆；漆器
lacteal a. 乳的,乳状的,输入乳糜的
lactic adj. 乳汁的
lacuna n. 空隙；脱漏
lad n.少年；小伙子
ladder n.梯子，梯状物
lade vt. 装载；汲取；塞满
laden lade的过去分词；adj. 装满的，充满了的
lading n. 装载,装船,船货
ladle n. 杓子,长柄杓
lady n.女士；有教养的妇女
ladybug n. 瓢虫
ladylike a. 娴淑的,如淑女的,高雅的
ladyship n. 夫人的身分,夫人,小姐
lag vi.走得慢 n.落后
laggard adj. 缓慢的，落后的，n. 落后者
lagniappe n. 免费赠品
lagoon n.泻湖
laid vt.lay(放)的过去式和过去分词
lain vi. lie(位于)(平放)的过去分词；平躺；位于
lair n. 野兽的巢穴，躲藏处
laird n. 地主,领主
laity n. 信徒，外行
lake n.湖
lam vt. 鞭打；越狱
lama n. 喇嘛
lamb n.羔羊，小羊；羔羊肉
lambaste v. 痛打，痛骂
lambent a. 轻轻摇曳的,柔和而光亮的,轻妙的
lambskin n. 小羊皮,羊皮纸
lame adj.跛的，瘸的
lameness n. 跛,瘸,残废
lament n./v. 悲伤、哀悼
lamentable adj. 令人惋惜的，悔恨的
lamentation n. 悲叹,哀悼
laminate v. 切成薄板(片)
laminated n. 叠片
lamp n.灯
lampoon n. 讽刺文章v. 讽刺
lampooner n. 讽刺作家
lamppost n. 街灯柱
lance n. 长矛、鱼叉
lancet n. 刺血针,小枪,尖顶窗
lancinate v. 刺，戳
land n.陆地
landed adj. 卸货的
landfall n. 初见陆地
landing n.上岸，登陆，着陆
landlady n.女房东；女地主
landler n. 兰德勒舞曲
landless a. 无土(陆)地的
landlocked adj. 被陆地，包围的
landlord n.地主；房东，店主
landmark n. 风景点；里程碑
landmass n. 大片陆地
landowner n. 地主
landscape n.风景，景色，景致
landslide n. 山崩，压倒性胜利
landsman n. 同胞,未出过海的人
landward  adj.  adv. 向陆地的
lane n.(乡间)小路；跑道
language n.语言
languid adj. 没精打采的，怠倦的
languish v. 衰弱，变得消瘦
languishing adj. 衰弱下去的
languishment n.衰弱; 憔悴
languor n. 身心疲惫
lank adj. 瘦削的，稀疏的
lanky 瘦长的
lantern n.提灯，灯笼
lap n.膝部；一圈
lapel n. 翻领
lapful n. 满膝,满兜
lapidary n. 宝石工，宝石专家
lappet n. 垂部,垂饰,垂布
lapse n. 失误，（时间等）流逝
laptop n. 小型计算机
lapwing n. 田凫
lar n. 守护神
larboard n. 左舷,左舷侧
larceny n. 盗窃
larch n. 落叶松
lard n. 猪油
larder n. 食物贮藏室,食品橱
lares n. 家神，守护神
large adj.大的；巨大的
largely ad.大部分；大量地
largeness n. 巨大,广大,大量
large-scale a. 大规模的
largess n. 慷慨的赠与
largesse n. 慷慨援助，施舍
lark n. 玩笑，嬉耍
larkspur n. 燕草属植物
larva n. （昆虫的）幼虫
larval a. 幼虫的,幼虫状态的
laryngitis n. 喉炎
larynx n. 喉
lascivious adj. 淫乱的，好色的
lase v. 发射激光
laser n.激光
lash n. 鞭子，鞭打
lass n. 少女,爱人,情妇
lassie n. 少女,姑娘,恋人
lassitude n. 无力，没精打采
lasso n. 套索（捕捉牛、马用）
last a.最后的 ad.最后
lasting a. 永久的,永恒的,持久的
lastly ad. 最后,终于
lat n. 纬度；地区(lat＝latitude)
latch n. 门闩
latchet n. 鞋带
late a.迟的 ad.迟，晚
lately ad.最近，不久前
latency n. 潜伏期
latent a.存在但看不见的
later adv. 以后，后来；更晚，；较晚；过一会儿；过后；a. 更后的，后面的；较迟的，较近
lateral adj. 横向的，侧向的；侧面的；旁边的
latest a. 新近的
latex n. 胶乳，乳液
lath n. 板条,瘦人
lathe n.车床 vt.用车床加工
lather n. 肥皂泡
Latin a.拉丁的 n.拉丁语
latitude n.纬度；黄纬
lattace n. 格子
latter a.(两者中)后者的
lattice n. 格子；点阵，网络；结构，(做篱笆或爬藤架等的)格子架
laud v. 称赞
laudable adj. 值得称赞的
laudanum n. 鸦片酊
laudation n. 赞美,赞赏
laudatory adj. 表扬的，赞扬的
laugh vi.笑，发笑 n.笑
laughable a. 可笑的,有趣的
laugh-maker n. 逗笑的人
laughter n.笑，笑声
launch vt.发射;发动(战争等)
launder n. 流槽
laundress n. 洗衣女工
laundry n.送洗衣店去洗的东西
laundryman  n. 洗衣业者; 洗衣匠
laureate a. 戴桂冠的,用月桂树造的,荣誉的
laurel n. 月桂树，桂冠
laurels n. 荣誉
lava n. 熔岩
lavatory n.盥洗室，厕所
lave v. 洗浴，慢慢冲刷
lavender n. 薰衣草adj. 淡紫色的
laver n. 水盆,紫菜类
lavish a. 浪费的；过度的
lavishly ad. 慷慨地；大方地
law n.法律，法令
lawbook n. 法律学课本；法典
lawful a. 法律许可的,守法的,合法的
lawgiver n. 立法者
lawless a. 非法的,违法的
lawmaker n. 立法者
lawn n.草地，草坪，草场
lawn-mower n. 草坪割草机
lawsuit n. 诉讼,控诉
lawyer n.律师；法学家
lax adj. 懒散的，松弛的
laxative n. 轻泻药adj. 通便的，放松的
laxity n. 松弛，放纵
lay vt.放，搁；下(蛋)
layday n. 装卸日期
layer n.层，层次；铺设者
layette n. 新生婴儿所用的全套衣服用品
laying n. 铺设
laying-out n. 布置
layman n. 普通信徒，门外汉
layoff n.临时解雇，停工
layout n.布局，安排，设计
lay-person n. 外行；俗人
lazar n. 穷病人
laze n. 懒散；v. 混的；懒惰，混日子
lazily ad. 懒惰地，慢吞吞地
laziness n. 怠惰,无精打采
lazy adj.懒惰的
lazy-bones n. 懒骨头
lea n. 草地
leach v. 分离，过滤掉
lead vt.领导
leaden a. 铅制的,呆滞的,铅灰色的,沉闷的
leader n.领袖；领导人
leadership n.领导
leading a.指导的；最主要的
leaf n.叶
leafless a. 无叶的
leaflet n.传单，活页；广告
leafy a. 叶茂盛的,多叶的,叶状的
league n.联盟
leaguer n. 围攻,盟员
leak n.漏洞，漏隙
leakage n.漏，泄漏；漏出物
leaky a. 易漏的,有漏洞的,易泄漏秘密的
leal a. 忠实的,诚实的
lean vi.倾斜，屈身；靠
leaning adj. 倾斜的
leanness n. 贫瘠,无脂肪,贫弱
leap vi.跃，跳
lear a. 空的；n. 学问，知识
learn vi.&vt.学，学习
learned a.有学问的；学术上的
learner n. 学习者,初学者
learning n.学习；学问，知识
learnt learn的过去式(分词)；学习；学习(learnt=learned)
lease n.租约，契约，租契
leasehold 租赁，租约，租赁权；租借期
leaseholder 租赁人，承租人
leaser 出租人
leash n. 拴狗颈之皮带
least a.最少的 ad.最少
leather n.皮革；皮革制品
leave vt.离开;剩下 vi.离去
leaven n. 发酵剂，影响力v. 发酵
leaves 叶子
lebanon n. 黎巴嫩(亚洲)
lecherous adj. 好色的
lechery n. 好色，纵欲
lectern n. 诵经台
lecture n.&vi.演讲，讲课
lecturer n. 演讲者,讲师
led v. lead(领导)的过去式和过去分词
ledge n. 暗礁；岩石的突出部分
ledger n. 帐簿
lee n. 背风处,避风处,庇护,保护,下风处
leech n. 水蛭,吸血鬼,榨取他人利益的人
leek n. 韭
leer v. 斜眼看，睨视
lees n. （葡萄酒等的）渣滓，酒糟
leet n. 民事法庭管辖区
leeward adj. 顺风的
leeway n. 风压,风压角,可允许的误差,
left a.左边的 ad.在左边
left-handed adj. 左手的，左侧的
leftover n. 剩余物
leg n.腿
legacy n. 遗产，遗留之物
legal a.法律的；合法的
legality n. 合法,正当,法律上的义务
legalize vt. 法律上认为正当,公认,使合法化
legally adj合法地
legate vt. 当做遗产让与
legatee n. 遗产受赠人
legation n. 使者的派遣
legend n.传说，传奇
legendary a. 传奇的
legerdemain n. 手法，戏法
legging n. 绑腿,裹腿,护痉
leggings n. 绑腿，裹腿
leghorn n. 麦秆鞭之一种,麦秆编制的帽子,
legible adj. 可辩认的，易读的
legibly ad. 字迹清楚地
legion n. 兵团，一大群
legionary a. 古代罗马军团的,军队的,多数的
legionnaire n. 兵团成员
legislate v. 制定法律
legislation n.立法；法规
legislative a. 立法的
legislator n. 立法者,立法官,立法委员
legislature n. 立法机关
legitimacy n. 合法,适法,正当
legitimate adj. 合法的，正当的
legitimation n. 合法
legume n. 豆类,豆荚
leguminous a. 豆的,生豆的,豆科的
leiomyoma n. 平滑肌瘤
leisure n.空闲时间；悠闲
leisurely a. 悠闲的,从容的
leman n. 爱人,情夫
lemon n.柠檬，柠檬树
lemonade n. 柠檬水
lend vt.把...借给
lender n. 出借人,贷方
lending n. 贷款，借款；n. & a. 借给，出租；借出的；贷放，贷款；贷出物，借出物
length n.长，长度；一段
lengthen vt.使延长 vi.变长
lengthwise a. 纵长
lengthy adj. 很长的，冗长的
lenience n. 宽大，温和
leniency n. 宽大,深情,慈悲为怀
lenient adj. 宽大的，仁慈的
lenin n. 列宁
leningrad n. 列宁格勒
leninism n. 列宁主义
lenity n. 慈悲,宽大处理
lens n.透镜，镜片；镜头
lent n. (基督教的)四旬斋；vt. lend的过去式与过去分词；借给
lentil n. 小扁豆
leo n. (天)狮子座，狮子宫
leonine adj. 狮子的
leonov 列昂诺夫(苏联宇航员)
leopard n.豹
leper n. 麻疯病患者,受蔑视的人
leprosy n. 麻疯病
leprous a. 麻疯病的,患麻疯病的,不洁的
lesion n. 伤口，损害
less a.更少的 ad.更少地
lessee n. （房地产的）租户
lessen vt.减少 vi.变少
lesser a. 较小的，次要的
lesson n.功课，课；课程
lessons 功课
lessor 出租人
lest conj.惟恐，以免
let v.让
lethal adj. 致命的
lethargic adj. 嗜眠性
lethargy n. 昏睡，倦怠
let's 让我们；(同)let us让我们
letter n.信；证书；字母
letterhead n. 信笺上方的印刷文句,该信笺
lettuce n.莴苣
leucocyte n. 白血病
leukemia a. 白血病的
levee n. 防洪堤，堤岸
level n.水平面 a.水平的
leveller  n. 平均主义者
lever n.途径，工具，手段
leverage n. 杠杆作用,杠杆装置,杠杆率
leviathan n. 大海兽，巨大之物
levitate v. (使)浮于空中
levity n. 轻率；轻浮；变化无常
levy n./v. 征税、征兵
lewd adj. 好色的，猥亵的
lewdness n.淫荡
lexical adj. 辞典的，词法的；词汇的，词典的
lexicographer n. 词典编纂人
lexicon n. 词典
lia n. 盖子
liabilities n. 负债，债务
liability n.责任；倾向；债务
liable a.易于…的；可能的
liaison n. 联系，暖昧关系
liar n.说谎的人
libation n. 奠酒（给神献酒），饮酒
libel n./v. （文字）诽谤，中伤
libellous adj. 诽谤的
libelous adj. 诽谤性的
liberal a.心胸宽大的；慷慨的
liberalism n. 自由主义
liberality n. 慷慨，心胸开阔
liberalization 自由化
liberate vt.解放
liberated adj. 无拘束的，放纵的
liberation n.解放
liberator n. 解放者,释放者
libertine n. 性行为放纵者，浪荡子
liberty n.自由；释放；许可
libidinous adj. 性欲强的，好色的
libido n. 性欲，生命力
libra 镑；磅
librarian n.图书馆馆长
library n.图书馆(室)
libretto n. （歌剧等）歌词，剧本
libya 利比亚
lice n. louse(虱子)的复数形式
licence n. 自由，放肆
license n.许可；执照 vt.准许
licensed 被许可的；得到许可，领有执照的
licenser 发许可证者；技术输出方
licentious adj. 纵欲的，放肆的
licentiousness n.放肆，无法无天
lichen n. 青苔,地衣,苔藓
licit adj. 不禁止的，合法的
lick vt.舔；舔吃
licorice n. 甘草,由甘草根熬成的精
lictor n. 执束杆侍从执政官惩罚人的官吏
lid n.(坛子、壶等)盖子
lido n. 浴场，公共游泳池
lidocaine n. 利多卡因(局部麻醉)
lie vi.躺，平放；位于
lief ad. 欣喜,自愿
liege n. 君主,王侯,臣下
liegeman  n. 臣子
lien n. 扣押权，留置权
lier n. 埋伏者；躺卧者
lieu n. 场所
lieutenant n.陆军中尉；副职官员
lieutenant-general n. 中将
lieve ad. 喜悦地；自愿地
life n.生命，生活
lifeblood n. 生命线；命根子
lifeboat n.救生艇
life-boat n. 救生艇
lifeguard n. 卫兵,禁卫军,救生员
lifeless a. 无生命的,无趣味的,死气沉沉的
lifelike a. 栩栩如生的,逼真的,酷象实物的
lifelong a. 终身的,毕生的
life-saving n. 救生
lifespan n.寿
life-threatening 威胁生命的
lifetime n.一生，终身
life-time n. 一生，终身
lift vt. 举起；抬起；升起，兴起；提升，搬起；拿起；提起，提高；运送；吊；vi. (烟，云等)消散；n. 电梯；搭便车；提，吊；举起；起重机；升力；升起
lifter n. 举起的人,贼,升降机
ligament n. 结带,纽带,韧带
ligature n. 绑缚之物（尤指系住血管以免失血的线）
light n.光 adj.明亮的
lighten vt.照亮，使明亮
lighter n.打火机，引燃器
lightering 驳运
light-hearted a. 轻松愉快的，无忧无虑的
lighthouse n. 灯塔
lighting n. 照明，发光
lightly ad.轻轻地，轻松地
lightness n.轻
lightning n.闪电，闪电放电
lightship n. 航路标志灯船,灯塔船
lightsome a. 畅快的,快活的,轻盈的
lightweight a. 重量轻的；n. 重量轻的人或物
light-year n.光年
lign (构词成分)木
ligneous adj. 木质的，木头的
lignite n. 褐煤
likable a. 可爱的
like prep.象；跟...一样
likelihood n.可能(性)
likely a.可能的 ad.很可能
like-minded a. 志趣相投的
liken v. 把…比作，比拟
likeness n.同样；类似，相似
likewise ad.同样地；也，又
liking n. 兴趣，嗜好；爱好；喜欢
lilac n. 紫丁花,丁香花,淡紫色
lilliput n. 小人国
lilliputian adj. 小人国的，气量小的
lilt v. 轻快的动作或歌唱
lily n.百合，百合花，睡莲
lima n. 利马(秘鲁首都)
limb n.分支，突出物
limber adj. （肌肉）松软的，柔软的
limbo n. 不稳定，中间状态
lime n.石灰
lime-light n. 舞台灯光，聚光灯
limerick n. 五行打油诗
limestone n.石灰石
lime-stone n. 石灰石
limewater n. 石灰水
limit n.限度；限制；范围
limitation n.限制；限度，局限
limitations n. 限制，边界
limited a.有限的
limiter n. 限制(幅)器
limiting n. (电路参数)限制处理
limitless a. 无限的,界限的
limn v. 描述，绘画
limnetic adj. 湖泊的
limousine n. 轿车，小客车
limp vi.蹒跚；瘸着走
limpet n. 帽贝,坚守岗位的职员
limpid adj. 清澈的，透明的
lincoln 林肯(美第十六任总统)
linda 林达(女名)
linden n. 菩提树
line vt.沿...排列 vi.排队
lineage n. 血统
lineal adj. 直系的，嫡系的
lineament n. 面貌，特征
linear a.线的；长度的
lineman n.  (电报、电话线等的) 架设
linen n.亚麻布；亚麻织物
liner n.班船，定期班机
lines n. 台词，诗
ling n. 石南
linger vi.逗留，徘徊；拖延
lingerie n.  (主要为妇女、儿童用的) 内衣类
lingering adj. 拖延的，依依不舍的
lingual adj. 舌的，语言的
linguist n. 语言学家
linguistic  adj. 语言的
linguistics n. 语言学
liniment n. 涂敷药
lining n.(衣服里的)衬里
link vt.有环连接 n.环
linkage n.联系；连锁；联动
linker n. 连接程序
linnet n. 红雀
linoleum n. 油毡
linseed n. 亚麻子
lint n. 保护伤口的软布
lintel n. 楣,楣石
lion n.狮子；勇猛的人
lioness n. 雌狮
lionize v. 崇拜，看重
lip n.嘴唇
lipoma n. 脂肪瘤
lipstick n.唇膏，口红
liquefaction n. 液化,溶解,液化状态
liquefy v. 液化，溶解
liquid n.液体 a.液体的
liquidate v. 清除，清偿，停止
liquidation n. 清除，停止营业
liquor n.酒；溶液，液剂
lira n. 里拉
lisle n. 莱尔线,其织物
lisp vt.vi. 咬着舌儿说
lissom adj. 姿态优雅的，柔软的
lissome a. 柔软的,敏捷的
list n.表；名单
listen vi.听，留神听；听从
listener n.听者，听众之一
listening n. 听(录音)
listing n. 列表，编目
listless adj. 无精打采的
lit light的过去式(分词)；a. 照亮的，点着的；明亮的；喝醉了的
litany n. 连祷,哀求
lite (构词成分)矿物，岩石
liter n.升(容量单位)
literacy n. 读写能力,识字,精通文学
literal a.文字(上)的；字面的
literally adv. 确确实实地；照字义，逐字地；简直，字面上；实际上；确实的，毫不夸张地
literary a.精通文学的
literate n. 有文化的；a. 有读写能力的，有文化的，受过良好教育的
literati n. 文人，学者(复数)
literature n.文学；文献
lithe adj. 柔软的，易弯曲的
lithograph 石版画
litigant n. 诉讼当事人
litigate 诉讼
litigation n. 诉讼,起诉
litigious adj. 好诉讼的
litmus n. 石蕊（蓝色染料）
litotes n. 间接肯定法,曲言法
litre n. 升(容量单位)
litter n.废物，杂乱 vi.乱扔
litter-basket n. 废物筐；废物篮
litterbin n. 垃圾桶
little adj.小的
little-appreciated a. 不被赏识的
littleness n. 渺小; 少量
littoral adj. 海岸的；沿岸的n. 海滨，沿海地区
liturgical adj. 礼拜式的
liturgy n. 礼拜形式
livable adj. 适于居住的，（人）可相处的
live vi.居住；活 a.活的
livelihood n. 生活；生计；谋生之道
liveliness n. 生气勃勃；繁华
lively adj.活泼的，有生气的
liver n.肝；肝脏
liverish adj. 患病的(尤指暴食所至)，易怒的
liverpool n.利物浦(英国西部港市)
liverwort n. 地钱
livery n. 制服,侍从
lives 生命
livestock n. 家畜类
livid adj. 青灰色的（撞伤），（脸色）苍白的
living n.生活；谋生
living-room n.起居室
lizard n. 晰蜴
lizzy 利齐(女名)
llama n. 骆驼
llano n. 大草原
load vt.装，装载
loaded a. 有负载的
loading n. 装入，加载，存放；装货，附加费用；装货
loaf n.一条面包，一个面包
loam n. 沃土
loan n.贷款；暂借 vt.借出
loanee 债务人
loaner 债权人
loath a. 不情愿的,勉强的
loathe v. 赠恨，厌恶
loathsome adj. 可憎的，令人作呕的
loathy adj. 可厌的，令人作呕的
lobby n.前厅，(剧院的)门廊
lobe n. 耳垂，（肺，肝等的）叶
lobster n. 龙虾
local a.地方的；局部的
locale n. 事件发生的现场，地点
locality n.位置，地点，发生地
localization n. 定位；局限；地方化
localize vt. 将<疾病等>控制在一个地方，局部化
locate vt.探明，找出，查出
locating n. 定位，查找
location n.定位，测位；测量
loch n. 湖,海湾
lock n.锁 vt.锁上，锁住
locker n. 抽屉,小柜,上锁人
locket n. 盒式小坠子
locking n. 锁定，加锁
lockjaw n. 破伤风之一种,牙关紧闭症
lockout n.工厂停工,闭厂 (不让工人进入)
locksmith n. 锁匠,锁店
lock-up n. 锁，固定资本
loco 当地交货
locomotion n. 运动，移位
locomotive a.运动的；机动
locus n. 所在地；病灶；地点，集中地
locust n.蝗虫
locution n. 说话的方式或语气，惯用语
lode n. 矿脉,水路,水道
lodestar n. 指示方向之星,北极星,指导原理
lodestone n. 天然磁石
lodge vi.暂住，借宿，投宿
lodger n. 寄宿人，房客
lodging n.寄宿，住宿；住所
lodgment n.住宿
loft n. 阁楼，顶楼
loftiness n. 高,高尚,崇高
lofty a.高耸的；高尚的
log n.原木，木料
logarithm n. 对数
logged a. 记录的，浸透的
logger n. 代木工
loggerhead n.傻瓜，笨蛋
logging n. 砍伐原木,砍伐运出,伐木量
logic n.逻辑，推理；逻辑性
logical a.逻辑的；符合逻辑的
logician n. 论理学者,逻辑学家
logistics n. 后勤学
logjam n. 浮木阻塞，僵局
logo 标识语
loin n. 腰部,腰肉,耻骨区
loiter v. 游荡，走走停停
loiterer n. 闲荡的人; 游手好闲的人
loll v. 懒洋洋地坐或卧
london n. 伦敦(英国首都)
londoner n. 伦敦人
lone a. 孤独的；孤立的
loneliness n. 寂寞,孤独,凄凉
lonely adj.孤独的；荒凉的
lonesome a. 寂寞的
long vi.渴望；极想念
long-drawn a. 漫长的
longevity n. 长寿
longhand n.普通写法(与shorthand速记相对而言)
longing n. 渴望；思慕；a. 显示渴望的
longitude n.经线，经度
longitudinal a. 轻度的,经线的,纵的
long-lost a. 失踪很久的
longshore n.码头装卸工人；在海岸工作的；海岸边的
longshoreman n. 码头装卸工人
long-suffering a. 坚忍的
long-term adj. 长期的
longueur n. 枯燥的部分或时期
look v.看
looking adj. …的样子；模样…的；外表…的
lookout n.守望；警戒
look-out n. 嘹望员；警戒
loom n.织布机
loon n. 愚人，懒人
loop n.圈，环，环孔
loophole n. 枪眼,小窗,换气孔
loose a.松的；宽松的
loosely ad. 松松地，松散地
loosen vi.变松
loot n. 掠夺品，v. 掠夺
lop v. 修剪，砍掉
lope n. 轻快的步伐，v. 轻快地迈着大步
lop-sided  adj. <物>倾向一边的; 一边较大的
loquacious adj. 多嘴的，饶舌的
lord n.贵族；上帝，基督
lordly a. 贵族气派的；高贵的
lordship n. 贵族身分,主权,支配
lore n. 知识，全部传说
lorgnette n.长柄眼镜
lorn a. 被弃的,孤独的,荒凉的
lorraine n. 洛林(法国地名)
lorry n.运货汽车，卡车
lose vt.失去；迷失；输掉
loser n. 失败者,遗失者,损失物
loss n.遗失；损失；失败
lost adj. 丢失的；迷途的；失败的；失去的；lose过去式；浪费掉的；失败了的；错过的；不知所措的；无望的，迷路的；丢途的
lot n.许多，大量；签，阄
loth  adj. = loath 不情愿的,勉强的
lotion n. 洗液,洗净,饮料
lottery n. 彩票，抽彩给奖法
lotus 美国的软件公司
loud a.响亮的；吵闹的
loudly adv. 大声地；高声地；响亮地 a. 大声地，高声的
loudness n. 响亮；音量；大声；喧闹
loudspeaker n. 扬声器，喇叭；扩音器
loud-speaker n.扩音器
lough n.湖泊，海湾；湖
louisiana n. 路易斯安那州(美国)
louisianian a. 路易斯安那州(人)的
lounge n.(旅馆等的)休息室
lounger n. 游手好闲之人
lour vi. 皱眉,变阴沉
louse n. 虱子,寄生虫
lout n. 粗人
loutish adj. 粗鲁的
lovable a. 可爱的,惹人爱的
love vt.爱，喜欢 n.爱
loveless a. 无爱情的,不可爱的
loveliness n. 可爱,美丽,魅力
lovely adj.可爱的；好看的
lover n.爱好者；情人；情侣
lovesick adj. 害相思病
loving adj. 爱的，有爱情的；热爱的
lovingly ad. 钟爱地,亲切地
low adj.低的；浅的
lowbred adj. 粗野的，鲁莽的
lower a.较低的 vt.放下
lowercase n. 下档，小写体
lowest a. 最低的，最小的
low-grade n. 低档
lowland n. 低地,苏格东南部的低地
lowliness n. 低,卑微,下贱
lowly a. 地位低的,卑下的,谦卑的
loyal a.忠诚的，忠心的
loyalist n. (美国独立战争时期)亲英分子
loyalty n.忠诚，忠心
lozenge n. 菱形,菱形花纹,菱形窗玻璃
lubber adj. 大而笨拙的
lubricant n. 润滑剂
lubricate vt.使润滑vi.加润滑油
lubrication n. 润滑
lubricator n. 润滑器
lubricious adj. 光滑的，好色的
lubricity n. 光滑,淫荡,不稳定,狡猾
lucent a. 光亮的,透明的
lucid a. 清澈的,透明的,透彻的
lucidity n. 明朗,清澈,透明
luck n.运气
luckily adv. 运气好地；幸运地；幸亏
luckless a. 不幸的,坏运气的
lucky adj.幸运的，侥幸的
lucrative adj. 赚钱的，有利可图的
lucre n. 钱，利益
lucubrate v. 刻苦攻读，埋头苦干
lucubration n. 刻苦研究
ludicrous a. 可笑的,滑稽的,荒唐的
luff n. 逆风航行,纵帆的前缘,船首弯曲部
lug vt.vi. 拖,拉
luggage n.行李；皮箱，皮包
lugubrious adj. 郁郁不乐的，悲哀的
lukewarm adj. 微温的，不热心的
luke-warm adj. 微温的
lull vt. 使安静
lullaby n. 摇篮曲
lumbar a. 腰的,腰部的
lumber n.木材；木料；制材
lumbering n. 伐木(业)
lumberman n.伐木工人,锯木工人
luminary n. 杰出人物，名人
luminescent a. 发光的
luminosity n. 发光；光明，光辉
luminous a.发光的；光明的
lump vt.(使)成团 vi.结块
lumpish adj. 笨拙的
lump-sum 总计，整批
lunacy n. 疯狂，愚行
lunar a.月亮的
lunatic n. 疯子，adj. 极蠢的
lunch n.午餐，(美)便餐
luncheon n.午宴，午餐，便宴
lunchtime n.午餐时间
lung n.肺脏，肺
lunge n. 刺；vt. 刺，推；vi. (at)猛向前冲
lunt n. 火把；烟；热水汽；烟火
lurch n. 突然向前或旁边倒v. 蹒跚而行
lure n. 诱惑力，引诱
lurid a. 火烧似的,苍白的,华丽而庸俗的,
lurk v. 潜伏，埋伏
luscious adj. 美味的，肉感的
lush a. 茂盛的；葱绿的；芬芳的；豪华的
lust n. 强烈的欲望
luster n. 光彩,荣誉,光泽
lustful  adj. 好色的,淫荡的
lustre n. 光亮，光泽
lustrous adj. 有光泽的
lusty adj. 精力充沛的
lute n. 琵琶,封泥
lux n. 勒克司(照明单位)
luxuriance n. 繁茂,丰富,肥沃,华丽
luxuriant adj. 繁茂的，肥沃的
luxurious a.爱好奢侈的，豪华的
luxury n.奢侈，奢华；奢侈品
lyceum n. 学园,学会
lycopene n.蕃茄红素
lye n. 碱水
lying lie的现在分词
lymph n. 淋巴腺,淋巴
lymphatic a. 淋巴的,输送淋巴的,淋巴性的
lymphoid a. 淋巴的或淋巴样的
lynch v. 私刑处死
lynn 林恩(男名)
lynx n. 山猫
lyre n. 七弦琴,小竖琴
lyrebird 琴鸟
lyric adj. 抒情的，n. 抒情诗
lyrical a. 抒情诗调的,有抒情味的,感情夸张的
lysis n. 渐退；消散，细胞溶解
m.p. 英国议会议员
m.s. (缩)轮船
m.v. (缩)m/s轮船，…轮
ma n. 妈
ma'am n. 夫人,称呼女王,公主的尊称
mabel 梅布尔(女名)
macabre adj. 骇人的，可怖的
macadam n. （铺路用的）碎石，碎石路
macadamize vt. 简易地铺装,以碎石铺
macaroni n. 通心面,纨绔子弟
macaroni-eating a. 吃通心面的
macaroon n. 蛋白杏仁饼干
macaw 金刚鹦鹉
mace n. 权杖
macerate v. 浸软，消瘦
mach n. 马赫(速度单位)
machete n. 弯刀
Machiavellian a. 马基雅弗利的,权谋术的
machination n. 阴谋
machinations n. 阴谋；诡计
machine n.机器；机械
machine-gun n. 机枪；机关枪
machinery n.(总称)机器；机构
machinist n. 机械师,机械安装修理工,机械工
mackerel n. 鲭
mackintosh n. 雨衣；防水胶布
macro n. 宏，宏功能，宏指令
macrocosm n. 宇宙，宏观世界
macroeconomics n. 宏观经济学
macro-economics 微观经济学
macros n. 宏命令(指令)
macroscopic a. 肉眼可见的，宏观的
macula n. (皮肤上的)斑点
maculate 弄污
mad adj.发疯的；疯狂的
madagascar 马达加斯加岛(非洲)
madam n.夫人，女士，太太
madame n.夫人
madcap a. 鲁莽的,狂妄的
madden vt. 使发狂,激怒
maddening adj. 使人恼火的，令人气恼的
made vt.make(制作)的过去式和过去分词；制造，捏造，虚构；a. 人工制造的；虚构的，捏造的；做；制作，使
mademoiselle n. (法语)小姐；法国女教师
madir n. 最低点
madman n. 疯子,精神病患者
madness n. 疯狂,愚蠢的行为
madonna n. 圣母玛利亚；圣母像
madras n. 头巾
madrid n. 马德里(西班牙首都)
madrigal n. 合唱曲，情诗，牧歌
maelstrom n. 大漩涡，灾祸
maestro n. 音乐大师
magazine n.杂志，期刊
mage  n.魔术师; 施奇术者
magenta n. & adj. 深红色(的)；紫红色(的染料)
maggot n. 狂想，空想，怪念头
magic n.魔法，巫术；戏法
magical a. 魔术的；神奇的
magician n.魔法师；变戏法的人
magisterial adj. 有权威的，威风的
magistracy n. 地方保安官的职位
magistrate n.地方行政长官
magnanimity n. 宽宏大量
magnanimous adj. 宽宏大量的，慷慨的
magnate n. 财主，巨头
magnesia n. 苦土,氧化镁
magnesium n. 镁
magnet n.有吸引力的人(或物)
magnetic a.磁的，有吸引力的
magnetism n.磁；魅力；催眠术
magnetize vt. 使磁化
magneto n. 磁发电机
magnification n. 放大，扩大；放大率
magnificence n. 富丽堂皇,华丽,宏大
magnificent adj.华丽的，豪华的
magnifier n. 放大镜,放大器
magnify vt.放大，扩大
magniloquent adj. 夸张的
magnitude n.大小；重大；星等
magnolia n. 木兰,玉兰类的植物
magpie n. 鹊，饶舌的人
mahogany n. 桃花心木,其木材,红褐色
mahout n. 驭象的人
maid n.女佣，女仆；少女
maiden n.少女，未婚女子
maidenhood n. 处女性,处女时代
maidenly a. 象处女的,谨慎的,稳静的
maid-servant n. 女拥人
mail n.邮件；邮递
mailbox n. 邮筒,邮箱
mailman n.邮递员
maim v. 使残废
main adj.主要的n.主要部分
Maine n.(美国州名)缅因
mainframe n. 主机，大型机
mainland n.大陆
mainly adv.主要地；大部分
mainmast n. 主桅
mainsail n. 大桅的帆,主帆,大桅帆
mainspring n.  (钟表等之) 主发条,大发条
mainstay n. 主流；主要资源
mainstream n. 主流
maintain vt.维持；赡养；维修
maintenance n.扶养；坚持
maize n. 玉蜀黍,黄色
majestic a. 雄伟的；壮丽的
majestical a. 宏伟的,庄严的
majesty n.威严，尊严；陛下
major a.较大的 n.专业
majordomo n. 管家,总监,大管家
majority n.多数；大多数
majorization 优化
majors 大公司，大商行，垄断组织
make v.造，制作，使...
maker n. 制造者,上帝,发期票的人
makereal 兑现
makeshift n. & adj. 权宜之计(的)，代用品
make-shift adj. 临时的；n. 权宜之计
makeup n. 组织；性格；化装品；组成，构造
make-up n. 捏造
making n. 制造，构造
maladministration 管理不善
maladroit n. 笨拙的
malady n. 病,疾病,弊病
malaise n. 马来西亚
malapert a. 不客气的,厚脸皮的
malapropism n. 字的误用
malaria n. 疟疾,瘴气
malarial adj. 疟疾的,瘴气的; 罹患疟疾的
malay a. 马来西亚的；马来人
malcontent n. 不满分子，反抗者
malcontented adj. 不满的
maldistribution 分配不当
male a.男的，雄的 n.男子
malediction n. 诅咒
malefactor n. 罪人,犯人,坏人
malevolence n. 恶意,狠毒
malevolent adj. 有恶意的，恶毒的
malfeasance n.不法行为；胡作非为；渎职
malfunction n. 事故，故障，障碍
malice n.恶意；蓄意犯罪
malicious adj. 恶意的，怨毒的
malign v. 诽谤，中伤adj. 邪恶的
malignant adj. 恶毒的，充满恨意的
malignity n. 邪恶，恶毒
malinger v. 装病以逃避工作
malingerer  n. 装病者
malingering n. 装病开小差
mall n.林荫小道
mallard n. 野鸭,野鸭肉
malleability n.可锻性；延展
malleable adj. 可塑的，易改变的
mallet n.马利特(男名)
mallow n. 锦葵属植物
malnutrition n. 营养不良
malodorous adj. 有臭味的，不合法的
malpractice n. 行为不当；失职；渎职，违法行为
malt n. 麦芽,啤酒
maltreat v. 虐待
mam (同)mamma妈妈
mama n. 妈妈
mamma n. 妈妈,乳房
mammal n.哺乳动物
mammals 哺乳动物
mammon n.财富,财神
mammoth n. 毛象(古哺乳动物，近似现代的象)；庞然大物
mammy n. 妈咪,保姆
man n.男人；人；人类
manacle n. 镣铐
manage vt.设法；对付
manageable a. 易办的,易管理的,易控制的
management n.管理；经营，处理
manager n.经理；管理人
managerial adj. 管理的
manatee n. 海牛
manchester n. 曼彻斯特(英国)
mandarin n. 中国官话,国语,满清官吏,中国柑桔
mandate n. 命令，指令，v. 批准
mandatory adj. 命令的，强迫的
mandible n. 颚,下颚,嘴的上部
mandolin n. 曼陀林(琴)
mandrake n. 曼德拉草
mane n. 鬃毛
maneuver n. 策略；花招
maneuverable adj. 可移动的，可操纵的
manful a. 男子气概的,雄伟的,勇敢的,
manfully adv. 勇敢地
manganese  n. 『化学』锰
mange vt. 操纵，运用
manger n. 马槽,牛槽,挡水板
mangle v. 撕成碎片，压碎
mango n. 芒果
manhattan n. 曼哈顿(美国)
manhood n. 成年,勇气,男儿
mania n. 癫狂，狂热
maniac a. 发狂的,颠狂的,疯狂的
maniacal adj. 发狂的，狂热的
manic a.疯狂的
manicure n. 修指甲术,修指甲,指甲修饰师
manifest vt.表明 a.明白的
manifestation n. 显示,证明,示威运动
manifestly adv. 明显的
manifesto n. 宣言；声明；声明书
manifold adj. 繁多的，多种的
manikin n. 侏儒，时装模特儿
manipulate vt.操作；控制，手持
manipulating v. 操纵，操作
manipulation n. 处理
manipulative adj. 操纵别人的，老于世故的
manipulator n. 机械手
man-killer n. 伤害人的动物
mankind n.人类
manlike adj. 似人的
man-like a. 象人的
manliness n. 男子气概,雄纠纠,勇敢
manly a.男子气概的，果断的
man-made adj. 人造的；人工的
manna n. 吗哪,精神食粮,天赐,甘露
manned a. 载人的
mannequin n. 时装模特儿，假人
manner n.方式；态度；礼貌
mannerism n. 明显或过分固守独特格调或形式,
manners n. 礼貌；n. & pl. 举止；风度
mannish a. 男子似的,成人似的
manoeuvre n. 调遣,演习,策略
manor n. 庄园，领地
manorial a. 庄园的
manpower n. 人力；劳力，人力资源
man-powered a. 人力的
manse n. 牧师住宅
manservant n. 男仆；女仆
mansion n.大厦，大楼；宅第
manslaughter n. 杀人,一般杀人罪
mantel n. 壁炉架
mantelpiece n.壁炉面饰
mantis n. 螳螂
mantle n. 披风，斗篷，v. 覆盖
manual a.体力的 n.手册
manually ad. 用手，手动地
manufactory n. 制造厂,工厂
manufacture vt.制造 n.制造；产品
manufactured adj. 制成的
manufactureer n.制造商；制造厂
manufacturer n.制造商；制造厂
manumission n. 解放,解放证书,释放令
manumit v. 解放（奴隶）
manure n. 肥料,粪肥
manuscript n.手稿，底稿，原稿
many a.许多的 pron.许多人
map n.地图；图；天体图
maple n.槭树，枫树
maps 地图(复数)
mar v. 破坏，损伤
marathon n.马拉松长跑； 马拉松
maraud v. 抢劫，掠夺
marauder n.掠夺者
marble n.大理石
marcel n. 波形卷发
march n.三月
marchioness n. 侯爵夫人,侯爵未亡人,女侯爵
mare n. 母马
margarine n. 人造黄油
margent n. 旁注
margin n.页边的空白；栏外
marginal a.记在页边的；边缘的
margrave n. 边疆伯爵
marie 玛丽(女名)
marigold n. 金盏草属植物,金盏菊属植物
marine a.海的；海上的
mariner n. 水手，海员
marionette n. 木偶
marish n. 沼泽
marital adj. 婚姻的
maritime a. 海的,海上的,海员的,沿海的
mark n.痕迹；记号；商标
markdown n.减价，标价商品价格
marked adj. 显著的；有标记的，标明的；有记号的；明显的
marker n. 作记号的人,记分员,书签,纪念碑,
market n. 市场；集市；行情；销路；市况，市场调查，市场研究；需要；需求；vt. (在市场上)销售；做买卖
marketability 交易能力，适销性；可销性
marketable a. 可销售的,销路好的,市场的
marketeer 市场上的卖主，市场商人
marketeria 自助市场
marketing n. 市场学，营销学；销售学；销售业务
marketplace n.市场
marking n. 条纹；标记；唛头，记号，传号
markon (成本)加成，批零差价
marksman n. 射手,狙击兵,神射手
markup n.提高标价，成本加价；毛利；赊账
mark-up 提高标价，成本加价；赊帐
marl n. 泥灰,泥灰土,土
marmot n. 土拨鼠
maroon v. 使（人）处于孤独无助之境
marque n. 捕拿特许,商品型号
marquee n. 大帐篷,华盖
marquess n.侯爵
marquis n.侯爵
marquisette n. 薄织物之一种
marriage n.结婚
marriageable a. 可结婚的,适合结婚的,妙龄的
married adj. 已婚的，婚姻的；有配偶的
marrow n. 骨髓，精华
marry vt.娶，嫁 vi.结婚
Mars n.火星；战争
marseilles n. 马赛(法国港口)
marsh n.沼泽地，湿地
marshal n.元帅；陆军元帅
marshmallow n. 药属葵,药属葵蜜饯
marshy a. 沼泽地的
marsupial n./adj. 有袋动物（的）
mart n. 商业中心,市场
martial a. 军事的,尚武的,威武的
martin (男名)马丁
martinet n. 要求严格服从纪律的人
martyr n.烈士，殉难者
martyrdom n. 殉教,殉难,殉节
marvel n.奇迹；惊奇 vt.惊奇
marvellous a.奇迹般的；了不起的
marvelous a. 令人惊异的,了不起的,不平常的
marvelously adv. 奇异地；奇迹般地
marx n. 马克思
Marxism n. 马克思主义
marxist adj. 马克思主义的；n. 马克思主义者
mary 玛丽(女名)
maryland n. 马里兰(州)(美国)
masculine a.男性的；强壮的
mash v. 捣成糊状
mask n.面具；伪装 vt.掩饰
masking n. 掩蔽，屏蔽
mason n. 石工，石匠
masonic a. 共济会会员的
masonry n. 石工技术，石屋
masque n. 假面剧,其剧本,化装舞会
masquerade n. 化装舞会，v. 伪装
mass n.(聚成一体的)团，块
massachusetts n. 麻萨诸塞(美国州名)
massacre n.大屠杀，残杀
massage n. 按摩,揉
massive a.粗大的；大而重的
massy adj. 厚实的
mast n.桅杆；杆 vt.扯帆
master n.主人；能手；硕士
masterful a. 傲慢的,主人派头的,能干的
masterpiece n.杰作，名著
mastership n. 主人身分,熟练
mastery n. 征服,统治权,精通,掌握
masthead n. 桅顶,桅顶展望人,发行人栏
masticate v. 咀嚼，把……磨成浆
mastication n. 咀嚼
mastiff n. 大型猛犬之一种
mastodon n. 乳齿象，庞然大物
mat n.席子；草席；垫子
matador n. 斗牛士
match n.比赛，竞赛
matching n. 匹配，调整；配合，协调，收支对应
matchless a. 无敌的,无比的
matchlock n. 火绳枪
mate n.伙伴，同事；配偶
mater n. (俚语)母亲
material n.原料；材料
materialism n.唯物主义
materialistic a. 唯物论的,唯物主义的
materialize v. 赋予形体，实现
materially ad. 实质上,重大,物质上
materials n. 衣料，材料；原料
maternal a. 母亲的,母系的,母方的
maternity n. 母性,母道,妇产科医院
math n. 数学
mathematical a.数学的，数学上的
mathematician n. 数学家
mathematics n.数学
maths n. (缩写词)数学；(英)数学
matinee n. 白天音乐会,日场,妇女便装之一种
matriarchy n. 母权制，妇女统治
matricide n. 弑母
matriculation n. 大学入学，入学许可
matrimonial ad. 与婚姻有关地,由于结婚,根据结婚的惯例
matrimony n. 结婚,婚姻生活,婚礼
matrix n. 模子，矩阵
matron n. (妇女团体)总干事；女总管
matter n.事情
matterhorn 马特峰
matter-of-fact a. 实事求是的
matting n. 席子,铺垫,其材料,无光粗糙的表面
mattock n. 鹤嘴锄
mattress n. 床垫
mature vt.使成熟 vi.成熟
matured 到期；到期，成熟
maturity n. 成熟
maudlin adj. 易伤感的；感情脆弱的，爱哭的；酒后伤感的
maugre prep. 不管
maul v. 撕裂皮肉，伤害
maunder vi. 唠叨地讲,徘徊
mausoleum n. 壮丽的坟墓,陵墓,阴森森的大厦
mauve n. 淡紫色染料的一种,淡紫色
maverick n. 独行者，想法与众不同的人
mavis n. 画眉鸟类
maw n. 反刍动物的第四胃,嗉囊,人的胃
mawkish adj. 自作多情的，令人作呕的
maxim n. 格言，普遍真理
maximal a. 最大的最高的
maximize v. 增加到最大程度
maximum n.最大量 a.最大的
may v.aux.可能，或许
may2nd 五月二日
maybe adv.大概，或许
mayfly 蜉蝣
mayhem n. 严重伤害罪，混乱
mayn't (口)(同)may not
mayonnaise n. 蛋黄酱
mayor n.市长；镇长
mayoralty n. 市长职位
maypole n. 五朔节花柱
maze n. 迷宫
mazy a. 迷阵似的,错综的,复杂的
mccallum n. 麦卡伦姆(姓)
mccarthyism n. 麦卡锡主义
me  pron. 我(i的宾格)
mead n. 蜂蜜酒,草地
meadow n.草地，牧草地
meager adj. 贫乏的，削瘦的
meagre adj.瘦的，贫乏的
meal n.(一)餐，(一顿)饭食
mealtime n. 进餐时间
mealy a. 粉状的
mean vt.意思是...
meander v. 蜿蜒而流，漫步
meaning n.意义，意思；意图
meaningful adj. 含义深远的
meaningless a. 无意义的
meanness n. 卑贱; 卑劣
means n.方法，手段，工具
meant mean的过去式(分词)；意思是
meantime n.其时，其间 ad.当时
meanwhile ad.同时，当时
measles n. 麻疹
measurable a.可测量的
measure vt.量，测量 n.分量
measured adj. 精确的，慎重的
measureless a. 无限的,不可量的
measurement n.衡量，测量；尺寸
meat n.肉
mecca n. 麦加(沙特阿拉伯)
mechanic n.技工，机械，机修工
mechanical a.机械的；力学的
mechanically adv. 机械地；无意识地
mechanics n.力学；技术性细节
mechanism n.机械装置；机制
mechanization n. 机械化
mechanize vt. 使机械化,用机械装置,机动化
medal n.奖章，勋章，纪念章
medallion n. 大奖章,圆形浮雕,圆形装饰
meddle vi. 干涉,干预,乱搞
meddlesome adj. 爱管闲事的
media n. 媒体
mediaeval a. 中古的,中世纪的
medial a. 中间的,平均的,普通的
median adj. 中间的，n. （三角形）中线
mediastinal adj. 纵隔的
mediate v. 调停
mediation n. 调停,调解,仲裁
mediator n. 调停者,仲裁人,基督
medical adj.医学的；医疗的
medicare n.医疗保
medication n. 药疗法；药剂；药物
medicinal a. 医学的,药的,有益的
medicine n.医学；内科学
medieval adj. 中世纪的，中古的
mediocre adj. 平庸的，平凡的
mediocrity n. 平庸，碌碌之人
meditate vt.沉思，冥想，反省
meditation n. 沉思,冥想
meditative adj. 沉思的、冥想的
mediterranean n. 地中海地区；地中海；a. 地中海的
medium n.媒质；中间a.中等的
medium-term 中期
medley n. 混杂
medulla n. 骨髓,髓质,延髓
medullary a. 骨髓的,髓质的,延髓的
medusa n. 水母；a. 水母然
meed n. 报酬,奖赏,赏与
meek adj. 温顺的，谦和的
meekly ad. 温顺地；卑恭屈节地
meekness n. 温顺,柔和
meet n.会；集会
meeting n.聚集，会合，会见
meeting-room n. 会议室
mega n. 兆，百万
megacycle n. 兆周
megalomania n. 自大狂
megaphone n. 扩音器
megatanker 超级油轮
melancholy n.&a.忧郁(的)，悲伤
melange n. 混合物；大杂烩
melee n. 互殴,乱斗,混战
mellifluous adj. （音乐等）柔美流畅的
mellow a. 成熟的,醇的,熟练的
melodic a.旋律优美的
melodious adj. 悦耳的
melodrama n. 情节剧，音乐戏剧
melody n.旋律，曲调；歌曲
melon n.瓜，甜瓜
melt vi.融化 vt.使融化
member n.成员，会员
membership n.成员资格；会员人数
membrane n. 薄膜，细胞膜
membranous  adj. 膜 (状) 的; 形成膜的
memento n. 纪念品
memo n. 备忘录
memoir n. 传记,实录,自传,回忆录,追思录
memorable a. 值得纪念的,难忘的
memorandam n.备忘录；便函
memorandum n. 备忘录
memorial a.纪念的；记忆的
memorialize vt. 建议,提出请愿书,纪念
memorise vt. 记住，熟记(memorize=memorise)
memorize vt.记住
memory n.记忆；回忆；存储
men n. man的复数；man(男人)的复数形式；人
menace vt.&vi.&n.(进行)威胁
menagerie n. 兽群，动物园
mend vt.改正，修正；改进
mendacious adj.不真的，撒谎的
mendacity n. 虚假
mender n. 修缮者,修理者,修改者
mendicant adj. 行乞的n. 乞丐
menial adj. 仆人的，乏味的，n. 家仆
meningitis n. 髓膜炎
mense n. 礼貌；vt. 向…致敬
mensuration n. 测定,测量,测定法
mental adj.精神的；脑力的
mentality n. 精神力,智力,头脑作用,思想
mentally ad. 内心里
menthol n. 薄荷脑
mention vt.&n.提到，说起
mentor n. 导师
menu n.菜单；饭菜，菜肴
meow n. 猫叫声
mercantile a. 商业的,商人的
mercenary adj. 唯利是图的n. 雇佣兵
mercer n. 布商,绸缎商人,呢绒布商
mercerize vt. 作丝光处理
merchandise n.商品，货物
merchandising n.销售规划
merchant n.商人
merchantman n. 商船,商人
merciful adj.仁慈的，宽大的
merciless a. 无慈悲心的,残忍的
mercurial adj. 善变的，活泼的
mercury n.水银，汞
mercy n.怜悯；宽恕；仁慈
mere a.仅仅的；纯粹的
merely ad.仅仅，只不过
meretricious adj. 华而不实的，俗艳的
merge v. 合并，淹没
merger n. 合并,归并
meridian n. 子午线,经线,顶点
meringue  n.蛋白酥皮筒
merino n. 美利诺羊,美利诺呢绒,美利诺丝绸
merit n.长处，优点；功过
meritorious adj. 有价值的，值得称赞的
mermaid n. 美人鱼
merman n. 人鱼,善泳的男子
merrily adv. 欢乐地，愉快地
merriment n. 欢喜,嬉戏
merry a.欢乐的，愉快的
merry-go-round n. 旋转木马
merrymaker  n. 行乐者,嬉戏者
mesa n. 高台地，平项山
mesh n.网眼，筛孔，网络
mesmerism n. 催眠术,催眠状态
mesmerize v. 对…催眠，迷住
mess n.混乱，混杂，肮脏
message n.信息，消息；启示
messaline  n. 美色林软缎
messenger n.送信者，信使
messmate n. 同餐之友,同餐桌的伙伴
messy a. 混乱的，肮脏的
met vt. meet(迎接)(遇见)的过去式和过去分词
metabolic a. 新陈代谢的
metabolism n. 新陈代谢
metabolize vt. (使)产生代谢变化
metal n.金属
metalic a.金属的
metallic a.金属的 n.金属粒子
metallography n. 金相学
metallurgical adj. 冶金的；冶金学的
metallurgist n. 冶金学家
metallurgy n. 冶金学，冶金术
metal-pointed a. 带铁尖的
metamorphose vt. 使变形,使变态,使变成
metamorphoses metamorphosis的复数
metamorphosis n. 变形，变态
metaphor n. 隐喻，暗喻
metaphorical adj. 隐喻的，比喻的
metaphrase vt. 直译，逐字翻译；修改…的措词
metaphysical a. 形而上学的,纯粹哲学的,抽象的
metaphysics n. 形而上学，玄学
metastasis n. 转移
mete vt. 量,测量,分配
meteor n. 流星,大气现象
meteoric adj. 流星的，昙花一现的
meteorological  adj. 气象 (学上) 的
meteorologist n. 气象学者
meteorology n.气象学
meter n.计量器，计，表
methinks vi. 我想,我以为,据我看来
method n.方法，办法；教学法
methodical a. 有方法的,有系统的
Methodism n. 卫理公会派，墨守成规者
Methodist n. 美以美教徒, 墨守成规者
methodology n. 方法(论)
methought methinks的过去式
meticulous adj. 细心的，注意细节的
meticulously adv. 胆小地
metre n.米，公尺
metric a.公制的，米制的
metrical a. 韵律的,有韵律的,测量的
metric-system n.公制，十进制
Metro n.地铁
metropolis n. 大城市
metropolitan a.主要都市的n.大主教
mettle n. 勇气，斗志
mettlesome adj. 精神抖擞的
mew n. 隐蔽处
mews n. 马厩
mexican n. 墨西哥人；a. 墨西哥(人)(语)的
mexico n. 墨西哥(拉丁美洲)
mezzanine n.『建筑』中层楼,楼中楼
miami n. 迈阿密(美国港市)
miasma n. 瘴气，坏影响
mica n. 云母
mice n. (pl.)鼠；鼠；mouse(鼠)的复数
michigan 密执安
mick 米克(男名)
mickey 米老鼠
mickle a. 很多的,许多的
micro a. & n. 微的，百万分之一
microbe n.微生物，细菌
microchip n. 芯片，微片
microcircuit n. 微型电路
microcomputer n.微型电子计算机
microcosm n. 小宇宙,小世界,人类
microeconomics n. 微观经济学
micro-economics 宏观经济学
microfilm n.微缩胶片
micrometer n. 测微计
microorganism n. 微生物
microphone n.话筒，麦克风
microprocesser v. 微处理器
microprocessor n. 微型信息处理机
microscope n.显微镜
microscopic a.显微镜的，微观的
Microsoft n.(美国)微软公司
microsurgery n. 显微外科；显微手术
microwave n. 微波
mid a. 中间的,中央的,中部的
mid-autumn 中秋
midd 错过
midday n.正午，中午
middle adj.中间的 n.中间
middle-aged a. 中年的
middle-class adj. 中产阶级的
middleman n. 中间人
middle-school 中学
middling a. 中等的,普通的,平凡的
middy n. 海军校生,水手衫
midge n. 蚊,侏儒
midget n. 侏儒，极小者
midland n.
mid-may n. 五月中旬
midmost a. 正中的
midnight n.午夜(晚上十二点钟)
midriff n. 膈,中腹部
midshipman n.((美))海军军官学校的学生
midst n.中部，中间，当中
midsummer n. 仲夏,夏至期
midterm a.期中的
midway n. 中途,中间,娱乐场
midwife n. 接生员
mien n. 风采，态度
might v.aux.可能，也许
mighty a.强大的；巨大的
mignonette n. 木犀草,灰绿色,有花样的手编花边
migrant n. 移民，候鸟
migrate vi.迁移，移居
migration n. 迁徙
migratory a. 迁移的,流浪的
mike 迈克(男名)；vi. 偷懒；鬼混；n. 话筒
mil n. 英里
milan n. 米兰(意大利)
milch a. 生乳的
mild a.和缓的；温柔的
mildew n. 霉（因温湿而生）
mildly ad. 略微地，适度地； 温和地；轻微地
mildness n. 温和,温暖
mile n.英里
mileage n. 哩数
mileometer n. 计程表
milestone n. 里程碑,里程石,一里程标
milieu n. （个人所处的）社会环境
militant adj. 好战的，好暴力的
military a.军事的；军人的
militate vi. 产生作用或影响
militia n. 义勇军,自卫队,国民军
militiaman n. 民兵
milk vt.&vi.挤奶；出奶
milkmaid n. 挤奶的妇女,在酪农场工作的女性
milkman n. 牛奶商,送牛奶的人,挤奶的男人
milkweed n. 乳草属植物
milk-white  adj. 乳白色的
milky a.牛奶的；乳白色的
mill n.磨坊；制造厂
millenarian a.千年的；千福的 n.相信太平盛事的人
millenium n.一千年，千禧年；太平盛世
millennium n. (复数millennia)一千年，千年期
miller n. 磨坊主人
millet n. 稷,栗,玉蜀黍之类
milligram 毫克
millilitre 毫升
millimeter n. 毫米
millimetre n.毫米
milliner n. 女帽制造及贩卖商
millinery n. 女帽及其装饰物
million num.&n.百万；百万个
millionaire n.百万富翁
millionth 第一百万
millokan 米里坎
mill-owner n. 磨坊主
millstone n. 磨石,碎器,重担
mime n. 比划手脚（以表达），哑剧（演员）
mimeograph n. 油印机
mimic v. 模仿，戏弄，n. 模仿他人言行的人
mimick vt. 模仿
mimicry n. 模仿，(动物等)拟态伪装
mimosa n. 含羞草
minaret n. 叫拜楼（伊斯兰教寺院的尖塔）
minatory adj. 威胁的，恫吓的
mince v. 切碎，小步走路
mincer n. 粉碎机
mincing a. 矫饰的,装腔作势的,装模作样的,
mind vi.介意 vt.注意,当心
minded a. 有…心的
mindful a. 深切注意的,留神的,留心的
mindless a. 不小心的,不留神的,不顾虑的
mine pron.我的
minelayer n.布雷舰艇
miner n.矿工
mineral n.矿物；矿石
mineralogy n. 矿物学
mingle vt.使混合vi.混合起来
miniature n.缩影 a.缩小的
minibus n. 小型公共汽车
minicomputer n. 微型计算机
mini-computer n.微型计算机
minimal a. 最小的，最低限度的
minimize vt.使减到最小
minimum n.最小量 a.最小的
mining n. 采矿；矿业
minion n. 奴才，低三下四之人
minister n.大臣；部长
ministerial a. 部长的,内阁的,执政的
ministrant a. 服务的,服侍的,辅助的
ministration n. 职务,服侍,援助
ministry n.(政府的)部
mink n. 貂,貂皮衣
minnesota n. 明尼苏达(美国州名)
minnow n. 鲦鱼，小淡水鱼
minor a.较小的；较次要的
minority n.少数；少数民族
minster n. 修道院附属的教堂,大教堂
minstrel n. 中世纪的吟游诗人，歌手
minstrelsy n.吟游诗人的歌艺
mint n.薄荷；薄荷糖
minuend n. 被减数
minuet n. 小步舞
minus a.负的 prep.减(去)
minuscule 小写的，小的
minute n.分钟
minuteness n. 微小,微细,棉密
minutia n. 微枝末节，细节
minutiae  n. pl. 小节,琐事,细目,细节
minx n. 轻佻女子,风骚女子
miracle n.奇迹
miraculous adj.奇迹般的
miraculously ad. 奇迹般地，神奇的
mirage n. 幻影，海市蜃楼
mire n. 泥沼，困境
mirror n.镜子 vt.反映，反射
mirth n. 欢乐，欢笑
mirthful a. 愉快的,高兴的
miry adj. 泥泞的
misadministration 管理失当
misadventure n. 运气不佳的遭遇
misallocation 不合理分配
misanthrope n. 愤世嫉俗者
misapplied  adj. 误用的; 乱用的; 滥用的
misapprehend 误解；私吞侵占
misapprehension n. 误会,误解
misappropriate 末送至目的地误投
misbehave vt.vi. (使)行为无礼貌,(使)行为不端
misbeliever  n. 异教徒,信邪说
miscalculate vt. 误算
miscall vt. 叫错...的名字,误称
miscarriage n. 失败,误送,流产
miscarry vi. 失败,被误送,流产
miscegenation n. 种族混合,杂婚
miscellaneous adj. 多种的，混杂的
miscellany n. 混合物
mischance n. 不幸,灾难
mischief n. 损害,伤害,淘气,恶作剧,灾祸
mischievous adj. 淘气的，有害处的
misconceive vt.vi. 误解
misconception n. 误解，错误的印象
misconduct vt. 办错,使行为不端
misconstrue v. 误解，曲解
miscorrect 误改
miscreant n. 恶棍，歹徒
misdate 写错日期
misdeed n. 罪行,犯罪
misdelivery 交付错误
misdemeanor n.不轨的行为,行为失检,品行不端
misdemeanour n. 行为不端
misdescribe 叙述失实
misdirect 指导错误，使用不当
miser n.守财奴，吝啬鬼
miserable a.痛苦的，悲惨的
miserably ad. 悲惨地；糟糕地
misery n.痛苦，悲惨，不幸
misestimate 错误估计
misfortune n.不幸，灾祸，灾难
misgive v.怀疑；恐
misgiving n.
misgivings n. 疑惧
misgovernment  n. 失政,恶政
misguide vt. 误导
misguided a.误入歧途的
mishandle v. 装卸不慎
mishap n. 不幸，坏运气
misinform vt. 告诉错误的消息
misinterpret v. 误解；曲解，误译
misjudge 判断错，估计错
misland 误卸(货物)，卸错
mislead vt.使误入岐途
misleading a. 骗人的
mislike vt. 嫌,厌恶
mismanage vt. 处置失当,办错
mismanagement  n. 管理
mismatch n. & vt. 失配，不匹配
misname vt. 叫错名字
misnomer n. 用词不当
misogynist n. 厌恶女人的人
misplace vt. 放错地方
misread vt. 读错,看错
misreport 谎报，误报
misrepresent vt.误传，歪曲，曲解
misrule vt. 施暴政
miss n.小姐
missal n. 弥撒用书
misshape vt. 使造型不佳,弄成畸形
missile n.发射物；导弹
missing a.缺掉的，失去的
mission n.使命，任务；使团
missionary n.传教士
mississippi n. 密西西比(河)(美国)
missive n. 公文,书信
misspell vt. 拼错
missus n. (已婚的)…夫人
mist n.薄雾
mistake n.错误 vi.误解，弄错
mistaken adj.弄错的，错误的
mistakenly ad. 错误地
mister n.先生
mistimed adj. 不合时机的
mistletoe n. 槲寄生
mistral n. 冷而干燥的强风
mistres n. 夫人(mistres=mrs.)
mistress n.女主人；夫人
mistrust vt. 不信任；怀疑
mistrustful a. 不信任的,深疑的
mists n. 史前时代
misty a. 有雾的,模糊的,含糊的
misunderstand vt.误解，误会，曲解
misunderstanding n. 误会，曲解；误解；隔阂
misuse n. 误用,滥用
mit n. 美国马萨诸塞理工学院
mite n. 极小量，小虫
miter a. 主教法冠
mitigate v. 减轻，缓和
mitigation n. 缓和,减轻,镇静
mitt n. 棒球手套,拳击手套,无指手套
mitten n.连指手套；露指手套
mix vt.&vi.混合；搅和
mixed a. 混合的；混杂的，综合的；中等的，适度的，公道的
mixer n.混合者，搅拌器
mixture n.混合；混合物
mmm interj. 毋； 嗯
mnemonics n. 记忆法
moan n.呻吟声 vi.呻吟
moat n. 壕沟，护城河
mob vi.聚众闹事
mobile a.运动的；流动的
mobility n. 流动性
mobilize vt.动员 vi.动员起来
moccasin n. 鹿皮鞋,软拖鞋
mock n.嘲弄 vt.嘲弄，挖苦
mocker n. 嘲弄者,模仿者
mockery n. 嘲弄,笑柄,蔑视
mod a. & n. 时髦的
mode n.方式，样式
model n.模型；模式；模特儿
moderate a.温和的；有节制的
moderately adv. 适度地，适中地；普通
moderation n. 缓和,适度,温和
moderator n. 调解人，仲裁人
modern adj.现代的
modernity n. 现代性
modernization n. 现代化
modernize vi. 现代化,近代化
modern-looking a. 时髦的
modest a.有节制的；谦虚的
modestly ad. 谦虚地；有节制地
modesty n. 谦逊；端庄；羞怯；谦虚；有礼；谨慎
modicum n. 少量
modification n.缓和；修改；修饰
modified adj. 改良的，改进的；修改的，变更的
modifier n. 修改量，变址数
modify vt.更改，修改；修饰
modish adj. 时髦的
modulate vt.调整，调节(声音)
modulation n. 调音,调节,抑扬
module n. 模数；模；组件；模量，模件； 模块(程序设计)； 舱
modulus 模数
mogul n. 显要人物，权势之人
mohair n. 马海毛
moiety n. 一半，半份
moil vi. 辛劳工作,忙碌工作,不断动摇
moist a.湿润的；多雨的
moisten vt. 弄湿
moisture n.潮湿，湿气；温度
molar n. 臼齿
molasses n. (单复数同)糖蜜
mold vt. 浇铸
moldy a. 发霉的
mole n. 痣,鼹鼠,防波堤
molecular adj. 分子的；克分子的
molecule n.分子，克分子
molest v. 骚扰，干扰
molestation n. 折磨,干扰,妨害
mollify v. 安慰，安抚
mollusk n. 软体动物
mollycoddle v. 过份爱惜，娇惯；n. 娇生惯养的人
molt n. 换毛,脱皮,换毛期
molten adj. 熔化的；melt的过去分词
moment n.片刻；瞬间；时刻
momentary a.瞬息间的，片刻的
momentous adj. 极重要的，严重的
momentum n. 推进力，势头
momet 乐章
monarch n.君主，最高统治者
monarchical  adj.  (似) 君主 (国) 的;  (拥护) 君主制的
monarchy n. 君主政体,君主国,君主政治
monastery n. 男修道院，僧院
monastic adj. 修道院的
monasticism n. 修道生活，禁欲主义
Monday n.星期一
monetary a. 货币的,金钱的
money n.货币；金钱，财富
money-box n. 储蓄罐
moneylender n. 放债者
money-lender 放债者
money-making n. 赚钱
monger n. 商人,...商,...贩
Mongol  n.蒙古人
Mongolian n. 属于蒙古人种的人,蒙古语,蒙古症患者
mongoose n. 『动物』蒙
mongrel n. 杂种动物，混血儿
monition n. 忠告,训诫,警告
monitor n.班长；监视器
monk n.和尚
monkey n.猴子，猿
monkeys 猴子
monkish a. 僧侣,修道院士的,禁欲的
mono a. & n. 单音的
monochrome n. 单色
monogamy n. 一夫一妻制
monogram n. 字母组合
monograph n. 专题论文
monolith n. 巨型独石,大独石碑
monolithic adj. 巨石的，巨大的
monologue n. 独白，个人长篇演说
monopolist n. 独占者,专卖者,独占论者
monopolistic 垄断的，专利的
monopolize vt. 独占,垄断
monopoly n.垄断，独占，专利
monosyllable n. 单音节字
monotone a. 单调的
monotonous adj. 单调的，无聊的
monotony n. 单调,干燥,无味
monoxide n. 一氧化物
monsieur n.先生(法语)
monsoon n. 季雨，季风，大雨
monster n.怪物；畸形的动植物
monstrosity n. 畸形，怪物
monstrous a.可怕的；极大的
montana n. 蒙大纳(美国州名)
monte n.(西班牙式)纸牌戏
month n.月，月份
monthly a.每月的 ad.每月
monument n.纪念碑；纪念物
monumental a. 纪念碑的,做为纪念的,不朽的
moo vi. 鸣叫
mood n.心情，情绪；语气
moodiness n. 忧郁
moody a. 心情不稳的,易怒的,喜怒无常的
moon n.月球，月亮；卫星
moonbeam n. 月光
moon-explorer n. 月球探索者
moonlight n. 月光
moonlighting n. 业余干活
moonlit a. 月光照耀的
moonshine n. 月光,无聊的事,荒唐的空想
moonstone 月球石
moon-suit n. 登月服
moonwalk 月面行走
moor vt.使停泊；使固定
mooring 停泊
Moorish a. 摩尔人的,摩尔人式的,摩尔人风格的
moorland n. 荒野,荒地
moose n. 『动物』麇
moot n. 大会,讨论会,辩论会
mop n.墩布，洗碗刷
mope n./v. 抑郁不乐，生闷气
moped n.机动脚踏车
moraine n. 堆石
moral a.道德的；合乎道德的
morale n. 士气，精神力量
moralist n. 道德学家，卫道士
moralistic adj. 道学气的
morality n.道德，美德，品行
moralize vt. 教化,解说道德,用道德意义解释
morally adv. 道德上；道义上
morass n. 沼泽地，困境v. 陷入困境
moratorium n. 停止偿付，禁止
morbid adj.病态的，（思想等）不健康的
morbidity n. 病态
mordant adj. 讥讽的，尖酸的
more a.更多的 ad.更
moreever ad. 再者，此外
moreover ad.再者，加之，此外
mores n. 风俗习惯，道德观念
morganatic a. 贵贱通婚的
morgue n. 陈尸所
moribund adj. 即将结束的，垂死的
morion n. 无面甲的头盔
Mormon n. 摩门教徒,一夫多妻主义者
morn n. 早晨,明天
morning n.早晨，上午
morocco 摩洛哥
moron n. 极蠢之人，低能儿
morose adj. 脾气坏的，不高兴的
morpheme n. 形态素,词素
morphemics n. 构词学
morphine n. 吗啡
morrow n. 次日
morsel n. 一小块（食物），小量
mortal a.终有一死的；致死的
mortality n. 必死的命运,死亡数目,死亡率
mortally ad. 致命地
mortar n. 小臼，乳钵，迫击炮
mortgage n.抵押 vt.抵押
mortgagee 承受抵押者，抵押权者
mortgagor 抵押人，出抵人
mortician n. 殡仪业者
mortification n. 耻辱，屈辱
mortify v. 使屈辱，使痛心
mortise n. 榫眼v. 用榫接合
mortuary n. 停尸间，太平间
mosaic n. 镶嵌细工，马赛克
Moscow n. 莫斯科
Moslem n.&a.穆斯林(的)
mosque n.清真寺
mosquito n.蚊子
moss n.苔藓，地衣
mossy a. 生苔的,似苔的,陈腐的
most a.最多的 ad.最，很
most-favored-nation 最惠国
mostly ad.主要的，大部分
mote n. 微粒，微尘
motel n.汽车游客旅馆
moth n. 蛾
mothball (复)封存，保藏
mother n.母亲
motherhood n. 母道,母性,母爱
mother-in-law n. 岳母，婆婆
motherland n. 祖国
motherly a. 母亲的
motif n. （作品）主题，主旨
motion n.运动；手势；提议
motionless a. 不动的,静止的
motivate vt. 促动；激励，激发；鼓励，作为…的动机，促使
motivated a.有积极性的
motivation n. 动机；目的
motive a.发动的，运动的
motiveless a. 无动机的
motley adj. 混杂的，杂色的
motor n.发动机；机动车
motorbike 摩托车
motorcar n. 汽车
motor-car n. 摩拖车
motorcycle n. 摩托车
motor-engine n. 汽车发动机
motorist n. 乘汽车者,常坐汽车的人
motorman n. 电车
motorway n. 汽车道，快车路；高速公路
motor-way n. 快车道
mottle vt. 使成杂色
mottled adj. 有杂色的，斑驳的
motto n. 座右铭，箴言
mould n.模子，模型 vt.浇铸
moulding n. 模制；覆盖的土壤
mouldy adj.发霉的
moult n. 换毛,脱毛
mound n. 土墩,堤,小山
mount vt.登上，爬上 n.…山
mountain n.山；山脉
mountaineer n. 登山家,山地人
mountainous a.多山的；山一般的
mountains n. 山区，山脉
mountaintop 山顶
mountebank n. 江湖郎中，骗子
mounte-bank n. 江湖医生；骗子
mourn vi.&vt.哀痛；哀悼
mourner n. 悲伤者,哀悼者,送葬者
mournful adj. 悲伤的
mourning n. 哀痛；悲伤；治丧；戴孝
mouse n.鼠，耗子
moustache n.(嘴唇上面的)胡子
mouth n.嘴，口，口腔
mouthful n.满口，一口，少量
mouthpicec n.(电话)送话口
mouthpiece n. 发话筒,代言人,电话筒对嘴的一端
movable n. 家具,动产
move n.行动，步骤
moveable n. 活动的；(pl.)动产
movement n.动作，活动；移动
mover n. 移动的人,动者,鼓动者
movie n.电影；电影院
moving a. 感人的，动的；活动的，移动，动人的，令人感动的n. & a. 活动的，自动的
mow n. 草堆,皱眉,怪脸
mower n. 刈草的人,刈草机
mowing n. 割草(谷)；饲料地
moxa n. 艾；灼烙剂
moxibustion n. 艾炙；艾灼
mozart 莫扎特(奥地利作曲家)
Mr. n. 先生
mrs n. 夫人，太太；abb. 夫人，太太
Mrs. n. 太太,夫人
Ms. n. 女士
mu n. 亩
much ad.非常，很 a.许多的
much-travelled a. 旅游多的
mucilage n. 粘液，胶水，粘质物
muck n. 堆肥，淤泥
mucosa n. 粘膜
mucous a. 粘液的,粘的,粘液性的
mud n.软泥，泥浆
muddle n. 混乱，迷惑
muddle-headed a. 糊涂的
muddy a.多泥的，泥泞的
mudguard n. 挡泥板,汽车的挡泥板
mudhole n.泥坑
muff n. 笨蛋，弄糟
muffin n. 松饼
muffle v. 使声音降低，裹住
muffled a. 捂住的，低沉的
muffler n. 消音器，围巾
mufti n. 常服,便服,回教法典说明人
mug n.大杯
muggy adj. （天气）闷热而潮湿的
mugwump 不拥护本党候选人之人
mulberry n.桑树；桑葚
mulch n. 护盖物,护根,根篱
mulct n. 罚金
mule n. 骡,倔强之人
muleteer  n. 骡夫
mull n. 软薄布,混乱
mullet n. 乌鱼
multi (词头)多
multifarious adj. 多种的，各式各样的
multiform a. 各种形式的,多样的,多种的
multifunction n. 多功能的
multilateral 多边的，涉及多方的
multilingual a. 使用多种与语言的
multimeter n. 万用表
multinational 多国的，跨国的
multiple a.复合的；并联的
multiples n.跨国公司
multiplexing n.连锁商店；多路传输
multiplicand n. 被乘数
multiplication n.增加；繁殖；乘法
multiplicity n. 多数,重复,多样
multiplier n. 增殖者,使繁殖者,乘数
multiply vt.使增加；乘
multiprocessing n. 多重处理，多道处理
multitude n.大批，大群；大量
multitudinous a. 多数的,群聚的,种种的
mum n.妈妈
mumble n. 喃喃而语,咕哝
mumbo-jumbo n. 繁文缛节
mummer n. 哑剧演员,伶人
mummery n. 哑剧,装模作样的仪式,虚礼
mummy n.木乃伊；干尸
mumps n.腮腺炎
munch vt.vi. 用力咀嚼,大声咀嚼
mundane adj. 现世的，世俗的
munich n. 慕尼黑(德国城市)
municipal a.市的，市立的
municipality n. 自治区,市当局,全市民
munificence n. 宽宏大量,慷慨给与
munificent adj. 慷慨的，大方的
muniments n. 契据，房契
munition n. 军需品
munitions n. 军火，弹药
mural adj. 墙壁的n. 壁画
murder vt.&n.谋杀
murderer n.杀人犯，凶手
murderous a. 凶狠的,杀人的,致命的
murk a. 暗的,阴沉的
murkiness n. 黝暗,阴沉
murky adj. 黑暗的，朦胧的
murmur n. 低沉连续的声音；怨言；咕哝；v. 低声喃喃而语；低声说； 发低沉声音；发牢骚；柔声地说，喃喃而言；咕哝
murrain n. 瘟疫,家畜传染病
muscle n.肌肉
muscular a.肌肉发达的，强健的
musculature n. 肌肉系统；肌肉组织
muse vi.沉思，默想，冥想
museum n.博物馆
mushroom n.蘑菇，菌类植物
music n.音乐
musical adj.音乐的
musician n.音乐家；作曲家
musk n. 麝香鹿,能发出麝香的各种各样的植物
musket n. 步枪
musketeer n. 持步枪的士兵,步兵
musketry n. 步枪,步兵部队,步枪射击术
muskrat n. 麝香蔷薇
musky a. 麝香的,产生麝香的,麝香似的
muslin n.穆斯林
mussel n. 贻贝,蚌类
must v.aux.必须；必然要
mustache n. 髭，小胡子
mustang n. 野马,海军行伍出身的军官
mustard n.芥子，芥末
muster v. 召集，聚集
mustn't mod. & v. 不可以；切勿
musty a. 发霉的,霉臭的,落伍的
mutability n. 易变性,性情不定
mutable a. 易变的,性情不定的
mutate v. (使)突变；(使)变异
mutation n. 突变，变异
mute a.缄默的 n.哑巴
mutilate v. 残害，切断
mutilated 残缺不全的
mutilation n. 切断,毁损
mutineer n. 反叛者，背叛者
mutinous adj. 加入叛变的，反抗的
mutiny n. 叛变,兵变
mutter vi.轻声低语；抱怨
mutton n.羊肉
mutual a.相互的；共同的
muzzle n. 动物之鼻口,口络,枪口
muzzy adj. 模糊不清的，昏迷的
my pron.我的
myna 八哥
myopia n. 近视，缺乏远见
myopic a. 近视的
myriad adj. 许多，无数
myrmidon n. 家仆,部下,跟班
myrrh n. 没药
myrtle n. 桃金娘(一种灌木）
myself pron.我自己
mysteries a. 古代的秘密宗教仪式
mysterious adj.神秘的
mysteriously ad. 神秘地；故弄玄虚地
mystery n.神秘小说，侦探小说
mystic a. 神秘的,奥秘的
mystical a. 神秘的
mysticism n. 神秘,神秘教,神秘论
mystify vt. 使...大为吃惊；使神秘化
myth n. 神话故事
mythical adj. 神话的; 神话中的
mythological a. 神话的
mythology n. 神话，神话学
myxedema n. 粘液性水肿
myxomatosis n. 多发性粘液瘤
nadir n. 最低点，无底
nag v. 唠叨，烦扰
naiad n. 水中的仙女,女游泳家
nail n.钉子 vt.将...钉牢
nainsook n.  (原产印度之) 一种薄棉布
naive a. 幼稚的；天真的
naivete n. 天真烂漫,无邪,纯真
naivety n. 天真，纯朴，幼稚
naked a.裸体的；无遮敝的
nakedness n. 裸,明显,赤裸裸
name n.名字；名誉 vt.说出
name...after... v. 以…命名
named vt. 名叫；指定的，被指名的
nameless a. 无名的,匿名的,不可名状的
namely ad.即，也就是
namesake n. 同名的人,同名物
nap n.小睡，打盹，瞌睡
nape n. 项,颈背
napery n. 抹布；餐巾
naphtha n. 挥发油
napkin n.餐巾(纸)
naples n. 那不勒斯(意大利)
napoleon n. 拿破仑
narcissism n. 自恋，自爱
narcissus n. 水仙
narcotic n. 催眠药adj. 催眠的
nard n. 甘松,甘松香
narrate vt.vi. 说故事,说明,叙述
narration n.叙述；故事；叙述法
narrative n. 叙述,故事
narrator n. 讲述者
narrow adj.狭窄的
narrowly ad. 勉强地；严密地
narrow-minded a. 思想狭隘的
narrowness n. 狭隘
nasal adj. 鼻的，有鼻音的
nascent adj. 初生的，萌芽的
nashville 纳什维尔(美国地名)
nasturtium n. 旱金莲属植物
nasty a.龌龊的；淫猥的
natal a. 出生的,诞生的
natation n. 游泳
natch 自然地
nation n.民族；国家
national adj.国家的；民族的
nationalism n. 民族主义,民族之特性
nationalist n. 民族主义
nationality n.国籍；民族，族
nationalization 国有化
nationalize v.国有化
nation-wide a.全国的
native adj.本国的，本土的
nativity n. 出生，诞生
natty adj. 整洁的，漂亮的
natural adj.自然的
naturalism n. 自然(状态)
naturalist n.博物学家
naturalization n. 归化,移入,移植
naturally adv. 自然地；天然地；必然地；天生地
nature n.大自然，自然界
naught n. 无，零，无用
naughty adj.顽皮的；淘气的
nausea n. 作呕，恶心
nauseate v. 使作呕，使厌恶
nauseous a. 令人作呕的,厌恶的
nautical adj. 船员的，航海的
nautilus n. 鹦鹉螺,缸鱼,鹦鹉螺号
naval n.海军的，军舰的
nave n. （教堂的）中殿，信众席
navel n. 肚脐，中心点，脐带
navicert 航运执照
navigable a. 可航行的,可通船的,适于航行的
navigate vi. 飞行；航行
navigation n.航行；航海术；导航
navigator n. 航海家
navvy n. 挖土工；挖泥机
navy n.海军
nay ad. 否,不,不但如是
nazi n. & adj. 纳粹
nazism n. 纳粹主义
n-bomb 中子弹
neap a. 小潮的
near ad.近，接近 a.近的
nearby adj.附近的 adv.附近
near-by a. 附近的；ad. 在附近
nearest adj. 最近的；ad. 最近的，最亲近的
nearly adv.几乎，差不多
nearness n.接近，亲近
nearsighted a. 近视的,浅见的
near-sighted a. 近视的
neat adj.整洁的；整齐的
neath prep. 在…下边
neatly ad. 整齐地
neatness n. 整洁,干净
nebula n. 星云，喷雾剂
nebulae n. 星云
nebulous adj. 模糊不清的，云状的
necessarily adv.当然；必定，必然地
necessary adj.必需的，必要的
necessitate vt. 迫使,使成为必需,需要
necessitous adj. 贫困的，急需的
necessity n.必要性；必然性
neck n.颈，脖子
neckerchief n. 围巾，颈巾
necklace n.项链，项圈
necktie n. 领带
neckwear n. 领子,领带,围巾之类
necrology n. 死者名册,死亡启事
necromancer n. 巫师
necromancy n. 巫术，通灵术
necropolis n. 公墓
nectar n. 甘美的饮料，甘露，花蜜
nectarine n. 油桃
need vt.需要 v.aux.需要
needful a. 必要的,需要的
needle n.针，缝补，编织针
needless a.不需要的
needlewoman n. 缝纫女工
needlework n. 刺绣,缝纫
needn't (同) need not
needy a. 贫穷的,贫困的,生活艰苦的
nefarious adj. 违法的，邪恶的
negate v. 取消，否认
negation n. 取消
negative a.负的，阴性的
neglect vt.忽视，忽略；疏忽
neglectful adj. 不留心的，疏忽的
negligence n. 疏忽，粗心
negligent a. 疏忽的,粗心的,不在意的
negligible a.微不足道的
negotiable adj. 可谈判的；可协商的，可转让的，可流通的；可商量的，(支票)可兑现的
negotiate vi.谈判，交涉，议定
negotiating 谈判
negotiation n. 谈判
negress n. 女黑人
Negro n.黑人 adj.黑人的
negroid a. & n. 黑人(似的)
negus n. 一种酒
Nehru n.(印度前总理，独立运动领袖)尼赫鲁
neigh n./v. 马嘶，马嘶声
neighbor n. 邻居
neighborhood n. 附近,邻近
neighboring adj. 邻近的，相邻的；接壤的
neighbour n.邻居；邻人
neighbourhood n.邻居关系；邻近
neighbouring a. 邻近的，接壤的
neither adj.&pron.(两者)都不
neither...nor 既不…也不
neither...nor... 既不…也不…
nemesis n. 报应，天罚
neolithic adj. 新石器时代的
neologism n. 新字，新义
neon n. 氖
neonate n. 初生婴儿
neophyte n. 初学者，新手
neoplasm n. 瘤；赘生物
nephew n.侄子，外甥
nephritis n. 肾炎
nepotism n. 裙带关系
Neptune 海王星
nereid n. 海精,海的女神,沙蚕
nerissa n. 尼莉莎(女名)
nerve n.神经；勇敢，胆量
nerveless adj. 无生气的；松散的；无勇气的
nervous adj.神经质的
nervously adv. 紧张不安地；神情激动地；神经质地；胆怯地
nervousness n.神经过敏
nescient a. 无知的；不可知论的
nest vi.筑巢 vt.为…筑巢
nestle v. 舒适地安顿，依偎在
nestling n. 尚未离巢的小鸟
Nestor n.(希腊诗人荷马)意指聪明的老人
net vt.用网捕；用网覆盖
nether adj. 下部的，下面的
Netherlands n. 荷兰,地区名
nethermost adj. 最低的，最下方的
nettle n. 荨麻，v. 烦忧，激恼
network n.网状物；网络
neural adj. 神经的
neuralgia n. 神经痛
neurology n. 神经病学
neuron n. 神经原，神经细胞
neurosis n. 精神病
neurotic n. 神经病患者
neurotoxic a. 毒害神经的
neutral a.中立的；中性的
neutrality n. 中立,不偏不倚,中间状态
neutralization 中和
neutralize v. 使无效，中和
neutron n. 中子
nevada n. 内华达(美国州名)
never adv.从来没有；决不
never-ending a. 永不休止的
nevermore ad. 决不再,不重覆
never-never 分期付款制
nevertheless conj.然而 ad.仍然
new adj.新的
newborn n. 婴儿
newcomer n. 新来者
newfangled a. 新奇的,最新式的,最新流行的
newfoundland n. 纽芬兰(岛)(加拿大)
newly ad.新近，最近
newly-crowned n.新获得冠军的
newly-weds n. 新婚夫妇
news n.新闻，消息
newsagent n. 报纸杂志经销社
newsboy n. 报童,送报人
newspaper n.报纸
newspaperman n. 新闻记者
newsreel n. 新闻影片；新闻短片
newt n. 蝾螈
newton n.牛顿(英国科学家)；牛顿(力的单位)
next a.紧接的；贴近的
nexus n. （看法等的）连系，连结
niagara n. 尼亚加拉河
nib n. 钢笔尖
nibble v. 一点点地咬，慢慢啃
nicaragua n. 尼加拉瓜(拉丁美洲)
nice adj.好的，好看的
nicely ad. 恰好地；谨慎地
nicety n. 美好,准确,精密,细节,纤细
niche n. （放艺术品等的）壁龛，合适的位置
nick n. 小伤口，刻痕
nickel n.镍；镍币
nickle n. 镍，五分镍币；vt. 镀镍(kickle=kickel)
nickname n.绰号，浑号
nicotine n. 尼古丁
niece n.侄女，甥女
nigeria n. 尼日利亚
nigerian n. 尼日利亚人
niggard n. 吝啬鬼
niggardly adj. 吝啬的，勉强的
niggling adj. 琐碎的，费神的
nigh a. 在附近的
night n.夜，夜间
nightcap n.睡帽
nightfall n. 傍晚,黄昏,日暮
nightgown n. (妇女、儿童的宽长) 睡袍
nightingale n. 夜莺
nightly a. 每夜的,夜间的
nightmare n.恶梦；经常的恐惧
nightshade n. 龙葵属植物
nightshirt n. 睡衣用的长衬衣
nihilism n. 虚无主义，无政府主义
Nike n.(商标名)耐克
nil n. 无，零分
nile n. 尼罗河(非洲)
nimble adj. 敏捷的，灵活的
nine n. 九；num. 九；九个
ninepin n. 九柱戏中的木柱
nineteen num.十九，十九个
nineteenth a. 第十九,十九分之一
ninetieth a. 第九十,九十分之一
ninety num.九十，九十个
ninth num.第九；九分之一
nip n. 捏,夹,寒冷,小饮
nipper n. 镊子,手铐
nippers n. 钳子，镊子
nipping adj. 尖酸的，剌骨的
nipple n. 乳头,奶头,奶嘴
nirvana n. 心灵的平静，解脱
nit n. 卵，幼虫；饭桶，傻瓜
nite n. 夜，夜间(nite=night)
niter n. 『化学』硝酸钾; 硝酸钠; 智利硝石
nitpick v. 挑剔，吹毛求疵
nitrate n. 硝酸盐
nitre n.硝石
nitric a. 氮的,含氮的,硝石的
nitrogen n.氮
nitrogenous a. 氮的,含氮的
nitrous a. 氮的,含氮的,硝石的
no adv.不，不是
no. n. 数子；号码；(缩)…号，第…号(no.＝number)
no...until... 直到...才...
noah n. (圣)诺亚
nob n. 头,和所翻牌同花的Jack,大人物
nobel 诺贝尔(姓)
nobility n. 贵族,高尚,贵族阶级
noble a.贵族的；高尚的
nobleman n.贵族
nobleness n. 高贵,高洁,高尚
nobly ad. 华丽地,高洁地,豪爽地
nobody pron.没有人
nock 弓两端的凹口；vt. 把(箭)搭在弦上
nocturnal adj. 夜晚的，夜间发生的
nod n.&vi.点头
node n. 节,结节,瘤
nodular adj. 有结节的
nodule n. 小节,小瘤,小结节
noes 鼻子
no-fault 不追究责任的
noise n.喧闹声；响声；噪声
noiseless a. 无声的,寂静的
noiselessly ad. 静静地，轻轻地
noisily adv. 喧闹地
noisome adj. 恶臭的，令人不快的
noisy a.嘈杂的；喧闹的
nomad n. 流浪者，游牧部落的人分割
nomadic adj. 游牧的，流浪的
nome n. 古代埃及的省名
nomenclature n. 术语，命名系统
nominal adj. 名义上的，有名无实的
nominate vt.提名，推荐；任命
nomination n. 提名，指派
nominative n. 主格,主格语
nominee n. 被提名的人,被任命者
non n. 不合理的推论或结论；ad. (拉)非，不是
non-auditory a. 非听觉的
nonavailable (缩)n.a.，无资料不详
nonce n. 现时,目前,当前
nonchalance n. 无动于衷，冷淡
nonchalant adj. 冷漠的，满不在乎的
nonchalnant a.冷漠
noncommittal adj. 态度暖昧的，含糊的
nonconcessional 非减让的，非优惠的
nonconformist n./adj. 不遵照传统生活的（人）
nonconformity n. 不遵从(传统)
noncontraband 非违禁品
noncontractual 非契约的
noncontributory 不用职工缴款的
nonconvertible 不可兑换的
nondeductible 不扣除的
nondefective 合格品良种
nondelay 不迟发无延误
nondelivery 无法投递末能送达
nondepreciable 不计折旧的
nondescript adj. 没有特征的，平凡的
nondetachable 不可拆开的
nondiscountable 非贴现的，不打折扣的
nondurable 非耐用品
none pron.没有人 ad.毫不
nonentity n. 无能力之人，不重要
nonequity 非股权
nonesuch n. 无匹敌的人，无双的人
nonetheless ad.然而；尽管；不过
non-existent a. 不存在的
nonfeasance 不履行义务
non-fiction n. 非小说类文学作品
nonflammable adj. 不易燃的
nonhuman a. 非人类的
noninteractive a. 不相关的，非交互的
noninterest 无利息
nonintervention 不介入，不干涉
noninvolvement 不卷介入
nonlinear a.非线性的
non-living a. 无生命的
nonloaded 空载的，无载的
nonloss 无损耗，无亏损
nonmarket 非市场的，非商业性的
nonmarketable 不可流通的，无销路的
non-metal n. 非金属物质
nonmonopoly 非垄断非独占
nonnegotiable 禁止转让的，不可流通的；不可谈判的，无商议余地的
nonobservance n. 不遵守，违犯(规则等)
nonoperating 非营业的
nonpareil n./adj. 无匹敌的（人）
nonpayment 无力支付，不支付，停止支付
nonperiodicity 非周期性
nonperishable 不易腐的
nonplus v. 使窘困，狼狈不堪
non-poisonous a. 无毒的
nonprivileged 大特惠的
nonproductive 非生产性的，无生产力的
nonprofessional 非专业的；无职业的
nonprofit a.非赢利的
nonreciprocal 单方面的，非互惠的
nonrecognition 不承认
nonrecourse 无追索权的
nonsense n.胡说，废话
non-skeletal adj. 不属于骨骼的
nonskid adj. (轮胎)防滑的
nonsmoker n.不抽烟者
non-smoker n. 不抽烟的人
nonspecific a. 非特异性的
nonstock 无库存无股票的
non-stop adj. 不停的
non-surgically ad. 非外科手术地
nontariff 非关税
nonviolent adj. 不使用暴力的，非暴力的
noodle n. 面条；(常用复数)面条
nook n. 凹角，隐匿处
noon n.中午，正午
noonday n. 正午
noontide n.中午,正午
noose n. 绳套，绞索（刑）
nor conj.也不；不
norm n. 标准，规范；平均数；定额；准则
normal adj.正常的，正规的
normality n.正常；常
normalization n. 正常化，标准化
normalize v. 使正常，使标准化
normally adv. 通常地；一般地；正常地；平常地
Norman n.诺曼第人
normandy n. 诺曼底(法国一地区)
normative adj. 规范的，惯常的
Norse  n.
Norseman n. 古代挪威人,古代斯堪地那维亚人
north n.北部，北方
northeast n.东北 a.位于东北的
northeasterly  adj. 东北的
northeastern a. 东北方的,在东北的,来自东北的
northerly a. 北方的,向北的,来自北方的
northern a.北方的，北部的
Northerner n.北方人,北部人
Northman n. 古代斯堪地那维亚人,古代北欧人,
northward adv.向北方
northwest n.西北 a.位于西北的
northwestern a. 在西北部的,西北方的,来自西北的
Norway n.挪威
Norwegian n. 挪威人,挪威语
nose n.鼻子
nosegay n. 花束
nostalgia n. 怀旧之情，思乡病
nostril n. 鼻孔
nostrum n. 秘方药，万灵丹
not ad.不，没有
not...but... 不是…而是…
not...until 直到…才
notability n. 著名，显著
notable n.值得注意的；著名的
notably adj. 尤其，值得注意地；ad. 显著地；著名地；特别是
notarial 公证的
notary n. 公证人
notation n. 记号法,表示法,注释
notch n. V字形刻痕，山间窄路
notched adj. 有凹口的，有缺口的
notco n. 诺特可(公司名)
note n.钞票，纸币；笔记
notebook n.笔记本，期票簿
noted a.著名的，知名的
notepaper n. 便条纸
note-taking n. 笔记，笔录
noteworthy a. 值得注目的,显著的
nothing n.没有东西 ad.毫不
nothingness n.无,空,不存在
notice vt.注意 n.通知；注意
noticeable a.显而易见的；重要的
noticeably ad. 显著地，显然
notice-board n. 布告牌
notification n. 通知,通告,告示
notify vt.通知，告知；报告
notion n.概念，意念；看法
notoriety n. 臭名昭彰
notorious a.臭名昭著的
nottingham n. 诺丁汉(英国城市)
notwithstanding prep.尽管，虽然
nought n.无，零
noun n.名词
nourish vt.提供养分，养育
nourishment n.食物；营养(情况)
nov. (同)november；n. 十一月
novation 更替
novel n.小说 a.新的
novelette n. 中篇小说
novelettish adj. 言情的，多愁善感的
novelist n. 小说家
novelty n.新颖；新奇的事物
November n.十一月
novice n. 生手，新手
novitiate n. 见习期
novocaine n. 奴佛卜因(一种麻醉药)
now ad.现在；立刻；于是
nowadays ad.现今，现在
nowhere ad.任何地方都不
nowise ad. 毫不,决不
noxious adj. 有害的，有毒的
nozzle n. 喷嘴
nuance n. 细微的差异
nubile adj. （女孩）到婚嫁年龄的，吸引人的
nuclear a.原子核的；核心的
nucleus n.核，核心；(原子)核
nude adj. 赤裸的，n. 裸体者
nudge v. （用肘）轻触，轻推
nudity n. 裸露
nugatory adj. 无价值的，琐碎的
nugget n. 金块,贵金属块,硬块
nuisance n.讨厌的东西
null a. 无效力的,无效的,无价值的
nullification n. 无效,废弃,取消
nullify v. 使无效，抵消
nullity n. 无效，无兴趣
numb adj. 麻木的，v. 使失去感觉
number vt.共计，达…之数
numberless a. 无数的,无号数的
numbers n. 音律，调子
numbness n. 麻木,麻痹,冻僵
numerable a. 可数的，可计数的
numeral n. 数字,数
numerate vt. 数，计算
numerator n. 分子,计算者,计算的东西
numeric n. & a. 数字的，分数
numerical a.数字的，数值的
numerology n. 命理学
numerous a.为数众多的；许多
numinous adj. 庄严的，神圣的
numismatic adj. 钱币学的
numismatist n. 钱币学家，钱币收藏家
nun n.修女，尼姑
nunnery n. 女修道院，尼姑庵
nuptial adj. 婚姻的，婚礼的
nuptials n. 婚礼
nurse n.护士
nursery n.托儿所；苗圃
nurseryman n. 苗圃主人,树苗培养工
nurses 护士
nursing n. 护理；保育
nursling n. 婴儿,幼儿,养子
nurture n. 养育,营养物,教育
nut n.坚果，干果；螺母
nutcracker n. 胡桃钳,星鸟类
nutmeg n. 肉豆寇,肉豆寇种子中的核仁
nutraceuticals n.营养药品
nutrient n. 营养品，滋养物
nutriment n. 营养物,食物,营养素
nutrition n. 营养
nutritional a.营养的，滋养的
nutritious a. 有营养的
nutritive a. 有营养的,有营养成分的,与营养有关的
nutshell 无价值的东西
nutting n.拾
nuzzle vt. 挨擦
nylon n.尼龙，耐纶
nymph n. 美女，幼虫，蛹
o int. …啊
o.k. adj. & n. (缩)对，行；a. & adv. 对，好可以，行
oaf n. 呆子,畸形儿
oafish adj. 呆子的，白痴的
oak n.栎属植物；栎木
oaken a. 橡木制的
oakum n. 填絮
oar n.桨；划手 vi.划(行)
oarfish n. 皇带鱼
oasis n.(沙漠中的)绿洲
oast n. 啤酒花烘炉
oat n. 燕麦,麦片粥
oaten a. 燕麦的,麦杆制的
oath n.誓言，誓约，宣誓
oatmeal n. 燕麦片,燕麦粥
obduracy n. 顽固,执拗,冷酷
obdurate adj. 固执的，顽固的
obedience n.服从，顺从；管辖
obedient n.服从的，顺从的
obeisance n. 鞠躬，敬礼
obelisk n. 方尖石塔,短剑号,疑问记号
obese adj. 极肥胖的
obesity n. 肥胖
obey vt.顺从 vi.服从
obfuscate v. 使困惑，使迷惑
obigor n.债务人，欠债者
obituary a. 死亡的
object n.物，物体；目的
objection n.反对，异议；不喜欢
objectionable adj. 令人厌恶的
objective a.客观的；无偏见的
objurgate v. 怒斥，谴责
objurgation n. 叱责,非难
oblation n. 宗教的供品，祭品
obligate vt. 使负义务,强制,预留,施恩惠于
obligation n.义务，职责，责任
obligator 欠债者，债务人
obligatory adj. 强制性的，义务的
oblige vt.强迫；迫使
obligee 债权人，权利人
obliging adj. 恳切的，热心助人的
obligor 债务人，义务人
oblique adj. 间接的，斜的
obliquity n. 倾斜,交叉,暧昧,不坦率,倾角
obliterate v. 涂掉，擦掉
oblivion n. 遗忘
oblivious adj. 不在意的，疏忽的
oblong n. 长方形,椭圆形
oblongata n. 延髓
obloquy n. 大骂，斥责，坏名声
obnoxious adj. 令人不愉快的，可憎的
oboe n. 双簧管
obscene adj. 淫秽的
obscenity n. 淫秽,猥亵
obscure a.阴暗的；蒙昧的
obscurity n. 费解，不出名
obsequies n. 葬礼
obsequious adj. 逢迎的，谄媚的
observable adj. 可观察的,看得见的; 可识别的
observance n. 遵守，奉行（法律，习俗）
observant adj.留心的,善于观察的
observation n.注意；观察；观察力
observatory n. 天文台,气象台,了望台
observe vt.&vi.观察
observer n.观察员，观测者
obsess vt. 迷住,使困扰
obsession n. 入迷，固执的念头
obsidian n. 黑曜石,十胜石
obsolescence  n. 废弃，过时，陈旧
obsolescent adj. 即将过时的
obsolete adj. 废弃的，过时的
obstacle n.障碍，障碍物，妨害
obstain vt. 获得，得到
obstetrician n. 产科医师
obstetrics n. 产科学，助产术
obstinacy n. 倔强,顽固,固执
obstinate a.固执的；顽强的
obstinately ad. 固执地
obstreperous adj. 吵闹的，难管束的
obstruct v. 阻塞，截断
obstruction n. 阻挠，障碍物
obtain vt.获得，得到，买到
obtainable  adj. 能得到的,可获得的,可到手的
obtention n. 获得
obtrude v. 突出，强加
obtrusive adj. 突出的，炫耀的
obtuse adj. 愚笨的，不锐利的
obverse n. 正面
obviate v. 排除（困难）
obvious adj. 明显的，显著的；显而易见的；清楚的；明白的
obviously adv.显而易见地
ocarina n. 陶制的卵形笛
occasion n.场合，时刻；时机
occasional a.偶然的；临时的
occasionally adv.偶然；非经常地；偶而，有时
occassion n....的时刻；机会；需要 vt.引起，导致
occident n. 西洋,欧美,西欧诸国
Occidental n./adj. 西方（的）
occult adj. 秘密的，不公开的
occupancy n. 占有,居住,占领
occupant n. 占有者,居住者,占领者
occupation n.占领，占据；职业
occupational 职业性的
occupy vt.占领；占，占有
occur vi.发生；出现，存在
occurence n.发生；出现
occurrence n. 发生，出现；(偶发)事件；事故
ocean n.海洋；洋
oceanarium n. 大型水族馆
Oceania n.大洋洲
oceanic a. 海洋的,海洋产出的,住于海洋的
oceanography n. 海洋学
ocelot n. 豹猫
ocher n. 赭土,赭石
ochre n. 赭石,赭色
o'clock ad.…点钟
oct. (同)october；n. 十月
octagon n. 八边形,八角形,八角堂
octave n. 『音乐』第八音; 第八度音程
octavo n. 八开纸,八开本
October n.十月
octogenarian n. 八十～八十九岁的人
octopus n. 章鱼
octuplicate 一式八份
ocular adj. 眼睛的，可见的
oculist n. 眼科医生
odd a.奇数的；单只的
oddity n. 奇异,奇妙,奇特
oddly ad. 奇妙地,奇怪地,单数地
oddments n. 残余物，零头
odds n. 困难，差额；可能性；差异；机会；优势
ode n. 长诗，颂歌
odious adj. 可憎的，讨厌的
odium n. 憎恶，反感
odometer n. 里程表，计程仪
odor n. 气味
odoriferous adj. 有香味的，芳香的
odorless a. 无气味的
odorous a. 芬芳的,臭的,有气味的
odour n.气味，香气；味道
odyssey n.长途冒险旅行；一连串的冒险
oesophagus n. 食道
of prep....的
off prep.&adv.(离)开
offal n. 渣滓，下水
off-duty adj. 不当班的
offence n.犯罪，犯规；冒犯
offend vt.冒犯 vi.犯过错
offender n. 罪犯,无礼的人,得罪人的人
offense n. 错事，得罪
offensive a.冒犯的；进攻的
offer vt.提供；提出 n.提供
offeree 特价提供
offerer 确认你方报盘
offering n. 报盘，提供的货物；提供；礼物；捐献；实盘
offertory n. 奉献仪式,捐款
off-grade adj. 等外的，质差的
offhand a. 即时的,即席的,无准备的
off-hand a.未经准备的；不客气的
office n.办公室；处，局，社
officer n.军官
official adj.官方的，正式的
officially ad. 作为公务员,职务上,官方地
officiate vt. 执行,司仪
officious adj. 爱发命令的，好忠告人的
offset n.分支，抵销 vt.抵销
offshoot n. 分支,支流
offshore adj. 离岸的；近海的；adv. 离岸，近海，向海面；商品销售，商品销售量
offspring n.儿女，子孙，后代
often ad.经常，常常
oftentimes ad. (古)屡次，常常
ofttimes ad.经常
ogle v. 送秋波，n. 媚眼
ogre n. 食人魔鬼,怪物,象鬼的人
oh int.嗬，哦，唉呀
ohio n. 俄亥俄(美国州名)
ohm n.欧姆
oil n.油；石油 vt.加油于
oilcloth n. 油布,油毯的一种
oilfield n. 油田
oilskin  n.油布,防水布
oily a. 油的,油滑的,油嘴的
ointment n. 油膏，软膏
OK adv.对；好；可以
okay (缩作OK)a.&ad.对，好
okey a. & ad. 对，好，可以；同意，许可(okey=okay)
oklahoma n. 俄克拉何马(美国)
old a.老的；…岁的
olden a. 古时的,从前的
old-fashioned a. 旧式的,保守的,挑剔的
old-time a. 老资格的；古时的
oleander n. 夹竹桃
olfactory adj. 嗅觉的
oligarchy n. 寡头政治
olive n.橄榄，橄榄树
Olympian a.奥林匹克的
Olympic adj.奥林匹克的
olympics n. 奥林匹克运动会
olympus n. (希腊)奥林匹斯山
omega n. 希腊字母的最后一个字,终了,
omelet n. 蛋卷，煎蛋皮
omelette n. 煎蛋
omen n. 征兆、预兆
ominous adj. 预兆的、不祥的
ominously ad. 不吉祥地
omious a.不祥的，不吉利的
omission n. 遗漏，省略
omit vt.省略，省去；遗漏
omnibus n. 公共汽车,公共马车,精选集
omnipotence n. 全能,无限的力量,全能之神
omnipotent adj. 全能的、万能的
omnipresent a. 无所不在的,同时遍在的
omniscience n. 全知,全知者,神
omniscient adj. 无所不知的、博识的
omnivorous adj. 杂食的，兴趣广泛的
on prep.在...上
on...basis 在...基础上
once ad.一次；曾经 n.一次
oncoming a.即将来临的；接近的
one pron.一(个，只...)
one-eyed adj. 一只眼的
one-man a. 个人的
onerous adj. 繁重的、麻烦的
ones n. 二进制反码
oneself pron.自己；亲自
one-sided adj. 片面
ongoing a.继续的
onion n.洋葱，洋葱头
on-line a. 联机的
onlooker n. 旁观者，观众
only ad.只，仅仅 a.唯一的
onomatopoeia n. 拟声,拟声语,声喻法
on-screen 在屏幕上的
onset n. 开始
onslaught n. 猛攻，猛袭
ontario n. 安大略湖(北美洲)
onto prep.到…上
ontology n. 实体论，本体论
onus n. 义务，责任
onward a. 向前的,前进的
onward(s) ad. & a. 向前(的)
onyx n. 缟玛瑙
ooze v. 慢慢地流，渗出，（勇气）逐渐消失
oozy a. 软泥的,漏的,渗出的
opacity n. 不透明，暖昧
opal n. 蛋白石,猫眼石
opalescent adj. 像蛋白石的，发乳白光的
opaque a.不透明的；不传导的
ope v. 打开
open a.开的；开放的 vt.开
open-air a. 户外的
opened a. 开路的，断开的
open-end 开放的；不受限制的
opener n.开始者,开启瓶盖、罐头等的工具
opening a.开始的 n.开始
openly ad. 公开地；直率地
open-minded a. 坦率的
opera n.歌剧
operate vi.&vt.动手术；操作
operatic a. 歌剧的,歌剧风格的
operating a. 操作的，控制的
operation n.运算
operational adj. 业务上的，操作的；可使用的；盍的
operative adj. （计划等）实施中的，生效的
operator n.操作人员，接线员
operetta n. 小歌剧
ophthalmia n. 眼炎
ophthalmology n. 眼科
opiate n. 安眠药，鸦片制剂
opine vt.vi. 想,以为
opinion n.意见，看法，主张
opinionated adj. 固执已见的
opium n.鸦片；麻醉剂
opossum n. 尾有卷握力的小有袋动物,负鼠
opponent n.对手，敌手；对抗者
opportune adj. 合适的，适当的
opportunist n. 机会主义者,投机取巧者
opportunity n.机会，良机
oppose vt.反对；反抗
opposed a. 反对的
opposite adj.对面的；相对的
opposition n. 反对；敌对
oppress vt.压迫；压抑
oppression n. 压抑,沉闷,压迫手段
oppressive adj. 残酷的、压迫的
oppressor n. 压迫者,压制者,暴君
opprobrious adj. 辱骂的，恶名声的
opprobrium n. 耻辱；责难；恶名声，侮辱
opt vi. (for)抉择；选择
optic a. 眼睛的,视觉的,光学的
optical a.眼的；光学的
optician n. 光学仪器商,眼镜商,光学仪器制造厂
optics 光学
optimal adj. 最佳的；最适宜的，最理想的
optimism n.乐观，乐观主义
optimist  n. 乐观主义者; 乐观者
optimistic a.乐观的；乐观主义的
optimize v. 最佳化；优选，优化
optimum n.最适条件，最适度
option n.选择，取舍
optional a.可以任意选择的
options 选择购买权；预约
optometrist n. 配镜师
opulence n. 富裕
opulent adj. 富裕的，充足的
opus n. 作品
or conj.或者
oracle n. 代神发布神谕的人
oracular adj. 神谕的，意义模糊的
oral a.口头的；口的
orally adv. 口头地
orange n.橙子，桔子
orange-coloured a. 橘红色的，橘黄色的
oranges 桔子
oration n. 正式演说，演讲
orator n. 演说者,演讲者,请愿人,原告,
oratorical a. 演说的,雄辩的,演说家的
oratorio n. 清唱剧
oratory n. 演讲术，祈祷室，小礼拜堂
orb n. 球,天体,圆形物
orbit n.运行轨道 vt.环绕
orchard n.果园
orchestra n.管弦乐队
orchestral a. 管弦乐的
orchid n. 兰花，称赞
ordain v. 任命，命令
ordeal n. 严峻考验，痛苦经验
order n.定货；定货单
orderly a.整洁的；有秩序的
ordinal a.依次
ordinance n. 法令，条
ordinarily adv. 通常；大概；普通地；一般
ordinary a.平常的；平凡的
ordinary-looking adj. 相貌平常的；长相一般的
ordinate n. 纵标，纵坐标
ordination n. 授任圣职
ordnance n. 大炮，军械
ordure n. 污物,排泄物,粪
ore n.矿，矿石，矿砂
oregon n. 俄勒冈(美国州名)
organ n.器官；机构；管风琴
organdie n.玻璃纱
organdy n.玻璃纱
organic a.有机体的；器官的
organisation n. 组织，安排，团体，有机休
organise n. 组织，安排，筹办
organism n.生物体；有机体
organist n. 风琴弹奏者
organization n.组织；团体，机构
organizational adj. 组织的
organize vt.组织，编组
organizer n.组织者，创办人
orgy n.狂欢，酒宴
oriel n.『建筑』凸窗
orient n.东方；亚洲，远东
oriental a.东方的；东方国家的
orientate vt.定...位；给...定位
orientation n.向东；定位；方向
oriented a. 有向的，定向的
orifice n. 小开口，小孔
origin n.起源；开端
original a.最初的；新颖的
originality n. 创造性，独特性
originally adv. 原来，当初；最初；本来；独创地
originate vi.发源 vt.首创
originator n. 创始人
oriole n. 金莺类,白头翁科的小鸟
orion n. (天)猎户星座
orison n. 祈祷
ork 管弦乐队
orleans n. 奥尔良(法国)
ornament n.装饰物 vt.装修
ornamental a.装饰的 n.装饰品
ornamentation n. 装饰
ornate adj. 华美的，充满装饰的
ornithologist n. 鸟类学者
ornithology n. 鸟类学
orotund adj. （声音）宏亮的，说大话的
orphan n.孤儿
orphanage n. 孤儿院
ort n. 吃剩下的食物
orthodontics n. 畸齿矫正学
orthodox adj. 正(传)统的；习惯的；正派的
orthodoxy n. 正统学说
orthography n. 正确拼字,拼字,正字法
orthopedics n. 矫形，正骨；骨科学；整形手术，整形外科
oscillate v. 摆动，犹豫
oscillation n. 振动，踌躇
oscillator n.摆；钟
osier n. 柳之一种
osmosis n. 渗透，渗透作用；潜移默化
osmotic a. 渗透的
osprey n. 白色的羽毛,鱼鹰
osseous adj. 骨的，多骨的
ossify v. 硬化，骨化
ost (特例)丢失的，迷途的
ostensible adj. 表面上的，伪装的
ostentation n. 夸示，炫耀
ostentatious a. 装饰表面的,夸示的,华美的
ostler  n.马夫
ostracise v. 排斥；放逐
ostracism n. 贝壳流放,放逐,排斥
ostracize v. 放逐，排斥
ostrich n. 鸵鸟，不接受现实的人
other pron.另一个人(或物)
otherwise ad.另外；在其他方面
otiose adj. 不必要的，多余的
otter n. 水獭,水獭皮
ottoman n. (有垫褥而无靠背或扶手之) 沙发
ouch int. 哎唷
ought v.aux 早应该，本应
ounce n.盎司，英两
our pron.我们的
ours pron.我们的
ourself pron. (同)myself
ourselves pron.我们自己
oust vt. 驱逐
out ad.出，在外；现出来
outage 储运损耗
outbalance 超过，胜过，优于
outbid v. 出价多于(他人)
outbrave vt. 勇敢地面对...,在勇气方面胜于,
outbreak n.(战争、愤怒等)爆发
outbuilding n. 外屋
outburst n.(感情的)爆发
outcast a. 被逐出的,被遗弃的,无家可归的
outcome n.后果，成果
outcry n. 呼叫；呐喊
outdated a.过时的，不流行的
outdo vt. 超越,胜过,战胜
outdoor a.户外的，室外的
outdoors ad.在户外，在野外
outer adj.外部的
outermost a.最外面的，最远的
outfit n. 用具,配备,机构
outfox v. 以机智胜过
outgo n. 外出,支出
outgoing adj. 友善的，即将离去的
outgrow vt. 发展得...不再够用
outgrowth n. 产地
outhouse n. 外屋,厕所
outing n. 郊游,远足
outland n. 偏僻地区
outlandish adj. 奇怪的，古怪的
outlast vt. 比...长久
outlaw n.被放逐者
outlawry n.公权的剥夺,宣布非法; 禁止;
outlay n. 费用,经费,支出
outlet n.电源插座
outline n.轮廓；略图；大纲
outlive vt. 生存得比…更久; 比…更经久
outlook n.观点，看法；展望
outlying a. 远离中心的；边远的
outmoded adj. 不再流行的，过时的
outnumber vt. 数目超过,比...多
out-of-date a. 废弃的，过时的
out-of-stock n.缺货；脱销
out-patient n. 门诊病人
outperform v. 超额完成，过度执行
outpost n. 前哨,前哨部队,前哨地点
outpour vt.vi. (使)注出,(使)流出
outpouring n.泻出；感情的流露
output n.产量；输出量；输出
outrage n. 残暴、暴行
outrageous adj. 粗暴的，无礼的
outright a. 彻底的
outrun vt. 超过,逃脱
outset n.开始，开端
outside n.外部；外表a.外部的
outsider n.门外汉,局外人
outskirt n. (常用复数)郊区；外边
outskirts n. 郊区，郊外
outspoken a.直言的，坦率的
outspread vt.vi. 扩张,展开,伸展
outstand vt. 末偿的； 容忍；超过限度
outstanding a.突出的，杰出的
outstretched a. 伸开的,扩张的,延伸的
outstrip v. 超过，跑过
outturn n. 卸货情况
outward adv.向外
outwards ad. 向外；往海外
outweigh vt. 超过
outwit v. 以机智胜过
oval a.卵形的 n.卵形
ovary n. (植)子房；(解)卵巢
ovation n. 热烈的欢迎，鼓掌
oven n.炉，灶；烘箱
over adv.结束，完了
overact v. 把(角色)表演得过火
overall n.工装裤 a.全面的
overalls n. (美)工装裤；工作裤
overarch vt. 在...上做拱
overawe vt. 威慑
overbalance vt. 过重,价值超过,使失去均衡
overbear vt. 威压,压服,压抑
overbearing adj. 专横的，独断的
overboard ad. 自船上落下,在船外
overburden vt. 使负担过重
overcame overcome的过去式
overcast a. 阴天的,阴暗的,愁闷的
overcharge vt.vi. 讨价过高,装药过多,过度充电
overcoat n.大衣
overcome vt.战胜，克服
overcrowd vi. 过度拥挤
overcrowded a. 过度拥挤的
overcrowding a. 人口过密的
overdo v. 做理过头，过火
overdose n. (药物)过度剂量
overdraft 透支，汇款过额；透支额
overdraught 透支，透支额
overdraw vt. 透支
overdrawing 透支，超支
overdue a. 过期的,未兑的,迟到的
overeat vt. (使)吃过量
overestimate vt.过高估计
overewhelming adj.压倒一切的
over-excited adj. 过于激动
overexposure n. 过度暴露
overextend v. 使…承担过多的义务
overflow vt.从…中溢出
overfulfill vt. 超额完成
overgrow vt. 在…上长满；丛生；vi. 生长过旺；长得太快
overgrown a. 发育过度的,生长过大的,不合身的
overhand a. 投下的,举手过肩而投掷的
overhang vt.悬于…之上vi.悬垂
overhaul n./v. 彻底检查，大修
overhead adv.在头上；在空中
overhear vt.偶然听到；偷听
overheat v.加热过度
overheating 市场狂热，景气过度
overjoy vt. 使大喜
overjoyed adj. 非常高兴
overland a. 陆路的,经过陆地的,陆上的
overlap vt.与…交搭 vi.重迭
overlapping adj. 相互重叠的
overlay n. 覆盖,覆盖图
overleap vt. 跳过,看漏,省略
overload vt.使超载
overlook vt.眺望；看漏；宽容
overmuch a. 过多的,过度的
overnight ad.一夜；突然
overpass n. 天桥,陆桥
overpay 付得过多
overpayment n. 多付的款项
overplus n. 剩余,过剩
overpopulation n. 人口过剩
overpower vt. 击败,打胜,克服
overprice 标价过高
overproduction n.生产过剩，过量生产
over-punctual n. 过分早到的人
overrall a.包括一切的，全部的 n.罩衫，工装裤
overrate vt. 评价过高,高估,估价过高
overreach v. 做事过头
override v. 不理会，推翻
overriding adj. 最主要的
overrule v. （高位的人）不准，否决（低位的人或事）
overrun n. 超越误差
oversea a. 海外的,国外的
overseas adv. & adj. 海外(的) ；到国外(的)，到海外(去的)
oversee vt. 向下看,了望,监督
overseer n. 监督,工头
oversell 售出过多，卖空
overset vt. 打翻,推翻,使失败
overshadow v. 遮蔽，使显得不重要
overshoe ]套鞋
overshoot vt. 打过头,越过
oversight n. 忽略；失察
oversleep 睡过(某一时刻)
overstep vt. 踏过,逾越,超出...的限度
overstore 商品过剩
overstrain vt. 伸张过度,使过度紧张,使工作过度
overstrike n. 过打印
overt adj. 公然的；明显的；公开的；非秘密的
overtake vt.追上，赶上；压倒
overtax vt. 课税过重,使负担过度
overthrew voerthrow的过去式
overthrow vt.推翻 n.推翻，瓦解
overthrown overthrow的过去分词
overtime a.超时的，加班的
overtone n. 泛音,暗示,折光的色彩
overtook overtake的过去式
overtop vt. 高耸...之上,凌驾,超出
overture n. 前奏曲、序曲
overturn n. 倾覆,破灭,革命
overvalue 过高估价
overvalued n.定价过高
overview n. 综述，概要
overwatch vt. 看守,掩护射击
overweening adj. 自负的，过于自信的
overweight n. 超过重量,过重,优势
overwhelm vt.压倒，使不知所措
overwhelming adj. 压倒的；势不可挡的；绝大多数的；巨大的
overwhelmingly ad. 以压倒之势地
overwork n. 过度操劳,过度工作
overwrite v. 重写
overwrought adj. 紧张过度的，兴奋过度的
over-zealously ad. 过了头地
ovum n. 卵,卵子,卵形装饰
ow int. 喔唷
owe  vi. & vt. 欠(债等)；感激；欠应该支付…；应该把…归功于
owing a. 未付的,亏欠的,归因于...的
owl n. 猫头鹰；枭
owlet n. 猫头鹰之子,一种小型猫头鹰
own vt.所有；拥有
owner n.物主，所有人
ownership n.所有(权)，所有制
ox n. 牛；公牛，阉牛
Oxford n.牛津(英国城市)
oxfordshire n. 牛津郡(英国)
oxhide n. 牛皮
oxidation n. 氧化
oxide n.氧化物
oxidize vt.氧化，使生锈
oxygen n.氧，氧气
oxygen-laden n. 带氧的；携氧的
oyster n.牡蛎；沉默寡言的人
p.e. n. 体育
p.m. n.午后；(缩)下午
p.s. (信末的)附言，再者
pa n. (口)爸；爸爸
pabulum n. 食物，精神食粮
pace n.(一)步(距离)；步速
pacemaker n. 起搏点
pachyderm n. 厚皮动物，厚脸皮的人
pacific adj.太平洋的n.太平洋
pacifier n. 调停者，和解人
pacifist n. 和平主义者,反战论者,不抵抗主义者
pacify vt. 使平静,安慰,绥靖
pack vt.捆扎；挤满 n.包
package n.包裹；包装
packaging n. 包装；打包
packed adj. 塞满的；满座的；挤得满满的；充满人的，拥挤的
packer n.包装者; 打包商
packet n.小包(裹)，小捆
packing n. 装箱，收拾行李；打包，包装物
packing-case n. 包装箱
packman 小贩，行商
pact n.协定；合同；公(条)约；契约；盟约
paction 契约，合同，协议书
pad n.垫；本子 vt.填塞
paddle n.桨形工具
paddock n. 围场
padlock n. 挂锁,关闭,禁止进入
padre n. 神仆,牧师,随军牧师
paean n. 赞美歌，颂歌
pagan n. 没有宗教信仰的人，异教徒
paganism n. 异教（信仰）
page n.页，页码
pageant n. 壮观的游行，露天历史剧
pageantry n. 壮观,华丽
paging 寻呼
pagoda n. 宝塔
paid pay的过去式(分词)；付讫；受雇的；付款
paid-in 已缴，缴入
paid-in-advance 提前付款，预付
paid-in-investment 实投资本
paid-up 付足，付讫
pail n.桶，提桶
pain n.疼；疼痛
painful a.使痛的；费力的
painfully adv. 痛苦地；费力地
painkiller n. 止痛药
pain-killer n. 止痛药
painless a. 无痛的,不痛的
painlessly ad. 毫无痛苦地
pains n.辛苦
painstaking a. 刻苦的
paint vt.漆，画 n.油漆
painter n.漆工，画家，绘画者
painting n.油画；绘画；着色
pair n.一对 vi.成对，配对
pajamas n. 睡衣,宽长裤
pakistan n. 巴基斯坦
pal n.好朋友；同谋
palace n.宫，宫殿
palaeontological a. 古生物学的
palatable adj. 美味的，愉快的
palate n. 上腭，口味，爱好
palatial adj. 宫殿般的，宏伟的
palatine a. 巴拉汀伯爵的,在领地内行使王权的,
palaver n./v. 空谈，奉承
pale a.苍白的；浅的
paleface n. 白人
paleness n. 变青,苍白,淡薄
paleography n. 古文字学
paleolithic adj. 旧石器时代的
Palestine n. 巴勒斯坦
palestinian n. 巴勒斯坦人
palette n. 调色板
palfrey n. 骑用的马,妇女骑用的小马
palimpsest n. 重写本
palings n. 篱笆，木栅栏
palisade n. 篱笆，栅栏
pall n. 棺罩,遮盖物
Palladian a.帕拉第奥的(古典主义建筑风格的)
palladium n. 钯
pallet n. 草铺,简陋的小床,调色板,棘爪
palletize 用托盘装运
palliate v. 减轻（痛苦），掩饰（罪行）
palliation n. 减轻，缓和
palliative a. 缓和的,减轻的,掩饰的
pallid adj. 苍白的，没血色的
pallor n. 苍白
palm n.手掌，手心；掌状物
palmary 最重要的，杰出的
palmer n. 朝圣者,游方僧,毛虫
palmetto n. 棕榈科之一种
palm-tree n. 棕榈树
palmy a. 棕榈的,多棕榈的,繁荣的
palpable adj. 明显的，易觉察的
palpation n. 触诊，扪诊
palpitate v. （心脏）急速而不规则地跳动
palpitation n. 悸动,跳动,心跳
palsy n. 中风,麻痹,麻痹状态
palter vi. 含糊其词,马虎处理,讨价还价,
paltry adj. 无价值的，微不足道的
paly n. 消遣
pampas n. 彭巴斯草原
pamper v. 纵容，过分关怀
pamphlet n.小册子
pamphleteer n. 小册子作者,檄文执笔者
pan n.平底锅，盘子
panacea n. 万灵药
Panama n. 巴拿马
pancake n. 薄烤饼
pancreas n. 胰脏
pancreatic a. 胰腺的
panda n.小猫熊；猫熊
pandemic adj. (病)大范围流行的
pandemonium n. 喧嚣，大混乱
pander v. 迎合
pandora n. (希神)潘朵拉
pane n.窗格玻璃
panegyric n. 颂词，颂扬
panel n.专门小组；面，板
paneling n. (集合词)镶木
panelist n.专门小组成员
pang n. 剧痛,悲痛,苦闷
panic n.恐慌，惊慌
panoply n. 全副穿戴，全副甲胄
panorama n. 全景，概观
panoramic adj. 全景的
pansy n. 三色紫罗兰
pant vi.,vt.&n.喘气
pantaloon n. 老旦,老丑角,裤子
pantheon n. 万神殿，众神
panther n.豹，黑豹；美洲狮
pantomime n. 哑剧
pantry n.食品柜，餐具室
pants n.裤子；男用短衬裤
pap n. 奶头,软食,半流质食物
papa n. 爸爸
papacy n. 罗马教皇职位,教皇权,教皇
papal a. 罗马教皇的,教皇制度的
paper vt.用纸包装(或覆盖)
paper-cut n. 剪纸，刻纸
papercutting n. 剪纸艺术
papers n. 文件，证书
papist n. 教皇制信奉者,天主教徒
papoose n. 幼儿，背婴儿的袋子
paprika n. 红椒之一种,其种子,红椒色
papule n. 丘疹；小突起
papyrus n. 莎草，沙草纸
par n. 同等，平均量
parable n. 寓言，比喻
parabola n. 抛物线
parachute n.降落伞；风散种子
parade n.游行；检阅 vi.游行
paradigm n. 范例，示范
paradigmatic adj. 作为示范的，典范的
paradise n.伊甸乐园；天堂
paradox n. 矛盾、似矛盾而正确的说法
paradoxical a. 似非而是的,矛盾的,诡论的
paraffin n. 石蜡
paragon n. 模范，典型
paragraph n.(文章的)段，节
parakeet n. 鹦鹉
parallax n. 视差
parallel a.平行的；相同的
parallelism n. 平行,对应,类似
parallelogram n. 平行四边形
paralyse vt.使麻痹，使瘫痪
paralysis n. 瘫痪，中风
paralytic a. 麻痹的,患麻痹的,中风的
paralyze v. 使瘫痪，使无效
parameter n. 参(变)数；参量；参变量
paramount adj. 最重要的，最高权力的
paramour n. 奸夫(妇)；情夫
paranoia n. 偏执狂，多疑症
paranoiac a. 偏执狂的
paranoid adj. 偏执狂的，过份怀疑的
parapet n. 栏杆,扶手,胸墙
paraphernalia n. 随身用具
paraphrase vt. 释义
parasite n. 寄生虫，食客
parasitic adj. 寄生的
parasol n. （女用）阳伞
parcel n.包裹
parch v. 烘烤，干热
parchment n. 羊皮纸，羊皮纸手稿
pard n. 豹,伙伴
pardon n.原谅；赦免 vt.原谅
pardonable a. 可原谅的,难怪的
pardoner n. 宽恕者
pare v. 削皮，修剪，削减
paregoric a. 止痛的
parent n.父(母)亲
parentage n. 亲子关系,出身,血统
parental a. 亲本的
parenthesis n. 插入语，括弧
parents n. 父母，双亲；父母亲
pariah n. 贱民，被社会遗弃者
paris n. 巴黎(法国首都)
parish n. 教区
parishioner  (C) 教区的居民
parisian n. & a. 巴黎人(的)
parity n. 同等,同格,同位,平价
park n.公园
parking n. 停放车辆
parlance n. 说法,语法,语调
parley n./v. 和谈，会谈.
parliament n.议会，国会
parliamentary a. 国会的,议会的,议会制度的
parlimental adj. 国会的，议会的
parlor n. 客厅
parlour n. 客厅,会客室,特别室
parlous adj. 靠不住的，危险的
parochial adj. 教区的，思想狭隘的
parody n. 嘲弄文章，拙劣的模仿
parole n. 誓言,释放宣言,语言
paroxysm n. 突发，阵发
parquet n. 镶木，地板
parquetry n. 镶木地板艺术或图案
parricide n. 杀尊亲,杀长辈,杀主人
parrot n.鹦鹉
parry v. 挡开，避开（武器，问题等）
parse vt. (语法)分析
Parsee  n. 亦作 Parsi. 祆教徒;  (印度之) 拜火
parsimonious adj. 太节省的，小气的
parsimoniously ad.过工节俭地；吝啬小气地
parsimony n. 过度节俭,吝啬
parsley n. 欧芹
parsnip n. 欧洲防风草
parson n. 教区牧师
parsonage n. 牧师住宅
part n.一部分；零件；本份
partake vt. 分担,分享
partaker n. 关系者,共享的人,分担者
parterre n.有花圃的草坪
partial a.部分的；不公平的
partiality n. 偏袒，偏心
partially ad.部分地
participant n.参加者 a.有份的
participate vi.参与，参加；分享
participation n. 参与
participator n. 参加者；a. 参加的
participle n. 分词
particle n.粒子，微粒
particular a.特殊的；特定的
particularity n. 特殊性,特质,细目
particularize vt.vi. 详细说明,列举,大书特书
particularly ad.特别，尤其，格外
particulars  n. 单独事项，详细说明；特点；事实，细节
parting n. 分别,分歧处
partisan n.游击队员
partition n.分开，分割；融墙
partly ad.部分地，不完全地
partner n.伙伴；搭挡；配偶
partnership n. 合伙,合股
partridge n. 鹧鸪
part-time adj. 兼职的；计时(干活)的；部分时间的
parturition n. 生产；分娩
party n.聚会
parvenu n. 暴发户，新贵
pasha n. 巴夏
pass v.传递(用具等)
passable a. 可通行的,可渡过的,尚可的
passage n.通过；通路，通道
passageway  n. 走廊; 通路
passbook n.存折；顾客赊欠账簿
passe  adj. 老式的,落伍的; 过时的,已过盛年
passenger n.乘客；旅客
passer n. 过路人,旅客,考试合格者
passerby n.过路人
passer-by n. 过客
passion n.激情，热情；爱好
passionate a. 热情的,热烈的,易怒的
passionately ad. 激越地；多情地；热烈地
passive a.被动的；消极的
Passover n. 逾越节,逾越节祭神的羔羊
passport n.达到目的的手段
password n. 密码,口令
past prep.过；经过
pasta n.意大利面制品，意大利面食
past-due adj. 过期的
paste n.糊，酱；浆湖
pastel n. 彩色粉笔画，柔和的色彩
pastern n. 胶
pasteurization n. 巴氏消毒法
pasteurize v. 以高热杀菌，消毒
pastiche n. （音乐等）混合作品
pastime n.消遣，娱乐
pastor n. (基)牧师；牧(羊)人
pastoral adj. 田园生活的，宁静的
pastry n. 糕点，点心
pasturage n. 畜牧,牧场,牧草
pasture n.牧场；牲畜饲养
pasty adj. 浆糊的，苍白的
pat vt.&vi.轻拍；抚摩
patch n.补钉；小块土地
patchwork n. 拼缝物
pate n. 头,脑袋,头脑
patent a.专利的 n.专利
patentee n. 专利权所有人
paternal a. 父亲的
paternity n. 父道,父权,父子关系
path n.路，小道；道路
pathetic a.哀婉动人的；可怜的
pathless a. 无路的,绝迹的,人迹未到的
pathogen n. 病原体
pathogenic a. 致病的
pathologic a. 病理的
pathological adj. 病理学 (上) 的; 病理 (上) 的
pathology n. 病理学
pathophysiology n. 病理生理学
pathos n. 哀婉，悲怆
pathway n. 路,径
pathy (构词成分)感情；痛苦，疾病；疗法
patience n.忍耐，容忍，耐心
patient a.忍耐的 n.病人
patiently ad. 有耐心地；坚韧地
patina n. 绿锈，光亮的外表
patio n. 庭院，平台
patois n. 方言,行话
patriarch n. 家长；族长
patriarchal a. 族长的；家长的
patriarchy n. 家长，父系社会
patrician n. 贵族
patricide n. 弑父
patrimonial a. 祖传的
patrimony n. 祖传的财物
patriot n.爱国者，爱国主义者
patriotic a.爱国的
patriotism n. 爱国主义，爱国心
patrol n.巡逻 n.巡逻，巡查
patron n.庇护人；赞助人
patronage n. 赞助，惠顾
patroness n. 女性保护人
patronize vt. 保护,支援,惠顾,庇护,赞助
patter n. 急速拍打声,轻快脚步声,饶舌,
pattern n.型，式样，模，模型
pattis 帕蒂思(姓)
patty n. Mathilda,Matilda,Martha 的昵称,
paucity n. 小量，缺乏
paul 保罗(男名)；(男名)保罗
paula 波拉(女名)
paunch n. 腹,胃,大肚子
pauper n. 贫民，乞丐
pauperism n.(须接受救济的) 贫穷状态
pause vi.&n.中止；暂停
pave vt.铺，筑(路等)
pavement n.(英)人行道
pavilion n.亭子
paving n. 铺砌；铺面
paw n.脚爪
pawn n./v. 典当，抵押，n. 小人物，走卒
pawnbroker n. 典当商，当铺老板
paw-paw n. 番木瓜
pay vt.给...报酬 n.工资
payable a. 可付的,应付的,有利益的
paycheck n.付薪金用的支票
payee 受款人，取款人，收款人
payer 付款人，付款单位
paying 付款，支付，有收益
payment n.支付，支付的款项
payroll 工资
pay-roll n. 薪金名册
pe n. 体育
pea n.豌豆；豌豆属植物
peace n.和平
peaceable a. 温顺的,温和的,和平的
peaceful a.和平的；安静的
peacefully ad. 平静地；安宁地
peace-loving a. 爱好和平的
peacemaker n. 调解者,和事佬
peach n.桃子，桃树
peacock n.孔雀
peak n.山顶，巅 a.最高的
peaky adj. 憔悴的
peal n. 隆隆声,编钟响亮的钟声
peanut n. 花生,极小的数额
pear n.梨
pearl n.珍珠；珍珠母
pearly a. 珠色的；珍珠似的
peasant n.农民
peasantry n. 农民,小农阶级
peasants 农民(复数)
peat n. 泥煤,放浪的女子
pebble n.卵石，细砾
pebbly a. 多砾石的
pecan n. 美洲山核桃树
peccadillo n. 小过失
peck vt.&vi.啄，啄起
pectoral adj. 胸部的，胸的
peculate v. 挪用（公款）
peculation  n. 盗用
peculiar a.特有的；特别的
peculiarity n.特性，独特性；怪癖
peculiarly ad. 特有地；古怪地
pecuniary adj. 金钱上的，金钱的（
pedagogic a.教学法
pedagogue n. 教师,教育者,爱假装博学者
pedagogy n. 教育学，教学法
pedal n.踏脚，踏板，脚蹬
pedant n. 迂腐之人，书呆子
pedantic a. 卖弄学问的,炫学者,假装学者的
pedantry n. 迂腐
peddle vi. 挑卖,沿街叫卖
peddler n. 小贩,传播者
pedestal n. （柱石或雕像的）基座
pedestrian n.行人，步行者
pediatric a. 儿科的
pediatrician n. 小儿科医师
pediatrics n. 儿科学；小儿科
pedigree n. 家谱，纯种系谱
pediment n. 山形墙,三角墙
pedlar n.(挨户兜售的)小贩
pedler n. 小贩；(谣言)传播者
peek v. 偷看
peel vt.剥(皮)，削(皮)
peep vi.(从缝隙中)偷看
peeper n. 窥视者；嘀咕的人
peer vi.凝视；隐约出现
peerage n. 贵族,贵族阶级,贵族地位
peeress n. 贵族夫人,有爵位的妇女
peerless a. 无比的,出类的,无双的
peevish adj. 坏脾气的，易怒的
peevishly adv. 暴躁地
peg n. 钉,藉口,销子,借口
pejorative adj. 带有轻蔑意义的，贬低的
peking n. 北京(市) (beijing)
pelf n. 财富，钱
pelican n. 鹈鹕鸟
pelisse n.妇女之长外衣
pell n. 一卷羊皮纸
pellet n. 圆球,小子弹,小药丸
pell-mell adv. 混乱地，匆促地
pellucid adj. 清晰的，清澈的
pelt n. 毛皮. v. 投掷，（雨）猛降
pelvic a. 骨盆的
pelvis n. 骨盆
pen n.钢笔
penal a. 刑罚场所的
penalize v. 置（某人）于不利地位，处罚
penalty n.处罚，刑罚；罚款
penance n. 自我惩罚
pence n. 便士(英货币)；penny的复数
penchant n. 爱好，嗜好
pencil n.铅笔
pencil-box n. 铅笔盒
pencilled adj. 用铅笔写的
pendant n. 垂饰,下垂物
pendent adj. 吊着的，悬挂的
pending adj. 即将发生的，未决的
pendulous adj. 悬挂而摇摆不定的
pendulum n.(钟等的)摆
penetrable a. 穿透的,可渗透的,使感动的
penetrate vt.穿过 vi.穿入
penetrating adj. 敏锐的，尖锐的
penetration n.穿入；渗透，侵入
penetrative a. 渗透的,有渗透力的,彻骨的
penfriend n. 笔友
penguin 企鹅
pen-holder n. 笔杆
penicillin n. 青霉素，盘尼西林
penicillium n. 特异青霉，(拉)青霉素
peninsula n.半岛
peninsular n. 半岛
penitence n. 后悔,忏悔,改过
penitent adj. 后悔的，忏悔的
penitential a. 后悔的,忏悔的,赎罪的
penitentiary n. 监狱，感化院
penknife n. 小刀
penmanship n. 书法,笔法,笔迹
pennant n. （船上用的）信号旗
pennate a. 有翼的
penniless a. 赤贫的,贫穷的
pennon n. 细长三角旗,小燕尾旗,枪旗
penny n.便士(英国辅币单位)
pennyworth n. 仅值一便士的东西
pens n. 钢笔(复数)
pension n.抚恤金，年金
pensioner n.年金受领者; 靠抚恤金生活的人
pensive adj. 沉思的，愁眉苦脸的
pent adj. 被监禁的
pentagon n. 五边形
Pentateuch n. 摩西五书
Pentecost n.『犹太教』五旬节
penthouse n. 搭连正房的屋顶,耳房,屋檐
pent-up a. 被抑制的
penultimate adj. 倒数第二的
penumbra n. 半明半暗之处，边缘部分
penurious adj. 贫困的，缺乏的
penury n. 贫穷
pen-wiper n. 抹笔布
peony n. 牡丹,芍药
people n.人民，民族；人
pepper n.胡椒，胡椒粉
peppercorn n. (晒干的) 胡椒子
peppermint n.『植物』辣薄荷
peppery adj. 胡椒味的，暴躁的
pepsin n. 胃蛋白酶
peptic adj.消化性的；消化液的；产生胃酶的，助消化的
peptide n. 肽
per prep.每，一
peradventure ad. 或者,偶然,不料
perambulate v. 巡行，巡视，漫步
perambulator n. 摇篮车,勘查者,路程计
perceive vt.察觉，发觉；理解
percent n.百分之…
percentage n.百分比，百分率
perceptible adj. 可以感觉到的，可见的
perception n.感觉；概念；理解力
perceptive n. 问题不同方面之关系；adj. 感觉敏锐的
perch n.(禽鸟的)栖木
perchance ad. 偶然,恐怕
percipient adj. 洞察力强的
percolate v. 过滤出，渗透
percolator n.过滤器
percussion n. 撞击，敲击
percussionist n. 敲击乐器，乐师
perdition n. 灭亡,破灭,贬落地狱
peregrination n. 游历（尤指在国外）
peremptory adj. 专横的，不容反抗的
perennial adj. 终年的，永久的
perennially 永久地
perfect adj.极好的，完美的
perfection n.尽善尽美；无比精确
perfectionist n. 力求完美者，吹毛求疵者
perfectly adv. 极好地，完美地；十分地；很，完全
perfidious adj. 不忠的，背信弃义的
perfidy n. 不忠，背叛
perforate v. 打洞
perforation n. 穿孔,贯穿,贯通
perforce ad. 必然地
perform vt.履行;表演 vi.行动
performance n.履行；演出；行为
performer n. 表演者
perfume n.香味，芳香；香料
perfumed a. 有香味的
perfumery n. 香料类,香水,香料制造
perfunctory adj. 草率的，敷衍的
perhaps adv.也许，可能
perigee n. 近地点
peril n.危机；危险的事物
perilous adj. 危险的，冒险的
perimeter n.周(边)，周长
period n.时期；学时；句号
periodic n.周期的；一定时期的
periodical n.期刊，杂志
periodically ad. 周期性地，定期地
peripatetic adj. 巡游的
peripheral adj. 边缘的，周边的；不重要的，外围的；末梢的
periphery n. 外围，不重要的部份
periphrastic adj. 迂回的，冗赘的
periscope n.潜望镜
perish vi.死亡，夭折；枯萎
perishable adj. （食物）易坏的
perishing adj. 严寒的
peristyle n. 绕柱式,列柱走廊,以柱围绕的内院
peritoneum n. 腹膜
peritonitis n. 腹膜炎
periwig n. 假发
periwinkle n. 长春花属的植物,玉黍螺
perjure v. 作伪证，发假誓
perjury n. 伪证，假誓
perk vi. 昂首,振作,渗透
perky adj. 活泼的，大胆的
perm n.电烫
permanence n. 永久,持久
permanent a.永久的，持久的
permanently adv. 永久地；持久地
permanganate n. 过锰酸盐
permeability n.弥漫；渗
permeable adj. 可渗透的
permeate v. 扩散，渗透
permeation n. 渗透，弥漫，充盈
permissible a. 可允许的,可容许程度的
permission n.允许，许可，同意
permissive adj. 过份纵容的
permit vt.允许 n.执照
permutation n. (数学中)排列变化，彻底改变
pernicious adj. 有害的，致命的
peroration n. 结尾，结论
peroxide n. 『化学』过氧化物
perpendicular a.垂直的 n.垂直(线)
perpetrate v. 犯罪，作坏事
perpetrator  n. 为非作歹者; 作恶者,作案者,犯人
perpetual a.永久的；四季开花的
perpetuate v. 使永存，使永
perpetuity n. 永恒，永久
perplex vt.迷惑，困惑，难住
perplexed adj. 困惑的；不知所措的；
perplexity n. 困惑，茫然
perquisite n. 固定津贴，福利
persecute vt.迫害，残害
persecution n. 迫害
persecutor n. 迫害者
perseverance n.毅力;坚持;不屈不挠
persevere vi.坚持，不屈不挠
persevering adj. 坚忍不拔的
Persia n. 波斯
persian a. 波斯的；n. 波斯人
persiflage n. 挖苦，嘲弄
persimmon n. 柿子
persist vi.持续，存留
persistence n.坚持；持续，存留
persistency n. 固执,坚持,持续
persistent adj. 固执的，坚持的
persnickety adj. 势利的，挑剔的
person n.人；人身；本人
personable adj. 英俊的，风度好的
personage n. 名人，（戏剧）角色
personal a.个人的；本人的
personalities n. 诽谤
personality n.人格，个性；人物
personally adv. 亲自，就个人而言
personate vt. 扮演,伪装,假冒,拟人化
personel a. 个人的，私人的；亲自的
personification n. 典型，完美榜样
personify vt. 看做人,赋与人性,使人格化
personnel n.全体人员，全体职员
perspective n.透视；远景；观点
perspicacious adj. 独具慧眼的
perspicacity n. 睿智，敏锐
perspicuity n. 明晰,明了,简明
perspicuous a. 明白的,明了的
perspiration n. 出汗
perspire vt.vi. 出汗,流汗
persuade vt.劝说；说服
persuasion n.劝说，说服；主张
persuasive adj. 能劝说的，善于游说的
pert adj. 活泼的，敏捷的
pertain v. 属于，关于
perth n. 珀思(澳大利亚城市)
pertinacious adj. 顽固的
pertinacity n. 执拗,顽固,顽强
pertinence n. 中肯
pertinent a.恰当的；有关的
perturb vt. 扰乱,使混乱,使心慌
perturbation n. 烦乱，扰乱
perturbed adj. 烦燥不安的
pertussis n. 百日咳
peru n. 秘鲁(南美洲)
perusal n. 熟读,精读,吟味
peruse v. 细读，精读
peruvian a. 秘鲁的；秘鲁人的
pervade v. 弥漫，普及
pervasive adj. 遍及的，弥漫的
perverse adj. 刚愎自用的，故意作对的
perversion n. 堕落，曲解
perversity n. 刚愎，背理行为
pervert v. 使堕落，滥用
pervious a. 使通过的,让过去的,可通的
pesky adj. 讨厌的，烦人的
pessimism n. 悲观,悲观主义
pessimist n. 悲观主义者
pessimistic adj. 悲观的；悲观主义的，厌世的
pest n.害虫；有害的东西
pester v. 纠缠，强求
pesticide n. 杀虫剂
pestiferous a. 传播疾病的,邪恶的
pestilence n. 瘟疫
pestilent adj. 致死的，有害的
pestilential a. 有害的；引起瘟疫的
pestle n. 杵，乳钵槌
pet n.爱畜；宠儿a.宠爱的
petal n. 花瓣
peter 彼得(男名)
petite a. 小的，次要的；娇小的
petition n.请愿 vt.向…请愿
petitioner n. 请愿人
petrel n. 海燕
petrifaction n. 石化，目瞪口呆
petrify vt. 使发呆；变为化石，使发呆；使僵化；v. 石化，吓呆
petrol vt. 加以汽油；n. (英)汽油；石油
petroleum n.石油
petrology n. 岩石学
PETS 公共英语等级考试
petticoat n. 衬裙,裙子
pettifogging a. 琐碎的；诡计多端的
pettish adj. 易怒的，使性子的
petty a.细小的；器量小的
petulance n.发脾气,生气,易怒,暴躁,性急
petulant adj. 性急的，暴躁的
petunia n.『植物』矮牵牛属
pew n. 长凳,座位
pewter n.白鞽(锡与铅或其他金属之合金)
phaeton n.一种双座二马四轮马车
phagocyte n. (吞)噬细胞
phagocytosis n. 噬菌作用；吞噬作用
phalanx n. 方阵,密集队,指骨,趾骨
phantasm n. 幻像,幻影,幽灵
phantasmal adj. 幻影的，幽灵一样的
phantom n. 鬼怪，幽灵，幻象
Pharaoh n. 法老王
pharisaic adj. 伪善的，伪装虔诚的
pharisaical adj.拘泥形式的,假装虔诚的,伪善的
Pharisee n. 法利赛人,法利赛教派之教徒
pharmaceutical adj. 制药的；药物的，药学的
pharmacist n. 药剂师
pharmacologist n. 药物学家
pharmacology n. 药理学，药物学
pharmacopoeia n. 药典
pharmacy n. 药房,配药学
pharyngitis n. 咽炎
pharynx n. 咽
phase n.阶段；方面；相位
pheasant n. 雉,野鸡
phenomena n. 现象(单数)；phenomenon的复数
phenomenal a. 现象的,能知觉的,异常的
phenomenon n.现象
phial n. 小瓶（药水瓶）
philander v. 调戏追逐女人
philanthropic a. 博爱的
philanthropist n. 慈善家
philanthropy n. 博爱,仁慈,慈善
philatelist n. 集邮家
philately n. 集邮
philippines n. 菲律宾(亚洲)
philistine n. 庸俗的人；腓力斯人；a. 市侩的
philology n. 语文学，语言学
philosopher n.哲学家
philosophical a. 哲学的,冷静的,哲学上的
philosophize vi. 进行哲学探讨
philosophy n.哲学；哲理；人生观
phlegm n. 痰,粘液,冷淡,迟钝
phlegmatic adj. 冷静的，冷淡的
phobia n. 恐惧症
phoebe n. (希神)月亮女神
phoebus n. (希神)太阳神
phoenix n. 凤凰
phone n. & vt. & vi. 电话机；打电话
phoneme n. 音素
phonetic a. 语言的,语言上的,表示语音的
phonetics n. 语音学；语言学
phonograph n. 留声机,电唱机,
phony adj. 假的，伪造的
phosphate n.『化学』磷酸盐
phosphorescent a. 发出磷光的,磷光性的
phosphoric  adj. 『化学』 (五价) 磷的,含有磷的
phosphorus n. 磷；a. 磷的，含磷的
photo n.相片
photocell n. 光电池，光电管
photochemical n. 光催化学物
photocopy n. & v. 影印，照像复印
photoelectric a. 光电的
photograph n.照片，相片
photographer n. (报纸、杂志等之) 摄影者,摄影家
photographer's 照相馆
photographic a.摄影的，摄影用的
photography n.摄影术
photos 相片
photostatic adj. 静电复印的
photosynthesis n. 光合作用
photosysthesis 光合作用
phrase n.短语；习惯用语
phrase-book n. 成语录，短语录
phraseology n. 措辞,语法,语词
phunge 盲目投资
physic n. 药品
physical adj.物理的
physically adv. 物质上，身体上；按照自然规律；a. 物理上，实际上
physician n.医生，内科医生
physicist n.物理学家
physics n.物理学
physiognomy n. 相面术，面貌
physiologic a.生理学
physiological a. 生理学的,生理学上的
physiologist n. 生理学者
physiology n. 生理学
physiotherapy n. 物理疗法(理疗)
physique n. 体格，地形
pianist n.钢琴家
piano n.钢琴
pianoforte  n. 钢琴
pianos 钢琴
piazza n. 阳台，广场，市场
picaresque a. 以歹徒为题材的
picasso 毕加索(西班牙画家)
pick n.镐，鹤嘴锄
pick...up 接(乘客)
pickaninny n. 黑人的小孩,小孩子
pickax n. 鹤嘴锄
picker n. 啄者,啄物,采摘者
pickerel n. 小梭鱼,梭鱼子
picket n. 支柱，哨兵
pickle n.腌制食品，泡菜
pickpocket n. 扒手
pickup n. 拾起，收集；获得
picnic n.郊游，野餐 vi.野餐
picnicker n.野餐者
picot n. 花边上饰边的小环
pictograph n. 象形字
pictorial a. 绘画的,插图的,用图画表示的
picture n.图画，照片
picture-book n. 图画书
picturesque a. 生动的,如画的,独特的
pie n.(西点)馅饼
piebald a. 花斑的
piece n.(文艺作品的)篇，首
piecemeal ad. 一件一件,一片
piecework n. 计件工作
pied adj. 杂色的
pier n.(桥)墩；码头
pierce vt.剌穿 vi.穿入
piercing adj. 刺骨的，敏锐的；刺(贯)穿的；尖刻的
pierre 皮埃尔(男名)
piety n. 虔诚
pig n.猪
pigeon n.鸽子
pigeonhole n. 鸽棚,出入孔,分类架
piggy n. 小猪
pigment n. 天然色素，干粉颜料
pigsty n. 猪圈
pigtail n. 辫子(口语用)
pike n. 矛,梭子鱼,通行费
pilaster n. 壁柱
pile vt.堆积，堆起
pilfer v. 偷窃
pilferage v. 偷窃
pilgrim n.香客，朝圣者
pilgrimage n. 朝圣之旅
pill n.药丸，丸剂
pillage n./v. 抢劫，掠夺
pillar n.柱，柱子；栋梁
pillory n. 颈手枷，示众，嘲弄
pillow n.枕头
pilot n.领航员；飞行员
pilotage 领航费，领港费
pimento n.多香果
pimp n. 皮条客
pimpernel n. 紫繁篓
pimple n. 丘疹,面泡,疙瘩
pin n.针，饰针 n.别住
pinafore n. 围巾,围裙,围涎
pincers n. 钳子，镊子
pinch vt.捏，拧，掐掉
pine n.松树，松木
pineapple n.凤梨，波萝
pinfold n. 家畜栏,监禁地
pingpong n. 乒乓球
pinhole n. 针孔,小孔
pinion v. 绑住，束缚
pink n.粉红色 a.粉红色的
pinnace n. 装载于舰上的中型艇
pinnacle n. 尖塔，山峰
pinnate  adj. 『植物』<叶子>羽状的
pinpoint vt. 精确地找到
pint n.品脱
pioneer n.先锋
pioneering n. 先驱的；v.倡导
pious a.虔诚的；虔奉宗教的
pip n. 果仁,种子,报时信号,忧郁
pipe n.管子，导管，输送管
pipeline n. 输油管；管道，管线；商品供应线，流水线
piper n. 吹笛者,风笛手
pippin n. 苹果之一种,优秀的东西
piquancy n. 辛辣,辣味,痛快
piquant adj. 辛辣的，开胃的
pique n./v. （因自尊心受伤害而导致的)不悦、愤怒
piracy n. 非法翻印，海盗行为
pirate n.海盗；每盗船
piratical adj. 海盗 (似) 的,海盗行为的
pirating 掠夺，招徕
pirouette n. & v.(舞蹈)脚尖立地的旋转
pisa n. 比萨(意大利中部城市)
piscatorial adj. 捕鱼的，渔民的
pistil n. 雌蕊
pistillate a. 有雌蕊的,只有雌蕊的
pistol n.手枪
piston n.活塞
pit n.坑
pitch n.沥青
pitcher n. 有柄水罐
pitchfork  (C)  (叉干草用的) 长柄叉, (耙肥料的)
pitchy a. 粘的,涂沥青的,漆黑的
piteous a. 哀怨的,可怜的
piteously ad. 可怜地；凄惨地
pitfall n. 陷阱，未料到的危险或困难
pith n. 精髓，要点
pithy adj. (讲话或文章)简练的
pitiable adj. 可怜的,令人同情的,悲惨的
pitiful a. 慈悲的,可怜的,同情的
pitiless a. 无情的,冷酷的,无怜悯心的
pittance n. 微薄的收入，少量
pittsburgh n. 匹兹堡(美国一城市)
pituitary n. 脑垂体
pity n.怜悯；遗憾 vt.同情
pivot n. 枢轴，中心v.旋转
pixy n. 妖精,小鬼
pizza n.意大利肉饼，比萨饼
pla 中国人民解放军
placable a. 易抚慰的；温厚的
placard n. 公告,布告,海报
placate v. 抚慰，平息(愤怒)
place n.地方，地点；住所
placebo n. 安慰剂
placement n. 布局；放置；布置；安排，安插
placenta n. 胎盘
placid adj. 安静的，平和的
plagiarism n. 剽窃，抄袭
plagiarize vt.剽窃，抄袭（别人学说、著作）
plague n.瘟疫，鼠疫；天灾
plaid n. 格子花呢披肩,格子花呢
plain n.平原 a.清楚的
plainly ad. 平坦地；简单地
plainness n. 平坦,明白,正直
plaint n. 悲叹,感叹,诉苦
plaintiff n. 原告
plaintive adj. 可怜的，伤心的
plait n./v. 发辫，编成辫
plan n.&vt.计划，打算
plane n.平面；飞机
planet n.行星
planetarium n. 行星仪,天文
planetary a. 行星的
plangent adj. 如泣如诉的，悲哀的
plank n.木板；厚板
plankton n. 浮游生物
planning 规划
plant n.植物；工厂 vt.栽种
plantain n. 车前草,香蕉之一种
plantation n.种植园；栽植
planter n. 种植者,耕作者,殖民者
plash n. 积水坑
plasma n.『生理』血浆,淋巴液
plasmodium n. 疟原虫
plaster n.灰泥；硬膏；熟石膏
plastered adj. 抹上灰泥的
plastic a.塑料的；塑性的
plasticity n. 可塑性
plastics n. 塑料；塑料制品
plat n. 小块地,地图
plate n.盘子；碟子
plateau n.高原；平稳时期
platelet n. 血小板
platform n.政纲，党纲，宣言
platinum n. 白金,铂
platitude n. 陈腔滥调
plato 柏拉图(古希腊哲学家)
Platonic adj. 纯友谊的(爱情)
platoon n. 排,一组,一群人
platter n. 大浅盘
platypus n. 鸭嘴兽
plaudit n. 拍手喝采,称赞,赞美
plausibility n. 似有道理,善装门面,善辩
plausible adj. 似乎合理的，嘴巧的
play n.戏剧，表演；玩耍
player n.比赛者，选手
playfellow n. 游伴
playful a. 爱打趣的,多趣的,嬉戏的
playground n.操场，运动场
playhouse n. 剧场,儿童之家,房屋玩具
playmate n. 玩伴,游伴
plaything n. 玩具,被玩弄的人
playwright n. 剧作家
plaza n. 广场，集市
plea n.请愿，请求，恳求
plead vt.为…辩护 vi.抗辩
pleader n. 辩论者,辩解者,答辩人
pleadings n. 恳求
pleasance n. 游园,愉快,快乐
pleasant adj.令人愉快的
pleasantly ad. 愉快地；令人愉快地；舒适地
pleasantry n. 幽默,开玩笑
please vt.使高兴，请vi.满意
pleased adj. 高兴的；欣喜的；乐意的
pleasing a. 令人喜爱的,愉快的,舒适的
pleasurable a. 快乐的,愉快的,心情舒畅的
pleasure n.愉快，快乐；乐事
pleat n. (衣服上的)褶
plebeian n./adj. 平民，平民的
plebiscite  n. 公民投票
pledge n.誓言 vt.使发誓
pledgee 接受抵押的人
pledger 抵押者，典当人
plenary a. 充分的,完全的,充实的
plenipotentiary n. 全权大使,全权委员
plenitude n. 完全，大量
plenteous a. 许多的,丰饶的,丰富的
plentiful a.丰富的，富裕的
plenty n.充足；大量
pleonastic adj. 赘语的，噜嗦的
plethora n. 过量，过剩
plethoric adj. 充血的，多血的
pleurisy n. 肋膜炎,胸膜炎
plexor n. 叩诊锤
plexus n. 丛
pliable adj. 易弯的，柔软的
pliancy n. 柔软,柔顺
pliant adj. 易受影响的，易弯的
plicate a. 折扇状的；具褶的
pliers n. 钳子
plight n. 困境
plinth n. 柱脚、底座
plod v. 重步走，吃力干
plodder n. 沉重行走的人,辛勤工作的人,
plosion n. 爆破音；(语音)爆发音
plosive a. 爆破音的
plot n.小块土地 vt.密谋
plough n.犁 vt.&vi.犁，耕
ploughman n. 农夫
ploughshare n. 犁头
plover n. 千鸟类
plow n.犁 vt.&vi.犁，耕
plowman n. 农夫
plowshare n. 犁头
ploy n. 花招，手段
pluck vt.鼓起(勇气)，振作
plucky a. 有勇气的,有胆量的,大胆的
plug vt.接上插头通电
plum n. 美差；肥缺
plumage n. 羽毛
plumb adv. 精确地，完全地v. 了解意义，测水深
plumber n. 水管工人
plume n. 羽毛v. 整理羽毛，骚首弄姿
plummet v. 垂直或突然地堕下
plump vt.丰满的；鼓起的
plumule n. （植）胚芽，（鸟）绒羽
plumy a. 有羽毛的,羽毛似的,用羽毛装饰的
plunder v.&n.掠夺，劫掠
plunderer  n. 掠夺者; 盗贼
plunge vt. 投入
plunger n. 跳进的人,潜水者,冲入物,活塞
pluperfect n. 过去完成时
plural a.复数的 n.复数
plurality n. 复数,较大数,许多,兼职
plus prep.加
plush adj. 豪华的
Pluto n. 冥王星,阴间之神
plutocracy n. 富豪，财阀统治
plutocrat n. 富豪,财阀
ply v. (搬运工等)等候顾客，弯曲
plymouth n. 普利茅斯(英国港市)
pneumatic a.空气的；气动的
pneumatics a. 气动力学；空气的，气体的，风动的，气动的
pneumonia n.肺炎
poach v. 偷猎，偷捕
poacher n. 偷猎者,侵入者
pocket n.衣袋
pocketbook n. 袖珍本；皮夹子；财力
pocket-book n. 袖珍书
pocket-money n. 零用钱
pod n. 豆荚，v. 剥掉(豆荚)
podiatrist n. 脚病医生
podiatry n. 足病科
podium n. 讲坛，指挥台
poem n.诗，韵文；诗体文
poesy n. 诗,诗歌,作诗法,诗才,韵文
poet n.诗人
poetaster n. 蹩脚诗人
poetess n. 女诗人
poetic a. 诗的
poetical adj. 用诗写的
poetry n.诗，诗歌，诗作
poignancy n. 辛酸事，尖锐
poignant adj. 伤心的，尖锐的
point n.观点；论点；要点
point-blank a. 直射的,由正面的,率直的,干脆的
pointed adj. 一针见血的；尖(锐)的；中肯的
pointer n. 一种短毛猎犬
pointless a.无意义的，无目标的
poise v. 使相等，使平衡n. 泰然自若，信心
poison vt.使中毒
poisoning 中毒
poisonous adj.有毒的；有害的
poke vt.戳，刺；伸(头等)
poker n. 拨火棍,戳的人,纸牌戏
poky adj. (地方)狭小的，不舒适的
Poland n. 波兰
polar a.南(北)极的；极性的
polarity n. 极性；极端性，二极分化；(思想，感情)归向，倾向
polarization n. 极化
polarize v.使两极
pole n.杆；柱
polemic n. 争论，论战
polemical adj. 引起论战的
police n.警察；警察当局
policeman n.警察
police-station 警察局
policewoman n. 女警察
policy n.政策，方针
polio n. ((口语))小儿麻痹症
poliomyelitis n. 脊髓灰质炎
polis n. 古希腊的城市国家
polish vt.磨光；使优美
polite a.有礼貌的；有教养的
politely adv. 有礼貌地；温和地；文雅地；客气地
politeness n. 有礼,优雅
politic a. 精明的,圆滑的,慎重的,策略的
political adj.政治的
politically ad.政治上
politician n.政治家；政客
politics n.政纲，政见，策略
polity n. 政治,政体,国体,政治组织
polka n. 波尔卡舞,女用紧身短上衣
poll n.投票 vi.投票
pollen n. 花粉
pollinate v. 给……授粉
pollination n. 授粉
pollster n. 民意测验家
pollutant n.污染物质
pollute vt.弄脏，污染，沾污
polluter n. 污染者；污染物质
pollution n.污染
polo n. 马球,水球
poltroon n. 懦夫
polyandry n. 一妻多夫制
polygamist n. 一夫多妻论者,多妻的人,一妻多夫论者
polygamy n. 一夫多妻制，多配偶制
polyglot n./adj. 通晓多种语言的(人)
polygon n. 多角形
polymath n. 知识广博者
polymer n. 聚合物，多聚物
polymetallism 多本位制
polynesian a. 波利尼西亚(群岛)的
polyp n. 水螅,鼻肉,鼻息肉
polysyllable n. 多音节字
polytechnic a. 各种工艺的,综合技术的
polytheism n. 多神教,多神论
pomegranate n. 石榴
pommel n. 柄端,鞍头,前鞍
pomp n. 盛况，不必要的炫耀
pompey n. 庞培(罗马将军)
pomposity n. 自大，傲慢
pompous adj. 自大的
poncho n. 斗篷，雨衣
pond n.池塘; 鱼塘
ponder vt.考虑 vi.沉思
ponderous adj. 笨重的，笨拙的
pone n. 玉米饼
pongee n. 茧绸
poniard n. 匕首，短剑
pontiff n. 罗马教皇,主教,祭司长
pontifical adj. 自以为是的，武断的
pontificate n. 教皇,主教,高僧的地位
pontoon n.浮桥,浮筒,二十一点,潜水箱
pony n. 小马
poodle n. 狮子狗
pooh int. 轻视之声
pool n.小池；水塘
pooling 联营，合并
poon n. 胡桐树；胡桐木
poop n. 舵楼,船尾,消息,啪啪声
poor adj.可怜的；贫穷的
poorhouse n. 救济院
poor-house n. 贫民收容所
poorly a. 不舒服的；ad. 贫穷地
pop n.流行音乐，流行歌曲
popcorn n. 爆米花
pope n.(罗马天主教的)教皇
popgun n. 纸弹枪,气枪
popinjay n. 多嘴而爱装腔作势的人,花花公子,
popish a. 天主教的
poplar n. 白杨,白杨木
poplin n. 毛葛,府绸
poppy n. 罂粟,深红色
populace n. 民众，老百姓
popular adj.大众的；流行的
popularity n.通俗性；普及，流行
popularize vt. 使成通俗性,使平易,使普及
populate vt. 居住于 <国家、城市等>
population n.人口；全体居民
Populist n.人民党党员；民粹派成员
populous adj. 人口稠密的，人民多的
porcelain n.瓷 a.瓷的，瓷制的
porch n.门廊，入口处
porcine adj. 猪的，似猪的
porcupine n. 豪猪，箭猪
pore n.毛孔，气孔，细孔
pork n.猪肉
porosity n. 多孔性,有孔性
porous adj. 可渗透的，多孔的
porphyry n. 斑岩
porpoise n. 海豚
porridge n.粥，麦片粥
port n.港，港口
portable a.可移动的
portage n. 水陆联运,搬运
portal n. 入口,大门
portcullis n. 吊闸
portend v. 预兆，预示
portent n.前兆,预示,异常之物
portentous adj. 凶兆的，有危险的
porter n.搬运工人
portfolio n. 皮包,公文包,有价证券,业务量
porthole n. 舷窗,装货口,炮门
portia n. 鲍西娅(女名)
portico n. （有圆柱的）门廊
portiere n. 门帷; 门帘
portion n.一部分；一分
portly a. 肥胖的,魁伟的,一表人材的
portrait n.肖像，画像；描写
portraiture n. 肖像画家,肖像画,人物描写
portray vt. 描绘；描述
portsmouth n. 朴次茅斯(英国军港)
Portugal n. 葡萄牙
Portuguese n.葡萄牙人；葡萄牙语
pose vt.(使)摆好姿势
poser n. 使人困惑的问题；装腔作势的人
poseur n. 装模作样的人
posit v. 假定，认为
position n.主张，立场；形势
positioning n. 定位
positive a.正的；阳性的
positively adv. 实在地，绝对地；确定的，断然；断言地，确实；肯定地
positiveness n. 肯定，信心
possess vt.占用，拥有(财产)
possessed adj. 疯狂的
possession n.所有；拥有；财产
possessions n. 财产；产业，财产，所有物
possessive n. 所有格
possessor n. 持有人,所有人
possibility n.可能；可能的事
possible adj.可能的
possibly adv.可能地；也许
possum n. (口)负鼠；vi. 装病
post vt.投寄，邮寄 n.邮局
postage n.邮费，邮资
postal a.邮政的，邮局的
postbox n. 邮箱
postcard n. 明信片,风景明信片
postcode n. 邮政编码
poster n.海报，招贴
posterior adj. (在时间，次序上)较后的
posterity n. 后代，子孙
postern n. 后门,便门,旁门
postgraduate n. 研究生；a. 大学毕业后的
posthumous adj. 死后的，遗腹的
posting n. 过帐，誉入总帐
postman n.邮递员
postmark n. 邮戳
postmaster n.邮政局(所)长
postmortem n./a.，验尸，尸体解剖；事后的，死后的
post-office a. 邮局的,邮政部的
post-operative a. 手术后的
postpone vt.延迟，推迟，延缓
postponement  n. 延期,延后
postprandial adj. 饭后的
postscript n. 附言,后记
postulate vt.要求，假定，假设
posture n. 姿势,态度,情形,形势
posturer n. 摆姿势者，装模作样者
postwar adj. 战后的；ad. 在战后
posy n. 小花束
pot n.罐；锅；壶
potable adj. 适于饮用的
potash n. 碳酸钾, 钾碱,草碱
potassium n. 『化学』钾
potation n. 畅饮，饮料
potato n.土豆
potatoes 马铃薯
potency n. 能力
potent adj. 强有力的
potentate n. 统治者，当权者
potential a.潜在的 n.潜力
potentiality n. 潜力；潜能
potentially ad. 潜在地；可能地，大概地
pother n. 烦恼，喧闹
potholer n. 洞穴探险家
potholing n. 洞穴探险
potion n. 波掀洒
potpourri n. 混杂，杂文集，
pottage n. 浓汤
potter n. 陶工,陶器匠,陶艺家
pottery n. 陶器
pouch n. 小袋，烟草袋
poultice n. 糊药
poultry n.家禽
pounce n. 猛扑,吸墨粉
pound n.英镑(英国货币单位)
pour vt.灌，倒 vi.倾泻
pout v. 凸出，鼓出
poverty n.贫穷，贫困
poverty-stricken adj. 贫困的
powder n.粉末；药粉；火药
powdery a. 粉的,粉状的,满是粉的
power n.能力；力；权；幂
powerful a.强有力的；有权威的
powerless adj.无力量的，软弱的
pox n.发疹的疾病,痘,疹,瘟疫
practicable a.能实行的；适用的
practical adj.实际的；应用的
practically ad.实际上；几乎
practice n.实践；练习；业务
practice/-tise n. 练习，实行，实施，业务；v. 练决，实习，开业，执业，实行
practiced a. 经验丰富的；熟练的
practise vt.练习
practised adj. 熟练的，精通的
practitioner n. 从业者,开业者
praetor n. 执政官,长官
praetorian adj.  (古罗马的) 执政官的
pragmatic adj. 实际的，实用主义的
pragmatism n. 实用主义
prairie n.大草原，牧场
praise vt.&n.赞扬，表扬
praiseworthy a. 值得称赞的,令人钦佩的,可钦佩的
pram n. 婴儿车，童车
prance v. （马）腾跃，（人）神气活现地走
prank n. 恶作剧，玩笑
prankster n. 恶作，剧者
prate v. 瞎扯，胡说
prattle v. 闲聊，空谈
prawn n. 明虾,大虾
pray vt.&vi.请求；祈祷
prayer n.祈祷，祈求
prays 祈求
prc 中华人民共和国
pre 以前的；(前缀)前，先；预先
preacceptance 事先承兑
preach vt.说教，布道；鼓吹
preacher n. 传道者,讲道者,牧师
preaching n. 说教；a. 说教的
preamble n. 前言，序言
pre-arranged a. 事先安排的
precarious adj. 危险的
precariously ad. 不安全地
precaution n.预防；警惕
precautionary a. 预先警戒的,预防的,留心的
precede vt.先于… vi.领先
precedence n. 优先,居先
precedent n. 先
preceding adj. 前面的，上述的；在先的；先的，以前的
precent vt. (from)预防，防止
precept n. 箴言，格言
preceptor n. 教师
precinct n. 范围，区域
preciosity n. 过分文雅，过于讲究
precious a.珍贵的，宝贵的
precipice n. 悬崖
precipitant n. 沉淀剂；adj. 突如其来的
precipitate v. 加速，促成adj. 匆忙的，鲁莽的
precipitation n. 急躁，降雨(量)
precipitous adj. 陡峭的，仓促的
precis n. 摘要，大纲
precise a.精确的，准确的
precisely adv.正好；正确地；严密的；精确地；刻板地；明确地
precision n.精确，精密，精密度
preclude v. 排除；除去；避免，防止
precocious adj. 早熟的
precocity n. 早熟,早成
precognition n. 预感，早知
preconceive vt. 预想
preconception n. 先入之见
pre-conditioning n. 事先思想准备
precursor n. 先驱，先兆
predate n.在日期上早于
predator n. 食肉动物
predatory a. 掠夺的,进行掠夺的,捕食生物的
predecessor n.前辈，前任者
predestinate vt. 注定
predestination n. 预定; 命运
predestine v. 注定
predetermine vt. 预定,先决,预先决定做...
predicament n. 困境，穷境
predicate n. 谓语,本质
predication 预报；判断
predicative a. 表语的；n. 表语
predict v.预言，预告，预测
predictable adj. 可预知的，平庸的
prediction n.预言，预告；预报
predilection n. 偏好
predispose vt. 预先安排,使偏向于
predisposition n. 倾向，癖性
predominance n. 主导地位；显著
predominant a.占优势的；主要的
predominate vi. 占主导地位
preeminence n. 杰出,卓越,超群
preeminent adj. 出类拔萃的
preempt v. 以先买权取得，取代
preemption n. 先买权，取代
preemptive 以先买权取得的；优先占有的
preen v. 整理羽毛，(人)打扮修饰
preengage 预约
preexist vt.vi. 先前存在
preexistent  adj. 先存的,先在的
preface n.序言，前言，引语
prefatory a. 前言的,序文的
prefect n. 长官,提督,地方首长
prefecture n. 任期,管区,县
prefer vt.宁可，宁愿
prefer...to... 比起…来还是…好
preferable a.更可取的，更好的
preferably adv. 更好地
preference n.偏爱，优先；优先权
preferential adj. 优惠的；优先的，特惠的，差别制的
preferment n. 升迁,升任,大官
preferred 优先的
prefigure v. 预示，预想
prefix n. 字首
pregnancy n. 怀孕，丰富
pregnant a.怀孕的；意义深长的
prehensile a. 适于抓住的
prehistoric a. 史前的
prejudge vt. 预先判断,未充分审问就判决,
prejudice n.偏见，成见
prejudicial adj. 有害的，引起偏见的
prelacy n. 高级教士之职,主教
prelate n. 高级教士
preliminary a.预备的，初步的
preliterate adj. 无文字
prelude n. 序幕，前奏
premarital a.婚前的
premature a. 早熟的,过早的,不按时的
premeditate vt.vi.预谋,预先考虑
premeditated adj. 预谋的，事先计划的
premeditation  n. 事先考虑; 计划
premier n.总理，首相
premiere n. 首次公演
premise n. 前提,房屋
premises n. 建筑物；房屋，房产
premium n. 保险费，奖金
premonition n. 预告,预感,征兆
premonitory a. 预告的,前兆的,前驱性的
preoccupied adj. 被先占的；心事重重的，出神的
preoccupy vt. 先占领,先取,迷住
preordain vt. 预定,预先注定命运
prepackaged n.预先包装好的商品
prepaid a. 预先付讫的
preparation n. 准备，预备；制备；预习(时间)；配制；安排，筹备，制剂
preparatory a. 预备的,准备的,初步的
prepare vt.&vi.准备；预备
prepared adj. 准备好的，预制的
prepay vt. 先付,预付,预缴
preponderance n. 优势，多数
preponderant a. 以重胜的,优势的,压倒性的
preponderate v. （数量重要性）压倒超过
preposition n.前置词，介词
prepositive a. 前置的，前缀的
prepossess vt. 给<人>好印象,使<人>有好感
prepossessing adj. (个性等)给人好感的
prepossession n.先入之见
preposterous adj. 荒谬的，可笑的
prepubescent adj. 青春期前的
pre-recorded a.预录的
prerequisite n. 先决条件
prerogative n. 特权
presage n. 预感，不祥感v. 预示
presbyter n. 发起人,牧师,长老
Presbyterian a. 长老会制的,长老教会的
presbytery n. 长老会,长老会管辖区,内室
prescience n. 预知,先见
prescient adj. 有先见之明的
prescribe vt.命令；处(方)
prescribed adj. 规定的
prescript n. 命令，规定
prescription n.药方，处方的药
prescriptive a. 规定的,指示的,惯例的
presence n.出席，到场；在
present a.现在的 n.目前
presentable a. 可见人的,漂亮的,有规矩的
presentation n.介绍；赠送；呈现
present-day a. 当前的；当代的
presenter n. 主持人
presentiment n. 预感,预觉
presently adv.一会儿，不久
presentment n.陈述,叙述
preservation n.保存，储藏；保持
preservative n./adj. 防腐的，防腐剂
preserve vt.保护；保存；腌渍
preserver n.保存者,保护者
preset vt. 预先装置；预置；预先调整；预先安排
preside vi.主持；主奏
presidency n. 总统职位,总裁职位,主席职位
president n.总统
presidential a. 总统的,首长的,支配的,统辖的,
press n.印刷机，印刷所
pressed a. 加压的，压缩的
pressing adj.紧迫的；急迫的；n. & a. 压制；紧急的
pressure n.压力；压力；压，按
prestidigitation n. 变戏法，手法敏捷
prestige n.威望，威信，声望
prestigious adj. 有名望的，有威信的
presto n. (音乐)快拍，急速
presumable adj. 可能的，可假定的
presumably adv. 也许，大概；推测起来；假定地，推测地
presume vt.假定，假设，揣测
presumption n. 假定，冒昧
presumptive a. 根据推定的,假定的,给与推定之根据的
presumptuous adj. 自大的，专横的，冒昧的
presuppose vt. 预先假定,预料,预料为必要的条件
presupposition n. 预先假定，臆测
pretence n. 虚伪，借口
pretend vt.假托，借口vi.假装
pretended adj. 假的，虚伪的
pretender n. 冒牌者,要求者,要求王位者
pretense n. 借口
pretension n. 自命不凡
pretentious adj. 做作的，自抬身价的
pretentiousness n. 自命不凡
preterit a. 过去的
preternatural adj. 异常的，超自然的
pretext n. 借口
prettily 悦人地
pretty a.漂亮的，标致的
prevail vi.胜，优胜；流行
prevailing adj. 占上风的；占优势的；主要的；盛行的，流行的
prevalence n. 普遍；流行
prevalent a.流行的；盛行的
prevaricate v. 支吾其词，说谎
prevarication n. 支吾,搪塞
prevent vt.预防，防止；阻止
prevent...from 防止
prevent...from... 防止…；阻止，妨碍；v. 使…不能
preventable  adj. 可阻止的,可防止的,可预防的
prevention n.预防，阻止，妨碍
preventive a. 预防的,做预防的,妨碍的
preview n. & vt. 预映；预习
previous a.先的；前的 ad.在前
previously adv. 预先，先前；以前
prevision n. 先见，预感
prewar a. 战前的
prey vi.猎物 vi.捕获
price n.价格；代价
priceless adj.无价的，极贵的
price-list n. 价格表
pricing n. 定价；核价；价格形成
priciple n. 原理，原则
prick vt.刺(穿) n.刺孔
prickle n. (动物或植物上的)刺，棘v. 刺痛
prickly adj. 多刺的，易生气的
pride n.骄傲；自满；自豪
priest n.教士，牧师，神父
priestess n. 尼,尼姑,女祭司
priesthood n. 神职,僧职,祭司职
priestly a. 僧的,僧侣似的
prig n. 自以为比别人更有道德的人
prim adj. 端庄的，整洁的
primacy n. 第一,首位,卓越
primal a. 原始的；最初的
primarily ad.首先；主要地
primary a.最初的；基本的
primate n. 灵长类(动物)
prime adj.首要的；基本的
primer n. 启蒙书，识字课本
primeval n. 原始的，早期的
primitive a.原始的；粗糙的
primogeniture n.长子的身分
primordial adj. 最初的
primp v. (妇女)刻意打扮
primrose n. 报春花,樱草花,樱草色
prince n.王子，亲王
princely adj. 王子的，慷慨的
princess n.公主，王妃
princeton n. 普林斯顿(美国城市)
principal a.主要的 n.负责人
principality n.公国,领地,封邑
principally ad.主要，大抵
principle n.原则，原理；主义
print vt.&n.印刷
printable a. 可印刷的
printed a. 印恻的
printer n.印刷工；印花工
printing n. 印刷；印刷术；印刷业；a. 印刷
printout n. 印出
prior a.在先的；优先的
prioress n. 女修道院副院长,小女修道院院长
priority n.先，前；优先，重点
priory n. 小修道院
prise vt. 撬开；撬动；(up)撬杠；n. 撬杠
prism n.棱柱(体)；棱镜
prismatic a. 用棱镜分析的,分光的,虹色的
prison n.监狱，监禁
prisoner n.囚犯
pristine adj. 太古的，纯洁的，新鲜的
prithee int. 请,求求你
privacy n. 隐私,隐居,秘密
private a.私人的；私下的
privateer n. 私有武装船,私掠船
privately adv. 私下地，秘密地；一个人
privation n. 丧失，贫困
privatization n.私有化
privilege n.特权，优惠
privileged adj. 有特权的；特许的
privy a. 个人的,私人的,秘密的,隐蔽的
prize n.奖赏，奖金 vt.珍视
prize-fighter n. 职业拳击家
pro ad. 正面地
probability n.可能性；概率
probable a.或有的；大概的
probably adv.很可能，大概
probate n. 遗嘱查验,遗嘱查讫证
probation n. 试用(期)，试验
probationer 试用人员
probe n.探针 vt.用探针探查
probing n. 探讨；adj. 好探索的，尖锐的
probity n. 刚直，正直
problem n.问题；习题，问题
problematic adj. 有问题的
problematical adj. 有问题的; 可疑的; 不确定的
proboscis n. (象)长鼻，(昆虫等)吸管
procaine n. 普鲁卡因
procedural a. 程序上的
procedure n.程序；手续；过程
proceed vi.进行；继续进行
proceeding n.程序，行动，事项
proceedings n. (会议)议程；议事录会议文件；记录汇编
proceeds n. 收入
process n.过程；制作法；工序
processer n. 处理器
processing n. & adj. 加工(的)；(数据)处理
procession n.队伍，行列
processional a. 游行的
processor n. 处理机，处理程序
proclaim vt.宣告，宣布；表明
proclamation n. 宣言,公布,文告
proclivity n. 倾向，癖性
proconsul n. 地方总督,殖民地总督
procrastinate v. 耽搁，拖延
procrastination  n.拖延,担搁
procreate v. 生育
procrustean adj. 强求一致的
proctor n. 代理人，学监
procuration 代理(权)委托；佣金；获得
procurator n. 代理人,行政长官,太守,检察官
procure vt. 获得,取得,促成
procurement n. 采购；取得，获得
prod n. 刺针,刺棒,签子
prodigal adj. 挥霍的，n. 挥霍者
prodigality n.放荡,淫逸,挥霍浪费
prodigious adj. 很大的，巨大的
prodigy n. 奇事，非凡之人，天才
produce vt.生产；产生；展现
producer n.生产者；舞台监督
product n.产品，产物；(乘)积
production n.生产；产品；总产量
productive a.生产的；丰饶的
productivity n.生产率；多产
proem n. 序文,绪言,开端
profanation  n. 亵渎神圣,冒犯; 滥用 (misuse)
profane v. 亵渎，玷污
profanity n. 不敬，渎神
profess vt. 声称,以...为业,伪称,讲授
profession n.职业
professional a.职业的 n.专业人员
professor n. 教授；索比教授；宣称者；声明者
professorship n. 教授之职
proffer v. 献出，赠送，n. 提议，建议
proffesor n. 教授
proficiency n.熟练，精通
proficient a.熟练的，精通的
profile n. 外形，轮廓侧面像
profit n.益处；利润 vi.得益
profitable a.有利的；有益的
profiteer n. 奸商，牟取暴利者
profiteering 抬高市价，贪图暴利
profitless a. 无利益的,无益的,浪费的
profit-making 营利
profligacy n. 放荡,不检点,浪费
profligate adj. 挥金如土的，n. 挥霍者
proforma adj. 形式的
profound a.深刻的；渊博的
profoundly ad. 深刻地；深深地
profundity n. 深奥，深刻
profuse adj. 很多的，浪费的
profusion n. 丰富、大量、浪费
progenitor n. 祖先，始祖
progeny n. 后代，子女
prognathous a. 下巴突出的
prognosis n. 预知,预测,预后
prognostic a. 表示预兆的,预后的
prognosticate v. 预测，预示
prognostication n. 预知,预言,预测
program vi.编制程序
programmable a. 可编程的
programme n.程序
programmer n. 项目，程序制定者；程序设计人员
programming n. 程序编排；程序设计，编程序
progress n.前进，进展；进步
progression n. 前进,连续,级数
progressive a.进步的；向前进的
prohibit vt.禁止，阻止
prohibition n.禁止；禁令，禁律
prohibitionist n. 禁酒论者
prohibitive adj. 抑制的，价格昂贵的
project n.方案，工程 vi.伸出
projectile n. 抛射物，发射体
projection n. 突出物
projector n.投影仪；探照灯
proletarian n./adj. 无产阶级(的)
proletariat n. 无产阶级
proliferate vt. 增生，繁殖；激增
proliferation n. 激增；扩散
prolific adj. 多产的，多结果的
prolix adj. 罗嗦的，冗长的
prolixity n. 冗长,罗唆
prolog 人工智能标准语言(PROgramming LOGical)
prologue n. 开场白，序幕
prolong vt.延长，拉长，拖延
prolongation n. 延伸,延长,延长部分
prolonged adj. 持久的；持续很久的；长时期的
promenade n./v. 散步，开车兜风
prometheus n. (希神)普罗米修斯
prominence n. 突起,突出,凸出,突出物
prominent a.实起的；突出的
promiscuity n. 滥交，混杂
promiscuous adj. 滥交的，杂乱的
promise n.诺言 vt.&vi.答应
promisee 受约人
promiser n.立约人
promising a.有希望的；有前途的
promisor 立约人
promissory a. 约定的,约好的,约定支付的
promontory n. 海角，岬，隆起
promote vt.促进，发扬；提升
promoter n. 发起人；促进者
promotion n.促进；提升；创立
prompt a.及时的 vt.敦促
prompter n. 提示台词者,激励者,唤起者
prompting n. 激励，鼓舞
promptitude n. 敏捷,迅速,机敏
promptly adv. 立刻地；迅速地，准时地；敏捷地，及时地，即时地；果断地adj. 迅速地
promptness n. 敏捷，迅速
promulgate v. 颁布，传播
promulgation n. 发布,公布,普及
pronate v. 使(手掌)转向下
prone adj. 俯卧的，易于…的
prong n. 叉状物,耙子,干草耙
pronoun n.代名词
pronounce vt.发…的音；宣布
pronounced adj. 发出音的；显著的；明显的，(观点等)强硬的
pronunciation n.发音，发音法
proof n.证据；证明；论证
proof-positive n.确凿的证据
proofread vt. 校正,校对
proofreading 校对
prop n. 支撑物，靠山v. 支持
propaganda n.宣传；宣传机构
propagate vt.繁殖；传播，普及
propagation n.繁殖；传播；蔓延
propel vt.推进，推动
propellants n. 推进剂
propellent adj. 推进的
propeller n.螺旋桨，推进器
propensity n. 嗜好，习性
proper a.合乎体统的，正派的
properly adv. 妥善地；恰当地；适当地；彻底地；合适地；严格地；真正地
property n.财产；财产权
prophecy n.预言，预言能力
prophesy vt.vi. 预言,预报
prophet n.预言家，先知
prophetess n. 女预言家,女先知
prophetic a. 预言的,先知的,预示的
prophylactic adj. 预防疾病的
propinquity n. 接近，类似，邻近
propitiate v. 讨好，抚慰
propitiation n. 安抚,抚慰; 劝解
propitiatory adj. 讨好的，调解的
propitious adj. 吉利的，顺利的
propogate v. 宣传，传播
proponent n. 支持者，拥护者
proportion n.比，比率，部分
proportionable a. 相称的,成比例的
proportional a.比例的；相称的
proportionate a. 相称的,成比例的,适当的
proportionately ad. 成比例地，相称地
proposal n.提议，建议；求婚
propose vt.提议 vi.求婚
proposed 被提议的
proposition n.命题，主题；提议
propound vt. 提出,提议
proppose vt. 提议，建议；提名，推荐
proprietary adj. 私有的
proprietor n. 业主，所有人
proprietorship n. 所有权
propriety n. 礼节，适当
propulsion n.推进，推进力
propulsive a. 推进的,有推进力的
prorate 按比例分配，按比便计算；分担，摊派
prorogation n. 休会
prorogue v. 休会，延期
prosaic adj. 单调的，无趣的
proscenium n. 舞台前部,幕装置,舞台,前部
proscribe v. 禁止
proscription n. 剥夺人权,处罚的宣告,放逐
prose n.散文
prosecute v. 告发，检举
prosecution n. 实行,经营,起诉
prosecutor n. 起诉人
proselyte n. 皈依者，改变宗教信仰者
proselytize v. 使……皈依
prosody n. 诗体学，韵律学
prospect n.展望；前景，前程
prospective adj. 未来的，预期的
prospector n. 勘探者
prospectus 计划书，简介发起
prosper vi. 繁荣
prosperity n.繁荣；昌盛
prosperous a.繁荣的，昌盛的
prostitute n. 妓女,男娼
prostitution n. 卖淫,卖身
prostrate v. 平放，征服，使……衰弱
prostration n. 平伏,跪倒,疲劳,虚脱
protagonist n. 主角；提倡者，支持者
protean adj. 易变的，多才的；变化自如的；多才多艺的
protect vt.保护
protect...from 保护…不受…
protection n.保护，警戒
protectionism n. 贸易保护主义；保护主义；保护贸易政策
protective a.保护的，防护的
protector n. 保护者,保护物,保护装置
protectorate n. 摄政,摄政政治,护民官之职
protege n. 被保护者,党羽,门徒
protein n.蛋白质，朊
protest vt.&vi.&n.抗议
Protestant n. 新教,新教徒
Protestantism n. 新教,新教教义,新教徒
protestation n. 主张,断言,明言
protester 拒付(期票)者
protocol n. 外交礼节，协议
proton n. 质子，氕核
protoplasm n. 原形质
prototype n.原型；典型，范例
protract v. 延长，拖长
protracted adj. 延长了的
protrude v. 突出，伸出
protrusive adj. 伸出来的，突出的
protuberance n. 节疤，突出，凸出
protuberant adj. 突出的，隆起的
proud adj.骄傲的；自豪的
proudly adv. 骄傲地；自豪地；傲慢地
prove vt.证明，证实
provenance n. (艺术等的)出处，起源
provender n. (牛马吃的)草料，粮秣
proverb n.谚语，格言，箴言
proverbial a. 谚语的,谚语式的,闻名的
proverbially adv. 无人不知地
provide vt.提供；装备，供给
provided conj.以…为条件
providence n. 深谋远虑，远见
provident adj. 深谋远虑的，节俭的
providential a. 天意的,根据神意的,天佑的,
province n.领域，范围，职权
provincial adj. 偏狭的，粗俗的
provision n.规定，条款，条项
provisional adj. 临时的；暂时的，假定；假定的
provisions n. 粮食，食品
proviso n. 附文；条件；(拉)但书，限期性条约
provocation n. 激怒
provocative adj. 激怒的、挑战的
provoke vt.对…挑衅；激发
provoking adj. 激怒人的，刺激人的
provost n. 负责校政人员,主监督,宪兵司令,
prow n. 船首,船首状物,机首
prowess n. 勇敢，不凡的能力
prowl n. 潜行,徘徊,悄悄踱步
proximate adj. 最接近的，直接的；近似的；贴近的；即将到来的；接近的；前后紧接的
proximity n. 接近，附近
proximo adj. 下月的
proxy n. 代理,代理人,委托书
prude n. 过份守礼的人
prudence n. 谨慎，小心
prudent a.谨慎的；精明的
prudential a. 谨慎的,细心的,明辨的
prudery n. 过分守礼，假正经
prudish adj. 过分守礼的，假道学的
prune n. 梅干(用李子“plum”做的干果)v. 修剪，剪除
prurience n. 好色，淫乱
prurient adj. 好色的，淫乱的
Prussia n. 普鲁士
prussian n. 普鲁士人；adj. 普鲁士的，普鲁士人的
pry v. 刺探，打听，撬开
psalm n. 赞美诗，圣诗
psalmist n. 赞美诗作者,诗篇作者
psalmody n. 圣歌吟唱,赞美诗,赞美诗集
psalter n. 诗篇,诗篇集
psaltery n. 古代弦乐器
psephology n. 选举学
pseudo a. 假的，伪的，冒充的
pseudonym n. 假名，笔名
pseudopod n. 假足，伪足
pshaw int. 表示不耐烦,轻蔑时的叫声
psyche n. 灵魂；心灵；心智
psychedelic adj. 引起幻觉的；n. 迷幻药
psychiatric adj. 精神病学的；精神病的
psychiatrist n. 精神病医师,精神病学家
psychiatry n. 精神病学
psychic adj. 精神的，心灵的
psychical a. 灵魂的,精神的,心灵的
psychoanalysis n. 精神分析
psychological a.心理的，心理学的
psychologist n. 心理学家
psychology n.心理学；心理
psychopathic a. 精神病的,精神错乱的,要发疯似的
psychosis n. 精神病，变态心理
psychotic adj. & n. 精神病的，疯子
pterodactyl n. 翼龙
ptomaine n. 尸毒
pub n. 酒店
puberty n. 青春期，春情发动期
pubescent adj. 青春期
public adj.公共的，公众的
publican n. ((英))酒馆 (pub) 的老板
publication n.公布；出版；出版物
publicist n. 国际法学家,政治评论家,政治记者,
publicity n. 公开,名声,宣传
publicize v. 宣传，引人注意
publicly adv. 公开地；公然；公众所有地
publish vt.&vi.出版；发行
publisher n. (报社)业主；出版商
publishing 出版；出版的
puce n. 紫褐色
puck n. 恶作剧的小妖精,淘气小孩,冰球
pucker v. 起皱n. 皱褶
pudding n.布丁
puddle n. 水坑，洼
pueblo n. 印第安人村庄
puerile adj. 幼稚的，儿童的
puerility n. 稚气，幼稚
puerperal adj. 分娩的
puff n.(一)喷，(一)吹
puffy a. 胀大的,肥满的,喘气的,一阵阵吹的
pug n. 狮子狗,泥料,拳师,(兽)脚印
pugilism n. 拳击，搏击
pugilist n. 拳击家
pugnacious adj. 好斗的
pugnacity n. 好斗性
puissance n. 权力
puissant adj. 强有力的，强大的
pulchritude n. 美丽
pulchritudinous adj. 美丽的
pull vt.拉，拖；拉，拉力
puller n. 拉的人,划手,拉出器
pullet n. 小母鸡,小姑娘
pulley n.滑轮，滑车，皮带轮
Pullman n. 卧车,普式火车
pullover n. 套衫
pullulate v. 繁殖，剧增
pulmonary adj. 肺的，对肺有影响的
pulp n.果肉；(植物的)髓
pulpit n. 讲道坛
pulsate v. 有规律的振动
pulsating adj. 节奏强的，极为兴奋的
pulsation n. 脉博,悸动,震动
pulse n.脉搏
pulverize v. 压成细粉，彻底击败
puma n. 美洲狮,美洲狮的毛皮
pumice n. 轻石,浮石
pummel v. (用拳)接连地打，打击
pump n.泵 vt.用抽机抽
pumpkin n.南瓜，南瓜藤
pun n. 双关语,俏皮话,押韵
punch vt.冲出 n.冲压机
puncheon n.一种容量为72至120加仑之大桶
punctilio n. 细节,拘泥形式,拘束
punctilious adj. 留心细节的；谨小慎微的
punctual a.严守时刻的；准时的
punctuality n. 严守时间,正确,规矩
punctually ad. 准时地
punctuate vt. 给…加标点符号
punctuation n. 标点
puncture n. 刺孔，穿孔v. 刺穿，刺破
punctured a. 被剌破的
pundit n. 权威人士，专家
pungency n. 刺激性，尖刻
pungent adj. 刺鼻的，苛刻的
punish vt.&vi.惩罚；处罚
punishable a. 该罚的,可罚的
punishment n.罚，惩罚，处罚
punitive a. 刑罚的,惩罚性的
punk n. 废物,小阿飞,半朽的木头
puny adj. 弱小的，发育不良的
pup n. 小狗,幼畜,学生
pupa n. 蛹
pupil n.小学生；学生
puppet n.木偶，玩偶；傀儡
puppy n.小狗；幼小的动物
purblind adj. 愚钝的，视力不佳的
purchasable a. 买得到的
purchase n.买，购买 vt.买
purchaser n. 买方,购买者
purchasing 采购
pure a.纯粹的；纯洁的
purebred adj. (动物)纯种的
purely adv. 全然，纯然；纯粹地，完全地；仅仅；简单地
pureness n. 清洁,纯净,纯粹
purgation n. 净化，洗罪
purgative n. 泻药
purgatory n. 炼狱，暂时的苦难
purge v. 清洗，洗涤
purification n. 纯化,提纯,涤罪
purify vt.提纯，精炼(金属)
Puritan n. 清教徒
puritanical adj. 极端拘谨的
purity n.纯净；纯洁；纯度
purl n. 金银丝,边饰,苦艾啤酒,潺潺声,
purlieus n. 邻近地区
purloin v. 偷窃
purple n.紫色 a.紫的
purport n. 意义，涵义
purpose n.目的；意图；效果
purposely ad. 故意地
purr vt.vi. 咕噜咕噜叫,发出喉音
purse n.钱包，小钱袋，手袋
pursuance n. 追赶,实行,从事
pursuant n. 追逐者
pursue vt.追赶，追踪；进行
pursuer n. 追赶者,追求者,研究者
pursuit n.追赶；追求；事务
pursuivant n. 纹章院官员,随从
purvey v. （大量）供给，供应
purveyance n. 粮食的供给
purveyor n. 承办者
purview n. 范围，权限
pus n. 脓,脓汁
push vt.推，逼迫 vi.推
push...aside 把…推到旁边
push...up 把…向上堆
pusillanimity n. 无气力,胆怯
pusillanimous adj. 懦弱的，胆小的
puss n. 猫,小姑娘,少女
pussy n. 猫,小姑娘
put vt.放，摆；使处于
put...away 把…收起来(放好)
put...down 把…放下
putative a. 想象的,推定的,传说的,被公认的
pute a. 纯粹的，单纯的
putrefaction n. 腐坏，腐败
putrefy v. 使腐烂
putrid adj. 腐臭的
putter n. 置放者,推车工,轻击棒
putty n. 油灰,玻璃,金属等的磨粉
puzzle vt.使迷惑；使为难
puzzled adj. 迷惑的；困惑的
puzzling a. 令人困惑不解的
pygmy n. 矮人，侏儒
pyjamas n.(宽大的)睡衣裤
pylon n. 高压电线架，桥塔
pyramid n.金字塔
pyramidal a. 金字塔形的,角锥状的,锥体的
pyre n. 火葬柴堆
pyridine n. 吡啶，氮苯
pyrites n. 硫化铁矿
pyromania n. 纵火狂
pyromaniac n. 放火狂
python n. 蟒蛇，巨蛇
qi n. 气(中医)
quack n. 冒充内行之人，庸医
quad n.四胞胎之一；同类的四个构成的一组
quadrangle n. 四边形
quadrangular a. 四边形的
quadrant n. 四分圆,象限,四分仪
quadrilateral a. 四边形的
quadrille n. 四人用四十张纸牌玩的牌戏,
quadruped n. 四足动物
quadruple a. 四倍的,四重的,四部组成的
quaff v. 畅饮
quagmire n. 沼泽地，困境
quail v. 畏惧，颤抖
quaint a. 古雅的,离奇有趣的,奇怪的
quake n. 地震
Quaker n. 教友派信徒
qualificate 品质证明书
qualification n.资格；限制条件
qualifications n. 资格，条件
qualified adj. 有资格的；合格的；受限制的；有限度的，胜任的
qualify vt. 修饰，限定；使合格；使胜任；使具有资格；限制；vi. 取得资格
qualitative adj. 质量的，质的，定性的
quality n.品质
quality-mind 产品质量
qualm n. 疑惧，紧张不安
qualms n. 不安；良心之谴责
quandary n. 困惑，进退两难
quanta n.额；
quantify vt. 确定…的数量；确定数量
quantitative a.量的；定量的
quantity n.数量
quantity-built 成批生产的
quantum n. 量，定量，份额，总量，定额；量子
quarantine n. 隔离检疫期，隔离
quard 卫兵
quarrel vi.争吵
quarrelsome a. 喜欢吵架的,好争论的,怒气冲冲的
quarry n. 采石场，v. 采石
quart n.夸脱(=2品脱)
quarter n.四分之一；一刻钟
quarterage 季度工资；季度税；季度津贴
quarterly a.季度的 ad.季度地
quartermaster n. 军需官
quarters n. 寓所，住处；住所；营房；方向，地区，方面
quartet n. 四重奏，四重唱
quarto n. 四开,四开大的书本
quartz n.石英
quasar n. 类星体
quash v. 取消，拒绝接受
quasi a. 类似的,外表的
quaver vi. 发颤音,震动
quay n. 码头,突堤,岸壁
queasy adj. 不喜欢的，令人作呕的
quebec n. 魁北克(加拿大省名)
queen n.女王；王后
queenly a. 女王的
queer a.奇怪的，古怪的
quell v. 制止、镇压
quench vt.熄灭，扑灭；压制
querulous adj. 抱怨的，多牢骚的
query n./v. 质问，疑问，询问
quest vt.寻找 vi.追求
question n.发问；问题；疑问
questionable a.可疑的，不可靠的
questionaire n. 调查表，征求意见表；问卷
questioning 质问
questionnaire n. 调查表,问卷,调查表
questions n. 询问，疑问，问题
quetzal n.丽鹃,绿咬鹃
queue n.行列 vi.排队等候
quibble n. 遁词，吹毛求疵的反对意见
quick adj.快的，迅速的
quicken vt.加快 vi.加快
quickly adv.迅速地；快速地；快地；敏捷地
quickly-cured adj. 迅速治愈的
quick-minded a. 头脑敏捷的
quickness n. 急速,迅速,速度
quicksand n. 流沙,流沙地,危险状态
quicksilver n. 水银,汞
quid n. 咀嚼块；(英俚)一镑
quiescence n. 静止,不活动,寂静
quiescent adj. 不动的，静止的
quiet adj.安静的，平静的
quieten vi. 平静下来
quietly adv. 安静地，平静地；轻轻地；静悄悄地，平稳地；静静地；静止地；寂静地
quietness n. 平静,寂静
quietude n. 平静,寂静
quietus n. （债务的）偿清，平息
quill n. （豪猪等动物的）刺
quilt n.被子
quince n. 植物的一种
quinine n. 奎宁
quintessence n. 典型，完美的榜样，精华
quintuplet n. 五胞胎之一
quintuplicate 一式五份
quip n. 名言，讽刺语 v. 讽刺，嘲弄
quire n. 唱诗班；歌咏队；鸟群；v. 合唱，合奏；歌唱队
quirk n. 奇事，怪癖
quisling n. 卖国贼，内奸
quit vt.离开，退出；停止
quite adv.很，十分
quittance n. 免除,解除,报复,赔偿,赦免
quitter n. 遇困难即放弃者
quiver vi.(轻微地)颤动
quixotic adj. 不切实际的，空想的
quiz n.小型考试，测验
quizzical adj. 爱挖苦的，戏弄的
quoit n. 圈环,掷圈环
quondam a. 原来的,以前的
quorum n. 法定人数,选出的团体
quota n. 配额,限额
quotation n.引用；引文；报价单
quotationmarks n.引号
quote vt.引用，引证；报价
quotidian adj. 每日的，平凡的
quotient n. 商,份额
rabbi n. 犹太的法学博士,法师,先生
rabbit n.兔
rabble n. 乌合之众，暴民，下等人
rabid adj. 患狂犬病的，疯的，失去理性的
rabies n. 狂犬病,恐水病
race n.比赛；赛跑；赛马
raceme n. 总状花序
racer n. 比赛者,一种黑蛇
racetrack n. 跑道
racial a.种族的，人种的
racing n. 竞赛，赛跑，竞走
rack n.搁物架；行李架
racket n.球拍
racketeer n. 讹诈钱财的歹徒
raconteur n. 善于讲故事的人
racoon n. 浣熊
racquet n. 球拍,拍球戏之一种,球拍型雪鞋
radar n.雷达，无线电探测器
radial a.光线的；放射的
radiance n. 发光，喜悦
radiant a.绚丽的；容光焕发的
radiate vi.发射光线；辐射
radiation n.辐射；射线
radiator n.暖气片，散热器
radical a.基本的；激进的
radicalism n. 激进主义
radically ad. 急剧地
radicate vt. 使生根，确立
radio n.收音机
radioactive  adj. 辐射性的；放射性的；放射引起的
radioactivity n. 放射性；放射(现象)；辐射
radio-astronomer n. 无线电天文学家
radiochemistry n. 放射化学
radio-frequency n. 无线电频率
radioisotope n. 放射性同位素
radios 收音机
radish n.小萝卜
radium n.镭
radius n.半径距离；界限
raffia n. 酒榔,其叶的纤维
raft n. 木排；木筏
rafter n. 椽子
rag n.抹布；破布
ragamuffin n. 衣裳褴褛的人,无赖,寒酸样子的孩子
rage n.大怒
ragged adj. 破烂的，（表面）凹凸不平的
ragout n. 蔬菜炖肉片
rags n. 破旧衣服
rag-tag adj. 乱糟糟的
raid n.袭击；突然搜查
raider n. 奇袭者,侵入者,特别攻击队
raihead 终点卸货站
rail n.铁轨；轨道；铁路
railing n. 扶手,栏干,抱怨
raillery n. 善意的嘲弄
railroad n.铁路 vi.由铁路运输
railway n.铁路，铁道
railway-line n. 铁路线
raiment n. 衣服
rain v.下雨 n.雨
rainbow n.虹，彩虹
raincoat n. 雨衣
raindrop n. 雨滴,雨点
rainfall n. 降雨,降雨量
rainstorm n. 暴风雨
rainy a.下雨的，多雨的
raise vt.提出，发起，发出
raiser n. 提高者,饲养者,栽培者
raisin n.葡萄干
rajah n.（印度）王公，邦主
rake n.耙子 vi.耙；搜索
rally n.&vt.&vi.(重新)集合
ram n. 公羊,撞锤
ramble vi.闲逛，漫步；聊天
rambler n. 漫步者
rambling a. 杂乱无章的
rambunctious adj. 喧闹的，放纵的
ramification n. 分支，支流
ramify v. 分支，分叉
ramp n./v. 诈骗，索高价
rampage v. 狂暴地乱冲；n. 暴怒
rampant adj. 蔓生的，猖獗的
rampart n. 壁垒，城墙
ramrod n. 推弹杆,严格执行纪律者
ramsay n. 拉姆齐(姓)
ramshackle adj. 摇摇欲坠的
ran v. run(跑)的过去式和过去分词
ranch n.(北美洲的)大牧场
rancher n.大牧场主；大牧场工人
ranchman n.牧场经营者; 牧场工人,牛仔
rancid adj. 不新鲜的，变味的
rancor n. 深仇，怨恨
rancorous adj. 怨恨的，憎恨的
rancour n. 敌意,深仇
rand n. 田埂；河边高地
random n.随机 a.随机的
rang v. ring(按铃)的过去式；响
range vt.排列；把…分类
ranger n. 守林人,骑警,徘徊者
ranging n. 测距
rangy a. 适于走来走去的,广阔的,四肢瘠长的
rank n.排，横行；社会阶层
ranking 证分等级，优先次序排队
rankle v. （怨恨，失望等）难以释怀
ransack v. 彻底搜索，洗劫
ransom n. 赎金，赎身，v. 赎回，解救
rant vt.vi. 咆哮,激昂地说
rap n.轻敲击声 vt.敲击
rapacious adj. 强夺的，贪婪的
rapacity n. 掠夺，贪婪
rape n. 抢夺,掠夺,油菜,葡萄渣
rapid adj.快的，迅速的
rapidity n.快，迅速；陡，险峻
rapidly adv. 迅速地，急速地；敏捷地；险峻地
rapids n. 急流，湍流
rapier n. 轻巧而细长的剑
rapine n. 劫掠，掠夺
rapport n. 和睦，意见一致
rapprochement n. 和好，和睦
rapt adj. 专注的
rapture n.狂喜，欢天喜地
rapturous adj. 着迷的，狂喜的
rare a.稀薄的；稀有的
rarefied a. 变成稀薄的,纯化的,考究的
rarely ad.很少，难得
rarity n. 稀罕,罕有,珍贵,稀薄
rascal n.流氓，恶棍，无赖
rascality n. 坏事,恶行,歹徒的作为
rascally a. 无赖的,恶棍的,狡猾的
rase vt. 毁灭,刮去,把...夷为平地
rash a.轻率的；鲁莽的
rashly ad. 莽撞地，轻率地
rashness n. 轻率，鲁莽
rasp n. 粗锉刀,擦菜板,刺耳声
raspberry n. 悬钩子,舌头放在唇间发出的声音
rat n.鼠
ratability 纳税义条，估价
ratal 纳税额，征税价格
ratch n. (机器)棘轮
ratchet n. 棘轮(亦作ratchet)
rate n.比率；速率；等级
rated a. 额定的；适用的额定的
rather ad.宁可，宁愿；相当
ratification n. 批准,承认,认可
ratify vt. 认可；批准
rating n. 类别；分类
ratio n.比，比率
ratiocination n. 推理，推论
ration n. 定额,定量,配给
rational a.推理的；适度的
rationale n. 基本原理，根据
rationalism n. 理性主义，唯理论
rationalist n. 理性论者,纯理论者,理性主义者
rationalization n. 合理化
rationalize vt. 使合理,合理地处理,使成有理数
rat-race n.商业竞争；事业竞争
rattan n. 藤,藤茎,藤杖
rattle vt.发出格格声
rattlesnake n. 响尾蛇
rattle-snake 响尾蛇
raucous adj. （声音）沙哑的，粗糙的
ravage n. 破坏,蹂躏
rave n. 热切赞扬，倾倒
raven n. 大乌鸦,掠夺
ravening ] adj. 贪婪的; 搜寻猎物的; 狼吞虎咽的
ravenous adj. 饿极了的，贪婪的
ravine n. 深谷，峡谷
ravish v. 迷住，强夺
ravishing adj. 令人陶醉的
ravishment n. 狂喜，陶醉
raw a.未煮过的；未加工的
rawhide n. （牛的）生皮
ray n.光线，射线，辐射线
rayon n. & a. 人造丝(的)
raze vt. 毁灭,刮去,把...夷为平地,
razor n.剃刀
re prep. 关于；(前缀)再，又
reach vt.&vi.伸手去够..
react vi.起反应；有影响
reaction n.反应；反作用
reactionary adj. 保守的，反动的
reactivate v. 使恢复活动；恢复活力，重新活跃
reactor n.反应器；反应堆
read v.读
readable a. 值得一读的,易读的,读起来津津有味的
reader n.读者；读物，读本
readily ad.乐意地；无困难地
readiness n. 预备,准备,敏捷
reading n.读，阅读；读书
reading-room n. 阅览室
readjust vt. 重新调整,再调整
readjustment  n. 重新调整; 重新整理; 重新铺排; 适
ready adj.准备好的，有准备
ready-made a. 现成的,做好的
reagent n. 试剂（导致化学反应）
real a.真的；现实的
realign v. 使重新成一直线，重新结盟
realise vt. 认识到，了解，实现
realism n. 写实主义,现实,实在论
realist n. 现实主义者,写实主义者,实在论者
realistic a.现实的；现实主义的
reality n.现实；真实
realization n.(理想等的)实现
realize vt.意识到
really ad.真正地；实在
realm n.王国，国土；领域
real-time 即时处理，实时；适时
realty n. 不动产,房地产
ream n. 令（纸张的张数单位）
reamer n. 钻孔器,铰孔锥,橘子榨汁器
reanalyze v. 再分析
reap vt.&vi.收割，收获
reaper n. 收割者
reappear vi. 再出现
reappears vi. 再现，重现
rear n.后部，后面；背面
rearrange v. 重新整理，重新排序
rearward ad. 在背后,向后方
reason n.理由；理性 vi.推理
reasonable adj.有道理的
reasonably adv. 合理地，适当地；相当地；有理地；adj. 合情合理地
reasoning n. 推(评)理；a. 推理的
reassemble vt. 重新召集
reassert vt. 再断言,重复主张
reassess 重新估价
reassume vt. 再采取,再接受,再假定
reassurance n. 安慰（的话），放心
reassure v. 使安心，安慰
reattach vt. 重新接上
reave v. 劫掠，抢走
rebarbative adj. 令人讨厌的，冒犯人的
rebate n. 折扣，回扣
rebel vi.造反 n.造反者
rebellion n.造反；叛乱；反抗
rebellious adj. 反抗的，难控制的
rebilling 重开发票
reborn a. 再生的,更新的
rebound vi. 弹回,复原,报应,返回
rebuff v. 断然拒绝
rebuild vt.重建；改造
rebuke vt.指责，非难，斥责
rebus n. （以音、画等提示的）字谜，画谜
rebut 辩驳，驳回
rebuttal n. 反驳，反证
recalcitrance n. 固执，顽抗
recalcitrant adj. 固执的，顽抗的
recall n. 回想；vt. 回忆，回想起；想到，叫回；收回；召回，忆起，记忆；撤消，取消；复活，检索
recant v. 改变，放弃（以前的信仰）
recantation n. 改变宗教信仰
recapitulate v. 扼要重述
recapitulation n. 重述要点,概括,摘要
recast vt. 重铸,重作,改造
recede v. 后退，收回（诺言）
receipt n.收到；收条，收据
receipts n. 收入，收到的物(或款项)
receivable a.应收的；可收的
receive vt.收到，接到
received a. 被接收的，公认的；已收到；末收到
receiver n.收受者，收件人
receiving 接收，验收，收取
recent a.新近的，最近的
recently adv.近来
receptacle n. 容器
reception a.接待；招待会；接受
receptionist n. 接待员
receptive adj. 善于接受的
receptor n. 感受器，受体
recess n. 壁凹（墙上装架子，柜子等凹处），休假
recession n. 衰退时期，萧条时期
recessive adj. 隐性遗传的，后退的
recherche adj. 精选的，珍贵的
recidivism n. 累犯，重犯
recipe n.菜谱，烹饪法；处方
recipient a. 领受的,容易接受的,感受性强的
reciprocal a.相互的；互利的
reciprocate v. 答谢，回报
reciprocation n. 交互作用,交换,来往
reciprocity n. 互惠主义，相互利益
recital n. 独奏，吟诵
recitalist n. 独奏家
recitation n. 详述,吟诵,背诵诗
recitative a. 吟诵的,背诵的,叙述的
recite vi.&vt.背诵；叙述
reck v. 注意的，有关；有关系，相干；顾虑，介意
reckless a.粗心大意的；鲁莽的
reckon vi.数，算帐 vt.认为
reckoning n. 计算；算帐；估计
reclaim vt.开垦，开拓；回收
reclamation n. 矫正,驯养,教化
recline vt. 使斜靠
recluse n. 隐士v. 隐居
recognise vt. 承认，认可，认出，识别
recognition n.认出，识别；重视
recognizance n. 具结,保证书,保证金,保释金
recognize vt.认识，认出；承认
recoil v. 退却，退缩
recollect vt.回忆，追忆，想起
recollection n. 记忆,回想,回忆
recommence vt.vi. (使)重新开始
recommend vt.推荐，介绍；劝告
recommendation n.推荐，介绍；劝告
recommended 被推荐的
recompense v. 报酬，赔偿
reconcile vt.使和好；调停
reconcilement n. 和解，调解
reconciliation n. 和解，讲和
recondite adj. 深奥的，难解的
reconnaissance n. 侦察，预先探索
reconnoitre vt.vi. 侦察,勘探
reconquer  vt. 再征服; 再占领
reconsider vt.vi. 再考虑,重新考虑
reconstitute vt. 重建
reconstruct vt. 重建,改造,复兴
reconstruction n. 复兴,改造,再建
record n.记录，记载；唱片
recorder n.录音机
record-holder n. 纪录保持者
recording n. 录音，记录
recording-room n. 录音室
record-player n. 电唱机
recount v. 描述，叙述
recoup 补偿，赔偿，扣除
recourse n. 求助，求援
recover vt.重新获得；挽回
recoverable a. 可恢复的，可回收的
recovery n.重获；痊愈，恢复
recreant n. 懦夫，叛徒adj. 胆怯的
recreate vt.vi.(使)得到休养,(使)得到娱乐
recreation n.消遣，娱乐活动
recriminate v. 反责，反控
recrimination n. 揭丑,反责
recross  vt. 再横过; 再横渡
recrudescence n. 复发,再发作
recruit n. 新兵，新成员v. 征募
recruitment n. 招募；招工，招聘
rectangle n.矩形，长方形
rectangular a. 矩形的，长方形的
rectification n. 纠正；改正，校正，提纯；整顿
rectifier n.改正者；矫
rectify vt.纠正；调整；精馏
rectitude n. 诚实，正直
rector n. 教区长,校长,院长
rectory n. 教区长的管区
rectum n. 直肠
recumbent adj. 侧卧的，休息的
recuperate v. 恢复（健康），复原
recuperation n. 恢复
recuperative adj. 有助恢复健康的
recur vi. 复发,回到,重现,循环,依赖,
recurrence adj. 重现，反覆
recurrent a. 再发生的,定期重复的,循环的
recursive a. 递归的，循环的
recusant adj. 不服从规章的
recycle vt. (使)再循环；vi. & n. 再循环
recycling n. 再循环
red adj.红色的
redbreast n. 知更鸟
redden v. (使)变红；脸红
reddish a. 微红的
redeem v. 赎罪，实践（诺言）
Redeemer n. 买回者,赎当者,赎身者,救世主
redefine vt. 重新规定(定义)
redelivery 重新发运，转售交货
redemption n. 赎罪
redevelopment n. 重新开放
redirect vt. 重定向
rediscount 再贴现，转贴现
rediscover vt. 再发现
redness n. 红,红色
redolent adj. 芬芳的芳香的
redouble  vt. 使…再倍增; 使…再加倍,加强; 使
redoubt n. 多面堡,防守阵地
redoubtable adj. 可敬畏的
redound v. 提高，增加
redraw vt. 再拉；提取(逆转汇票)
redress n./v. 改正，修正
reduce vt.缩减；减少
reduction n.减少，减小，缩减
redundancy n. 过剩，似乎多余其实重要的后备力量
redundant adj. 累赘的，多余的
redwing n. 红翼鸫
redwood n. 美国杉树,红色木材,红色木质的树
ree v. 筛
reecho vi. 再反响,响遍
reed n.芦笛，牧笛
reeducate v.再教育
reedy a. 芦苇丛生的,芦苇做的,芦苇状的
reef n.礁，礁石，暗礁
reek n. 恶臭
reel vt.卷，绕
reelect vt. 重选,改选
reelection n. 重新选举
reenter n. 重进入
reestablish vt. 重建,复兴,恢复
reexport v. 再出口
refection n. 便餐,点心,茶点,恢复体力
refectory n. 餐厅,休息室
refer vt.把...提交 vi.提出
referee n.(足球等)裁判员
reference n.参考文献；参照系
referenda n. 复决(权)；公民投票
referendum n. 公民投票,普通投票,请示书
referent n. 被谈到的事
referential 供参考的
refill n. 再注满,替换物
refine vt.&vi.精炼，提纯
refined adj. 精炼的，精的；精制的；文雅的
refinement n. 提炼，文雅
refinements n. (生活)风雅
refinery n.精炼厂，提炼厂
refit vt.vi.n. 整修,改装
reflation 通货再膨胀
refle 步枪
reflect vt.反射；反映；思考
reflection n.反对；水中映像
reflection/-exion n. 映象，倒影，反射，沉思，熟虑
reflective adj. 深思熟虑的
reflector n.反射器；反射
reflex n. 反射,反射光,映像
reflexive 『文法』
reflow v. & n. 回流，逆流
reflux n. 逆流,退潮
reform vt.&n.改革，改良
reformat v. 重定格式
reformation n. 改革,改正,改善
reformatory adj. 改革
reformer n. 改革家,改革运动者
refract vt. 使折射,测定...的折射度
refraction n. 折光,折射
refractory adj. 难驾驭的，（病）难治的
refrain vi.抑制，制止，忍住
refresh vt.使清新vi.恢复精神
refreshing adj. 使心神爽快的；使精神快乐的
refreshment n.茶点，点心，便餐
refrigerate vt. 使冷却,使清凉,冷藏
refrigeration n. 冷却,冷藏,冷冻
refrigerator n.冰箱，冷藏库
refuge n.避难，庇护；庇护者
refugee n.难民，流亡者
refulgence n. 辉煌，光亮
refulgent adj. 辉煌的，灿烂的
refund n. 偿还
refurbish v. 刷新，擦亮
refusal n.拒绝
refuse vt.拒绝 vt.拒绝
refutation n. 反驳,辩驳,反驳的言论或意见
refute vt.驳斥，反驳，驳倒
regain vt. 恢复,重回,复得
regal adj. 帝王的，华丽的
regale v. 款待，使…享受
regard vt.把…看作；尊敬
regard...as... 认为…是…
regarding prep.关于
regardless ad.不顾一切地
regards n. 问候；致意
regatta n. 赛舟会
regency n. 摄政统治,摄政权,摄政统治区
regenerate adj. 改过自新的，新生的
regeneration n. 再生
regenerative a.新生的；回授的
regent n. 摄政者（代国王统治者）
regicide n. 弑君,大逆,大逆者
regime n.政体，政权；制度
regimen n. 养生法，生活规则
regiment n.团，军团；一大群
regimental a. 团的,附属于团的
regimentation n. 严格控制，纪律
region n.地区，地带；领域
regional adj. 地区的，区域的；地方的，局部的
regionalization n. 区域化
regionalize v. 使区域化
register n.&vt.登记，注册
registered adj. 登记的，注册的；挂号的
registrant 注册人，登记者
registrar n. 记录者,登记者,登记官员
registration n. 登记,挂号,注册
registry n. 记入,登记,登记名册
regress n.退回,后退,逆行; 回归
regression 回归，经济衰退
regressive adj. 退步的，退化的
regret vt.&vi.遗憾，抱歉
regretful a. 惋惜的,遗憾的,哀惜的
regretfully adv. 遗憾地
regrettable adj.可后悔的；可惜的；可遗憾的
regular a.规则的；整齐的
regularity n.规则性；整齐
regularly adv. 规则地；经常地；定期地；有规律地；整齐地
regulate vt.管理，控制；调整
regulation n.规章，规则；调节
regulator n.调节
regulatory a.按规定的
rehabilitate v. 修复恢复（职位等）
rehabilitation n. 恢复
rehearsal n.排练，排演；练习
rehearse vt. 预演,排演,使排练,复述,背诵,
rehypothecate 转抵押
reign n.支配；朝代；统治；王朝；统治时期，王朝领域；称王v. 统治，盛行；支配；占优势
reigning a. 在位的
reimbursable 可补偿的
reimburse v. 偿还
reimbursement n.还款；偿付，补偿；偿还(的款项)
reimplant v. 再植入
rein n.缰绳 vi.驾驭，控制
reincarnate v. 使化身，转生
reincarnation n. 化身，转世的生命
reindeer n. 驯鹿
reindex v. & n. 变换(改变)符号
reinforce vt.增援，支援；加强
reinforcement n.加强,强化,增援
re-insert vt. 重新插入
reinstate v. 恢复（原职）
reinsurance 再保险，分保，转保
reiterate v. 重申，反复地说
reive vt.vi. 掠夺
reject vt.抛弃；拒收
rejected 拒付，退回
rejection n. 拒绝,抛弃,驳回,呕出物,排泄物,
rejoice vi.欣喜，高兴
rejoicing n. 欢庆，欢欣；高兴；(pl.)欢呼；欢乐，狂喜
rejoin v. 回答，答辩
rejoinder n. 回答
rejuvenate v. 使返老还童，回春
rejuvenator n. 使返老还童的人,返老还童药,
rekindle v. 重新点燃
relapse n./v. 旧病复发，再恶化
relate vt.叙述；使联系
related adj. 有亲缘关系的；与…有关的；叙述的；有联系的；相关的
relation n.关系，联系；家属
relationship n.关系，联系
relative a.有关系的；相对的
relatively adv. 比较地，相对地
relativity n. 相互依存；相对性；相关性
relax vt.&vi.(使)松驰,放松
relaxation n.松驰，放松；休息
relaxed adj. 轻松的；松懈的，不拘束的
relay vt.分程传递；使接替
relearn v，重新学习
release vt.释放；放松；发表
relegate v. 降级，贬谪
relent v. 动怜悯心，减弱
relentless adj. 无情的，残酷的
relevance n. 中肯,适当
relevancy n. 切题；中肯
relevant a.有关的，贴切的
reliability n.可靠性
reliable a.可靠的，可信赖的
reliance n.信任，信赖，信心
relic n. 遗物，遗迹
relics 崩溃
relict adj. 残存的
relief n.宽慰；欣慰
relieve vt.减轻，解除；救济
relieve...of 使解除
relieved 免除的；放心的
religion n.宗教；宗教信仰
religious adj.宗教的；虔诚的
relinguish vt.放弃；撤回
relinquish v. 放弃，废除
relinquishment n.放弃；撤回；停止
relish n./v. 味道，喜好，享受
reload vt. 再装
reluctance n. 不愿,勉强,厌恶
reluctant a.不愿的，勉强的
reluctantly ad. 勉强地；a. 不情愿地；勉强地
rely vi.依赖，依靠；信赖
remain vi.保持，仍是；剩下
remainder n.剩余(物)；余数
remaining a.剩余的
remains n.剩下的东西，残余
remand n. 送还,还押
remark vt.&vi.&n.评论，谈论
remarkable a.异常的，非凡的
remarkably ad. 非凡地；显著地
remarry vi.再婚；再娶；再嫁
remediable adj. 可纠正的，可治疗的
remedial a. 治疗的,补救的,矫正的
remedies 法律补偿
remedy n.&vt.治疗；补救
remember vt.记得，想起；记住
remembrance n. 记得，记忆(力)；回忆
remembrancer n. 纪念品,提醒者
remind vt.使想起
reminder n. 提醒的人,暗示
reminisce v. 追忆，怀旧
reminiscence n. 回想，追忆，（复）回忆录
reminiscences n. pl. 回忆录
reminiscent a. 回忆的,怀旧的
remiss adj. 疏忽的，不留心的
remission n. 宽恕，赦免
remit v. 免除，宽恕，汇款
remittance n. 汇款
remittee 汇款领取人
remittent adj. (病)间歇性的，忽好忽坏的
remitter 汇款人
remnant n. 残余物，零头布料
remodel v. 重建，改变形状
remonstrance n. 抗议，抱怨
remonstrate v. 抗议，规劝
remorse n. 懊悔，悔恨
remorseful a. 极为后悔的,懊悔的
remorseless a. 无慈悲的,冷酷的,不知过错的
remote a.相隔很远的；冷淡的
remoteness n. 遥远，疏远
remould vt. 改造；再铸
remount vi. 再骑上,回溯
removal n.移动；迁移；除掉
remove vt.移动，搬开；脱掉
remover n. 移转者,搬家公司,剥离剂
remunerate v. 报酬，补偿；酬劳；给…补偿
remuneration n. 报酬
remunerative adj. 报酬高的，有利润的
Renaissance n. 复兴，再生
renal a. 肾脏的
rename vt. 重新命名,再命名,改名
renascence n. 新生，复活，复兴
renascent adj. 再生的，复活的；新生的
rend v. 撕裂，猛拉
render vt.表示，给予；使得
rendering n. 演出，翻译
rendezvous n. 约会，约会地点，会合
rendition n. 翻译,描写,施舍,表演
renegade n. 叛教者，叛徒
renege v. 背信，违约
renew vt.使更新 vi.更新
renewable adj. 可续期的
renewal n. 重新获得，更新
renin n. 肾高血压蛋白酶
renounce v. 宣布放弃，抛弃
renovate vt. 更新,革新,恢复,修复,刷新
renovation n. 革新,刷新,修理
renown n. 名望；声誉vt. 使有名望
renowned adj. 著名的；有名的，有声望的
rent n.租金，租 vi.出租
rental n. 租费
renter n. 承租人,佃户,债主
renunciation n. 放弃，抛弃
reopen vt.vi. 重开,再开始,再开
reorder v.(按序)排列，排序
reorganization n. 改组,再编制,改造
reorganize vt.vi. 改组,再编制,改造
repaint vt. 重画
repair vt.&n.修理，修补
repairer  n. 修理者; 修补者
repairmen n. 修理，修补，纠正
reparable adj. 能补救的，可挽回的
reparation n. 赔偿，补偿
repartee n. 机灵的回答
repass vt.vi. 再经过,再通过
repast n. 餐,食量,就餐
repatriate v. (自异国)遣返
repay vt.&vi.偿还，报答
repayment n. 偿付
repeal vt.撤销；放弃 n.撤销
repeat vt.重说，重做 n.重复
repeated a. 反复的；重复的
repeatedly ad.重复地；一再
repeating n. 重复，循环
repel vt.拒绝；使厌恶
repellent adj. 令人厌恶的
repent vi.悔悟，悔改vt.后悔
repentance n. 悔恨
repentant adj. 对…感到悔恨的
repercussion n. 反应，影响，回声
repertoire n. （剧团等）常备剧目
repetition n.重复，反复
repetitive adj. 重复的，反复的
repine v. 不满，心中抱怨
replace vt.把…放回；取代
replaceable a.可替换的
replacement n.归还；取代；置换
replant vt.改种,移植,使移居
replenish v. 补充，再装满
replenishment n. 补充(货物)
replete adj. 饱满的，塞满的
repletion n. 充满，吃饱
replica n. 复制品
replicate vt. 重复，复制
replication n. 回答；反响；答辩
reply vt.&n.回答；答复
report vt.,vi.&.n.报告,汇报
reportage n. 报告文学
reporter n.记者
reporting 申报，报道
repose v. 躺着休息，安睡
repository n. 贮藏室，仓库
repossess v. 取回，收复
reprehend v. 谴责，责难
reprehensible adj. 应受谴责的
represent vt.描绘；代表；象征
representation n.描写；陈述；代表
representative a.代表性的 n.代表
repress v. 抑制，镇压
repression n. 抑制,抑压,制止
repressive adj. 镇压的，残酷的
reprieve n./v. 缓刑，暂时解救
reprimand n./v. 训诫，谴责
reprint n. 再版,翻版,重印
reprisal n. （政治或军事的）报复
reproach vt.&n.责备，指责
reproachful a. 申斥的,非难的,应责备的
reprobate v. 谴责，指责 n./adj. 堕落的（人）
reprobation n. 非难,叱责,排斥
reproduce vt.&vi.繁殖，生殖
reproduction n.再生(产)；繁殖
reproductive a. 生殖的
reproof n. 斥责，责备
reprove v. 责骂，申斥
reptile n.爬行动物；两栖动物
reptilian adj. 爬虫类的，卑下的
republic n.共和国
republican a.共和国的
republication n. 再版,翻版,再发布
repudiate v. 拒绝，抛弃
repudiation n. 抛弃,否认,拒付
repugnance n. 嫌恶，反感
repugnant adj. 令人厌恶的
repulse v./n. 驱逐，击退，厌恶
repulsion n. 击退,反驳,反感,排斥
repulsive adj. 令人厌恶的，驱逐的
reputable adj.名誉好的，有声望的
reputation n.名誉，名声；好名声
repute n. 名望,名气,声望
request n.&vt.请求；要求
requested 被请求的
requiem n. 安魂弥撒
require vt.需要；要求
required a. 需要的
requirement n.需要；要求
requisite a.需要的 n.必需品
requisition n. 要求，请求
requital n. 酬劳，报答.
requite v. 报答，报复
reread vt. 重读，再读
re-read vt. 再读
rescind v. 废除，取消
rescission n. 废止,取消,使无效,撤消
rescript n. 公告，法令，重抄
rescue vt.&n.营救；援救
rescuer n. 救助者
research n.调查；研究
researcher n. 调查者；探究者；研究人员
resemblance n.相似，相似性
resemble vt.像，类似
resent vt.对…不满，怨恨
resentful adj. 愤恨的,气愤的,愤慨的,愤怒的
resentment n. 憎恨
reservation n.保留；预定，预订
reserve vt.储备，保留；预定
reserved adj. 保留的，预订的；预备的；说话不多的
reservoir n. 水库
reset vt. 重新安置；置“0”；使复位；重接(断骨)；重复试验
reshipment 重新装运
reshuffle v. 再洗牌，改组
reside vi.居住，驻扎；属于
residence n.居住；驻扎；住处
resident a.居住的 n.居民
residential a. 住宅的,与居住有关的
residual a.剩余的；残数的
residue n. 剩余（财产）
resign vt.使顺从，使听任于
resignation n.听从，屈从，顺从
resigned adj. 逆来顺受的，顺从的
resilience n. 弹性，弹力
resilient a. 弹回的,有弹力的,愉快的
resin n. 树脂
resist vt.&vi.抵抗；抵制
resistance n.抵抗；抵制；抵抗力
resistant a.抵抗的，反抗的
resistless a. 不能抵抗的,无抵抗力的
resolute a.坚决的，果敢的
resolutely adj. 坚决地，果断地；ad. 坚决地；果断地
resolution n.坚决，坚定；决定
resolve vt.解决；决心 n.决心
resolved a.有决心的；决心的；坚定的
resonance n. 回响，共鸣
resonant adj. （声音）洪亮的，共鸣的
resort vi.&n.求助，凭借
resound vi. 回响,鸣响,传遍,驰名
resounding a. 洪亮的
resource n.资源
resourceful a. 策略的,机智的,资源丰富的
resources 资源，物资，物(财)力
resourse n. 资源
respect n.&vt.尊敬，尊重
respectability n.体面，正当
respectable a.可敬的；人格高尚的
respecter n. 趋炎附势者，尊敬者
respectful a.恭敬的，尊重的
respectfully adv. 恭敬地
respecting prep. 关系,说到
respective 各自的，各个的
respectively adv. 分别地；各自地，各自，个别地
respiration n. 呼吸
respirator n.呼吸器
respiratory a. 呼吸的
respire vt.vi. 呼吸
respite n. 休息，中止，暂缓
resplendence n. 灿烂，辉煌
resplendent adj. 华丽的，辉煌的
respond vi.作答；响应
respond...to 有反应
respondent n. 被告
response n.作答，回答；响应
responsibility n.责任，责任心；职责
responsible a.重要的；可靠的
responsive adj. 敏感的，反应快的
respose n. 回答，响应
ress
rest vi.&vt.(使)支撑(在)
restart v. 重新启动，再启动
restaurant n.餐馆，饭店，菜馆
restful a. 给人休息的,平安的,安静的
restitution n. 归还，赔偿
restive adj. 不安静的，不安宁的
restiveness n. 不安宁，不满足
restless a.不安定的，焦虑的
restlessly ad. 不安定地；烦躁地
restock v. 重新进货
restoration n. 恢复
restorative adj. 恢复健康的，恢复的
restore vt.恢复；归还；修补
restorer n.使恢复原状之人
restrain vt.抑制，制止，遏制
restraint n.抑制；遏制；克制
restrict vt限制，限定，约束
restricted a. 受限制的，受约束的
restricting n. & a. 限制(的)
restriction n.限制，限定，约束
restrictive n. 限制的
restructure vt. 调整，重新组织
result n.结果；效果
resultant a.作为结果而发生的
resulting a. 结果的，合成的
resume n.(谋职者的)个人简历
resumption n. 重新开始
resurgence n. 复兴，再起；复活
resurgent adj. 再起的，复活的.
resurrect v. 使复活，挖出
resurrection n. 复活
resuscitate v. 使复活，使苏醒
ret v. 沤麻，沤软； (干草等)受潮腐烂
retail n.零售 a.零售的
retailer n. 零售商
retain vt.保持，保留，保有
retainer n. 家臣,扈从,保持者
retake vt. 再取,取回,重摄
retaliate v. 报复，反击
retaliation n. 报复,报仇
retaliative 报复性的
retard vt.延迟，放慢
retardant n. 阻化剂
retarded adj. 智力迟钝的
retch vi. 作呕，恶心；n. 恶心
retell vt.再讲，重述，复述
retention n. 保留，保持
retentive adj. 有
reticence n. 无言,沉默,谨慎
reticent adj. 沉默不语的
reticulated a. 网状的,vt.vi. (使)成网状
reticulation n. 网目，网状
retina n. 视网膜
retinue n. 侍从，随员
retire vi.退下；引退；就寝
retired adj. 退休的；通职的
retirement n.退休，引退；退隐
retiring adj. 隐居的，不喜社交的
retort vt.&vi.反击；反驳
retouch vt.vi. 润饰,修正
retrace v. 回顾，追想
retract v. 缩回，收回
retracted a.可伸缩的
retraction n. 缩进,取消,撤回
retreat vi.(被迫)退却，后退
retrench v. 节省，削减
retrenchment  n. 削减,减少支出,节约
retribution n. 报应，罚
retributive adj. 报应的
retrieval n. 取回，补偿
retrieve v. 寻回，取回，挽回（错误）
retroactive a. 反动的,追溯的,有追溯力的
retrograde adj. 后退的，v. 倒退
retrogress v.退化，有追溯效力的，倒行的；倒退
retrospect n. 反顾，回顾
retrospection n. 回顾,追忆,考虑
retrospective adj. 追想的，回顾的
retry vt. 再试，复算
return vi.&n.回来，返回
returned a. 退回的
reunion n. 团圆,重聚
reunite vt.&vi.重新统一
re-united a. 重新团聚的
revaccinate vt. 再给…接种疫苗
revaluation 升值，重估价
reveal vt.展现；揭示，揭露
revel n. 作乐,狂欢,宴会
revelation n. 显示，泄露的事实
reveler n. 揭露者，展示者
revelry n. 狂欢
revenge vt.替…报仇 n.报仇
revengeful a. 报复的,深藏仇恨的
revenue n.收入；收入数目
reverberant adj. 起回声的
reverberate v. 起回声，反响
reverberation n. 反响,混响,反射
revere vt. 崇敬,敬畏,尊敬
reverence n. 崇敬，敬礼
reverend n. 教士,神职人员,牧师
reverent adj. 恭敬的，虔诚的.
reverential a. 虔诚的,表示尊敬的,充满崇敬心的
reverie n. 幻想，梦幻曲，白日梦
reversal n. 翻转,颠倒,反转
reverse vt.颠倒，翻转 n.背面
reversion n. 返回（原状，旧习惯），逆转
revert vi. 恢复,复归,回复
review vt.再检查 n.复习
reviewer n. 评论家,批评家,书评家; 评论杂志
revile v. 辱骂，恶言相问
revise vt.修订，校订；修改
revision n. 校订,修正,修订本
revisionism n. 修正主义
revisionist n. 修正主义者；a. 修正主义的
revisit vt. 再访,重游,重临
revitalize v.重新活跃，恢复元气，重新调整； 使复活
revival n. 苏醒；复兴
revive vt.&vi.苏醒；复兴
revocable adj. 可废除的，可撤销的
revocation n. 废弃，取消
revoke v. 废除，取消
revolt vi.&n.反抗，造反
revolting adj. 令人厌恶的
revolution n.革命；旋转，绕转
revolutionary a.革命的 n.革命者
revolutionist n. 革命家
revolutionize vt. 鼓吹革命,大事改革
revolve vt.&vi.(使)旋转
revolver n. 连发左轮手枪
revolving 循环的，周转的
revulsion n. 收回，抽回
reward n.报答；报酬 vt.奖赏
rewarding adj. 有收获的；有报酬的，值得做的
rewrite vt.重写；改写
rhapsodize v. 过份赞美
rhapsody n. 溢美之词，狂想曲
rheostat n. 可变电阻器
rhetoric n. 修辞学，浮夸的言语
rhetorical a. 修辞学的,符合修辞学的,修辞的
rhetorician n. 修辞学者,雄辩家
rheum n. 发炎性分泌物,鼻粘膜炎,感冒,
rheumatic a. 风湿症的,患风湿症的,引起风湿症的
rheumatism n. 风湿症
rheumy adj. 阴冷的
rhine n. 莱因河(欧洲西部)
rhinestone n. 莱茵石；水晶石
rhinitis n. 鼻炎
rhinoceros n. 犀牛
rhododendron n. 杜鹃属的植物
rhubarb n. （植物）大黄，n./v. 喧闹
rhyme n. 韵,押韵,韵文
rhythm n.韵律，格律；节奏
rhythmic adj. 有节奏的
rhythmical a. 有节奏的；有韵律的
rib n.肋，肋骨
ribald adj. 下流的，粗鄙的
ribaldry n. 下流,猥亵的话
riband  n. 『古』 (装饰用之) 缎带,丝带
ribbed n. 呈肋状的；有罗纹的
ribbon n.缎带，丝带；带
rice n.米饭；大米
rich adj.有钱的，富裕的
richardson n. 理查森(姓)
riches n.pl. 财富,财产
richly ad. 富裕地；浓厚地
richness n. 富裕,丰富,肥沃
rick n. 干草堆
rickets n. 软骨病,佝偻病,驼背
rickety adj. 摇摇晃晃的，不牢固的
rid vt.使摆脱，使去掉
riddance n. 摆脱,除去,驱逐
ridden ride的过去分词；骑
riddle n.谜，谜语
ride vt.&vi.骑(马,自行车)
rider n.骑马的人；乘车的人
ridge n.脊；岭，山脉；垄
ridicule vi. & n. 嘲弄，挖苦；嘲笑；奚落；讪笑；荒谬
ridiculous a.荒谬的，可笑的
rife adj. 流行的，普遍的
rifle n.步枪，来复枪
rift n. 裂口；不和；裂缝；隙缝；空隙；分裂
rig n./v. 欺骗，舞弊，伪造
right adv.正好，恰恰
righteous a. 公正的,正义的,正直的
righteousness n. 正义,公正,正直
rightful a. 合法的,正直的,当然的
right-hand a. 右手的，右边的
right-handed a. (惯)用右手的
rightly ad. 应该；正义地；正确地
rigid a.刚硬的；僵硬的
rigidity n. 固执，坚定，僵化
rigidly ad. 坚硬地；不易弯地
rigmarole n. 冗长无聊的废话
rigor n. 严厉，酷厉
rigorous a.(性格等)严峻的
rigour n. 严格,严厉,苛刻,精确,严密,
rik 里克(男名)
rill n. 小河
rim n.边；边缘，(眼镜)框
rime n.白霜,霜
rind n. （西瓜等）外皮
ring n.环形物(如圈、环等)
ring...up 给…打电话
ringed a. 带环的；戴戒指的
ringer n. 套环,投环,按铃者,敲钟者
ringleader n. 魁首
ringlet n. 卷发
ring-shaped a. 圆形的
rink n. 溜冰场；冰球场；vi. 溜冰
rinse v. 漂洗，润丝；冲洗；轻洗；涮；嗽；以清水冲洗
riot n.&vi.骚乱，暴乱
rioter n. 暴民,暴徒,喝酒狂闹的人
riotous adj. 暴乱的，蛮横的
rip vi.撕啐，扯破，划破
ripe a.熟的；时机成熟的
ripen vt.使熟 vi.成熟
ripeness n. 成熟,圆通,完成
ripple vt.&vi.(使)起细浪
rired 疲劳的
rise vi.起立；升起；上涨
risen rise的过去分词；增长；升高
risible adj. 可笑的，引人发笑的
risk n.风险，危险，冒险
risk-taking a.冒险的
risky a. 危险的
risque adj. 下流的，淫猥的
rite n. （宗教的）仪式
ritual n. 仪式，
rival n.竞争者 a.竞争的
rivalry n. 敌对,竞争,对抗
rive v. 散开，劈开
river n.江，河
riverside n.河边
rivet n. 铆钉v. 吸引（注意力）
riveting adj. 非常精彩的
rivulet n. 小溪，小河
rna 核糖核酸
roach n. 蟑螂
road n.路，道路，公路
roadside n.路边 adj.路边的
roadstead n. 『航海』 (港外的船的) 停泊处
roadster n. 跑车,流浪者
roadway n. 车道,道路,轨道
roam vt.在…漫步，漫游
roan adj. 杂色的；n. (装订书用)柔软羊皮
roar vi.吼叫；呼喊 n.吼
roaring n. & a. 怒吼(的)，轰鸣(的)
roast vt.&vi.烤，炙，烘
roasted a.烤好的
roaster n. 炙烤的人,烘烤器,红烧烤炉
rob vt.掠夺；抢劫
robber n.强盗，盗贼
robbery n.抢劫，劫掠，盗取
robe n.长袍；上衣
robert 罗伯特(男名)
robin n. 欧鸲；知更鸟
robinson 鲁滨逊(姓)
robot n.机器人
robust adj. 健壮的
rock vt.摇，使动摇 vi.摇
rock-bottom n. & adj. (价格)最低(的)
rocket n.火箭，火箭发动机
rocking adj. 摇动的
rocky a. 岩石的,多石的,象岩石的,摇晃的,
rococo n. 洛可可
rod n.杆，竿，棒
rode ride的过去式；n. 骑
rodent n. 啮齿类动物（如鼠等）
rodeo n. 牧马骑术表演
rod-shaped a. 杆状的
roe n. 鱼卵
rogue n. 恶棍,流氓,小淘气
roguish adj. 捣蛋的，无赖的
ROI (=return on investment)投资收益率/利润率
roil v. 搅浑，激怒
role n.角色，作用，任务
roll vi.打滚；滚动
roller n.滚柱，滚筒，滚轴
rollerblade v.滑旱冰(用旱冰鞋滑)
roller-skate vi. 用滚轮溜冰
rollick vi.n. 欢闹
rollicking adj. 欢乐的
rolling a. 摇晃的；n. 滚动；打滚
Roman n.古罗马人 a.罗马的
romance n.传奇；浪漫文学
romancer n. 传奇小说作家,讲虚构故事的人
Romanesque adj. 罗马式的
romantic a.浪漫的；传奇的
romanticism n. 浪漫精神,浪漫主义
romanticize vt. 使浪漫化
Rome n.罗马(意大利首都)
romp n. 轻易取胜
rood n.十字架上的基督像
roof n.屋顶；顶，顶部
roofing n. 屋顶盖法
roofless a. 无屋顶的,无家的,无屋可住的
rook n. 白嘴鸦；赌棍；vt. 骗；(国际象棋的)车
rookie n. 新兵，新球员
room n.房间
roommate n. 室友
roomy a. 广阔的,宽敞的,宽大的
roost n./v. 栖息，鸟巢
rooster n.公鸡；狂妄自负的人
root n.根，根子 vi.生根
rope n.绳子
rosary n. 玫瑰园,玫瑰花坛
rose n.玫瑰花
roseate a. 玫瑰色的
rosebud n. 蔷薇花蕾,妙龄少女
rosemary n. 迷迭香
rosette n. 蔷薇结,蔷薇花饰,装饰圆窗
rosewood n. 紫檀,香水
rosin n. 松香,树脂
ross n. 树皮上粗糙带鳞状的表皮
roster n. 值勤表，花名册
rostrum n. 讲坛
rosy a. 美好的；乐观的；玫瑰色的
rot vi.&vt.(使)腐烂
rotary a.旋转的，转动的
rotate vt.&vi.(使)旋转
rotation n. 旋转，转动；循环；更替；交替；自转
rotator n. 旋转机
rotatory a. 回转的,使回转的,轮流的
rote n. 死
rotor n. 转子
rotten a.腐烂的，发臭的
rotund adj. (人)圆胖的，(音声)洪亮的
rotunda n. 圆形建筑,圆形大厅
rotundity n. 球状,圆形,圆形物
rouble n. 卢布
rouge n. 胭脂，口红
rough a.表面不平的；粗略的
roughage n. 粗饲料,粗粮
roughen vt.vi. (使)变粗糙
roughly adv. 粗暴地；粗糙的；粗野地；粗鲁地；大致地；大约地，粗略地；毛糙地；大体上
roughness n. 粗糙,凹凸面,篷乱的毛发
roulette n. 轮盘赌,点线机,转迹线
round prep.围(绕)着
roundabout a.迂回的；转弯抹角的
roundelay n. 反复的小调,圆舞之一种,小鸟的鸣啭
roundish a. 圆的
roundsman 推销员
roundup n. 驱集,召募,被驱集一起的家畜
roup vt. 拍卖；n. 拍卖
rouse vt.唤醒，唤起；惊起
rout n. 大败，溃败
route n.路；路线
routine n.例行公事 a.日常的
rove v. 流浪，漂泊
rover n. 漂泊者,流浪者,海盗
row n.(一)排，(一)行
rowboat n.有桨的船；划船
rowdy adj. 吵闹的，粗暴的
rowel n. 马刺前端的小齿轮,排脓条
rower n. 划手
roy 罗伊(男名)
royal a.王的；皇家的
royalist n. 保皇党员,君主支持者,顽固分子
royalty n.皇家，王族，皇族
rub vt.&vi.摩擦
rubber n.橡皮
rubberized  adj.涂敷或灌入橡胶的
rubbery adj. 强韧的
rubbish n.垃圾，废物；废话
rubble n. （一堆）碎石，瓦砾
rubella 风疹
rubicund adj. （脸色）红润的
rubric n. 红字,红色印刷,题目
ruby n.红宝石
ruck n. 皱褶，普通群众，大量；一堆，一群vt. 弄皱；
rucksack n. (旅行等的)背包
rudder n. 船舵，领导者
ruddy adj. （脸色）红润的，红色的
rude adj.无礼的；粗鲁的
rudely ad. 粗鲁地，原始地；粗略地
rudeness  n. 无礼; 粗野; 粗暴; 野蛮; 未加工; 猛
rudiment n. 基本原理
rudimentary adj. 初步的，未充分发展的
rudiments n. 基础知识，入门
rue n. 后悔，遗憾.
rueful adj. 后悔的，遗憾的
ruff n. 出王牌,环状领
ruffian n. 恶棍，歹徒. adj. 残暴的
ruffle v. 变皱，弄皱，激怒
rug n.小地毯；毛毯
rugby n. 橄榄球
rugged a. 崎岖的；不平的
ruin n.毁灭；废墟 vt.毁坏
ruined a.破坏的；毁坏
ruinous a. 破坏性的,招致毁灭的,零落的
rule n.规则；规定
ruler n.尺
rulers 尺
ruling adj. 统治的；流和的，现有的
rum n. 甜酒
rumble v. 发隆隆声；隆隆地进行
rumbling a. 隆隆响的
ruminant n. 反刍动物adj. 反刍类的，沉思的
ruminate v. 反刍，再嚼，深思
rumination n. 反刍,沉思,默想
ruminative adj. 沉思默想的
rummage n. 翻寻
rummaging 海关检查，撤清底货
rumor n. 谣言；传闻；vt. 谣传
rumour n.谣言，谣传，传闻
rump n. 尾部,臀部
rumple v. 弄皱，弄乱
run v.跑
runabout n. 轻便汽车,流浪者
runagate n. 游民,游荡者,逃亡者
runaway n. 逃走的人,逃亡,亡命者
run-down a. 破旧的
rund-raising n.资金募集(工作)；募揖(活动)
rung n. 脚蹬横木,横档,车辐,棍子
runnel n. 小河,细流
runner n.赛跑的人
running n. 跑步；经营；adj. 连续的；奔跑的；流动的；运行着的，游动的
running-up 亚军
runtime n. 运行时间
runway n.飞机跑
rupture n./v. 破裂，断裂
rural a.农村的，田园的
ruse n. 诡计adj. 狡猾的
rush vi.冲，奔 vt.催促
rushed adj. 繁忙的
russet a. 枯叶色的,红褐色的,手织的
Russia n.俄国；俄罗斯
Russian a.俄罗斯的 n.俄国人
rust n.锈 vi.生锈，氧化
rustic adj. 乡村的，乡土气的
rusticate n. 过乡间生活
rusticity n. 乡村式,田园生活,质朴
rustle vi.(树叶等)沙沙响
rustler n. 偷牛(马)贼
rusty a.生锈的；变迟钝的
rut n. 常例，老一套
ruth n. 同情；悔恨
ruthless a.无情的，冷酷的
ruthlessly ad. 无情地
rye n. 裸麦,黑麦,绅士
s.s. n. (缩)轮船
Sabbath n. 安息日
sabbatical a. 安息日的
saber n. 军刀,骑兵,骑兵队
saber-toothed a. 长着锐利的长犬牙的
sable n. 黑貂，adj. 黑色的
sabotage n. 阴谋破坏，颠覆活动
sabre n. 军刀，击剑用刀
sac n. 囊
saccharin n. 糖精
sacerdotal a. 僧侣的,祭司的,祭司制度的
sachem n. 酋长,Tammany 派的干部,政党领袖
sachet n. 小袋，小香袋
sack n.袋，麻袋；开除
sackbut n. 低音喇叭,竖琴的一种
sackcloth n. 制袋用粗麻布,粗布衣,麻衣
sacrament n. 圣礼，圣事
sacramental  adj. 圣礼的,圣事的,秘迹的,圣典的,圣
sacred a.上帝的；神圣的
sacredness n. 神圣不可侵犯性
sacrifice n.&vt.牺牲；南祭
sacrificial a. 牺牲的,献祭的,具有牺牲性的
sacrilege n. 亵渎圣物,冒渎,悖理逆天的行为
sacrilegious adj. 亵渎神圣的
sacrosanct adj. 神圣不可侵犯的
sad adj.悲哀的
sadden vt. 使忧愁,使悲哀
saddle n.鞍子，马鞍
saddler n. 制造马鞍的人,马具商,乘用之马
sadistic a. 虐待狂的,残酷成性的
sadly adv. 难过地，悲哀地；痛心的；伤心的；悲痛地，可惜；凄惨地；忧愁地悲哀地
sadness n.悲痛，悲哀
safari n. 狩猎旅行，长途考察
safe adj.安全的
safe-conduct n. 安全通行权
safeguard n.保护措施；护照
safely adv. 安全地；平安地；可靠地；平安地；确实地
safety n.安全，保险
saffron n. 番红花,此花的花茎,番红花色
sag v. 下陷，下垂，消沉
saga n. 英勇故事，长篇小说
sagacious adj. 聪明的，睿智的
sagacity n. 聪慧，洞察力
sage adj. 智慧的n. 智者
sago n. 西米,西米椰子
said adj. 上述的，该；say的过去式(分词)；(法律、商业文件等用语)上述的，该…；说
sail vi.航行
sailboat n. 帆船
sailing adj. 启航的；n. 航行；驶行，航海，开航
sailor n.水手，海员，水兵
saint n.圣徒；基督教徒
saintly a. 圣洁的
saith says的古体
sake n.缘故，理由
salability n. 适销性
salable adj. 有销路的，适销的
salacious adj. 好色的，淫荡的
salacity n. 好色，淫荡
salad n.色拉；莴苣，生菜
salamander n. 火蜥蜴,火怪,耐火的人
salary n.薪金，薪水
sale n.卖，销售
sales n. 销售；销售额；adj. 出售的
salesgirl n. 女售货员
salesman n.售货员，推销员
salesmanship  n. 推销技术,销货术
saleswoman n. 女售货员,女店员
salicin n. 柳醇，水杨甙
salient adj. 显著的，突出的
saliferous adj. 含盐的，产盐的
saline a. 盐的,苦涩的,由碱金属或含镁之盐类而成的
salinity n. 盐浓度，盐分
saliva n. 唾液，口水
salivary a. 唾液的,分泌唾液的
sallow n. 柳树，adj. 病黄色的
sally n. 突击,出击,远足
salmon n.鲑，大马哈鱼
salon n. 沙龙，(法国等大邸宅的) 大厅,客厅
saloon n. 大厅,展览场,酒吧,大会客室
salsify n. 波罗门参
salt n.盐
saltatory adj. 跳跃的; 舞蹈的
saltpeter n. 硝石
saltpetre n.硝石
salt-shaker n.盐瓶
salty adj. 咸的；盐的
salubrious adj. 有益健康的
salutary adj. 有益的，有益健康的
salutation n. 致敬，（信开头）称呼
salute vi.,vt.&n.敬礼；致敬
salution n. 致敬
salvage n./v. （从灾难中）抢救，海上救助
salvation n. 得救，拯救
salve n. 药膏，v. 减轻，缓和
salver n. 盘子,盆子
Samaritan adj. 撒马利亚的
same adj.同样的
samisen n. 三弦琴
sammy 萨米(男名)
sampan n. 舢板,小船
sample n.样品；实例，标本
sampler n. 刺绣花样，取样员
sampling n. 抽样
samurai n. (日本封建时代的) 武士
sanatorium n. 疗养院，休养所
sanctification n. 神圣化,灵化,使神圣
sanctify vt. 使神圣,奉献给神,使成为神圣之物
sanctimonious adj. 伪装虔诚的
sanction n./v. 批准，认可
sanctity n. 神圣,尊严,圣洁
sanctuary n. 圣堂，避难所
sanctum n. 圣地，密室
sand n.沙，沙地
sandal n. 凉鞋,草鞋,檀香木
sandblast n. 喷沙,喷沙器
sandman ] (传说撒沙于小孩眼睛,将其
sandpaper n. 沙纸
sandpiper n. 矶鹞
sands n. 沙漠
sandstone n. 沙岩
sandwich vt.夹入，挤进
sandy n.沙的，含沙的
sane adj. 神志清楚的，明智的
sang sing的过去式；唱
sangfroid n. 沉着，临危不惧
sanguinary adj. 有血的，血腥的
sanguine adj. 充满希望的，乐观的
sanitarium n. 疗养院,疗养所,静养地
sanitary n. 疗养院；公共厕所；adj. 卫生的，清洁的；神智清楚的，心理健全的
sanitation n. （公共）卫生
sanity n. 神志清楚
sank sink(下沉)的过去式；沉下
sap n.树液
sapid a. 有味道的,风味良好的,有趣味的
sapience n. 贤明，睿智.
sapient adj. 有智慧的
sapless adj. 没有无气的
sapling n. 树苗，年轻人
sapphire n. 青玉，蓝宝石，adj. 天蓝色的.
sappy a. 树液多的,精力充沛的
sapsucker n. 啄木鸟的一种
sara 萨拉(女名)
saracen n. & a. 撒拉逊人(的)
sarcasm n. 讥讽，讽刺，嘲笑
sarcastic adj. 讽剌的
sarcastically ad. 讽刺地
sarcoma n. 肉瘤
sarcophagus n. (精美的)石棺
sardine n.沙丁鱼
sardonic adj. 讽刺的，嘲笑的
sargasso n.马尾藻
sarsaparilla n.『植物』洋菝契
sartorial adj. 裁缝的，缝制的
sash n. 腰带，肩带.
sassafras  n.『植物』察树
sat sit的过去式(分词)；坐
Satan n. 撒旦,魔鬼
satanic adj. 穷凶极恶的
satchel n. 书包，小背包
sate v. 使心满意足，使厌足
sateen n. 棉缎
satellite n.附属物
satiable a. 可满足的
satiate v. 使饱足，生腻
satiation n. 充分满足，饱，足
satiety n. 饱足，满足
satin n. 缎子,假缎
satinwood n. 缎木,缎木木材
satiny adj. 光滑的，柔细的
satire n. 讽剌（作品）
satirical adj. 讽剌的，爱挖苦的
satirist n. 讽刺诗作者,讽刺家,爱挖苦别人的人
satirize vt. 讽刺,挖苦,对...写讽刺文章
satisfaction n.满意；快事；赔偿
satisfactorily adv. 圆满地；令人满意地
satisfactory a.令人满意的，良好的
satisfied 满足的
satisfy vt.使满意；使满足
satisfying a. 令人满意的
satrap n. 太守,总督,暴吏
saturate vt. 使渗透,浸透,使充满,使饱和
saturation n.饱和(状态)；浸透
Saturday n.星期六
Saturn n.农神；土星
saturnalia n. 纵情狂欢
saturnine adj. 忧郁的，阴沉的
satyr n. 好色之徒,森林之神
sauce n.调味汁，酱汁
saucepan n. 长柄而有盖子的深锅子,炖锅
saucer n.茶托，浅碟
saucy a. 傲慢的,莽撞的,活泼的,漂亮的
sauerkraut  n. 泡甘蓝(油菜)菜
saunter n./v. 闲逛，漫步
sausage n.香肠，腊肠
saute  n. 炒菜,煎肉
savage n.野人 adj.野蛮的
savagely ad. 野蛮地；原始地
savagery n. 野性,原始状态,野蛮人
savanna n. 大草原；热带或亚热带之大草原
savant n. 专家，学者，博学之士
save vt.救，挽救
save-all n. 围裙
saver n.救助者,援救者
saving n. 搭救；节约；存款；储蓄a. 保存的；补偿的；储蓄，存款，节约的；挽救的
savings n. 储金
savior n. 救助者,救世主,救星
saviour n. 救助者,救世主,救星
savoir n. 才干；急智；手腕
savor n. 味道，滋味，v. 品尝，欣赏
savory a. 风味极佳的,可口的,味香的
savour n. 滋味,气味,食欲
savoury a. 风味极佳的,可口的,味香的
saw n.锯子 vt.锯，锯开
sawdust n. 锯屑
sawmill n.锯木厂
sawyer n. 锯木匠,漂流水中的树木,食木虫
Saxon n. 撒克逊人
saxophone n. 萨克斯管
say v.说，讲
say"hello"to 向…问好
say"hi"to 向…问好
saying n.话；俗话；谚语
says v. 说(第三人称单数)
scab n. 创口上所结的疤，痂
scabbard n. （刀、剑）鞘，枪套
scabrous adj. 粗糙的
scads n. 大量，巨额
scaffold n. 脚手架（造房时搭的架子）
scalar 标量
scald v. 烫，用沸水消毒n. 烫伤
scalding adj. 滚烫的
scale n.天平，磅秤，秤
scallop n. 扇贝
scalp n. 头皮，战利品v. 击败
scalpel n. 外科手术刀，解剖刀
scaly adj.有鳞的; 鳞状的
scamper v. 奔跑，快跑
scan vt.细看；浏览；扫描
scandal n.丑事，丑闻；耻辱
scandalize vt. 使生反感,使震惊,诽谤
scandalmonger n. 专事诽谤的人,到处传播丑闻的人
scandalous adj. 丢脸的，诽谤性的
Scandinavia  n. 斯堪的那维亚,北欧
scandinavian a. 斯堪的纳维亚的
scanner n. 扫描器
scant adj. 不足的，缺乏的
scantling n. 一点点，少量
scanty a. 缺乏的,仅有的,节省的,狭小的,
scape v. 避开，避免；逃跑，逃脱
scapegoat n. 替罪的羔羊,替人顶罪者,替身
scar n.伤疤，伤痕；创伤
scarab n. 甲虫
scarce a.缺乏的；希有的
scarcely ad.仅仅；几乎不
scarcely...but 不…的…几乎没有
scarcely...when 刚…就…
scarcity n.缺乏，不足，萧条
scare vt.惊吓 vi.受惊
scarecrow n. 稻草人,衣衫褴褛的人
scared adj. 怕；惊慌的，吓坏了的；害怕的，恐惧的
scarf n.围巾，头巾；领带
scarify vt. 乱刺,乱割,松(土),苛责,乱划
scarlet n.猩红色 a.猩红的
scarp n. 悬崖，陡坡
scat int. 嘘!
scathe n./v. 损害，烧焦
scathing adj. 苛刻的，严厉的
scatter vt.使分散 vi.分散
scatterbrain 注意力不集中的人
scattered a. 分散的
scavenge v.(在废物中)寻觅，(动物)食腐肉
scavenger n. 食腐动物，拣破烂的人
sceen 银幕
scenario n. 剧情说明书，剧本
scend vi.(船)被波浪抬起
scene n.(戏剧等的)一场
scenery n.舞台布景；风景
scenic adj.天然景色的
scent n.气味，香味；香水
scentless a. 无气味的,无臭的,遗臭已消失的
scepter n. 笏,节杖,王权
sceptic n. 怀疑论者
sceptical adj. 怀疑的，不相信的
scepticism n. 怀疑论,怀疑主义
sceptre n. 权杖，君权
schedule n.时间表；计划表
schematic adj. 扼要的，图解的
schematize v. 扼要，表示
scheme vt.计划 vi.搞阴谋
schemer n. 计划者,阴谋家,策士
scheming a. 计划的；诡计多端
schism n. 组织分裂
schismatic adj. 分裂的
scholar n.学者(尤指文学方面)
scholarship n.学业成绩；奖学金
scholastic a. 学校的,学校教育的,学者的,
school n.学校
schoolbag n. 书包
schoolbook n. 课本，教科书
schoolboy n. 男学生
schoolchildren n.小学生
schoolfellow n. 同学
schoolgirl n.中小学女学生
schoolhouse n.校舍
schooling n. 教育；学校教育；正规学校教育
school-leaver n. 学校毕业生
schoolman n. 教授,烦琐哲学家,学校教师
schoolmaster n.(男)教师；校长
schoolmate n.同学
schoolmistress n. 女教师；女校长
schoolroom n.教室
schoolteacher n. (中小学)教师
schoolyard n.校园；操场
schooner n. 大酒杯，大篷车
science n.科学
scientific adj. 科学的；科学(上)的
scientifical a. 科学的
scientifically ad. 合乎科学地,学问上,有系统地
scientist n.(自然)科学家
Scifi n.(science fiction的缩略)科幻小说
scimitar n. 弯刀,半月形刀
scintilla n. 一点，丝毫
scintillate v. 闪烁、（淡吐）流露机智
scintillating adj. 才气横溢的
scintillation n.火花的迸出,闪烁
sciolism n. 一知半解的学问
scion n. 嫩芽，子孙
scissors n.剪刀，剪子
sclera n. 巩膜
scoff vt.&vi.嘲笑，嘲弄
scoffer n. 嘲笑者
scold vt.斥责，责备
sconce n. 突出的烛台,头,头盖
scone n. 烤饼
scoop n. 铲子,勺子,独家新闻,口,穴
scooter n. (儿童玩的) 滑行车,踏板车
scope n.范围；余地，机会
scorch vi.烧焦，枯萎；挖苦
scorching adj. 灼热的；酷热的
score n.二十；(比赛)得分
scorn n.轻蔑；嘲笑 vt.轻蔑
scornful a. 轻蔑的
scornfully ad. 轻蔑地，藐视地
scorpion n. 蝎子
Scot n. 估定的款项,税赋
Scotch v. 镇压、粉碎
Scotland n.苏格兰
scots adj. 苏格兰(人)的
scotsman n. 苏格兰人
scott 斯科特(姓)
Scottish a. 苏格兰的,苏格兰人的
scoundrel n. 恶棍
scour v. 四处搜索
scourge n./v. 鞭笞，磨难
scout vt.搜索，侦察，跟踪
scouting n. 童子军活动
scoutmaster n. 童子军领队
scow n. 大型平底船,盘艇
scowl n. 皱眉，怒视，愁容
scramble vi.&n.爬行，攀登
scrap n.碎片；废料 vt.废弃
scrapbook n. 剪贴簿
scrape vt.&vi.&n.刮，擦
scraper n. 刮刀,刮的人
scrappy adj. 好斗的，生气勃勃的
scratch vt.&vi.&n.搔；抓
scrath v. 抓，搔，抓伤；n. 抓痕
scrawl v. 潦草地写，乱涂
scrawny adj. 细而瘦的
scream vi.尖叫；呼啸
screaming a. 发尖叫声的
screech vi.发尖叫声
screed n. 冗长的演说，长篇大论的文章
screen n.屏；屏幕 vt.掩蔽
screw n.螺旋，螺丝 vt.拧紧
screwdriver n. 螺丝起子
screw-top a.有螺旋盖的
scribble v. 乱写、乱涂
scribbler n. 潦草书写的人,三流作家,小文人
scribe n. 书记,抄写员,划线器,作家,作者
scrip n. 便条,纸条,纸片
script n. 手迹,手稿,副本
scriptural a. 圣经的,手稿的,依据圣经的
scripture n.《圣经》；圣书
scrivener n. 代书,公证人,代笔人
scroll n. 卷轴，纸卷，画卷
scrub n.&vt.擦洗，擦净
scrumptious adj.(食物)很可口的，漂亮的
scruple n./v. 顾忌、迟疑
scrupulous adj. 谨慎小心的、细心的
scruting n. 详细检查，仔细观察
scrutinize n. 详细检查，细读
scrutiny n. 细看,仔细检查,监视,选票的复查
scud v. 疾行，疾驶
scuff 拖足而走
scuffle v. 混战，打斗
scull n. 短桨,尾桨,橹
scullery n. 碗碟洗涤处,碗碟储藏室
scullion n. 在厨房里帮忙的仆人
sculpt v. 雕刻
sculptor n. 雕刻家
sculptural a.雕刻的
sculpture n.雕刻(术)；雕刻品
scum n. 泡沫，社会渣滓
scupper n. 排水孔
scurf n. 头屑,皮屑
scurrilous adj. 下流的、恶言毁谤的
scurry v. 急跑，疾行
scurvy adj. 卑鄙的、可鄙的
scutcheon n.饰有纹章的盾
scuttle v. 急赶、疾走，逃辟
scythe n. 大镰刀
sea n.海洋，海
seabed n. 海床
seaboard n. 海岸,沿海地带
sea-chest n. 从海底捞起的箱子
seacoast n. 海岸,沿岸
sea-damaged 海损的
seafarer n. 船员,航海家
seafaring adj. 航海的，跟航海有关的
seafood n.海产品，海鲜
seagull n. 海鸥
sea-horse n.海马
seal n.封蜡；印记 vt.封
sealed a.密封的；封口
sea-level adj. 海平面
sealing-wax n. 封口蜡
seam n.缝口；接缝；骨缝
seaman n.海员，水手；水兵
seamanship  n. 船舶操纵术,航海技术
seamless a. 无缝合线的,无伤痕的
seamstress n. 女裁缝
seamy adj. 黑暗的，恶劣的
seaport n.海港，港市
sear v. （以烈火）烧灼
search vt.在…中搜寻，搜查
searcher n. 搜寻者
searching n. 搜索
search-light n. 探照灯
searing adj. 灼热的
seascape n. 海景
seashore n. 海岸,海滨
sea-shore n. 海岸
seasick a. 晕船的
sea-sick a. 晕船的
seaside n.海滨(胜地)；海边
season n.季，季节，时节
seasonable a. 适合于季节的,合于时宜的,应时的
seasonal a. 季节性的
seasoning n. 调味品，佐料
seat n. 座；座部；座位；中心；席位；所在地，场所；v. 就座；容纳
seated 坐着
Seattle n.(美国城市名)西雅图
seaward n. 朝海的方向
seawater n. 海水
seaweed n. 海草,海藻
seaworthy a. 适于航海的,经得起航海的
sebaceous a. 脂肪的,脂肪质的,分泌脂肪的
secede v. 正式脱离或退出（组织）
secession n. 脱离、退出
seclude v. 和别人隔离
secluded adj. 隐遁的，隔绝的
seclusion n. 隐遁，隔离
seclusive adj. 好隐居的
second num.第二 a.二等的
secondary a.第二的；次要的
secondhand adj. 二手的，间接的
second-hand n.旧的，第二手的
secondly adv.其次；第二(点)
secrecy n. 保密
secret n.秘密
secretarial adj. 秘书的；文书的
secretariat n. 秘书处
secretary n.秘书；书记；大臣
secrete v. 分泌，藏匿
secretion n. 分泌,分泌物,分泌液
secretive a. 保密的；喜欢保密的
secretly ad. 秘密地；隐蔽地
sect n. （宗教等）派系
sectarian a. 宗派的,党派心强的,偏狭的
sectary n. 属于某宗派的人,非教会派的新教徒
section n.切下的部分
sectional a. 部分的,部门的,节的,截面的
sector n. 扇形,尺规,函数尺
secular adj. 世俗的、尘世的
secure a.安心的；安全的
securely ad. 安全地；无疑地
securities  n. 证券，有价证券；债券
security n.安全，安全感
sedan n.色当(法国城市)
sedate adj. 安静的、镇静的
sedative n./adj. （药物）镇静的，镇静剂
sedentary adj. 久坐的，固定不动的
sedge n. 蓑衣草
sedgy a. 蓑衣草密茂的,蓑衣草的
sediment n. 沉淀物，渣
sedimentary a. 沉渣的,沉淀物的,由沉淀物所生成的
sediment-covered a. 沉淀物覆盖的
sedition n. 煽动叛乱
seditious adj. 煽动性的
seduce v. 勾引、诱惑
seductive adj. 诱人的、有魅力的
sedulous adj. 聚精会神的、勤勉的
sedulously ad. 孜孜不倦地
see v.看，看见；了解
see...off 为某人送行
seed n.种子
seeder n. 播种者,播种机,去核器
seed-head n. 种子穗
seedling n. 幼苗
seedsman n. 播种者,卖种子的店铺
seeing see的现在分词；n. 视觉；看见；观看
seek vt.寻找，探索；试图
seem vi.好像，似乎
seeming a. 表面上的；n. 外观
seemingly ad.表面上，外表上
seemly a. 适当的,恰当的,合适的,好看的
seen v. see(看)的过去分词；看见
seep v. （液体等）渗漏
seepage n. 渗出物
seer n. 预言者,先知,幻想家
seesaw n. 跷跷板,上下动
seethe v. 沸腾，汹涌
seething a. 火热的；激昂的
segment n.切片，部分；段，节
segmental a.部分
segregate v. 隔离
segregation n. 种族隔离
seigneur n. 封建领主,君主,诸侯
seine n. 塞纳河(法国北部)；大捕鱼网；拉网
seismic adj. 地震的
seismometer n. 测震表
seize vt.捉，抓；掠夺
seizure n. 捕获,夺取,占领,充公,没收,
seldom adv.很少；不常
select vt.&vi.选择；挑选
selected a. 精选的
selection n.选择，挑选；精选物
selective a. 有选择性的
self n.自我，自己
self-assertion n. 坚持己见，自信
self-confidence n. 自信
self-conscious adj. 感到很不自然
self-containment n. 不合群
self-control n. 克己,自制
self-denial n. 克己
self-destruction 自我毁灭
self-discipline n. 自我约束
self-disciplined a. 自我训练的；自律的
self-discovery n. 自我发现
self-evident a. 自明的
self-generating adj. 自然发生的
self-government n. 自治,自制,克己
self-improvement n. 自我改造
self-interest 自身利益
selfish a.自私的，利己的
selfishness n. 自我中心,利己主义,任性
selfless adj. 无私的，忘我的
selflessly adv. 忘我地
selflessness n. 无私，忘我
self-limited a. 自限的
self-made n. 白手起家的
self-possession n. 沉着，镇定
self-propelled a. 自动推进的
self-repairing a. 自行修整的
self-respecting a. 有自尊心的
self-restoring a. 自行恢复的
self-sacrifice n. 自我牺牲,献身
self-sacrificing a. 自我牺牲的
selfsame a. 完全一样的，同一的
self-same adj.完全相同的
self-satisfied a. 自鸣得意的
self-selection 自选
self-taught 自学的；自修的
sell vt.&vi.卖
seller n.卖者；行销货
selvage n. 布等的织边,镶边
selvedge n. 布等的织边,镶边
selves n. self(自我)的复数形式
semaphore n. 旗语
semblance n. 外貌，相似
semester n.半年；学期，半学年
semicircle n.半圆，半圆形体
semicircular a. 半圆的
semicolon n. 分号(；)
semiconductor n. 半导体
seminal adj. 有创意的
seminar n. 研讨会，学术讲座；研究班
seminary n. 神学院
Semitic adj. 闪族的
semitropical a. 亚热带的
senate n.参议院，上院
senator n.参议员；评议员
senatorial a. 参议院的,参议员的
sence n. 感官，官能；感觉，判断力；意义
send vt.送；派遣；发射
sender n. 寄信人
senescence n. 老朽,衰老
senescent adj. 衰老的，老化的
seneschal n. 管家，总管
senile adj. 年老的
senility n. 衰老，老化
senior a.年少的；地位较高的
seniority n. 长辈,前任者的特权,老资格
senior-oriented a.面向年长者的
sensation n.感觉，知觉；轰动
sensational adj. 耸人听闻的，轰动的
sense n.感官；感觉；见识
senseless a.愚蠢的，无意义的
sensibility n. 感性,感觉,情感
sensible adj. 合情合理的；感觉得到的；明智的；感知的；明显的；通情达理的；可察觉的；明理的
sensitive a.敏感的；灵敏的
sensitivity n. 敏感性；灵敏性；灵敏度
sensor n. 传感器；灵敏元件；敏感元件
sensory a. 感觉的
sensual adj. 肉欲的、淫荡的
sensuality n. 淫荡、好色
sensuous a. 感觉上的,给人美感的
sent vt. sand的过去式与过去分词
sentence vt.判决，宣判
sententious adj. 好说教的，简要的
sentient adj. 有知觉的，知悉的
sentiment n.感情；情操；情绪
sentimental a. 多愁善感的
sentimentalist n. 容易感伤的人,多愁善感的人,感情
sentimentality n. 多感情,多愁善感,感伤癖
sentimentally ad. 感情上
sentinel n. 哨兵
sentry n. 哨兵，步哨
sepal n. 萼片
separable a. 可分离的,可分的
separate a.分离的；个别的
separate...from... 使…和…分离；把…分开
separated a. 分开的
separately adj. 分离地；单独地；adv. 分别地；分离地；孤独地；各别地，单独地
separation n.分离，分开；分居
separator n. 区分者,从事分离的人,分离器
sepsis n. 脓毒病，败血
September n.九月
septic adj. 受感染的、腐败的
sepulcher n. 埋葬所，坟墓
sepulchral adj. 坟墓的，阴深的
sepulchre n. 坟墓,埋葬所
sepulture n. 埋葬,坟墓,墓
sequacious adj. 前后一贯的，盲从的
sequel n. 继续,续集,趋势,结果,结局,
sequence n.连续，继续；次序
sequent n. 后果,继起的事
sequential adj. 连续的，一连串的
sequentially ad. 顺序地
sequester v. （使）隐退，隐居
sequestrate v. 扣押，没收
sequestration n.隔离; 退隐,隐遁
sequin  n. 亮片
sequoia n,. 红杉
seraglio  (C)  (回教国家的) 后宫,土耳其皇宫
seraph n. 六翼天使
seraphic adj. 如天使般的，美丽的
sere adj. 干枯的，凋萎的
serenade n. 夜曲，小夜曲
serendipity n. 善于发掘新奇事物的天赋
serene a. 宁静的,沉着的,安详的,晴朗的
serenity n. 宁静,沉着,晴朗
serf n.农奴
serfdom  n. 农奴的身分; 农奴制度
serge n. 斜纹哔叽布料
sergeant n.警士；军士
serial n. 序列,连载小说
sericulture 养蚕
series n.连续，系列；丛书
serious a.严肃的；认真的
seriously adv. 严肃地，严重地；认真地；重大
seriousness n. 认真
sermon n.布道，讲道，说教
sermonize 说教，讲道
serpent n.蛇(尤指大蛇或毒蛇)
serpentine adj. 似蛇般绕曲的，蜿蜒的
serrated adj. 呈锯齿状的
serried a. 密集的,林立的,重重叠叠罗列的
serum n. 浆液,血清,乳浆
servant n.仆人，佣人
serve vt.开(饭)，上(菜)
server n. 服伺者,服勤者,伺候者
service n.服务
serviceable a. 有用的,耐用的
services n. 部门
servile adj. 奴性的，百依百顺的
servility n. 奴态,卑屈
servitor n. 仆人,从仆,工读生
servitude n. 奴隶状态,惩役,地役权
servo-system n. 伺服系统
sesame n. 芝麻
session n.会议，一段时间
set n.(一)套 vt.镶，嵌
set...free 释放(某人)
setback n. 挫折，失败；(疾病的)反复
settee n. 有靠背的长椅
setter n. 安放者,镶嵌者,排字工人
setting n.安装，调整；环境
settle vt.安排；安放；调停
settled a. 固定的
settlement n.调停；(新)住宅区
settler n. 移民者,居留者,赠予者
setup n. 安排，准备，配置
set-up n.计划，安排
seven num.七
seven-course n. 7道菜
sevenfold adj. 七倍
seventeen num.十七，十七个
seventeenth num. 第十七,十七分之一的
seventh num.第七；七分之一
seventieth num. 第七十,七十分之一的
seventy num.七十，七十个
sever v. 切断，脱离
several adj.&pron.几个，数个
severance n. 切断，分离
severe a.严格的；严厉的
severel 几个，数个
severely adv. 严厉地，苛刻地；严肃地；严格地；剧烈地
severity n. 严格,严重,激烈
sew vi缝纫 vt.缝制，缝补
sewage n. (下水道)污水；污物
sewed 缝
sewer n. 排水沟，下水道
sewerage n. 排水设备,污水
sewing n. 缝纫，缝制物；(书的)装订
sewing-machine n. 缝纫机
sewn 逢；缝
sex n.性别，性
sextant n. 六分仪(航海定向仪器)
sexton n. 教堂司事
sexual a. 性的,性别的
sexuality n. 性欲
shabby adj.破旧的；蹩脚的
shack n. 简陋的小屋，棚屋
shackle n. 脚镣，枷锁
shad n. 鲱鱼类
shade n.(色彩的)浓淡，深浅
shadow n.影子
shadowy a.有影的；幽暗的
shady a.成荫的，阴凉的
shaft n.(工具的)柄，杆状物
shag n. 粗毛,蓬乱一团
shaggy a. 毛发蓬松的,长浓而粗的,表面粗糙的
shake vt.摇，使震动 n.摇动
shaken shake的过去分词；摇；摇动
shaker n. 摇动者;摇荡器;搅拌器
shakespeare n. 莎士比亚
shaky a. 震动的,摇晃的,动摇的
shale n. 页岩
shall v.aux.(我，我们)将要
shallop n. 轻舟，小舟
shallow a.浅的；浅薄的
sham n.假冒；膺品 vt.假装
shamble vi. 蹒跚地走,摇摇晃晃地走,摇晃不稳
shambles n. 混乱之处，凌乱的地点
shame n.羞耻，羞愧；羞辱
shamefaced a. 害羞的,谦逊的,不惹眼的,羞耻的
shameful a.可耻的；不道德的
shameless a. 不知羞耻的
shampoo vt.用洗发剂洗 n.洗头
shanghai 上海
shank n. 胫,腿骨,杆,柄
shan't (同)shall not
shanty n. 简陋的小木屋
shape n.形状；情况 vt.形成
shapeless adj. 无形的,无定形的
shapely a. 样子好的,定形的,形状美好的
shard n. （陶器等）碎片，破片
share vt.分享 n.一份
shareholder n. 股东
shares n. 股票
shark n.鲨鱼；贪婪狡猾的人
sharon 莎伦(女名)
sharp adj.锋利的；尖的
sharpen vt.削尖，使敏锐
sharpener n. 铅笔刀，磨石
sharply ad.锐利地，敏锐地
sharpness n. 锐利,严厉,疾速
shatter vt.粉碎，破碎；毁坏
shave vt.剃，刮 vi.修面
shaving n. 刮,修胡须,削
shavings n. 刨花
shawl n. （妇女用）披肩，围巾
shay  n.轻便马车
she pron.她
sheaf n. 一捆、一束
shear vt.剪；剥夺 vi.剪
shears n. 大剪刀
sheath n.壳，套；(刀，剑)鞘
sheathe vt. 插入鞘,覆盖
shed n.棚；小屋
she'd (同)she had；she would
sheen n. 光辉，光泽
sheep n.羊，绵羊
sheepfold n. 羊圈
sheepish a. 懦弱的,羞怯的
sheepskin n.羊皮
sheer a.纯粹的；全然的
sheet n.被单；纸张；薄板
shelf n.搁板，架子
shell n.炮弹，猎枪子弹
she'll (同)she will；she shallwhile
shellac n. 虫漆
sheller n. 剥壳者,脱壳机
shelly a. 多壳的,壳一般的,由壳而成的
shelter n.隐蔽处；掩蔽，庇护
sheltered a. 蔽阴的
shelter-forest n.森林防护带
shelve v. 搁置
shelves shelf的复数
shepherd n.牧羊人，羊倌
shepherdess n. 牧羊女
sherbet n.冰果冻
sheriff n.郡长；警察局长
sherry n. 雪利酒,葡萄酒
she's (同)she is；she has
she-wolf 母狼
shibboleth n. 陈旧语句，习俗
shield n.盾；防护物 vt.保护
shift vt.替换，转移 n.转换
shifting 移动，转嫁
shiftless adj. 没有决断力的，偷懒的
shilling n.先令
shimmer v. 闪烁，微微发亮
shin n. 胫骨
shine v.照耀；发光
shingle n. 木瓦，屋顶板
shingles n.  『医』带状泡疹
shining a. 闪闪发光的，明显的
shiny a. 有光泽的,发光的,辉煌的
ship n.轮船
shipboard n. 舷侧,船
shipbuilding n.造船(业)，造船学
ship-handling n.造船，驾船
shipmail n. 随船带交
shipmate n. 同船水手
shipment n.装货；装载的货物
shipowner n. 船主
shipper n. 装货者,货主
shipping n. 船运，装运；船运业；船舶(总数)；海运
ships 轮船
shipshape adj. 整洁的，井然有序的
ship-shaped n.船状的，船形的
shipwreck n.船舶失事
shipwright n. 造船者
shipyard n. 造船所
shire n. 郡
shirk v. 逃避，规避
shirr n. 宽紧线,橡皮线
shirt n.(男试)衬衫
shirting n. 衬衫衣料
shiver vi.颤抖，哆嗦 n.冷颤
shoal n. 浅滩、浅水处，一群（鱼）
shock n.冲击；震惊 vi.震动
shocked 震惊的
shocking a. 令人震惊的；可怕的
shoddy adj. 伪造的；劣等的；n. 劣质的，冒充好货的
shoe n.鞋
shoecase 鞋柜
shoemaker n. 鞋店,皮鞋匠
shoes n. 鞋
shoestring 小额资本
shone shine的过去式(分词)；发光；照耀；发光(shone=shined)
shoo int. 赶走鸟等时所发声音
shook shake的过去式；摇；摇动
shoot vt.发射；射中 n.发芽
shooting n. 射击
shop n.商店，店铺；车间
shop-assistant n.售货员
shopkeeper n.店主
shopman n.售货员
shopper n. 购物者
shopping n. 买东西；购物
shopwindow n. 商店橱窗
shore n.滨，岸
shore-line n. 海岸线
shoreward ad. 向岸,朝岸,朝向陆地
shorn shear的过去分词
short adj.矮的
shortage n.短缺，不足额
shortcake n.油酥糕饼
shortcoming n.短处，缺点
shortcut n. 近路，捷径
shorten vt.弄短，缩小，减少
shortening n. 缩短
shortfall 缺额，缺少，不足，亏空
shorthand n.速记，速记法
shorthanded 人手不足的
shorthorn n. 短角牛
short-landed 短卸
short-landing 短卸
short-lived a. 短命的,短暂的,无常的
shortly adv.立刻；不久
shortman n. 矮人
shortness n. 短促，短，矮
short-range adj短程的，短期间的
shorts n. 短裤；短运动裤
short-sighted n. 眼光浅
short-term 短期
short-wave n. 短波
short-weight n. 短装，短重
shose 选择
shot n.发射；射击声
should aux.v.将；万一；就
shoulder vt.承担，挑起，肩负
shouldn't (同)should not
shout vi.vt.&n.喊；高呼
shouting n. 叫喊声，哗笑
shove vt.推 vi.(使劲)推
shovel n.铁锨
shovelful n. 一铁铲
show vt.给…看；表明
show...around 带领(某人)参观…
showcase n. 陈列柜
showed 出示
shower vi.下阵雨 vt.使湿透
showery a. 阵雨的
showing n. 显示，表现
showman n. 马戏团的老板,玩杂耍的人
shown show的过去分词；出示；出示(shown=showed)
showoff n. 卖弄者
showpiece n. 陈列品，精品，样品
showroom n. 展室，陈列室
showy adj. 鲜艳的，显眼的
shrank shrink的过去式
shrapnel n. 开花弹,榴弹,弹片
shred v. 切成细条，撕成碎片
shrew n. 泼妇,一种似鼠的动物名
shrewd adj. 判断敏捷的，精明的
shrewish a. 泼妇一样的
shrewsbury n. 舒兹伯利(英国城市)
shriek vi.尖声喊叫 n.尖叫声
shrill a.尖声的 vt.尖声地叫
shrilly ad. 尖声地
shrimp n.(小)虾，河虾，褐虾
shrine n.神殿，神龛，圣祠
shrink vi.收缩；缩小；退缩
shrinkage n. 收缩,缩小,减低
shrive vi. 忏悔
shrivel v. （使）皱缩，干涸，枯萎
shroud n. 寿衣，遮蔽物v. 覆盖
shrub n.灌木，灌木丛
shrubbery n. 灌木,灌木林
shrug vt.&vi.耸(肩) n.耸肩
shuck n. (植物的)壳，夹，无用之物
shudder n. 战栗,发抖
shuffle v. 拖步走，支吾，洗牌
shun v. 避免，闪避
shunt v. 使（火车）转到另一轨道，转移方向
shut vt.&vi.关闭
shute n. 舒特(姓)
shutter n.百叶窗；(相机)快门
shuttle n.(织机的)梭
shuttlecock n. 羽毛球
shy a.易受惊的；害羞的
shylock n. 夏洛克(男名)
shyly adv. 怕羞地；胆小地；羞怯地；畏缩地；害羞地
shyness n. 羞怯,胆怯
si n.((符号))『化学』silicon
Siamese  adj. 暹罗的; 暹罗语
siberia n. 西伯利亚
siberian a. 西伯利亚的
sibilant adj. 嘶嘶作声的
sibling n. 兄弟或姊妹
sibyl n. 女预言家，女先知
sibylline adj. 预言的
sicily n. 西西里(岛)(意大利)
sick a.有病的；恶心的
sickbed n. 病床
sicken vt. 患病,使厌倦,使恶心
sickening a. 令人作呕的；引起疾病的
sickle n. 镰刀
sickly a. 病弱的,阴沉的,无精打采的
sickness n.疾病
side n.边；面
sideboard n. 餐具柜
sidecar n. 轻快的双轮马车,机器脚踏车的边车
sideline n. 副业,旁线,旁观者的看法,兼职,
sidelong ad. 向横,向侧面,斜向着,间接地
sidereal adj. 恒星的
sides 侧
sidesplitting adj. 令人捧腹大笑的
side-street 小街道
sidewalk n. 人行道
sideway ad. & a. 斜向一边(的)，侧身(的)
sideways ad.斜向一边地
sidle v. （偷偷地）侧身而行
siege n.包围，围攻，围困
sienna n. 赭色
sierra n. 呈齿状起伏的山脉
sieve n. 筛，滤杓v. 筛出、滤出
sift vt.筛，过滤 vi.通过
sifter n. 筛子
sigh n.&vi.叹气，叹息
sighs 叹息
sight n.视力；视觉；见
sightless a. 盲目的,不在目前的,不可见的
sightly a. 看着舒服的,悦目的,眼界好的
sightseeing n.观光，游览
sight-seeing n. & a. 观光
sign n.征兆，迹象，病症
signal n.信号 vi.发信号
signalize vt. 使著名,使显著,使显眼
signatory 签字人；签过名的
signature n.署名，签字，签名
signboard n. 招牌,布告板
signet n. 印,图章
significance n.意义，意味；重要性
significant n.有意义的；重要的
signification n. 含义,意义,表示
signify vt.表示，意味着
signor n.…先生,…君
signora n.…夫人,…太太
signpost n. 招牌柱,广告柱,路标
Sikh  n.  (印度的) 锡克教徒
silage n. 储藏的饲料
sile vi. 下滑，下降
silence n.寂静，沉默
silent a.沉默的；寂静无声的
silently adv. 静静地；寂静地；沉默地
silhouette n. 剪影，轮廓
silica n. 硅石
silicate n. 硅酸盐
silicon n.硅(旧名矽)
silk n.(蚕)丝；丝织品，绸
silken a. 丝的,绸制的,柔软的,圆滑的
silkworm n.蚕
silky a. 丝的,柔滑的
sill n. 基石，门槛，窗台
silly a.傻的，愚蠢的
silo n. 筒仓,地窖
silt n. 淤泥、淤沙
silvan a. 森林的,乡村的
silver n.银；银子；银器
silversmith n. 银器匠
silverware n. 银餐具；银器
silver-ware n. 银器
silvery a. 象银的,银色的,银铃一样的
simian adj. 猿的、猴的n. 类人猴
similar a.相似的，类似的
similarity n.类似,类似处
similarly adv. 同样地；类似地，相似地
simile n. 直喻，明喻
similitude n. 相似,外表
simmer vt. 慢慢地煮
simony n. 僧职买卖,僧职买卖罪
simper v. 傻笑、假笑
simpering adj. 傻笑的
simple adj.单纯的；简易的
simpleton n. 笨蛋,傻子
simplicity n.简单，简易；朴素
simplified a. 精简了的，简化了的
simplify vt.简化，使单纯
simplistic a.过分简单化的
simply adv.简单地；仅仅
simulate v. 假装，模仿
simulated adj. 伪装的，模仿的
simultaneous a.同时的，同时存在的
simultaneously adv. 同时地；同时，一起
simutaneous a.同时进行的
sin n.罪，罪孽 vi.犯罪
since conj.由于；既然
sincere a.真诚的；真挚的
sincerely adv. 真诚地；诚恳地；真挚地
sincerity n.真诚，诚意；真实
sine n. (数学)正弦
sinecure n. 挂名差事，闲职
sinew n. 腱，力量，精力
sinewy adj. 多腱的，强壮有力的
sinful a. 有罪的,罪孽深重的
sing v.唱，演唱
singapore n. 新加坡；新加坡人
singe v. （轻微地）烧焦，烫焦
singer n.歌唱家，歌手
singing n. 唱歌
single a.单一的；独身的
singleness n. 单一,单独,独身
singletree n. 系曳绳的横木
sing-song n.歌咏
singular a.异常的，奇异的
singularity n. 卓越，奇异
singularly ad.不可思议地，少见地
sinister adj. 不吉祥的，险恶的
sink n.(厨房内的)洗涤槽
sinker n. 使下沉的人,锤子,开凿工人
sinking n.下沉；沉没；投资
sinless a. 无罪的,清白的
sinner n. 罪人,不知礼仪的人,无赖
Sino-British a.中英的
sinuous adj. 蜿蜒的，迂回的
sinus n. 窦,静脉窦,湾,下陷或凹下去的地方
sip v. 啜饮
siphon n. 虹吸
sir n.先生，阁下；…爵士
sire n. 陛下,殿下,父
siren n.汽笛，警报器
sirloin n. 牛的上部腰肉
sirocco n. 从非洲吹向南欧一带的非洲热风,
sirrah n. 小子
sirup n. 糖浆,糖蜜
sis n. ((口语))小姐
sissy n. 女孩子,女人般的男人,胆小无用的男子
sister n.姐、妹
sisterhood n. 姊妹关系,姊妹之谊,妇女团体
sister-in-law n. 夫,妻的姊妹
sisterly a. 姊妹一般的,象姊妹的
sit v.坐
site n.地点，地基；场所
sitting adj. 坐着的；n. & a. 坐，就坐
sitting-room n.起居室
situate v. 位于，坐落在；使处于
situated a.位于…的
situation n.位置；处境；形势
six num.六
sixpence n. 六便士银币,六便士
sixteen num. 十六；十六个
sixteenth num. 第十六,十六分之一
sixth num.第六；六分之一
sixtieth num. 第六十,六十分之一
sixty num.六十
sizable a. 相当大的,大小相当的
size n.尺寸，大小
sizzler n. 炎热天气，大热天
skate v.滑冰
skater n. 溜冰者
skating n. 滑冰，溜冰；滑冰的
skein n. 一束（线或纱）
skeletal a. 骨骼的,骸骨的
skeleton n.骨骼，骷髅；骨架
skeptic n. 怀疑者
skeptical adj. 怀疑的
skepticism n. 怀疑态度
sketch n.略图；速写；概略
sketchy adj. 概略的，粗略的
skew 偏斜；adj. 不直的，歪斜的
skewer n. （烤肉用的）串肉杆v. 用杆串好
ski n.滑橇 vi.滑雪
skid vt. 刹住,滚滑
skier n. 滑雪者
skiff n. 轻舟，小船
skiing n. 滑雪；滑雪运动
skilful a. 精巧的；熟练的；灵巧的
skill n.技能，技巧；熟练
skilled a.有技能的，熟练的
skillet n. 煎锅
skillful a.灵巧的，娴熟的
skim vt.掠过，擦过；略读
skimmer n. 撇取浮皮的器具,大略阅读的人,
skimming 漏税，剔除
skimp v. 节省花费，吝啬
skimpy adj. 吝啬的，贫乏的
skim-read v.略读；浏览
skin n.皮，皮肤
skinflint n. 吝啬鬼
skin-grafting n. 植皮手术
skinny adj.极瘦的
skip vi.跳，蹦 vt.跳过
skipper n. 船长,主将,正驾驶
skirmish n. 小战，小争吵
skirt n.女裙
skittish adj. <马等>容易受惊的,容易惊恐的
skulduggery n. 舞弊，作假
skulk n. 躲藏，偷偷摸摸地走
skull n. 头盖骨，脑壳
skunk n. 臭鼬，黄鼠狼
sky n.天空
skyey a. 天空的,天蓝色的,高达天际的,
skylark n. 云雀,发疯般的胡闹
skyline n. 天涯,地平线,以天空为背景的轮廓
skyrocket v. 陡升，猛涨
skyscraper n.摩天楼
slab n. 厚板，厚块
slack a.萧条的；懈怠的
slacken v. （使）松弛，放松
slacker n. 逃避工作的人，懒虫
slag n. 炉渣，矿渣
slain slay的过去分词
slake v. 解渴，消渴
slam vt.使劲关，砰地放下
slander n.&vt.诽谤，诋毁
slanderous adj. 诽谤的，中伤的
slang n.俚语；行话，黑话
slant vi.倾斜
slap vt.掴，拍 n.巴掌，拍
slapdash adj. 草率的，马虎的
slash vt.vi. 猛砍,乱砍
slat n. 条板,金属板
slate n. 石板，候选人名单v. 提名
slattern adj. 不整洁的
slaughter vt.&n.屠杀，屠宰
Slav Adj.斯拉夫人的
slave n.奴隶
slave-driver n. 驱使奴隶作工的人
slaveholder n. 奴隶所有者
slaver v. 流口水，渴望n. 口水
slavery n.奴隶制度；苦役
Slavic adj. 斯拉夫人
slavish a. 奴隶的,奴性的,奴隶根性的,
slay v. 杀，残杀
slayer n.杀人者
sleaze adj. 质地薄的；粗糙的
sleazy a. 质地薄的,没有内容的,廉价的
sled n. 雪撬,小雪撬
sledge n. 雪橇,大锤
sledgehammer n. 长柄大锤
sleek v. （使）光滑，adj. 光滑的，整洁的
sleep v.&n.睡，睡眠
sleeper n. 睡眠者,枕木,卧铺
sleepily ad. 瞌睡地；懒散地
sleepiness n. 想睡
sleeping n. & a. 睡(眠)着(的)
sleeping-bag n. 睡袋
sleepless a. 不睡眠的,睡不着的,不休息的
sleeplessness n.失眠
sleepy a.想睡的；寂静的
sleet n. 雨夹雪
sleeve n.袖子，袖套
sleeveless a. 无袖的
sleigh n. 雪撬
sleight n. 巧妙手法，巧计，灵巧（分割
slender a.细长的；微薄的
slept sleep的过去式(分词)；睡
slew slay的过去式；v. (使)旋转；n. 大量许多
slice n.薄片，切片；部分
slick a. 光滑的,熟练的,聪明的,平凡的,
slid slide的过去分词
slide vi.滑动
sliding 可调整的
slight a.细长的；轻微的
slightly adv. 轻微地；轻蔑地；略微地；稍微，有点；细长的；轻轻地
slim a.细长的；微小的
slime n. 黏液
slimy adj. 泥泞的，令人讨厌的
sling v. 投掷，扔，n. 吊腕带，吊索
slink v. 偷偷走动
slip vt.&vi.(使)滑动
slippage 滑动，打滑，下降，延期
slipper n.拖鞋，便鞋
slippery adj. 滑的；使人滑跤的；不稳固的；不稳定的；滑溜的，狡猾的，不可靠的
slipshod a. 破烂的,马虎的,潦草的
slit vt.切开 n.狭长的切口
slither v. （蛇）滑动，扭动前进
sliver n. 长条，细片，v. 裂成细片
slobber n. 口水；v. 流口水，粗俗地表示
slogan n.标语，口号
sloop n. 小帆船
slop n. 外衣,工作服,泥浆,污水
slope n.倾斜；斜面 vi.倾斜
sloping a.倾斜
sloppy adj. 邋遢的，不整洁的
slot n. 水沟,细长的孔,硬币投币口,
sloth n. 懒惰，树懒（一种动物）
slothful a. 懒惰的
slouch n. 没精打采的样子,耷拉,笨人
slough n./v. （蛇等）蜕皮，蜕壳
sloven n. 不修边幅的人
slovenly adj. 不整洁的，马虎的
slow a.慢的；迟钝的
slowdown n. 放慢，迟缓；怠工
slowly adv. 慢慢地；缓慢地；减速地，adj. 慢慢地
slow-up 衰退，减退
sludge n. 软泥,泥泞,泥状雪
slue v. (使)旋转
slug n. 鼻涕虫,懒汉,子弹,金属小块
sluggard n. 懒鬼
sluggish adj. 行动迟钝的，缓慢的
sluice n. 水门，水闸，n. 冲洗，奔流
slum n.贫民窟
slumber n.睡眠；沉睡状态
slumberous adj. 昏昏欲睡的
slump n./v. 猛然落下，暴跌，萧条
slur v. 含糊不清地讲
slush n. 烂泥,雪水
slut n. 懒妇,荡妇
sly a.狡猾的；躲躲闪闪的
smack n. 风味,滋味,少量,拍击声,海洛因,
small a.小的，少的；小型的
smallpox n. 天花
smalls 小商品
small-scale 小规模的
smart a.巧妙的；洒脱的
smartly adv. 轻快地，灵巧地，漂亮地
smartness n. 现代风格,敏捷,机灵
smash vt.粉碎；击溃；猛掷
smattering n. 略知，少数
smear n. 油渍，污点v. 弄脏，玷污
smell n.嗅觉；气味 vt.嗅
smelt v. 熔解，熔炼
smelter n.冶炼工人
smile v.微笑
smirch v. 玷污；n. 污点
smirk v. 假笑，得意地笑
smite vt. (常用被动语态)深深影响，打动
smith (姓)史密斯
smithy n. 锻冶匠的工作场所
smitten smite的过去分词
smock n. 工作服,罩衫,套挂
smog n.烟雾
smoke n.烟；抽烟 vi.冒烟
smokeless a. 无烟的
smoker n.吸烟者
smoking n. 吸烟；冒烟；熏制；抽烟
smoky a. 冒烟的,似烟的,熏脏的,呛人的
smolder v. 无火焰地闷烧，压抑
smooth adj.光滑的；平静的
smoothly adv. 顺利地，通顺地；光滑地；平稳地；安稳地；流畅地；平滑地，流利地
smoothness n. 柔滑,平滑,平坦
smote smite的过去式
smother n. 浓烟；vt. 窒息，扼杀，抑制，忍住，覆盖，笼罩；熄灭，(使)闷死
smoulder vi. 闷烧,郁积
smudge n. 污点,脏污,为除虫而升的熏火
smug adj. 自满的，自命不凡的
smuggle vt.私运 vi.走私
smuggler n. 做走私口者,走私船,制造私酒者
smuggling n. 走私
smut n. 煤尘,污迹,黑穗病
smutty adj. 淫秽的
snack n.快餐，小吃
snaffle n. 马嚼子
snag n. 意外的障碍
snail n.蜗牛；行动缓慢的人
snake n.蛇
snake-charmer n. 弄蛇者
snaky adj. 似蛇的，弯曲的，阴险的
snap vt.猛咬，突然折断
snapdragon  n.『植物』金鱼草
snappish adj. 脾气暴燥的
snappy adj. 精力充沛的，潇洒的
snapshot n. 快照
snare n. 罗网，陷井
snarl n./v. 纠缠，混乱
snarled adj. 纠缠不清的
snatch vt.&vi.攫取；抓住
sneak v. 鬼鬼祟祟而行，偷窃
sneakers n. 旅游鞋
sneaking adj. 秘密的，不公开的
sneer vi.&n.冷笑；嘲笑
sneeze vi.打喷嚏
snide adj. 讽刺的，含沙射影的
sniff n.以鼻吸气,嗅,vi.嗅,嗤之以鼻
sniffle n. 抽鼻子声；抽泣(声)；vi. 抽噎
snigger v. & n. 暗笑，窃笑
snip v. 剪，剪断
snipe n. 鹞,足以轻蔑的人物,香烟屁股,
snips n. 铁剪
snitch v. 告密，偷窃
snivel vi. 流鼻涕,哭泣
snob n.势利小人
snobbery n. 势利
snobbish a.势利的，谄上欺下的
snoop v. 窥伺，打听；n. 窥探者
snore vi.打鼾，打呼噜
snort vi. 喷着气弄响鼻子,哼着鼻子,
snout n. 鼻部
snow n.雪 vi.下雪
snowball n. 雪球,打雪仗,滚雪球式的募捐法
snowdrift n. (被风吹成的)雪堆
snowdrop n. 『植物』雪花莲
snowfall n. 一场雪；下雪
snowflake n. 雪花
snowman n. 雪人,雪人
snowshoe n. 雪鞋；vi. 穿着雪鞋走
snowstorm n.雪暴，暴风雪
snowsuit n. 孩童用防雪装
snowy a.雪的，下雪的
snub v. 冷落，不理睬
snuff n. 烛花,用鼻吸气,嗅,气味,鼻烟,
snuffle n. 鼻音,鼻息,鼻塞
snug adj. 温暖的，舒适的
snuggle v. 挨近，依偎
so adv.这么，那么
so...that 如此…以致于
so...that... 如此…以致…
soak vt.浸，泡 vi.浸泡
soaked adj. 湿透的
soap n.肥皂
soapstone n. 皂石
soapy 索皮(人名)
soar n. 高扬,翱翔
soaring (价格的)猛涨
sob vi.&n.啜泣，呜咽
sober a.清醒的；适度的
soberly ad. 严肃地；清醒地
sobriety n. 节制，清醒
sobriquet n. 浑名，绰号
so-called a.所谓的，号称的
soccer n.英式足球
sociability n. 社交性,好交际,善于交际
sociable a. 好交际的,社交的,友善的
social a.社会的；社交的
socialism n.社会主义
socialist a.社会主义的
socialistic a. 社会主义的
socialite n. 社会名流，名士
socialize  vt. 使<人>适于社会生活
socially ad. 社交上；社会上
society n.社会；会；社团
sociological a. 社会学的,社会学上的
sociologist n. 社会学家
sociology n.社会学
sociopath n. 反社会者
sock n.短袜
socket n. 窝,穴,插座,眼窝
socrates n. 苏格拉底(哲学家)
sod n. 草地,草坪,故乡
soda n.碳酸钠，纯碱；汽水
sodden adj. 浸透了的
sodium n.钠
sofa n.长沙发，沙发
sofronie 索芙朗妮(姓)
soft adj.软的；柔和的
softball n. 垒球
soften vt.使变软
softly adv. 柔软地；轻轻地；温柔地；温和地；软化地；柔和地
soft-management 软弱无力的经营
softness n.温和，柔和；软弱
softspot 软弱不振的企业
software n.(计算机的)软件
softwood n. 软木材,针叶树
soggy adj. 湿透的，濡湿的
soil n.土壤；土地
soiled adj. (衣服)穿脏了的
soiree n. 晚会,黄昏时的聚会
sojourn n./v. 逗留，寄居
sojourner n.寄居者，逗留者
solace n. 安慰. 慰藉
solar a.太阳的，日光的
sold sell(卖)的过去式和过去分词；销售
solder v. 焊接，焊合
soldier n.士兵，战士
soldiery n. 士兵,军人,军队
sole n.脚底，鞋底，袜底
solecism n. 文法错误，举止失礼
solely adv. 唯一地，只；完全；单独地
solemn a.庄严的；隆重的
solemnity n. 庄严，肃穆
solemnize vt. 隆重地庆祝,庄重地举行,使显庄严
solemnly ad. 严肃地，庄严地
solicit v. 恳求，乞求，教唆
solicitation n. 恳求，教唆
solicitor n. 初级律师
solicitous adj. 热切的，挂念的
solicitude n. 热心;关怀
solid a.固体的 n.固体
solidarity n.团结；休戚相关
solidify vt.&vi.团结；凝固
solidity n. 固体性,坚硬,体积,稳健,坚固
soliloquy n. 自言自语，独白
solitaire n. 纸牌
solitary adj. 孤独的，n. 隐士
solitude n. 孤独
solo n.独唱，独奏；独唱曲
solomon n. 所罗门
solstice n. 至,至日,至点
soluble a.可溶的；可以解决的
solute n. 溶质，溶解物
solution n.解决，解答；溶解
solve vt.解答；解决
solvency n. 偿付能力；溶解力，还债能力
solvent adj. 有偿债能力的，n. 溶剂
somatic adj. 肉体的
somber adj. 忧郁的，阴暗的
sombre adj.阴沉的，忧郁的
some adj.&pron.一些
some...others... 一些人…，其他人…
somebody pron.某人，有人
someday adv. (今后)有一天；改天
somehow ad.由于某种原因
someone pron.某人，有人
somersault n. 翻筋斗
something pron.某事，某物
sometime adv.在某一时候
sometimes ad.不时，有时
somewhat pron.一点儿 ad.有点
somewhere ad.在某处 n.某地
somnambulist  n. 梦行
somnolent adj. 思睡的，催眠的
son n.儿子
sonar n. 声纳
sonata n. 奏鸣曲
song n.歌曲
songster n. 歌手,作曲者,诗人,鸣鸟
sonic a. 音速的；声音的
son-in-law n. 女婿,养子
sonnet n. 十四行诗
sonny n. 宝贝,小家伙
sonority n. 响亮，宏亮
sonorous adj. （声音）宏亮的
soon adv.不久；很快
sooner 不久
soot n.煤烟
sooth n. 真实
soothe vt. 缓和,使安静,安慰,奉承
soothing a. 抚慰性的
soothsayer n. 预言者,占卜者,算命者
sop n. 面包片,湿透的东西,懦夫
sophism n. 诡辩
sophist n. 诡辩学者,诡辨家,学者
sophisticated a.老于世故的；高级的
sophistication n. 精密；复杂；尖端
sophistry n. 诡辩
sophomore n. 大学二年级生
sophomoric adj.大学二年级学生的， 一知半解的,傲慢的
sophy (构词成分)知识，学问
soporific adj. 催眠的，n. 安眠药
soprano n. 女高音，最高者
sorb vt. 吸附，吸收
sorcerer n. 男巫士,魔术师
sorceress n. 巫婆
sorcery n. 巫术，魔法
sordid adj. 卑鄙的，肮脏的
sore a.痛的；恼火的 n.疮
sorely ad. 痛苦地；剧烈地
sorghum n. 蜀黍属的植物,芦栗做的糖蜜
sorority n. 妇女联谊会,女学生联谊会
sorrel a. 栗色的,栗色毛的
sorrow n.悲痛；遗憾
sorrowful a.使人伤心的；悲伤的
sorry a.难过的；对不起的
sorry-looking a. 愁容满面的
sort n.种类；类别 vt.整理
sortie n. 出击,突围
SOS n.紧急求救信号
so-so adj. 一般；不怎样；凑合
sot n. 醉鬼,酗酒者
sottish a. 酗酒的,愚蠢的
sou n. 法国铜币名
sought seek的过去式(分词)
soul n.灵魂；精神；人
soulless a. 没有精神的,没有灵魂的,泄气的
sound a.健康的；完好的
sounder n. 使东西鸣响的人,鸣响的东西,
sounding n. (测得的)水深度；a. 发声的；稳妥价值，同合理价值
soundly ad. 酣畅地，完好地
soundness n. 完全坚固,稳固,公正
soup n.汤
soupcon n. 少量，一点点
sour a.酸的；脾气坏的
source n.来源；根源
sourly ad. 愠怒地；敌对地
souse v. 浸在水中，使湿透
south n.南，南方 a.南方的
southampton 南安普敦(英国港市)
southeast n.东南 a.位于东南的
southeastern a. 东南方的
southerly a. 向南的,来自南方的
southern adj.南方的，南部的
southward n. 南方
southwards ad. 向南方
southwest n.西南 a.西南的
south-west n.西南
southwestern adj. (在) 西南的
souvenir n.纪念品，黄豆
sovereign n.君主 a.统治的
sovereignty n. 主权，统治权
soviet adj.苏联的
sow vt.播(种) vi.播种
sown adv. 向下，在下面
soy n.酱油；大豆，黄豆
soybean 大豆
spa n. 矿泉,温泉浴场,矿泉治疗地
space n.空间；场地；空白
spacecraft n.航天器，宇宙飞船
space-craft n. 宇宙飞船
spaceman n. 太空船上的飞行员,宇宙人
spaceship n.航天飞船
spaceshuttle n. 航天飞机
spacing n. 间隔(歇)；间距
spacious a.广阔的，广大的
spade n.铲，铁锹
spades 锹(复数)
spaghetti n.通心粉；面条
Spain n.西班牙
span n.跨距；一段时间
spangle n. （缝在衣服上的）金属亮片，v. 闪光
Spaniard n. 西班牙人
spaniel n.西班牙猎狗
Spanish n.西班牙语
spank v. 打，拍打（在屁股上）
spanking n. 打屁股；adj. 急速的；轻快的，敏捷的
spanner n. 螺线钳
spar n. 晶石,圆材,斗鸡,争论
spare vt.节约 a.多余的
sparing adj. 节俭的，节约的
spark n.火花，火星
sparkle vi.发火花 vt.使闪耀
sparrow n.麻雀
sparse adj. 稀少的，贫乏的
sparsely-populated 人口稀少的
spartan adj. 简朴的，刻苦的
spasm n. 痉挛，抽筋
spasmodic adj. 痉挛的，间歇性的
spat n. 口角，小争论
spatchcock v. 把(文字)插入
spate n. 大批，大量，（水）泛滥
spatial a.空间的，占据空间的
spatter vt. 溅,中伤
spatula n. （调拌等用的）抹刀，刮刀
spavin n.  『兽医』 (马脚的) 跗节瘤
spawn n. （鱼等）卵子，v. 大量产卵，大量生产
speak v.说话
speaker n.场声器
speaking n. 说话；a. 发言的
spear n.矛，梭镖
spearman n. 枪兵
special adj.特别的；特殊的
specialise vt. 专攻，专门研究，使…特殊化；vi. 专攻，专门研究
specialist n.专家
speciality n.专业，特长；特产
specialization n. 特别化,特殊化,专门化
specialize vi.成为…专家；专攻
specialized adj. 专业的，专门的
specially ad.专门地，特别地
specially-made a. 特制的
specialties 特别股
specialty n. 专业，专长；特别；名产，特产
specie n. 正币,硬币
species n.种类；(生物分类)种
specific a.特有的；具体的
specifically ad. 特定的,明确的
specification n.载明，详述；规格
specifics n. 细微问题，细节
specified 指定的
specify vi.指定，详细说明
specimen n.样本，标本，样品
speciosity n. 似是而非，外表美观
specious adj. 似是而非的，华而不实的
speck n. 小点，斑点，少量
speckle vt. 使弄上斑点；沾污
spect 表示"看，查"；(构词成分)看
spectacle n.光景，景象；眼镜
spectacled a. 戴眼镜的
spectacles n. 眼镜
spectacular adj. 壮观的，引人入胜的
spectator n.参观者，观众
specter n. 鬼魂，幽灵，恐惧
spectral adj. 幽灵的，鬼魂的
spectre n. 幽灵,妖怪,恐怖的根源
spectroscope n. 分光镜
spectrum n.系列，范围；波谱
speculate vi.思索，沉思；投机
speculation n. 思索，推测，投机
speculative a. 投机的
speculator n. 投机商
sped speed的过去式(分词)
speech n.言语，讲话
speechless adj. 不会说话的
speech-maker n. 演讲者
speed n.速度
speed-boat n. 快艇
speedily ad. 赶紧,快快地
speedometer n. 速度计,里程计
speedway n. 机器脚踏车的竞赛场,高速公路
speedy a. 快的,迅速的
speleology n. 洞穴学
spell vt.拼写 vi.拼字
spellbinding 引诱，吸引
spellbound a. 被咒语所镇住的,被迷住的,茫然不知所之的
speller n.拼字
spelling n.拼字，拼法，拼写法
spelunking n. 洞穴探察
spencer n. (羊毛)短上衣
spend vt.用钱，花费；度过
spend...on 在…上花费(时间等)；在…花费(钱)
spending 消费；开支
spendthrift adj. & n. 挥金如土的(人)
spent spend的过去式(分词)；花费
sperm n. 精液,精虫,鲸油
sphere n.球，圆体；范围
spherical a.球形的，球面的
spheroid n. 球状体,回转椭圆体
sphinx n. 狮身人面像，谜一样的人
sphygmomanometer n. 血压计
spice n.香料，调味品；香气
spices 香料
spick-and-span a. 崭新的,新格调的,极干净的
spicy a. 香的,多香料的,辛辣的,下流的
spider n.蜘蛛
spigot n. 栓,嘴,龙头,饮水的地方
spike n. 长钉，大钉
spiky a. 大钉一般的,尖的,钉满钉子的
spill vt.使溢出 vi.溢出
spin vt.纺；使旋转 n.旋转
spinach n. 菠菜
spinage n. 菠菜(同)spinach
spinal a. 针的,尖刺的,尖刺状突起的,
spindle n. 纱锭,纺锤,轴
spindly adj. 细长的，纤弱的
spine n. 脊椎
spineless adj. 没骨气的，懦弱的
spinet n. 小型拨弦古钢琴
spinner n. 微调控制项
spinneret n. (纺)喷丝头
spinning n. 纺织；a. 纺织品的
spinster n. 未婚女人，老处女
spiny adj. 针状的，多刺的
spiral a.螺旋(形)的，盘旋的
spire n. （教堂）尖顶，尖塔，高点
spirit n.精神；气魄；情绪
spirited a. 有精神的,活泼的,生气勃勃的
spiritless a. 无生气的,沮丧的,无生命的,
spirits n. 烈性酒；洒精
spiritual a.精神的，心灵的
spirituality n. 灵性,属于心灵的事,精神 (性)
spiritualize  vt. 使…精神化
spirituous  adj. 酒精成分强的
spit vi.&vt.吐痰；吐唾沫
spite n.恶意，怨恨
spiteful a. 怀恨的,怀有恶意的,心眼坏的
spittoon n. 痰盂
splash vt.&n.溅，泼，飞溅
splashy adj. 大而显眼的，引人注目的
splay vt. 展开,张开,使成八字形
spleen n. 脾脏,坏脾气,怨恨
spleenish adj. 脾气坏的，易怒的
splendid a.壮丽的；显著的
splendidly ad. 光彩夺目地；辉煌地
splendor n. 壮丽，辉煌
splendour n. 光辉,壮丽,显赫
splenetic adj. 脾气暴的，易怒的
splice n./v. 接合，衔接
splint n. （固定断骨的）夹板，托板
splinter n. 尖片，裂片
split n.分裂，分化；派系
splitting n. 分区(裂)
splurge n. 炫耀，摆阔，卖弄
spoil vt.损坏，糟蹋；宠坏
spoiler n.损坏者,破坏者
spoke n. (车轮上)幅条，阻碍物；轮幅；说；vt. 用煞车煞住
spoken speak的过去分词；a. 口头的；口语的；说
spokesman n.发言人，代言人
spoliation n. 强夺,掠夺,毁灭文件
sponge n.海绵
spongy adj. 像海绵的，不坚实的
sponsor n.发起者 vt.发起
sponsorship n. 发起，主办
spontaneity n. 自然，自发
spontaneous a.自发的；本能的
spontaneously ad.自发地；一时冲动地
spoof v. 揶揄，嘲讽
spook n. 幽灵,鬼
spool n. （缠录音带等的）卷盘（轴）
spoon n.匙，调羹
spoonerism n. 首音误置
spoonful adj. 一匙的量；n. 一匙
spoor n. (野兽的)足迹
sporadic adj. 不定时发生的，零星的
spore n.孢子
sport n.运动
sportive a. 嬉戏着的,戏谑的,闹着玩的,
sports n. 运动会
sportsman n. 运动员；好运动的人
sportsmanship n. 运动家精神
spot n.点；班点；地点
spotless a. 无脏污的,无缺点的,无可挑剔的
spotlight n. 照明灯,车头灯,聚光灯
spots 小额钞票；n. 现货
spousal n. 结婚,结亲,结婚仪式
spouse n. 配偶,夫妻
spout v. 喷出，滔滔不绝地讲
sprain n./v. 扭伤
sprang spring的过去式
sprat n. 鲱鱼属的小鱼,瘦瘦的人,小个子
sprawl n./v. 伸展手足而卧，懒散地躺
spray vt.&vi.向...喷射；喷
sprayer n. 喷出水沫的人,喷雾,喷雾器
spraygun n.喷枪，喷漆枪
spread vt.伸开；传播 n.传播
spreader n. 散布者，传播者
spree n. 狂欢，纵乐，宴会
sprig n. 嫩枝，小枝
sprightly adj. 愉快的，活泼的
spring n.春天，春季
spring-board n.跳板
spring-cleaning n. 春季大扫除
springtime n.春季，春天
springy a.有弹性的
sprinkle n.洒，撒；小雨
sprinkler n. 洒水装置，洒水车
sprinkling n. 点滴，少数
sprint n. 全速奔跑
sprit 精神，妖怪
sprite n. 小妖,小鬼,妖精
sprocket n. 链轮齿
sprout v. 长出，萌芽，嫩芽
spruce n. 云杉，adj. 整洁的，潇洒的
sprung spring的过去分词
spry adj. 活泼的，敏捷的
spud n. 小锄头,剥取树皮用的刀,马铃薯
spume n. 泡沫
spun spin的过去分词；a. 纺成的，像纺成的
spunk n. 勇气，胆量
spur n.刺激物 vt.刺激
spurious adj. 假的，伪造的
spurn v. 拒绝，摈弃
spurt n. 喷射,冲刺
sputter n. 喷溅声,劈啪声,咕哝,急语
sputum n. 唾液,痰
spy n.间谍，特务 vt.侦察
spy-glass n. 小望远镜
squab a. 羽翼未丰的,矮胖的,刚孵出的
squabble n. 争吵，口角
squad n. 班,小队,小集团
squadron n. 骑兵营,分遣队,小舰队
squalid adj. 污秽的，肮脏的
squall n. 狂风,暴风雪,哇哇叫声
squalor n. 不洁，污秽
squander v. 浪费，挥霍
square n.正方形；广场
squarely ad. 成方形地；正直地
squash vt.压碎 n.鲜果汁
squat vi.&vt.(使)蹲下
squatter n. 擅自占地者
squaw n. 女人,妻子
squawk n. 瓜瓜声,苍鹭
squeak vi. 尖叫
squeal n. 尖叫,告密,高声诉苦
squeamish a. 过于拘谨的,洁癖的,神经质的,
squeeze vt.&vi.榨，挤；压榨
squeezer n.  压榨器
squelch v. & n. 压制，镇压
squib n. 爆竹,嘲讽,讽刺文章
squid n. 枪乌贼,钓乌贼用钓钩,反潜水雷发射装置
squilla 虾蛄
squint adj. 斜眼的，斜视的v. 斜视
squire n. 乡绅,大地主,治安官
squirm v. 蠕动，扭曲
squirrel n.松鼠
squirt vt.vi. 喷出,溅迸,注射
stab vt.&vi.&n.刺，戳
stabilise v.(使)稳定，(使)稳固
stability n.稳定，稳定性，巩固
stabilization n. 安定,安定化,稳定
stabilize vt. 使安定,使坚固
stable a.稳定的，不变的
staccato adj. （音乐）断音的，不连贯的
stack n.堆，垛 vt.堆积
stadium n.体育场
staff n.工作人员；参谋
stag n.雄鹿
stage n.舞台；戏剧；阶段
stagflation 滞胀
stagger vi.摇晃；蹒跚
staggering adj. 令人吃惊的
stagnancy 停滞，萧条
stagnant adj. 不流动的，停滞的
stagnate vt.vi. (使)淤塞,(使)停滞,(使)沉滞,
stagnation n. 淤塞,停滞,沉滞
stagy adj. 不自然的，演戏一般的
staid adj. 稳重的，沉着的
stain vt.沾污；给…着色
stainless a.纯洁的；不锈的
stair n.(常用复数)楼梯
staircase n.楼梯，楼梯间
stairs n. 楼梯
stairway n.楼梯
stake n.桩；赌金；奖品
stalactite n. 钟乳石
stalagmite n. 石笋
stale n.陈腐的；走了气的
stalemate n. 和棋局面，僵局
stalk n.主茎，叶柄；高烟囱
stall n.货摊，书摊；厩
stallion n. 种马
stalls 正厅前座
stalwart adj. 健壮的，坚定的
stamen n. 雄蕊,雄性花蕊
stamina n. 体力，耐力
stammer vt.口吃地说 n.口吃
stamp n.戳子；邮票；标志
stamp-collecting n.集邮
stampede vt.vi. (使)惊跑,(使)蜂拥
stance n. 站姿，立场；态度；姿势
stanch v. 止住(血等)；制止(血液)
stanchion n. 支柱,标柱
stand vi.站；坐落 n.架，台
standard n.标准 a.标准的
standardize vt.使与标准比较
standby 备品，准备，等待
standing n. 起立,持续,身分
standpoint n.立场，观点
stands n. 看台上的观众
standstill n. 停止,停顿
stanza n. （诗）节，段
staphylococci n. 葡萄状球菌
staple n. 主要产品
stapler n. 钉书机
star vt.&vi.主演
starboard n. 右舷,右侧
starch n. 淀粉,浆糊,刻板
starchy adj. 含淀粉的，刻板的
star-crossed adj. 时运不济的
stare vi.&vt.盯，凝视
starfish n. 海星
stark adj. （外表）僵硬的，完全的
starlight n. 星星的闪光,星光
starlike a. 星形的,星般闪烁的
starling  n. 『鸟』星椋鸟
starry a. 星光照耀的,多星的,星形的,
start vt.开始 vi.出发
start...moving 开动…
starter n. 起跑者
starting n. 出发，开始；a. 起始的
startle vt.使大吃一惊 n.吃惊
startling adj. 使人惊愕的；惊人的
startup n. 启动
start-up 创立，开始
starvation n. 饥饿,饿死
starve vi.饿死 vt.使饿死
starveling n. 挨饿者
stash v. 藏匿，隐藏
state n.州；国家；政府
stated a. 决定了的,一定的,定期的,规定的
stateliness n. 威严,庄严
stately a. 庄严的；雄伟的；堂皇的
statement n.陈述，声明
stateroom n. 谒见室,大客厅,特别室
statesman n.政治家，国务活动家
statesmanship  n. 政治手腕,治理国家的本领
static a.静的；静态的
statical a. 静态的，静力的
statics n. 静力学
station vt.驻扎；安置
stationary adj. 静止的，不动的
stationer n. 文具商,文具店
stationery n.文具；信笺
stationmaster n. 火车站站长
station-master n. 站长；为车站站长
statistical a.统计的，统计学的
statistics n. 统计；统计学；统计(数字、资料)
statuary n. 雕像，雕塑艺术
statue n.塑像，雕像，铸像
statuette n. 小雕像
stature n. 身高，身材
status n.地位，身分
statute n. 法规，法令
statutory adj. 法定的，受法令所约束的
staunch adj. 坚定的，忠诚的v. 止血
stave n. 狭板,梯级,棍棒,诗句
stay vi.停留；暂住
stead n. 代替,有利,好处
steadfast a. 坚定的,踏实的,固定的,不变的
steadily ad.稳定地，不变地
steadiness n. 稳健,坚定,不变
steadly adv. 稳定的，稳步地，平稳地
steady a.坚定的，扎实的
steak n.大块牛肉；牛排
steal vt.偷，窃取
stealth n. 秘密行动,秘密,鬼祟
stealthily ad. 偷偷地，隐秘地
stealthy a. 秘密的,掩人耳目的,鬼鬼祟祟的
steam n.蒸汽 vi.蒸发 vt.蒸
steamboat n. 汽船,轮船
steamed adj. 蒸熟的
steam-engine n. 蒸汽机
steamer n.轮船，汽船
steamroller n.蒸汽压路机
steamship n. 汽船,轮船
steam-ship n. 蒸汽轮船
steed n. 马，骏马
steel n.钢
steely a. 钢铁的,钢铁制的,钢铁一般的
steelyard n. 秤
steep a.险峻的，陡峭的
steepen vi. 变得更陡峭
steeple n. 尖塔，尖阁
steeply ad. 陡峭地
steer vt.&vi.驾驶
steerage n. 最低票价的舱位,士官的二等室,
steering-wheel n. 方向盘，舵轮
steersman n. 舵手
stein n. 啤酒壶
stellar a. 星的,似星的,恒星的,主要的
stem n.词干；(手表的)转柄
stench n. 臭气，恶臭
stencil n. （用以刻写图案，文字的）模板v. 用模板刻写
stenographer n. 速记员
stenography n. 速记，速记法
stentorian adj. （指声音）极响亮的
step n.(脚)步；步骤 vi.走
stepchild n. 前妻(前夫)所生子女
stepfather  (C) 继父,后父
stepladder n.四脚梯
stepmother n.继母
steppe n. 特指西伯利亚一带没有树木的大草原
stepson  n. 夫或妻以前婚姻中所生之子
stereo n.立体声 a.立体声的
stereoscopic a. 立体的
stereosonic a. 立体声的
stereotype n. 陈规，旧框框；陈规习俗；固定形式，老套；固定的模式(或形象)
stereotyped adj. 铅版的
sterile adj. 不孕的，无细菌的
sterility n. 不毛,不孕,内容贫乏
sterilization n. 使成不毛,断种,杀菌,绝育
sterilize v. 使不育，杀菌
sterling n. 英国货币,标准纯银
stern n.艉，船尾；臀部
sternly adv. 严厉地，严肃地；坚定地
sternum n. 胸骨,胸片,胸板
steroid n. 甾族化合物，类固醇
stertorous a. 打鼾的
stethoscope n. 听诊器
steve 史蒂夫(男名)
stevedore n. 装卸工人,码头工人,脚夫
stew vt.炖 vi.炖着 n.炖肉
steward n.乘务员，服务员
stewardess n.空中小姐，女乘务员
stewardship n. steward 的职务,工作,管理
stick vt.&vi.伸，伸出
sticking a.粘的
stickler n. 坚持细节之人
sticky a.粘性的；胶粘的
stict 严格的
stiff a.硬的；僵直的
stiffen vt.使硬；使僵硬
stiffly ad. 硬；顽固地
stiffness n. 坚硬，硬度
stifle v. 闷死，镇压
stigma n. 耻辱,污名,烙印
stigmatic a. 不名誉的,有烙印的,丑恶的
stigmatize v. 污蔑，玷污
stile n. 墙两边的阶梯
stiletto n. 小剑，匕首
still adj.寂静的；静止的
stillness n.寂静，无声
stilly a. 不动的,平静的
stilt n. 支撑物；支撑架
stilted adj. （文章，谈话）不自然的
stimulant n. 兴奋剂，刺激物
stimulate vt.刺激，激励，激发
stimulating a.使人兴奋的
stimulation n. 刺激,激励,鼓舞
stimulus n. 刺激，激励（复：stimuli）
sting vt.刺；刺痛 vi.&n.刺
stingy adj. 吝啬的，小气的
stink n./v. 发臭，臭味
stint v. 吝惜，节省
stipend n. 薪水，薪俸，养老金
stipple v. 点画，点描
stipulate v. 要求以…为条件，约定
stipulation n. 规定，约定
stipule n. 托叶
stir vt.动；拨动；激动
stirring a. 活泼的,活跃的,忙碌的,激动人心的
stirrup n. 马镫,马镫铁,马镫形的工具
stitch n.一针，缝线 vt.缝
stoat n. 鼬
stock n.原料；库存品；股本
stockade n. 栅栏，围栏
stockbroker n.证券经纪人
stockholder n. 股东
stockholding n.股金，股份
stockholm n. 斯德哥尔摩
stocking n.长(统)袜
stockjobber n.证券批发商；股票抽机商
stockmarket n.股票市场
stockpile n.囤储物资
stocktaking n.存货盘点，盘货
stocky adj. 矮胖的，粗壮的
stockyard n. 牲畜围栏
stodgy adj. 艰涩难懂的，乏味的
stoic n. 坚忍克己之人
stoical a. 坚韧的；淡泊的
stoicism n. 坚忍克己
stoke v. 添加燃料，司炉，激起，吞食
stoker n. 司炉,供煤机,自动添煤装置
stole steal的过去式；偷
stolen steal的过去分词；偷
stolid adj. 无动于衷的，感情麻木的
stoma n. 细孔,口,气孔
stomach n.胃；肚子；食欲
stomachache n. 胃痛
stomach-ache n. 胃痛；腹痛；肚子痛
stomacher n. 三角胸衣
stone n.果核，(水果的)硬核
stonewall v. 阻碍议事，妨碍
stony a.多石的；冷酷的
stood stand的过去式(分词)；理解；站
stool n.凳子
stoop vi.俯身；弯身 n.弯腰
stop vt.塞住；阻止；停止
stop...from 阻止；阻拦
stoppage n.中止 (活动) ; 停止
stopper n. 阻止的人,木塞,制止器
stopping n. 停止，制动(状态)
stopwatch n. 跑表；记秒表(可暂停的表)
storage n.贮藏；贮藏量
store vt.存贮，储藏
stored-up a. 储藏起来的
storehouse n. 宝库，见识广博之人
storekeeper n.(美)零售店店主
store-keeper n. 杂货店主
store-room n. 贮藏室
stores n. 食物储藏
storey n.(层)楼
stories 故事
stork n. 鹳
storm n.风暴；暴(风)雨
stormy a.有暴风雨的；激烈的
story n.故事，小说，传说
story-book n. 故事书
stout a.矮胖的；坚固的
stouthearted adj. 勇敢的
stoutly ad. 断然；牢固地
stoutness n. 坚固,刚毅
stove n.炉，火炉，电炉
stow vt. 收藏,装填,贮藏,堆垛,使暂留,
stowage n. 装载
stowaway n. （藏于轮船，飞机中的）偷乘者
straddle v. 叉开腿，伸展
strafe v.轰击；斥责
stragety 战略
straggle v. 迷路，漫延
straggling a. 散乱的
straight a.直的；正直的 ad.直
straighten vt.把…弄直vi.挺起来
straightforward a.老实的 ad.坦率地
straightway ad. 直接地,立刻地
strain vt.拉紧 vi.尽力
strained adj. 不自然的，不友好的
strainer n. 用力拉的人,松紧扣,过滤器
strait n.海峡
straiten v. 使…困苦，使狭窄
straits n. 海峡；困难，窘境
strand n. 绳索之一股,绳,河岸,海滨,串
stranded adj. 搁浅的，进退两难的
strange a.陌生的；奇怪的
strangely adv. 奇怪的；陌生地
stranger n.陌生人；新来者
strangle vt. 勒死,扼死,抑制,使窒息,压制
strangthen vt. & vi. 加强，变强
strangulation n. 扼杀，勒死
strap n.带子 vt.捆扎
strata n. 地层，阶层
stratagem n. 谋略，策略
strategic a. 战略的,战略上的
strategics 战略学
strategy n.战略；策略
stratify v. （使）层化
stratoscope n. 平流层观察镜
stratum n. 地层，社会阶层
straw n.稻草，麦杆吸管
strawberry n.草莓
strawflower  n. 麦杆菊
stray vi.迷路 a.迷路的
streak n. 线条，条纹，v. 加线条
stream n.(小)河；溪流
streamer n. 横幅,饰带,彩色纸带
streamlet n. 小溪,细流
streamline n. 流线；流线型；v. 精简；a. 流线型的
street n.街道
streetcar n. 路面电车
strength n.力量；力气
strengthen vt.加强，巩固
strenuous adj. 费力的，精力充沛的
strenuously ad. 奋发地；使劲地
streptomyces n. 链霉菌素
streptomycin n. 链霉素
stress n.压力；重音 vt.着重
stretch vt.伸展 vi.伸 n.伸展
stretcher n. 担架,延伸器
strew vt. 散播,撒满
strewn strew的过去分词
striated adj. 有条纹的
stricken a. 受打击的,负了伤的,衰老的,
strict a.严格的；严谨的
strictly adv. 全然；严格地，严谨地；绝对；明确地；adj. 严厉地，严格地
strictness n. 严格,严密,严重
stricture n. 谴责，严厉，束缚
stride vi.大踏步走 n.大步
stridency n. 尖锐，刺耳
strident adj. 尖声的，刺耳的
strife n.冲突，竞争
strike vt.&vi.打；击
striker n. 打击者,罢工者
striking a.显著的，惊人的
strikingly  adv. 显著地; 引人注目地
string n.细绳；带子
stringent adj.（规定）严苛的，缺钱的
strip n. 条带；细长条，条；窄条，长带；带状物；一片，一条；狭长的一片；vt. 剥(光)；夺；剥去；剥夺，脱去…的衣服vi. 剥，剥去；脱光衣服；
stripe n.条纹，条子
striped adj. 有条纹的
stripling n. 年轻男子
strive vi.努力，奋斗，力求
strode stride的过去式
stroke n.打，击；鸣声；中风
stroll n.&vi.漫步；闲逛
stroller n. 散步者,流浪者
strolling adj. 巡回演出的
stroma n. 基质
strong adj.坚固的；强有力的
stronghold n. 要塞,堡垒,大本营
strong-looking a. 外表健壮的
strongly adv. 强有力地；强壮地，强烈地
strong-minded a. 有坚强意志的
strongpoint n. 防守上的战略据点
strop n. 磨剃刀用的皮带,滑索
strove strive的过去式
struck strike的过去式(分词)
structural a.结构的，构造的
structure n.结构；构造 vt.建造
struggle n.&vi.斗争，奋斗
strumpet n. 妓女
strut v. 昂首阔步地走
strychnine n. 『化学』马钱子碱
stub n. 断株,烟蒂,存根,残余,树桩
stubble n. 断株,茬,剪成短短的头发
stubborn a.顽固的；顽强的
stubbornly ad. 顽固地，倔强地
stubbornness n. 顽固的，固执的
stucco n. 装饰用的灰泥
stuck stick的过去式(分词)
stud n. 图钉,装饰钮扣,种马,领扣,大头钉
student n.学生
studied a. 有计划的,故意的,有意的,有知识的
studies v. 学习(第三人称单数)
studio n.工作室；播音室
studious a. 爱好学问的,努力的,故意的,
study v.学习
stuff n.材料 vt.装，填，塞
stuffing n.填料，填充物，填充剂
stuffy a.不透气的，闷热的
stultify v. 使无效，使无价值
stumble vi.绊倒；犯错误
stumbling-block n.障碍
stump n. 残株,树桩,烟蒂,讲演台
stun v. 使昏迷，使发愣
stung string的过去式(分词)
stunning adj. 极富魅力的
stunt v. 阻碍（成长），n. 特技，绝技
stuntman n. 特技演员
stupefaction n. 麻醉,昏睡,昏迷
stupefy v. （使）茫然，吓呆
stupendous adj.巨大的，大得惊人的
stupid a.愚蠢的；感觉迟钝的
stupidity n. 愚蠢,糊涂事
stupor n. 昏迷，不醒人事
sturdiness n. 坚固；牢实
sturdy a.坚定的；牢固的
sturgeon n. 鲟鱼
stutter v. & n. 口吃，结巴
sty n. 猪栏,猪圈
stye n. 猪栏,猪圈
Stygian adj. 冥河 (Styx) 的
style n.风格；文体；式样
stylish a. 现代风格的,流行的,潇洒的
stylist n. 时装设计师
stymie v. 妨碍，阻挠
suave adj.温和的；柔和的
suavity n. 柔和,温和,愉快
sub-agency 分代理处，分销处
subaltern n. 次长,副官,中尉
sub-branch 支店，分行
subcompany 子公司
subconscious n. 潜在意识,模糊的意识
subcontract n.转包合同；分契；对象
sub-directory n. 子目录
subdivide vt.把…再分
subdivision n. 细分,一部
subdue vt.使屈服，征服
subgroup n. 分组，子群
subheading n.副标题；小标题
subject n.题目；学科；主语
subjection n. 征服，服从，隶属
subjective a. 主观的,个人的
subject-matter n. 主题；素材
subjugate v. 征服，镇压
subjugation n. 屈服
subjunctive n. 假设法
sublet v.转租；分租
sublimate v. （使）升华，净化
sublime adj.雄伟的，崇高的，n. 顶峰
subliminal adj. 潜意识的，下意识的
sublimity n. 庄严,崇高,气质高尚
subloan 转贷
submarine a.水下的 n.潜水艇
submerge vt.浸没 vi.潜入水中
submission n. 服从，恭顺
submissive adj. 恭顺的
submit vt.使服从 vi.服从
subnitrate n. 次硝酸盐
subordinate a.下级的，辅助的
subordination n. 放置在下级,使隶属,看不起
suborn v. 收买，贿赂
subpackage 分包，分装
subpoena n. (法律)传票；v. 传讯
subrogate 权益转让，代位行使，
subrogation 债权转移
subroutine n. 子程序
subscribe vi.订购，认购；预订
subscriber n. 签署者,捐献者,订户
subscrible vt./vi.捐款，捐助；订阅；同意，赞成
subscript a. 写在下方的；n. 注脚，下标
subscription n.预约，用户，订阅费
subsequence n. 后果；随后，后来；随后发生的事，结果
subsequent a.随后的，后来的
subsequently adv. 后来，其后，其次，接着；按着；随后，a. 其次，接着
subserve vt. 对...有用,对...有帮助,对...有益,
subservience n.裨益,有用,贡献
subservient adj. 恭顺的
subset n.子集，子设备
subside v. （建筑物等）下陷，（天气等）平息，平静
subsidence n. 沉淀,下沉,陷没
subsidiary a.辅助的，补充的
subsidise v. 补助
subsidize vt. 给与补助金,给与奖助金,贿赂
subsidy n. 补助金
subsist vt. 供给食物,供养
subsistence n. 活命；生存
subsoil n. 下层土,底土
substance n.物质；实质；本旨
substantial a.物质的；坚固的
substantially ad. 大体上；本质上；实质上
substantiate v. 证实，确证
substantive adj. 独立存在的，直接的
substitute n.代替人 vt.用…代替
substitute...for 代替
substitution n. 代理,替换,交换
substratum n. 基础，根据
subsume vt. 包含，包摄；包容
subterfuge n. 诡计，托辞
subterranean adj. 地下的
subtitle n.(书籍)副标题；译文字幕
subtle a.微妙的；精巧的
subtlety n. 狡猾，微妙（的感情）
subtotal n. & v. 小计，求部分和
subtract vt.减，减去，去掉
subtraction n. 减少；减去
subtrahend n. 减数
subtropical a. 亚热带的
suburb n.郊区，郊外，近郊
suburban adj. 郊外的，市郊的
subvention n. 补助金，津贴
subversion n. 颠覆,打倒,破坏
subversive adj. 颠覆性的，破坏性的
subvert v. 颠覆，推翻
subway n.地道；地下铁路
succeed vt.继…之后 vi.成功
success n.成功，成就，胜利
successful a.成功的，结果良好的
successfully adv. 成功地；有成绩地；出色地；结果良好地
succession n.继承(权)，后裔
successive a.连续的；接连的
successively ad. 一个接一个地
successor n.继承人，继任者
succinct adj. 简明的，简洁的
succor n./v. 救助，援助
succulence n. 多汁,青饲料
succulent adj. 多汁的，多水份的
succumb v. 屈从，屈服，因…死亡
such adv.那么 adj.这样的
such...as 像…这样的
such...that... 那样的…以致
suck vt.吮吸；舐食
sucker n. 乳儿,吸管
suckle vt. 哺乳,养育,吮吸
suckling n. 乳儿,乳臭未干的小子
sucrose n. 蔗糖
suction n. 吸,吸入,吸力,吸引,吸上
sudd n.(白尼罗河上游的)大块漂浮植物
sudden a.突然的，意外的
suddenly adv. 突然地；忽然；a.突然的
sudorific a. 使发汗的,促使发汗的
suds n. 肥皂水,泡沫
sue 秀(女名)
suede n. 表面粗糙的软皮革
suet n. 牛脂,羊脂,板油
suez n. 苏伊士(埃及港市)
suffer vi.受苦 vt.遭受
sufferance n. 容许,默认,默许
sufferer n. 受苦的人；患者
suffering n.痛苦；苦难
suffice vi.足够；有能力
sufficiency n. 充分,充分的数量,足够的资力
sufficient a.足够的，充分的
sufficiently adv. 充分地，足够地
suffix n. 后缀,下标
suffocate v. （使）窒息而死
suffocation n. 窒息
suffragan n. 副监督,副主教,辅佐司教
suffrage n. 选举权，投票权
suffuse v. （色彩等）弥漫，染遍
suffusion n. 充满,弥漫,满布
sugar n.糖
sugarcane v. 甘蔗
suggest vt.建议；暗示
suggested 暗示的
suggestible adj. 易受影响的
suggestion n.建议，意见；暗示
suggestive a. 提示性的,影射的,暗示的
suicide n.&vi.&vt.自杀
suit n.一套(衣服)
suitable a.合适的；适宜的
suitably ad. 适当地
suitcase n.小提箱，衣箱
suite n. 随员,套房,一组
suitor n. 求婚者，（法律）原告
sulfa adj. 磺胺的；n. 磺胺类药物
sulfate n.『化学』硫酸盐
sulfur n.硫磺
sulk n. 闹情绪,快快不乐
sulky adj. 呕气的，生气的
sullen a.绷着脸不高兴的
sullenly ad. 不高兴地
sully v. 玷污，污染
sulphate n.『化学』硫酸盐
sulphur n.硫(磺)，硫黄
sulphureous a. 硫磺的,硫磺质的,硫磺一般的
sulphuric adj.硫磺的,含多量硫磺的
sulphurous adj.硫磺的,硫磺状的,硫磺味的
sultan n. 回教君主,苏丹,土耳其皇帝
sultana n. 回教国的王妃 ,公主,国王的姊妹
sultry adj. 闷热的，（人）风骚的
sum n.总数；金额 vi.共计
summarily adv. 概括地，仓促的
summarise vt. 概括，总结
summarize vt.概括，概述，总结
summary a.概括的；速决的
summation n. 总和,和,合计
summer n.夏，夏季
summertime n. 夏,夏季
summit n.顶点，最高点；极度
summon vt.召唤；鼓起(勇气)
summons 召唤
sumpter n. 拉货车的马或驴子,赶驮马的人,
sumption n. 大前提
sumptuary a. 限制费用的,禁止奢侈的
sumptuous adj. 豪华的，奢侈的，华丽的
sun n.太阳，日
sunbathe vi. 沐日光浴
sunbathing n.(沐)日光浴
sunbeam n. 阳光
sunburn n.晒黑，晒黑处
sundae n. 圣代
Sunday n.星期日，礼拜日
sunder v. 分裂，分离
sundew n. 毛毯苔
sundial n. 日规,日晷
sundown n.日落；日没
sundry 各式各样，各种的
sunfish n. 翻车鱼,淡水产小鱼
sunflower n. 向日葵
sung sing的过去分词；唱
sunglasses n.太阳镜，墨镜
sunk 沉；沉下
sunken a. 沉没的,下凹的
sunless a. 阳光照射不到的,阴暗的
sunlight n.日光，阳光
sunny adj.睛朗的
sun-powered adj. 太阳能发动的
sunrise n.日出(时分)
sunset n.日落(时分)
sunshade n. 遮阳伞,天棚,帽遮
sunshine n.(直射)日光，阳光
sunstroke n. 中暑
sup n. 一口
super a.极好的，超级的
superadd  vt. 再加…
superannuate vt. 以年老而辞退<某人>
superannuated adj. 老迈的，老式的
superb a.壮丽的；超等的
supercargo n. 货物管理员
supercilious adj. 目中无人的，高傲的
superconductor n. 超导体
supereminent a. 卓越的,极为出色的
superficial a.表面的；肤浅的
superfluity n. 多余; 过剩; 过多; 超过; 过量
superfluous adj. 多余的，累赘的
superhighway n. 超级高速公路
superhuman a. 超人的,人类能力所不能及的,
superimpose v. 加在上面，附加
superintend v. 监督
superintendence n. 指挥,管理,监督权
superintendent n. 主管人；监督人
superior a.较高的；优越的
superiority n.优越,高傲
superlative adj.最佳的
superlattace n. 超点阵，超晶格
superlattice n. 超晶格，超点阵
supermarket n.超级市场
supernal adj. 天堂的，天上的
supernatural a. 超自然的
supernumerary adj. 多余的，额外的
superpose vt. 放在上面,重叠
superposition n. 重叠,叠合,重合
superpower n. 超级大国
superscription n. 标题,姓名住址,题名
supersede v. 淘汰，取代
supersonic a.超声的，超声速的
superstition n.迷信，迷信行为
superstitious a. 迷信的
superstructure n. 上部构造,建筑物,上层建筑
supervene  vi. <事件> (以意想外的形态) 发生,接
supervise vt.&vi.监督，监视
supervision n. 监督,管理
supervisor n. 监督；主管
supine adj. 仰卧的，懒散的
supper n.晚餐
supplant v. 排挤，取代
supple adj.伸屈自如的，灵活的
supplement n.&vt.增补，补充
supplemental a. 补足的,追加的
supplementary a. 补充的；附加的
suppliance n. 恳求,哀求
suppliant a. 恳求的,哀求的,哀求性的
supplicant n. 乞求者，恳求者
supplicate v. 恳求，乞求
supplication n. 恳求,哀求,祈愿
supplier n. 供应商；供应者，供应厂商
supply vt.&n.供给，供应
support vt.支撑；支持；维持
supporter n. 支持者,后盾,伴随者
suppose vt.假定；猜想
supposed a. 想象的；假定的；推测的
supposedly ad.想象上，恐怕
supposing conj. 假使
supposition n. 猜想，推测
supposititious a. 偷偷掉换的,冒充的,私生的,
suppositive a. 想象的；假定的；推测的
suppress vt.镇压；抑制；隐瞒
suppressed vt. 抑制，取消
suppression n. 抑压,镇压,抑制
suppurate v. （伤口）化脓
supremacy n. 至高无上，最高地位
supreme a.最高的；最大的
surcease n. 终止，停止
surcharge n. 装载过多,超载,追加罚款,额外费
surcingle n. 肚带,法衣的腰带
sure adj.确信的，肯定的
surely adv. 确实，一定；当然；必定地，无疑地；肯定，谅必；a. 确实；稳当地
surety n. 保证人,保证,担保
surf n. 海浪,拍岸浪
surface n.地面，表面；外表
surfeit n. （食物）过量，过度
surf-riding n. 冲浪运动
surge n./v. 波涛汹涌，波动
surgeon n.外科医师；军医
surgery n.外科，外科手术
surgical a. 外科的,外科医生的,手术上的
surly adj.脾气暴躁的，阴沉的
surmise n./v. 推测，猜测
surmount v. 克服，战胜，越过
surname n.姓
surpass vt.超过，超越，胜过
surplice n. 白色法衣,白袈裟
surplus n.过剩，剩余(物资)
surprise n.惊奇，诧异
surprised a. 惊讶的
surprising a.惊人的；出人意外的
surprisingly ad. 惊人地；意外地
surrender vt.&vi.投降；自首
surreptitious adj. 鬼鬼祟祟的，保密的
surrey  n. 萨里郡
surrogate n. 代替品，代理人
surround vt.围，围绕，圈住
surrounding n. 周围的事物；环境；adj. 环绕的；周围的；包围
surroundings n.周围的事物，环境
surse vi. 护理，看护；n. 护士，保姆
surtax n. 附加税
surveillance n. 监视,监督
survey vt.俯瞰；检查；测量
surveyor n. 测量员,检查员
survival n.幸存(者)；生存
survive vt.幸免于 vi.活下来
survivor n. 幸存者
susceptibilities n. 脆弱的感情
susceptibility n. 感受性,感情
susceptible adj.易受影响的，多情的
sushi n.寿司(一种做成糕饼状或丸状的冷米饭)
suspect vt.怀疑 vi.疑心
suspend vt.吊，悬；推迟
suspender n. (裤子的)背带
suspense n. 悬念，悬疑，挂念
suspension n. 悬挂,暂停,中止
suspicion n.怀疑，疑心，猜疑
suspicious a.可疑的；猜疑的
sustain vt.支撑；供养；忍受
sustained adj. 持久的，经久不衰的
sustenance n. 食物，粮食，生计
suture n. 缝线v. 缝合
suzerain n. 领主,庄主,宗主
suzerainty n. 宗主权,领主的地位
svelte adj. (女人)体态苗条的
swab n. 拖把,药签
swaddle n. 襁褓
swagger v. 大摇大摆地走
swain n.乡下的年轻人,美男子
swallow n.,vt.&vi.吞，咽
swam swim的过去式；游泳
swamp n.沼泽，沼泽地
swampy a. 沼泽地的
swan n.天鹅
swank v. 夸耀，炫耀
swap v. 交换，交流
swapdata 互换资料
sward n. 草地,草皮
swarm n.一大群 vi.密集
swarthy adj. （皮肤等）黝黑的
swash vi. 冲激,溅泼,虚张声势
swat vt. 用力打下去,重拍
swath n.刈分的牧草
swathe vt. 绑,裹,包围
sway vi.摇动 vt.摇；摇动
swear vt.宣(誓) vi.诅咒
sweat n.汗
sweater n.厚运动衫，毛线衫
Swede n.瑞典人
Sweden n.瑞典
Swedish n. 瑞典人,瑞典语
sweep vi.掠过；袭来
sweeper n. 清扫夫
sweeping adj. 巨大的；一览无遗的；掠过的；n. 扫(清)除
sweepingly ad. 大规模地；彻底地
sweet adj.甜的
sweetbread n. 小牛,小羊的胰脏或胸腺
sweeten vt.使变甜 vi.变甜
sweetening n. 变甜；使变甜之物
sweetheart n. 情人,爱人
sweetly adv. 亲切地；甜蜜地；美妙地
sweetness n.甜蜜；新鲜；温和
swell vi.&vt.使膨胀，隆起
swelling 肿胀
swelter vi. 闷热,被暑气所苦,汗流夹背
sweltering adj. 酷热的
swept sweep的过去式(分词)；扫；打扫
swerve v. 转向，突然改变方向
swift a.快的；反应快的
swiftly adv. 迅速地；敏捷地
swiftness n. 迅速,快
swill v. 冲洗，痛饮
swim vi.游，游泳；眼花
swimmer n. 游泳者
swimming n. 游水,目眩
swimming-pool n. 游泳池
swimsuit n.(整身的)女式游泳衣
swindle v. 诈骗，骗取
swindler n. 骗子
swine n. 猪
swineherd n. 养猪的人
swing vi.摇摆；回转 n.摇摆
swinish a. 猪的,猪一般的,卑鄙的
swirl n./v. 旋转，漩涡
swish n. 嗖嗖声
Swiss a.瑞士的 n.瑞士人
switch n.开关；转换 vt.转换
switching n. 开关，转接，交换
Switzerland n.瑞士
swivel n. 转环,旋转轴承,旋转椅的台座
swollen swell的过去分词
swoon n. 昏晕,晕厥
swoop n. 俯冲,攫取
sword n.剑，刀
Swordgrass 剑状叶草工作室，感谢您的使用。
sword-thrust n. 刀剌；剑剌
swore swear的过去式
sworn swear的过去分词
swum 游泳
swung swing的过去式(分词)
sycamore n. 小无花果树,枫树的一种
sycophant n. 马屁精
sycophantic adj. 拍马的，谄媚的
sydney n. 悉尼(澳大利亚港市)
syllable n. 音节
syllabus n. 教学大纲；课程表；教学纲要
syllogism n. 三段论法,推论法,演绎
sylph n.空中仙女，身材苗条之女子
sylvan adj. (有) 森林的
symbiosis n.共生，共栖
symbol n.象征；符号，记号
symbolic a.象征
symbolical n. 代号a. 象征的,符号的
symbolize vt. 象征
symmetric adj. 对称的，匀称的
symmetrical a.对称的，匀称的
symmetry n.对称(性)，匀称
sympathetic a.同情的；和谐的
sympathetically ad. 同情地
sympathise a. 同情，体谅
sympathize vi.同情；同感，共鸣
sympathy n.同情；同感；慰问
symphony n.交响乐
symposium n.酒会；座谈会
symptom n. 症状，征候，征兆；徵候；表征
symptomatic a. 具有征候的,症状的,根据征候的
synagogue n. 犹太人集会,犹太教会堂
synchronization n. 同步
synchronize v. 使同步；(使)同时发生
synchronous adj. 同时发生的，同步的
syncopate v. 词中省略，缩写
syndicate n. 企业联合,辛迪加
syndicator n. 辛迪加组织者
syndrome n. 综合症
synergic adj. 协同的；n. 协同作用
synergy n.增效作用，协同作用
synod n. 宗教会议,大会,会议
synonym n. 同义字
synonymous adj. 同义的
synopsis n. 摘要，概要
synoptic adj. 摘要的，高瞻远瞩的
syntax n. 语法,有秩序的排列,句子构造
synthesis n.合成；综合，综合物
synthesize vt. 综合
synthetic a.综合的；合成的
synthetical adj. 合成的；非自然的
syphilis n. 梅毒
syria n. 叙利亚(亚洲)
syrian a. & n. 叙利亚人(的)
syringe n. 注射器
syrup n. 糖浆,果汁
system n.系统，体系；制度
systematic adj. 系统的，有组织的；成体系的；分类的；有计划的，有步骤的，有秩序地，有规则的
systematical a. 系统的，体系的
systematically adv. 系统地，有规则地；有系统地；有秩序地
systematize vt. 使组织化,使系统化,把...分类
systemic a. 全身的；系统的
systimatic adj.有系统的
systolic adj. 收缩的
t.b. 结核病
tab n. 制表
tabby n. 平纹,斑猫
tabernacle v. 临时住所，暂住
table n.桌子
tableau n. 画面，活人画（舞台上活人扮的静态画面）
tablecloth n. 桌巾
table-cloth n. 桌布
tableland n. 高原，台地
tables 桌子
tablespoon n. 大汤匙
tablespoonful n. 一汤匙之量
tablet n.碑，匾；药片
tableware n. 餐具
taboo adj. 讳忌的n. 禁忌
tabor n. 小鼓
tabular a. 制成表的,扁平的,表格式的,
tabulate vt.把…制成表
tabulation n. 作表,表格
tach n. 扣，钩
tacit adj. 心照不宣的，静默的
taciturn adj. 沉默寡言的
tack n.平头打 vt.钉住
tackle vt.解决，对付 n.用具
tacky adj. 粘的
tact n. 机敏，圆滑，得体；老练，机智；圆通
tactful adj. 圆滑的，机敏的
tactic n. (达到目的)手段，战术
tactics n.策略；战术，兵法
tactile adj. 有触觉的
tadpole n. 蝌蚪
taffeta n. 塔夫绸,波纹绸
taffy n. Wales人,太妃糖,阿谀
tag n.附加语；标签
tail n.尾巴；尾部
tailing-off n. 曳沙带
tailor n.裁缝
tailoring n. 裁缝业；缝工
tailwind n. 顺风
tain 铁片，锡箔
taint n./v. 玷污，败坏
tainted  adj. 染污的; 有污点的; 感染的; 腐败的
take v.拿，取；就座
take...as 把…理解为；把…当作为
take...as... 把…当做
take...for (错)当作，(误)认为
take...out 把…拿出来，取出
take...over 把…翻过不定期；把…翻过来
take-away adj. & n. (可带走的)熟食
taken take 的过去分词；拿
take-off n. 起飞
takeover n.兼并；接收
taker n. 吃药人
taking n. 捕获物；adj. 楚楚动人的；迷人的
talc n. 滑石,云母
talcum n. 滑石
tale n.传说；故事
talent n.天才；才能；人才
talented adj. 有才能的；天才的；能干的；有天份的，有才干的
talisman n. 避邪物，护身符
talk v.说话，谈话
talkathon n.冗长的演说
talkative a. 喜欢说话的,饶舌的,多嘴的
talker n. 说话的人,健谈者,饶舌者,空谈者
talking 谈话
tall adj.高的
tallow n. 牛脂,动物脂
tally n.分数，计算，票据
talon n. 猛禽的锐爪
tamarind n. 罗望子,其果实
tambourine n. 铃鼓，手鼓
tame adj.驯服的
tamer n. 驯服手
tam-o'-shanter n. 大黑头巾形帽子
tamp vt. 砸实；夯实，捣实；n. 夯具
tamper vi.(with)损害；削弱；窜改；贿赂；vt. 干预； 窜改；玩弄
tan n.棕褐色 a.棕黄色的
tandem ad. 前后直排地,纵排地
tang n. 强烈的味道
tangent n. 切线
tangential adj. 切线的，离题的；肤浅的
tangible adj. 可触摸的
tangle vt.使缠结，使纠缠
tango n. 探戈舞
tangsa 坦萨(印度地名)
tank n.水池；槽
tankard n. 单柄大酒杯
tanker n.油船；空中加油飞机
tanner n. 制革工人
tannery n. 制革厂,硝皮厂
tannic a. 丹宁的,得自鞣革的
tannin n. 单宁酸
tantalize v. 挑惹，挑逗
tantamount adj. 与…相等的
tantrum n. 勃然大怒，脾气发作
tap vt.&vi.&n.轻叩
tape vt.系，捆
tape-measure n.皮尺，带尺，卷尺
taper n.细小的蜡烛；微光
tape-recorder n. 录音机
tape-recording n. 录音
tapestry n. 挂毯，丰富多采的画面
tapeworm n. 绦虫
tapioca n. 树薯粉
tapir n. (动)貘
taproot n. 主根，直根；根本
taps  n.  (用作单数)  (美国军中之) 熄灯号音
tapster n. 酒吧的酒保
tap-talking 敲打的谈话方式
tar n.柏油，焦油
tarantula n. 毒蜘蛛之一种
tardiness n. 缓慢，迟滞，迟延
tardy adj. 缓慢的，迟缓的
tare n. 莠草，杂草
target n.靶，标的；目标
tariff n. 关税，价目表
tarn n. 山中的小湖或水潭
tarnish n./v. 失去光泽，晦暗
taro n. 芋头
tarpaulin n. 防水布，油布
tarry v. 耽搁，延迟
tart adj. 酸的，尖酸的
tartar n. 酒石,牙垢
task n.任务，工作，作业
taskmaster n. 工头
tassel n. 流苏，穗
taste vt.尝；尝到 n.味觉
tasteful adj. 有滋味的，好吃的
tasteless a. 没味道的,无鉴赏力的
tasty adj.美味的，可口的
tatter v. 撕碎n. 碎片
tatterdemalion n. 衣服褴褛的人
tattered adj.(衣服等)破烂的；衣衫褴褛的，破旧的
tattle n./v. 闲谈，泄密
tattoo n. 小马,归营号,得得的连敲声,
taught teach的过去式(分词)；教
taunt v. 嘲笑，讥笑
taupe n. 暗灰褐色
taut adj. 拉紧的，绷紧的
tautological adj. 冗赘的，用语重复的
tautology n. 同义反复,重复
tavern n. 小洒店；客栈
tawdry adj. 低级的，俗的而不值钱的
tawny a. 黄褐色的,茶色的
tax vt.抽税 n.税
taxation n. 课税,征税,租税
tax-free 免税的
taxi n.出租汽车
taxicab n. 出租车
taxi-cab n. 出租汽车
taxi-driver n. 出租汽车司机
taxonomy n. (动植物的)分类学
taxpayer n. 纳税人
tea n.茶；茶叶；茶树
teach vt.讲；教育 vt.教书
teachable a. 可教的,听教训的,驯良的
teacher n.教师
teaching n.教学，讲授；教导
teacup n. 茶杯
teak n. 柚木，柚木树
teal n. 水鸭
team vi.协作，合作
teammate n. 同队队员(队友)；队友
teamster n. 赶一群牲畜者,卡车驾驶员
teamwork n. 合作；协同工作
teapot n. 茶壶,小茶壶
tear vt.扯开，撕裂
tearful adj.眼泪汪汪的
tease vt.逗乐，戏弄；强求
teaspoon n. 茶匙
tea-spoon n. 茶匙
teaspoonful  n. 一茶匙的量
teat n. 奶嘴，乳头
tea-tray n.茶盘
technical a.技术的，工艺的
technicality n. 专门性,学术性,专门的事项
technically ad. 技术上，技能上
technician n.技术员，技师
technique n.技术，技巧；技能
technocrat n. 技术人员，技术统治
technological adj. 技术的，工艺的
technology n.工艺学，工艺，技术
technology-intensive 技术密集的
ted vt. 翻晒；撒，撒开
tedious a.冗长乏味的，沉闷的
tedium n. 单调乏味
tee n. T字,T字形之物,目标,球座,发球处
teem v. 充满，到处都是v. 倾盆大雨
teeming a. 丰富的
teenager n.青少年
teens n. 十多岁
teeter vi. 上下摇摆
teeth n. 牙(复数)；tooth的复数；齿，牙齿
teethe vi. 生牙，出乳齿
teetotal adj. 滴酒不沾的
teheran n. 德黑兰(伊朗首都)
tele 表示"远"
telecast n. vt. & vi. 电视广播
telecommunication n. 电信；通讯，电讯
telefax n. 传真；v. 发传真
telefilm n. 电视影片
telegram n.电报
telegraph n.电报机；电报
telegrapher n. 电报员
telegraphy n. 电报，电报学
telelens 长焦距镜头
teleology n. 目的论,有目的,目的论者
telepathy n. 心灵感应，精神感应
telephone n.电话 vi.打电话
telephone-box n.公用电话亭
telephotograph n. 传真照片
telescope n.望远镜
telescopic a. 用望远镜看到的
television n.电视；电视机
telex n.电传，用户电报
tell v.告诉；讲述
tell...apart 把…区分开；分辨，区别
tell...from 辨别，分辨；认出
teller n. 讲话者,告诉者,出纳员
telling a.有效的；有力的
telltale n. 搬弄是非者,证据
Telstar n. 通讯卫星
temerarious a. 不顾一切的,极大胆的
temerity n. 鲁莽，大胆
tempatation n. 诱惑，引诱
temper n.韧度；心情，情绪
temperament n. 气质,性质,性情
temperamental adj. 性情的，喜怒无常的
temperance n. 自制，节制，禁酒
temperate adj. 自制的
temperature n.温度
tempest n. 暴风雨，骚动
tempestuous adj.狂暴的
template n. 标准框，样板，模板
temple n.庙宇；寺院
tempo n. （动作、生活的）步调，速度
temporal adj. 时间的，世俗的
temporarily ad. 暂时地
temporary adj.暂时的；临时的
temporize v. 拖延
tempt vt.引诱，诱惑，劝诱
temptation n.诱惑，引诱
tempter n.诱惑者
tempting a. 引诱人的，吸引人的
temptingly ad. 迷人地；诱惑地
ten num.十
tenable adj. 站得住脚的，无懈可击的
tenacious adj. 坚忍不拔的，固执的
tenacity n. 坚持，固执
tenancy n. 租佃,租赁
tenant n.承担人，房客，佃户
tenantless  adj. 无人租赁的
tenantry n.佃户,房客
tend vt. 护理；照料；照管，趋向；走向；照顾；vi. 倾向于；往往是；走向，趋向；服务；易于
tendance n. 照顾,服侍,照料
tendency n.趋向，趋势，倾向
tendentious adj. 有偏见的，有倾向的
tender adj.嫩的；脆弱的
tenderer 投标人
tenderly adv. 深情地，温存地；娇嫩地；柔和地
tenderness n. 柔软,亲切,易触痛,敏感
tendon n. 腱
tendril n. 卷须,蔓,卷须状之物
tenebrous adj. 黑暗的，难解的
tenement n. 房屋,住户,租户,地产
tenet n. 信念，信条
tenfold a. 十倍的,十重的
tennessee 田纳西(美国州名)
tennis n.网球
tenon n. 凸榫，榫舌
tenor n. 男高音，要点，要旨
tense n.时态，时
tensile a. 张力的；能伸长的；拉力的
tension n. 紧张,不安,拉紧,电压,压力,
tensive a. 张力的，引起张力的
tent n.帐篷
tentacle n. 触角
tentative adj. 试探性的，尝试性的
tentatively ad. 尝试性地
tenth num.第十；十分之一
tenth-rate adj. 最劣等的
tenuous adj. 细薄的，稀薄的，空洞的
tenure n. 任期，终身职位
tepee n. (圆帷形)帐篷
tepid adj. 微温的
tercentenary n. & a. 三百年纪念日
tergiversation n. 搪塞,背叛,变节
terify vt. 使恐怖，恐吓
term n.期；学期；条件；词
termagant adj. 凶悍的，暴躁的n. 悍妇
terminable adj. 可终止的
terminal n.计算机终端；线接头
terminate vt.&vi.停止，终止
terminating n. 终止，终结，收信
termination n. 结束；中止
terminology n.术语学，术语
terminus n. （火车，汽车）终点站
termite n. 白蚁
terms 条件，条款
tern n. 燕鸥
terpsichorean adj. 舞蹈的
terrace n.平台，阳台，露台
terra-cotta n. 陶瓦,赤土陶器,赤土色
terrain n. 地势，地形；
terramycin n. 土霉素
terrapin n. 泥龟，水龟
terrestrial adj. 地球的，陆地的
terrible a.可怕的；极度的
terribly adv. 可怕地；极坏地；厉害地；极
terrier n. 狗的一种,国防自卫队,地籍册
terrific a.可怕的；极大的
terrified a. 恐惧的
terrify vt.使恐怖，使惊吓
terrifying a. 使人害怕的
territorial a. 领土的
territory n.领土，版图；领域
terror n.恐怖，惊骇
terrorism n. 恐怖主义(行为)
terrorist n.恐怖分子
terrorize vt. 使恐怖,恐吓
terror-stricken a. (受了)惊吓的
terse adj. 简洁的，简明的
tertian a. 每三天发生一次的,隔日的
tertiary a. 第三的,第三位的,第三世纪的
tertiary-industry n.第三产业
tessellated adj. 镶嵌花样的
test n.&vt.测验，考查
testament n. 遗嘱，证明
testamentary a. 遗嘱的,据遗嘱的,遗嘱中有的
testator n. 立遗嘱之人
tester n. 考试人,试验装置,天盖,华盖
testificate 证件
testify v.证明，证实，作证
testimonial n. 证明书，奖状
testimony n. 证言，证明
testing n. 试验，测试
test-tube n. 试管
testy adj. 性急的，暴躁的
tetanus n. 破伤风
tether n. 系绳,系链,界限,范围
tetracycline n. 四环素
Teuton n. 条顿人,日耳曼人,德国人
Teutonic a. 条顿人,条顿语的,日耳曼的
texas 得克萨斯州(美国州名)
text n.课文；课本
textbook n.课本，教科书
textile n.纺织品 a.纺织的
textual adj. 课文的，正文的
texture n. 质地，结构
thallus n. 叶状体,扁平体
thames n. 泰晤士河(英国)
than conj.比
thane n. 大乡绅,领主
thank v.谢谢
thankful adj.感激的，感谢的
thankless a. 不感谢的,忘恩的,不知感恩的
thanks n. 谢谢(只用复数)；谢意；感谢；int. 谢谢
Thanksgiving n.感恩节
that a.那 pron.那 ad.那样
thatch n. 茅草屋顶，茅草
that's (同)that is
thaumaturgist n. 魔术师,奇术士
thaw v. 解冻，溶化
the art.这(那)个；这些
theater n.戏院,电影院,剧场,全体观众,
theatre n. 剧场，戏院； (阶梯式)教室；戏剧效果；舞台；剧院(theatre=theater)
theatric a. 剧场的,夸张的,戏剧性的
theatrical adj. 戏剧的，矫揉造作的
theatricals 戏剧
theft n.盗窃，偷窃(行为)
their pron.他(她、它)们的
theirs pron.他(她)们的东西
theism n. 一神论，有神论
them pron.他(她)们，它们
theme n.题目；词干；主旋律
themselves pron.他们自己
then adv.那么；然后
thence adv. 由彼处,从那里
thenceforth ad. 从那时,其后
thenceforward ad. 从那时,其后
theocracy n. 神权政治
theologian n. 神学者
theological adj. 神学 (上) 的
theology n. 神学，宗教
theorem n.定理；原理，原则
theoretic a. 理论上的,空谈的
theoretical a.理论(上)的
theoretically ad. 从理论上说
theorist n. 理论家,空谈家
theorize  vi. 创立理论
theory n.理论；原理
theosophy n. 见神论,接神论,接神学
therapeutic adj. 治病的
therapist n. 治疗学家；治疗专家
therapy n. 治疗；疗法；理疗
there adv.那儿
thereabout ad.在附近，大约
thereabouts ad. 在那附近，大约
thereafter ad.此后，以后
thereby ad.因此，从而，由此
therefor adv.为此; 因此
therefore adv.因此；所以
therefrom ad. 从那里,从此
therein ad.在那里，在那时
thereof ad.它的，其；由此
thereon adv. 关于那
there's there is；there has
thereto ad. 对那,往那边,到那
thereupon ad.因此，于是
therewith ad. 随其,以其,于是
therewithal  adv.其外; 此外; 又
thermal a.热的；温泉的
thermodynamics n. 热力学
thermometer n. 温度计,体温计
thermometre n. 温度计
thermos n. 热水瓶
thermostat n. 恒温机制
thesaurus n.词典，同类词汇编
these pron.&adj.这些
thesis n.论题，论点；论文
thespian adj. 戏剧的，演戏的
thews n.肌肉, 体力
they pron.他们(她们,它们)
they'll (同)they will
they're (同)they are
they've (同)they have
thiamin n.硫胺(维生素B1)
thick adj.厚的；浓的
thicken vt. 使变厚(或粗、密)； 加厚，变浓
thicket n. 树丛，灌木丛
thickly ad. 茂密地；葱葱地；厚厚地；密密地
thickness n.厚(度)；密(度)
thief n.窃贼，偷窃犯
thieve vt. 偷,行窃
thieves thief的复数；贼
thievish a. 有偷窃癖的,象盗贼的,偷偷摸摸的
thigh n.股，大腿
thimble n. 顶针,嵌环,套管
thin adj.瘦的
thing n.事情，东西
think vt.想；想要；认为
thinkable adj. 可以想象的
thinker n. 思想家
thinking n. 思考；思想；见解
thinly ad. 薄地；稀疏地
third num.第三
thirdly ad. 第三
thirst n.渴，口渴；渴望
thirstily ad. 口渴地
thirsty adj.渴的；干燥的
thirteen num.十三，十三个
thirteenth num. 第十三,十三分之一
thirtieth num. 第三十,三十分之一
thirty num.三十
thirty-three n. 三十三
this pron.&adj.这，这个
thistle n. 蓟
thistledown n. 蓟花的冠毛
thither a. 对岸的,那边的
tho ad. & conj. (同)though
thong vt. 装皮带,用皮鞭打
thoracic a. 胸的
thorax n. 胸,胸膛,胸腔
thorn n.刺，棘；荆棘；蒺藜
thorny a. 有刺的
thorough a.彻底的；详尽的
thoroughbred adj. 良种的，纯种的
thoroughfare n. 通路,大道
thoroughgoing a. 彻底的
thoroughly adv. 彻底地；透彻地；充分地；完全地；全面地
those pron.&adj.那些
thou pron. (古，诗)汝，尔
though conj.虽然 ad.可是
thought n.思想；思维；想法
thoughtful a.沉思的；体贴的
thoughtfully adv. 沉思地；深思地；体贴地； 若有所思地
thoughtless a.欠考虑的；自私的
thousand num.千
thousandth a. 第一千,千分之一
thrall n. 奴隶，农奴
thralldom n. 奴隶的身分,束缚
thrash vt.痛打，鞭打 vi.打
thread n.线
threadbare adj. 磨破的，陈腐的
threadlike a. 丝状的,象丝的,细长的
threat n.威胁，恐吓，凶兆
threaten vt.&vi.威胁，恐吓
three num.三
threefold a. 三倍的,三重的
threescore n. 六十,六十岁
three-storeyed adj. 三层楼的
threnody n. 挽歌，哀歌
thresh vt.打谷，脱粒；推敲
thresher n. 打谷者,打谷机,长尾鲨
threshold n.门槛；入门，开端
threw throw的过去式；抛；投掷
thrice ad. 三倍,三次,屡次,十分地
thrift n. 节约,繁荣
thriftless a. 不节俭的,无储蓄心的,浪费的
thrifty a.节俭的；兴旺的
thrill vt.&vi.(使)激动
thriller n. 惊险小说，电影
thrive vi.兴旺，繁荣，旺盛
thriving a.繁盛的
throat n.喉咙
throaty adj. 嗓子沙哑的
throb n. （心脏）的跳动，悸动
throbbing a.跳动的，悸动的
throe n. 剧痛,阵痛
throes n. 剧痛
thrombocyte n. 血小板，凝血细胞
thrombosis n. 血栓形成
throne n.宝座，御座；王位
throng n.群，人群 vt.挤满
throstle n. 画眉鸟,纺织机的一种
throttle v. 掐脖子，扼杀，n. 节流阀
through prep.穿过ad.从头到尾
throughout prep.遍及
throw vt.&vi.投掷；摔倒
throw...to... 把…扔给…
thrown throw的过去分词；抛；投掷
thrum n. 织边,织余,乱弹,纱头,线头
thrush n. 画眉,鹅口疮,蹄叉腐疽
thrust vt.,vi.&n.刺，戳，插
thud n. 砰击声,重击
thumb n.(大)拇指
thumbscrew n. 翼形螺钉,拇指夹
thumbtack n. 按钉，图钉
thump n. 重打,重击声
thumping n. 敲击，打击
thunder n.雷 vi.打雷 vt.吼出
thunderbolt n. 霹雳,雷电,意外,怒喝
thundercloud n. 雷云
thunderous a. 雷声般的
thunderstorm n. 暴风雨
thunderstruck a. 惊愕的,吓呆的,遭雷击的
Thursday n.星期四
thus ad.如此，这样；因而
thwack n. 拍地一声打,强打
thwart v. 阻挠，使…受挫
thyme n. 麝香草属的植物,百里香
thymus n. 胸腺
thyroid a. 甲状腺的,盾状的,甲状软骨的
tiara n. (妇女的) 头饰
tibet n. 西藏
tibetan adj. 藏族的；n. 藏人
tibia n. 胫骨,胫节,从前的一种笛
tick n.滴答声；记号
ticket n.(交通违章)罚款传票
ticket-collector n. 收票员
ticket-office n. 售票处，票房
tickle vt.挠，胳肢；逗乐
tickler n. 棘手的问题，难题
ticklish a. 易倒的,不安定的,难对付的,
tidal a. 潮汐的,定时涨落的
tide n.潮；潮水
tidewater n. 潮水,受海潮影响的河水,低洼的海岸
tidings n. 消息
tidy a.整洁的；整齐的
tie vt.(用绳等)系，栓
tie-in-sale n.搭配销售，搭卖
tier n. 列,行,等级,层
tie-up n. (资金)占用，冻结
tiff v. 吵嘴，呕气； 争执；啜，饮；n. 争执，淡酒
tiger n.老虎
tight adv.紧紧地adj.牢固的
tighten vt.&vi.(使)变紧
tight-fitting adj. 紧身的
tightly adv. 紧地；牢固地；紧紧地，紧密地
tigress n. 母虎,雌虎
tile n.瓦片，瓷砖；贴砖
tiling n. 盖瓦；铺瓷砖
till prep.conj.直到…为止
tillage n.耕种,耕耘
tiller n. 耕种者,分蘖
tilt vt.&vi.(使)倾斜
tilth n. 耕作,耕作深度,耕地
timber n.木料；木材
timbre n. （音乐）音色，音质
timbrel n. 小手鼓
time n.时间
time-consuming a. 费时间的
timely a.及时的；适时的
time-out n. 暂停
timepiece n. 时钟,座钟
times n. 时代；倍；次数
timetable n.时间表，时刻表
time-table n. 时刻表；时间表
timetalbe n.时间表，时刻表；课表
time-waster n. 浪费时间的人
time-zone 国际时区
timid a.胆怯的；羞怯的
timidity n. 胆小,胆怯,羞怯
timidly ad. 胆怯地
timing n. 安排时间
timorous adj. 胆小的，胆怯的
timothy n. 牧草之一种
tin n.锡；罐头
tinct n. 颜色,色彩
tincture n. 颜色,色调,染料,气味,特征,
tinder n. 火绒，火种
tined adj. 尖端的
tinfoil n. 锡纸
ting n. 铃的响声,丁丁声
ting-a-ling n. 铃声,叮铃,叮当
tinge v. 给……染色
tingle vi. 兴奋,激动,感到刺痛,抖动
tinker n. 修补匠,焊锅
tinkle n. 清脆的金属音,叮当声
tinny a.(声音)细弱无力的
tinsel n. 闪亮的金属片,金属丝,金属箔,
tint vt. 给...着色；染色
tiny a.微小的，极小的
tip n.梢，末端，尖，尖端
tipple vt. 不断喝
tipsy a. 喝醉的,倾斜的
tiptoe n.脚趾尖 vi.踮起脚
tirade n. 长篇的攻击性演说
tire vi.疲劳，累；厌倦
tired adj.疲劳的，累的
tireless a. 不疲倦的,不厌倦的,不屈不挠的
tiresome a.使人厌倦的，讨厌的
tissue n.薄绢；薄纸；组织
tissue-type 组织类型
tissue-typing 组织分类
tit n. 山雀,轻打,女人,奶头
titan n. 泰坦神,太阳神,巨人
titanic adj. 巨人的，力大无比的
titbit n. 珍品,珍闻
tithe n. 十分之一之税；小部分
titillate v. 使觉得痒，使…兴奋，使愉快
title n.标题，题目；称号
titmouse n. 山雀类的小鸟
titter n. 嗤笑,偷笑
tittle n. 些量,微量,符号,小点,微小
titular adj. 有名无实的，名义上的
to prep.到...
toad n.蟾蜍，癞蛤蟆
toadstool n. 伞菌
toady n. 谄媚者，马屁精
toast n.烤面包 vt.烘，烤
toaster n. 烤面包器
tobacco n.烟草，烟叶
tobacconist n. 烟草商
toboggan n.平底雪橇
tocsin n. 警钟（的声音），警报
tod 托德(男名)
today ad.在今天；现在
toddle vi. 东倒西歪地走,蹒跚学步,散步
toe n.脚趾，足尖
toga n. 宽外袍,参议员的职位
together ad.共同，一起
toggle n. & v. 触发器；系紧
toil n./v. 辛苦，辛勤劳作
toiler n. 辛苦工作的人,劳动者
toilet n.厕所，盥洗室，浴室
toilsome a. 费力的,辛苦的,劳苦的
token n.象征；辅币；纪念品
tokyo n. 东京(日本首都)
told vt. tell(告诉)的过去式和过去分词
tolerable a. 可容忍的,可以的
tolerance n.忍受，容忍；公差
tolerant a.容忍的；有耐力的
tolerate vt.忍受，容忍，宽恕
toleration n. 宽容,默认,宗教自由
toll n. 通行费,代价,钟声
tolstoy 托尔斯泰(俄国小说家)
tom 汤姆(男名)
tomahawk n. 战斧,钺
tomato n.番茄，西红柿
tomatoes 西红柿
tomb n.坟墓
tombstone n. 墓石,墓碑
tome n. 册,卷,大型书本
tomfoolery n. 愚蠢举动(言语)
tomorrow ad.在明天 n.明天
ton n.吨(重量单位)
tonality n. 音质，音调
tone n.色调，光度；风气
toneless a.单调的，沉闷的
tongs n. 夹子，钳子
tongue n.舌头；语言；口语
tongueless a. 没有舌头的,缄默的,哑的
tonic n. 增进健康之物，补品
tonight ad.在今夜 n.今夜
tonnage n. 登记吨位,排水量
tonne n. 公吨
tonsil n. 扁桃腺
tonsillitis n. 扁桃腺炎
tonsure n. 剃发,剃去头发的部分,削发式
too adv.也
too...to 太…而不能
too...to... 太…而不能…；太…以致不能…
took vt. take(拿)的过去式
tool n.工具；用具
toolbox n.工具箱
toot n. 嘟嘟声,酒宴
tooth n.牙齿
toothache n. 牙痛
toothbrush n. 牙刷
toothpaste n. 牙膏
toothpick n. 牙签
top n.顶；首位 a.顶的
topaz n. 黄晶，黄玉
topic n.(文章的)题目；主题
topical a. 论题的,题目的时事问题的,局部的
topmast n. 中桅
topmost a. 最高的,顶端的
topographical adj. 地形学的
topography n. 地形学，地形
topple v. 倾覆，推倒
topsail n. 上桅帆
topsoil n. 表层土
topsy-turvy ad. 颠倒地,相反地,乱七八糟地
torch n.火炬，火把；手电筒
torchlight n. 火炬之光
tore vt. tear(撕)的过去式
toreador n.  骑马斗牛士
torment n.痛苦 vt.折磨
tormentor n. 使苦痛之人,使苦恼之物,长肉叉
torn v. tear(撕、扯)的过去分词
tornado n. 飓风，龙卷风
toronto n. 多伦多(加拿大城市)
torpedo n.鱼雷，水雷
torpid adj. 懒散的，死气沉沉的
torpor n. 有气无力，死气沉沉
torque n. 转(力)矩，扭(力)矩；项圈；火炬，火把；(英)手电筒
torrent n.奔流，激流，洪流
torrential a. 奔流的，急流的，激烈的
torrents n. 倾注
torrid adj. 酷热的
torso n. （人体的）躯干，躯干像
tort n. 民事侵权行为
tortilla  n. 一种圆形的玉米薄饼
tortoise n.龟，乌龟
tortoiseshell n. 龟甲；玳瑁壳
tortuous adj. 弯弯曲曲的，蜿蜒的
torture n.拷问；折磨 vt.拷打
tory n. & a. 保守党党员(的)
toss vi.翻来复去
tot n. 小孩,少量,合计
total adj.总的 n.合计
totalitarian adj. 极权主义的
totality n. 全部，总数
totally adv. 统统，完全地；全部地
totem n. 图腾，崇拜物
totter v. 摇摇欲坠，步伐蹒跚
touch vt.触摸；接触
touchable 可触知的
touchdown n. 触地,触地得分,着地,降落
touching prep. 提到；a. 动人的，感人的
touch-me-not 含羞草
touchstone n. 试金石,标准
touchy adj. 敏感的，易发脾气的
tough a.坚韧的；健壮的
tough-looking a. 丑恶的
toupee n. 男用假发
tour n.&vi.旅行，游历
tourism n. 旅游业；旅游，观光
tourist n.旅游者，观光者
tournament n. 比赛，（旧时）骑士比武大会
tourney n. 比赛,竞赛,锦标赛
tourniquet n. 止血带
tousle v. 弄乱(头发)
tout 推销，招徕，兜售，招徕业务者；v. 招徕顾客，极力赞扬
tow vt.&n.拖引，牵引
toward prep. 向,对于,为了
towards prep. 向，朝；对于；朝着；走向，近…；为了，有助于
towel n.毛巾，手巾
tower n.塔
towering adj. 高耸的；强烈的；耸立的，杰出的
town n.镇，市镇，城镇
town-folk n. 镇上的人
township n. 镇区
townsman n.市民
toxic adj. 有毒的；中毒的
toxin n. 毒素，毒质
toxoid n. 类毒素
toy n.玩具，玩物
trace n.痕迹；丝毫 vt.跟踪
tracer n. 追踪者,描图者,誊写员
tracery n. 细纹构成之图样,花饰窗格,窗饰
trachea n. 气管,导管,螺旋纹管
tracheitis n. 气管炎
tracheobronchial adj. 气管，支气管的
track n.足迹；(火车的)轨道
trackless a. 无足迹的,无路的
tract n. 广阔的地面,土地,地方,小册子
tractable adj. 易于驾御的，温顺的
traction n. 拖拉，牵引力
tractor n.拖拉机；牵引车
tractor-driver n. 拖拉机手
trade vi.经商，进行贸易
trademark n. 商标
trader n.商人；商船
tradesman n.商人；手艺人
tradition n.传统，惯例
traditional a.传统的，惯例的
traditionally ad. 世代相传地
traduce v. 中伤，诽谤
traffic n.交通，街道，车辆
tragedian n. 悲剧演员,悲剧作家
tragedienne n. 悲剧女演员
tragedy n.悲剧；惨事，惨案
tragic a.悲剧性的，悲惨的
tragical a. 悲惨的,悲剧的
trail n.痕迹；小径
trailer n. 拖车；跟踪者
trailing n. & a. 结尾；尾随的
train n.火车
trainee n. 受训练者；受训者
trainer n. 训练者；教练；训练员，教(练)员
training n.训练，锻炼，培养
trait n. 特征
traitor n.叛徒，卖国贼
traitorous a. 叛逆的,不忠的,口蜜腹剑的
trajectory n. （抛射物）弹道轨道
tram n.(有轨)电车
trammel n./v. 束缚，妨碍，鱼网
tramp vt.&vi.&n.步行，跋涉
trample vt.&vi.&n.践踏，蹂躏
tramway n.木制铁道
trance n.恍惚；出神；发呆
tranquil a.平静的；稳定的
tranquility n. 宁静
tranquilize vt. 使平静；使镇定
tranquillizer n. 镇定剂
transact vt. 办理,处理,执行
transaction n.处理；交易；和解
transatlantic a. 横渡大西洋的,大西洋那边的,
transcend v. 超越，胜过
transcendence n. 超越，卓越
transcendent adj.卓越的,超群的,超凡的; 不寻常的
transcendental adj. 超越经验的，形而上学的.
transcontinental a. 横贯大陆的,大陆那边的
transcribe v. 抄写，转录
transcript n. 抄本,副本,正式文本,成绩单
transept n.  (十字形教堂的) 袖廊
transfer vt.转移；调动vi.转移
transferable adj. 可转让的
transference n.调
transfiguration n. 变形,变貌,变容
transfigure v. 美观，改观
transfix v. 刺穿，钉住
transform vt.改变；改造；变换
transform...into 改变为
transformation n.变化；改造；转变
transformer n.变压器，转换器
transfuse v. 输血，充满
transfusion  n. 注入,输血; 移注
transgress v. 冒犯，违背
transgression n. 违反,犯罪,逸出
transgressor n. 违反者,犯规者,罪人
transient adj. 短暂的，转瞬即逝的
transistor n.晶体管
transit n. 经过,通行,转变,运输线,运输
transition n.转变，变迁；过渡
transitional adj. 过渡的，转移的
transitive a. 及物的
transitory adj. 短暂的
translate vt.翻译，译 vt.翻译
translate...into 把…译成…
translate...into... 把…译成…
translation n.翻译；译文，译本
translator n. 翻译者
translucent adj. 半透明的
transmigration n. 轮回
transmission n.传送；传动；发射
transmit vt.传送，传达；发射
transmitter n. 转送者,传达人,让渡者
transmogrify v. 变得古怪，变形
transmutation n. 变形,变化
transmute v. 变化，变作
transom n. 横档,横楣,横梁
transparency n. 透明,透明度,透明物
transparent a.透明的；易识破的
transpiration n. 蒸发,发散 (作用)
transpire v. 发生，蒸发，泄露
transplant vt.&vi.移植，移种
transplantation n. 移植；移植法
transport n.运输；运输工具
transportable a. 可移动的
transportation n.运输，运送，客运
transpose vt. 交换；调换
transship v. 转运，转船
transshipment n. 转运
transverse a.横切的 n.横轴
trap vt.设陷阱捕捉；诱捕
trapdoor n. 地板门,活板门,活盖
trapeze n. 吊秋千
trapezoid n. 梯形,不等边四边形
trapper n. 设陷阱捕兽者
trappings n. 马具,马饰,装饰
trash n. 废物，垃圾
trauma n. 精神创伤，外伤
traumatic adj. 创伤的；外伤的；受创伤的
travail n. 艰苦劳动，痛苦
travel vi.&n.旅行
traveled a. 见面广的；旅客多的
traveler n. 旅行者
traveller n. 旅客；旅行者
travelogue n. 旅行见闻，游记
travels 游记
traverse vt.横越，横切，横断
travesty n./v. 歪曲，曲解
trawl n. 拖网；v. 用拖网捕鱼，搜罗
tray n.浅盘；碟
treacherous adj. 阴险的，危险的
treachery n. 背叛；背信弃义；阴险
treacle n. 糖浆，过分甜蜜的声调
tread vi.&vt.踩，踏，践踏
treason n.谋反，通敌，叛国罪
treasonable a. 叛逆的,谋叛的,不忠的
treasonous a. 叛逆的,谋叛的,不忠的
treasure n.财富；珍宝 vt.珍视
treasure-house n. 宝库
treasurer n.司库，财务主管
treasury n. 宝藏
treat vt.治疗
treatise n. 论文
treatment n.待遇；治疗，疗法
treaty n.条约；协议，协定
treble n. 最高音部,三倍
tree n.树
tree-dotted 树木点缀的
treetop n. 树顶，树梢
tree-trunk n. 树干
trek n./v. 长途跋涉
trellis n. （葡萄等的）架子，棚子
tremble vi.发抖；摇晃
trembling a. 震颤的
tremendous a.极大的，非常的
tremendously ad. 可怕地；极大地
tremolo n. (意)震音；震音装置
tremor n. 震动，地震
tremulous adj. 颤动的，不安的
trench n.深沟；壕沟，战壕
trenchant adj. 一针见血的，精辟的
trencher n. 挖沟者,战壕兵,木盘
trencherman n. 食量大的人
trend vi.伸向；倾向 n.倾向
trendy a. 流行的，赶新潮的
trepidation n. 恐惧，惶恐
trespass n./v. 侵犯，闯入私人领地
trespasser n. 侵犯者
tress n. 头发一束,卷发,发辫
tresses n. 女人的长发
triad n. 三个一组,三幅一组,三和音
trial n.试，试验；审判
triangle n.三角(形)
triangular a.三角的；三者间的
tribal a. 部落的,种族的
tribe n.部落，宗族
tribulation n. 苦难，磨难，考验
tribunal n. 法庭，裁判所
tribune n. 护民官,军团指挥官,民众保护者,
tributary n./adj. 支流（的），进贡（的）
tribute n.贡物；献礼，贡献
trice n. 瞬间，一刹那v. 吊起
trick n.诡计；计谋
trickery n. 欺骗，诡计
trickle vi.滴，淌 n.滴；细流
trickster n. 骗子,魔术师
tricky adj. 巧妙的，狡猾的
tricycle n. 三轮车,机器三轮车
trident n. 三叉戟,三叉曲线,三叉鱼叉
tried try的过去式(分词)
triennial a. 每三年一次的
trifle vi.玩忽；闲混；嬉耍
trifler  (C) 轻薄者; 戏谑者
trifling a. 微小的；轻浮的；微不足道的
trigger n.扳机 vt.触发，引起
trike n. 三轮车
trill n. 颤声,颤音,啭声
trillion n. 万亿；兆
trilogy n. 三部曲
trim a.整齐的 vt.使整齐
trinity n. 三位一体,三人一组,三个一组的东西
trinket n. 小装饰品，不值钱的珠宝
trio n. 三重唱
triolet n. 八行两韵诗
trip vi.绊；失足 vt .绊倒
tripe n. 肚子,内脏
triphosphate n. 三磷酸盐
triple n. 三倍之数,三个一组
triplicate a. 三倍的,三重的,三乘的
tripod n. 三脚桌,三脚架
trireme n. 三层桨座之战船
tri-service 三军
trite adj. 陈腐的，陈词滥调的
triumph n.凯旋；胜利 vi.成功
triumphal a. 胜利的,凯旋的
triumphant a.得胜的；得意洋洋的
triumphantly ad. 胜利地；洋洋得意地
triumvir n. 三执政官之一人
triumvirate n. 三人执政,三头统治,三人执政之职
trivet n.(用以承托锅等于火上的) 三脚架
trivia n. 琐事，无价值之物
trivial a.琐碎的；平常的
triviality n. 琐事,平凡,轻浮
trod tread的过去式(分词)
troglodyte n. 古代穴居者；隐士
troll vi. 旋转,轮唱,钓鱼
trolley n.手推车；无轨电车
trolley-bus n. 无轨电车
trolly n. 手推车，小车；(美)电车
trombone n. 长号
tron (构词成分)电子管；…器
troop vi.群集，集合
trooper n. 骑兵,骑兵警察,伞兵
troops n. (pl.)部队
trope n. 修辞,比喻
trophy n. 奖品，战利品
tropic n.热带地区；回归线
tropical a.热带的
tropics n. 热带
trot vi.&n.(马)小跑，慢跑
troth n. 真实,诚实,约定
troubadour n. 抒情诗人
trouble n.烦恼；困难 vi.烦恼
troubled adj. 不安的，困惑的；麻烦，使烦恼
troublesome adj.令人烦恼的
troublous a. 纷乱的,骚乱的,动乱不安的
trough n. 木钵,水槽,马槽
trounce vt. 痛打；严责；痛骂
troupe n. 歌唱团，剧团
trouser n.裤子
trousers (pl.)n.长裤
trousseau n. 嫁装,嫁妆
trout n. 鲑鱼
trowel n. 泥刀，小铲子
truancy n. 逃学，旷课
truant n.逃避责任者；逃学者
truce n. 停战，休战（协定）
truck n.卡车
truckle n. 小轮,滑轮
truculence n. 凶猛，粗暴
truculent adj. 残暴的，凶狠的
trudge v. 跋涉
true a.真的；忠实的
truffle n. 块菌
truism n. 自明之理，真理
truly adv.真正地，真实地
trump n. 王牌,法宝,喇叭
trumpery adj. 中看不中用的，无价值的
trumpet n.喇叭，小号
trumpeter n. 小号手
truncate v. 把（某物）截短，去尾
truncheon n. 警棍，警棒
trundle n. 小车轮,脚轮,滚动
trunk n.象鼻；树干
truss vt. 捆绑
trust vt.&n.信任
trusted a. 信任的；
trustee n. 受托人,理事
trustful a. 相信的,信任的
trusting  adj. 信赖的,信任的;  (信任而) 不怀疑人
trustor 委托人，信托人
trustworthy a. 可信赖的
trusty a. 可信任的,可信赖的,可靠的
truth n.真理；真相
truthful adj.  <人>不说谎的,说实话的,诚实的
try vt.审问，审判
try...on 试穿(衣、鞋、帽等)
trying a. 难受的,费劲的
tryout n.选拔表演；(美国口语)选拔赛；努力；n. 试用；预演；选拔赛
trypsin n. 胰岛素
tryst n. 幽会，约会
tsar n. 沙皇
t-shirt n. t恤衫
tub n.桶，盆，浴缸，浴盆
tuba n. 大号,风琴音栓之一种
tubal a. (输卵)管的
tube n.管；电子管，显像管
tuber n. 块茎，球根
tubercle n. 小块茎,小瘤,结节
tubercular a. 有小瘤的,结节的,结核的
tuberculosis n.结核病，肺结核
tubular a. 管状的
tuck vt.折短，卷起；塞
tucker n. 打横褶的人,打褶装置,领布
Tuesday n.星期二
tuff n. 凝灰岩
tuft n. 一簇,丛生植物
tug n.拖；牵引；拖船
tugboat n. 拖船
tuition n.教，教诲；学费
tulip n.郁金香
tumble vi.摔倒，跌倒；打滚
tumbler n. 杯子,一杯量,打滚的人,翻斤斗者
tumbrel n. 拖肥车
tumid adj. 肿胀的；浮夸的；肿起的
tumor n. 『医』肿瘤,瘤,赘瘤
tumour n. 瘤,肿块
tumult n. 骚动,拥挤,混乱
tumultuary adj. 喧嚣的; 骚动的
tumultuous adj. 乱哄哄的，喧哗的
tun n. 大桶，大洒桶
tuna n.金枪鱼
tundra n. 冻原地带
tune n.调子；和谐 vt.调谐
tuneful a. 和谐的,音调谐美的
tungsten n. 钨,钨锰铁矿,金属元素
tunic n. 束腰外衣
tunnel n.隧道，坑道，地道
turban n. 穆斯林的头巾
turbaned a. 缠头巾的
turbid adj. 混浊的，紊乱的
turbine n.叶轮机，汽轮机
turbulence n. 狂暴；汹涌
turbulent a.骚动的，骚乱的
tureen n. 有盖的汤盘,盛汤的碗
turf n.草皮
turgid adj. 浮肿的，浮夸的
turk n. 土耳其人；突厥人
turkey n.火鸡；火鸡肉
turkish n. 土耳其语；a. 土耳其的；土耳其人(语)的
turmoil n. 混乱，骚乱
turn v.翻；转
turn...into 把…变成
turn...on 开；旋开(电灯等)
turn...over 把…翻过来
turncoat n. 背叛者,变节者
turner 特纳(姓)
turning n.旋转；变向；转弯处
turnip n.萝卜，芜菁
turnkey n. 监狱的看守,狱吏
turnover n. 翻覆,翻折,半圆卷饼,周转,流通量
turnpike n.收费高速公路
turnspit  n. 旋转烤肉叉的人
turpentine n. 松脂,松脂精,松节油
turpitude n. 邪恶，卑鄙（行为）
turquoise n. 绿松石，adj. 碧绿的
turret n. 塔楼，角塔
turtle n.海龟，玳瑁；甲鱼肉
tusk n.(象、野猪等的)长牙
tussle n./v. 扭打，搏斗，争辩
tut int. 嘘(表示焦虑,责难的发声)
tutelage n. 保护；教育；监护，指导；守护
tutelar a. 保护的,监护的,保护人的
tutelary adj. 保护的；守护的；监护的
tutor n.家庭教师；导师
tutorial a. 指导的
tuxedo n. 礼服，无尾礼服
TV n. 电视
twaddle n. 胡说八道，瞎扯
twain n. & a. (古)二，对，双
twang n.拨弦声
tweed n. 斜纹软呢,斜纹软呢服
tweet vi. 鸣叫
tweezers n. 镊子
twelfth num.第十二
twelve num.十二
twelvemonth n.十二个月,一年
twentieth num.第二十
twenty num.二十，二十个
twenty-first num. 第二十一
twenty-four num. 二十四
twenty-odd 二十多个
twenty-one n. 二十一；num. 二十一
twice ad.两次，两倍
twig n. 小枝，嫩枝，v. 理解
twilight n.黎明，黄昏；曙光
twill n. 斜纹织物
twin a.孪生的 n.孪生儿
twine n. 合股线,麻线,搓
twinge n. （生理，心理上的）剧痛，刺痛
twinkle vi.&vt.闪闪发光
twins (pl.) & n. 孪生，双胞胎
twirl v. 旋转，急转
twist vt.捻；拧 vi.&n.扭弯
twit v. 责备，挖苦
twitch vi. 急拉,抽搐,阵痛
twitter n. 鸟鸣声,喋喋不休
two num.二
two-dimensional a. 二维的
two-edged a. 双刃的
twofold a. 两倍的,两重的
tycoon n. 企业界巨头，企业家；有钱有势的企业家大亨
tyle n. 胼胝
tyler n. 守门人
tympanic a. 鼓皮似的,鼓膜的,鼓室的
tympanum n.鼓膜,中耳
type n.类型；样式
typewriter n.打字机
typewriting n. 打字; 打字术
typhoid n. 伤寒症
typhoon n.台风
typhus n. 斑疹伤寒症
typical a.典型的，代表性的
typically ad. 有代表性地
typist n.打字员
typography n.(活版)印刷术
tyrannical adj. 暴虐的，残暴的
tyrannize vi. 施行虐政,压制,欺压
tyranny n.暴政，专制；残暴
tyrant n.暴君；专制君主
tyre n.轮胎，车胎
tyro n. 新手
U.S (=the United States)美国
u.s.a (缩)美国
ubiquitous adj. 无所不在的，普通的
udder n. 乳房
UFO n.unidentified flying object 不明飞行物
ugliest a. 最丑的，最丑恶的
ugliness n. 丑陋
ugly adj.难看的
ugly-looking a. 模样丑陋的
uk 联合王国
ukase n. 敕令,法令,布告
ukulele n. 夏威夷的四弦琴
ulcer n. 溃疡，腐烂的事物
ulcerate v. 溃烂，生恶疮
ulm n. 乌尔姆(德国地名)
ulster n. 系带的宽大衣
ulterior adj. 较晚的，较远的，不可告人的
ultimate a.最后的，最终的
ultimately adv. 最后，终究；最终；终于
ultimatum n. 最后的话,最后通牒,基本原理
ultimo adj. 上月的
ultra a. 过度的,过激的,极端的
ultramundane adj. 超俗的，世界之外的
ultrasonic n. 超声波；adj. 超声速的；超音速的；超声的
ultrasound n. 超声
ultraviolet a.紫外的n.紫外线辐射
ululate v. 哀鸣；大声叫喊
um interj. 嗯
umber n. 棕土,焦茶色
umbrage n. 不快，愤怒
umbrageous a. 成荫的,阴翳的,多荫的
umbrella n.伞
ump n. 裁判员；vt. 当裁判
umpire n. 裁判，v. 对…进行仲裁
un 联合国(united nations)
unabashed adj. 不畏惧的，不害躁的
unable adj.不能的，不会的
unabridged a. 未经删节的,完整的
unabsorbed a. 未被吸收的
unacceptable adj. 不能接受的
unaccommodating adj. 不能通融的
unaccountable a. 无法解释的,无责任的
unaccountably ad.无缘无故地
unaccustomed a. 不习惯的,不惯的,异乎惯例的,
unadvised adj. 草率的，鲁莽的
unadvisedly ad. 鲁莽地,不顾前后地,欠思虑的
unaffected adj. 自然的，不矫揉造作的
unaffordable adj. 买不起的
unafraid a. 不怕的，不畏惧的
unaided a. 无助的；独立的
unalloyed adj. 未掺杂的，纯粹的
unalterable a. 不能改变的,不变的,坚定不移的
unanimity n. 全体一致
unanimous a.(全体)一致的
unanimously ad. 一致同意的
unanswerable a. 无法回答的,没有责任的
unanswered a. 未答复的
unapproachable a. 不易接近的,不可亲的,无与伦比的
unarm vt. 缴械
unassuaged adj. 未满足的
unassuming adj. 不摆架子的，不造作的
unavailable a. 不能利用的
unavailing adj. 无结果的，徒劳无功的
unavoidable adj. 不可避免的
unaware a. 不知道的
unbalanced a. 不平衡的
unbar vt. 拔去横木,拔去门闩,打开
unbearable a.难堪的，忍受不了的
unbecoming a. 不适合的,不得体的,不相配的
unbelief n. 不信,疑惑,不信仰
unbelievable a.难以置信的
unbeliever n. 不相信者,不信仰者,异教徒
unbiased a. 没有偏见的
unbiassed adj.公正的
unbidden adj. 未经请求的，未经邀请的
unbind vt. 解,解开,解放
unblemished a. 无瑕疵的,无缺点的,无污点的,
unborn a. 未诞生的,未来的,在胎内的,
unbosom vt.vi. 吐露心事,剖明心迹
unbound a. 已获得自由的,未装订的
unbounded adj. 无限的
unbridled a. 无缰辔的,无羁勒的,无拘束的
unbroken adj. 未破的,完整的,完好的
unbuckle vt. 解开
unbutton vt. 解开...的钮扣,
uncalled-for a. 多余的；不适宜的
uncanny adj. 神秘的，不可思议的
unceasing a. 不绝的,不断的,不停的
uncertain a.无常的；不确定的
uncertainly ad. 不明确地；怀疑地
uncertainty n. 不确定,不可靠,半信半疑
unchain vt. 解除,释放,解放
unchallenged a. 无可匹敌的
unchanged a. 不变的；依然如故的
uncharitable a. 无慈悲心的,无情的,不宽恕的
uncharted adj. 地图上没标明的
unchaste a. 无节操的,不贞的,不简洁的
unchristian adj.非基督教徒的; 反基督精神的;
uncivil a. 无礼貌的,失礼的,粗野的,不文明的
unclaimed 无人认领的，无人主张的
unclasp vt. 解开…的扣子
uncle n.叔，伯，舅，姨父
unclean a. 不洁净的,不纯洁的,行为不检的
unclose vt. 揭开,打开
uncollectible 无人认领的；无法收集的，无法收回的
uncomfortable a.不舒服的；不自在的
uncommitted adj. 不受约束的，不承担责任的；(犯罪)未遂的；未作保证的，中立的(中立国)
uncommon a. 不寻常的,不凡的,罕有的
uncomplaining adj. 没有怨言的；不诉苦的；不发牢骚的；坚忍的
uncomplicated a. 不复杂的
uncompromising a. 不让步的,不妥协的,强硬的
unconcerned a. 不关心的
unconditional a. 无条件的,无限制的,绝对的
unconditionally adv. 无条件地
unconfirmed 末经确认的
unconscionable adj. 无节制的，过度的
unconscious a.不省人事的
unconsciously ad. 无意识地；不觉察地
unconsciousness n. 无意识,意识不清,人事不省
unconstitutional a. 非立宪的,违反宪法的,违宪的
unconventional a.不寻常的；不按惯例
uncork vt. 拔去塞子,开口,泄漏,透露
uncouple vt. 解开,分开
uncouth adj. 笨拙的，无教养的
uncover vt.&vi.揭开...的盖子
uncovered 末包装的，末冲销的
uncrumpled a. 衣冠整洁的
unction n. 注油,涂油式,津津有味,虚情假意,
unctuous adj. 油腔滑调的
uncultivated a. 不文明的,无教养的
undated a. 无定期的；不限日期的
undaunted adj. 不屈不挠的，无畏的
undeceive vt. 使不受欺骗,使醒悟
undecided a. 未定的
undeclared a. 未经宣布的
undefiled a. 无污的,洁净的,洁白的,纯粹的
undefined a. 不明确的,未下定义的
undeniable a. 不可否认的
undeniably  adv. 无可否认地,分明地,明显地
under prep.在...下面
underbrush n. 树林下的草丛,丛林
undercharge n.潜流；(思想，情绪)暗流
underclothes n. 内衣,贴身衣
undercover a. 秘密从事的,秘密的,被雇间谍活动的
undercurrent n. 下面的水流,暗流,潜流
undercut 削价出售
underemployment 就业不足
underestimate vt.低估，看轻
underfoot ad. 在脚下面,碍事
undergo vt.经历，经受，忍受
undergone undergo的过去分词
undergraduate n.大学肆业生
underground adj.地下的
undergrowth n. 下层丛林,生于大树下的矮树
underhand a. 秘密的,下投的,欺瞒的
underhanded adj. 不光明的，卑鄙的
underlie vi. 构成...的基础
underline vt.着重；预告
underling n. 下属，手下
underlying adj. 根本的，基础的；下层的；优先的；潜在的，在下面的
undermentioned adj. 下述的
under-mentioned 下述的
undermine v. 破坏，损坏
underneath ad.在下面，在底下
undernourished a.营养不良
underpin v. 加固；支持
underplay v. 表演不充分，对...轻描淡写
underrate vt. 低估,估计过低,看轻
underscore vt. 强调，加强
undersell vt. 以低于市价售出,抛售
undershirt n. 汗衫
underside n. 下侧；下面
undersigned adj. 在…下面签名的
undersirable a.不受欢迎
understand vt.懂；获悉 vi.懂得
understandable a. 可理解的
understanding n.理解；理解力；协定
understock n. 供货不足
understood understand的过去式；理解
undertake vt.约定，保证；从事
undertaker n.承办者，企业家
undertaking n. 任务，工作；事业；许诺；承担；事业；计划
under-tens n.10岁以下的孩子
undertone n. 低音,浅色,小声
undertook undertake的过去式
underwaist n. 穿在马甲下的胸衣,小孩的内衣
underwater a. 在水下的
underwear n.衫衣，内衣，贴身衣
underwood n. 树林下的草丛,丛林
underworld n. 地狱,下层社会,尘世
underwrite 包销，承销，保险；承保，认购
underwriter n. 保险商，承购人；保险业者，承保人，承销人
underwriting 包销，承销；保险
undesirable a.不合需要的；讨厌的
undetected a.未被发现的；未被觉察的
undeveloped a. 未开发的
undisguised a. 无伪装的,不戴假面具的,公然的
undisputed a. 无可置辩的,无异议的,确实的
undistinguished  adj. 无杰出之处的,平凡的
undisturbed a. 安静的,镇定的
undo vt.解开，打开；取消
undoing n. 毁灭，祸根；崩溃
undone a. 未完成的,破灭的,解开的
undoubted a. 无疑的,确实的
undoubtedly adv. 无容置疑地；肯定地；无疑地，确实地；无庸置疑；真正地
undoubting a. 不怀疑的，有信心的；轻信的
undraw vt. 拉开,被...拉回
undress vt.使脱衣服vi.脱衣服
undue a. 不适当的,过度的,未到期的
undulate v. 波动，起伏
undulation n. 波动,弯曲,起伏
unduly ad. 不适当地,过度地
undying a. 不死的,不灭的,不朽的
unearth v. 挖出，发现
unearthly a. 非尘世的,神秘的,怪异的
uneasily ad. 不安地；局促地
uneasiness n. 不舒适,不安,局促
uneasy a.不安的；拘束的
uneconomical a.不节俭
unemployed a. 失业的,未被利用的
unemployment n.失业；失业人数
unequal a. 不相等的,不规则的,不能胜任的
unequivocal a. 不含糊的,不模棱两可,明白的
unerring a. 有错的,无过失的,没有打歪的
unethical a.不道德的；非伦理的
uneven a. 不平坦的；不公平的；不均等的
unexampled adj. 空前的，无前
unexceptionable a. 无懈可击的,极好的,完全的
unexpected a.想不到的，意外的
unexpectedly ad. 出人意味地；意外地；突然地；未料到地
unexplained a. 未得到解释的
unfailing adj. 无尽的，无穷的
unfair adj.不公平的
unfaithful a. 不诚实的,不忠实的
unfaltering a. 不晃晃摇摇的,坚决的,专心的
unfamiliar a. 不熟悉的
unfasten vt. 解开,放松
unfathomable a. 难测的,深不可测的,无底的
unfathomed adj. 深不可测的，无法理解的
unfavorable a. 不宜的,不理想的
unfavourable adj.不利的，反对的
unfeeling a. 无感情的,无情的,冷酷的
unfeigned a. 不虚伪的,真实的,诚实的
unfettered adj. 无忧无虑的
unfinished a. 未完成的
unfit adj.不合适的
unfold vt.展开 vi.呈现
unforeseen a. 无法预料的
unforgettable v. 展开，打开
unforgivable a. 不可原谅的
unformatted a. 无格式的
unfortunate a.不幸的；可取的
unfortunately adv. 不幸地，不凑巧；倒霉地；可惜；遗憾地；a. 使人遗憾的，不幸的
unfounded adj. 无事实根据的
unfriendly ad. 不友善地
unfruitful a. 无效果的,徒然的,空的
unfurl v. 打开，展开
ungainly adj. 笨拙的，不雅的
ungodly a. 无信心的,不敬畏神的,邪恶的
ungovernable a. 难管制的,难压制的,放肆的
ungracious a. 不殷勤的,没有教养的,无礼貌的
ungrateful a. 忘恩负义的,使人不愉快的,徒劳的,
unguarded adj. 不留神的，没有防备的
unguent n. 药膏，软膏
unhallowed a. 未使神圣的,不神圣的,污渎的
unhand vt. 将...放掉
unhandsome adj. 不美的; 丑的
unhappiness n. 不幸福
unhappy a.不幸福的，不快乐的
unhealthy adj. 不卫生的；不健康的；不高兴的，愁苦的
unheard a. 听不到的,未被倾听的,未知的
unheard-of a. 无前例的,前所未闻的,空前的
unholy a. 不神圣的,不洁净的,邪恶地
unhorse vt. 赶…下马
unhurt  adj. 未受损的,未受害的,无伤的
unicorn n. （传说中的）独角兽
unidentified 末查明的，末识别的
unification n. 统一,联合,一致
unified 统一的
uniform a.一样的 n.制服
uniformity n. 同样,划一,一致
uniformly adv. 相同地；一贯；单调地，一样地；一致地，齐心地
unify vt. 统一,使成一体
unilateral a. 单方面,单边的,片面的
unimaginative a. 缺乏想象力的
unimpeachable adj. 无可指摘的，无可置疑的
unimpeded a. 无阻碍的
unimportant adj. 不重要的；琐碎的；平凡的；无价值的
uninformed a. 未得到通知的
uninhibited adj. 无拘束
uninitiated a.不知情的
unintelligible a. 无法了解的,难解的,莫明其妙的
uninterested adj.冷淡的；不感兴趣的
uninterrupted a.不中断的
union n.联合；联合会，团结
unionist n. 工会会员
unions 联合会
unique a.唯一的，独一无二的
uniquely ad. 唯一地
uniqueness n.唯一；独特；无与伦比
unison n. 调和,和谐,齐奏,齐唱,一致
unit n.单位；单元；部件
unite n. 联合，统一，合并，(使)一致行动；vi. 统一；联合；团结；vt. 使联合；联合会，使结合
united adj. 统一的；联合的
uniton n. 联合；联盟
unity n.单一；统一；团结
universal a.宇宙的；普遍的
universality n. 普遍性,一般性,普及
universally adv. 普遍地；一般地
universe n.宇宙，世界
universities 大学
university n.综合性大学
unjust a.非正义的；不公平的
unkempt adj. （衣服，头发）不整洁的
unkind a.不仁慈的，不和善的
unkindness n.不友善，不客气
unknown adj.不为人所知的
unlace vt. 解开带子
unlawful a. 非法的,私生的
unlearned a. 无学问的,无教育的,不学而知的
unleavened a. 没放酵粉的,未受激发的
unless conj.除非，如果不
unlettered a. 无教育的,无学问的,文盲的
unlike a.不同的 prep.不象…
unlikely a.未必的，未必可能的
unlimited a.无限的；不定的
unload vt.从...卸下货物
unlock vt.开门，箱等
unloose vt. 解开,松开,放开
unlucky a.不幸的；不吉的
unmade a. 未经修筑的
unman vt. 使失去男子气质,使怯懦,使气馁
unmanly a. 无男子气概的,女人似的,怯懦的
unmanned a. 无人的
unmannerly a. 无礼貌的,撒野的,粗鲁的
unmarked a. 没有标记的
unmarried a. 未婚的，独身的
unmask vi. 脱去假面具
unmatchable a. 不能匹敌的,无法对抗的
unmeaning a. 无意义的,无所谓的,发呆的
unmeasured a. 不可测的,无法测定的,没有限度的
unmeet a. 不适合的,不适当的
unmerchantable adj. 无销路的
unmindful a. 不留心的,不注意的,漫不经心的
unmistakable  adj. 不会弄错的,不致于被误解的,明显
unmitigated a. 未缓和的,未减轻的,纯然的
unmoved a. 不动摇的,坚决的,冷静的
unnatural a. 不自然的,反常的,不近人情的
unnecessarily ad. 不必要地
unnecessary a.不必要的，多余的
unnerve vt. 使失去气力,使丧失勇气,使焦躁
unnoticed  adj. 未被发觉的,不被注意的,不被顾及
unnumbered a. 没有数的,数不清的,无数的
unobserved a. 没有观察到
unobstrusive adj. 考虑周到的；不容易看到的
unobtainable adj. 无法得到的
unoccupied a. 空闲的,没人占的,未被占领的
unpack vt. 卸下,打开,解除
unpaid a.未付的；不支薪水的
unparalleled a. 无比的,优良无比的,空前的
unpeople  vt. 自…迁移居民;  (因瘟疫、暴力等而
unpleasant a.令人不快的，讨厌的
unpleasantness  n.不愉快,煞风景,扫兴
unpopular adj. 不受欢迎的,名声不佳的,不流行
unprecedented a. 空前的
unprecedentedly adv. 空前地
unpredictable a. 无法预测的
unprejudiced a. 无偏见的,没有成见的,公平的
unpremeditated a. 无预谋的,非故意的,偶然的
unprepared a. 无准备的,即席的,还没有准备好的
unpretending a. 不虚装门面的,不矜持的,谦逊的
unprincipled a. 无原则的,不道德的,不合人道的
unproductive adj. 无生产力的
unprofitable a. 无利益的,不赚钱的,不上算的
unpronounceable  adj. 不能发音的; 难以正确发音的
unprovoked adj. (生气等)无缘无故的
unqualified 没有资格的，无条件的
unquenchable  adj. 不能消除的,无法抑制的
unquestionable a. 无疑问的,确实的,无可挑剔的
unquestionably ad. 当然地，无可非议地
unquestioned adj.不成问题的,毫无疑问的
unquiet a. 不平静的,动摇的,不稳的
unravel v. 解开，拆散
unreal adj. 非真实存在的,想像的,虚构的,非
unrealistic a. 不真实的
unreasonable a.不讲道理的；过度的
unreasoning a. 盲目冲动的
unrecognized a. 未被认出的
unredeemed 末履行的，末偿还的
unreflecting a. 不反省的,无思虑的,浅薄的
unregarded a. 不受注意的,不被关心的,被疏忽掉的
unregenerate  adj.  (精神上、宗教上) 不能重生的,罪
unrelated a. 互不相关的
unrelenting a. 不宽恕的,无情的,冷酷的
unreliable a. 不可靠的
unremitting a. 不懈的,不断的,坚忍的,持续的
unreserved a. 不客气的,不隐瞒的,坦白的
unrest n. 不安的状态,动荡的局面
unrestrainedly ad. 无限制地
unrivaled adj.无敌的，无与伦比的
unrivalled adj.无敌的，无与伦比的
unruffled a. 不骚动的,不混乱的,安静的
unruly adj. 粗野的，无法无天的
unsafe a. 不安全的,不安稳的,危险的
unsalable adj. 不好销售的
unsatisfactory a.不能令人满意的
unsavory n.不好的，令人讨厌的
unsavoury adj.不好的，令人讨厌的
unsay vt. 取消,撤回
unscathed adj. 未受损伤的，未遭伤害的
unschooled adj. 没进过学校的，没有经验的
unscrew vt. 拧开，旋开
unscrupulous adj. 肆无忌惮的，无天理的
unsearchable a. 找不出的,不能探究的,神秘的
unseemly adj. 不适当，不宜
unseen adj.未看见的
unselfish a. 不自私的,无欲的,不任性的
unselfishness n. 无私；慷慨
unsettled a. 未处理的,未决定的
unsettling a. 令人不安地
unshakable a. 不可动摇的
unsheathe vt. 抽出鞘,拔出
unshift v. 未移动，不移档
unshod a. 未穿靴的,赤脚的,未钉铁蹄的
unsightly  adj. 难看的,不体面的,不雅观的,刺眼
unsigned a. 无符号的
unsinkable a. 不沉的
unskilful a. 不熟练的
unskilled a. 不熟练的,未成熟的,拙劣的
unskillful a. 笨拙的,不熟练的,不灵巧的
unsmiling a. 板着脸，不笑的
unsophisticated a. 简单的；不复杂的；质朴的；天真的
unsought  adj. 未经 (搜寻) 追求的; 意外获得的
unsound a. 不健全的,有病的,不可靠的,
unsparing adj.不吝啬的,大方的,慷慨的
unspeakable adj.不能 (以言语) 表达的,无法形容的
unspotted adj. 清白的，无污点的
unstable a.不稳固的；不稳定的
unsteadiness n. 不稳定
unsteady adj. 不安定的,不稳的; 摇晃的
unstudied adj. 不造作的，优雅的
unsuccessful a. 不成功的，失败的
unsuitable adj. 不合适的，不适宜的；(for)足够的，充分的
unsuited a. 不适宜的,不适合的,不适当的
unsullied a. 无污点的,清白的
unsung a. 未被唱的,未在诗歌受歌颂的,
unsuspected adj. 未被怀疑的,没有被认为奇怪的
unsympathetic a. 不表示同情的
untenable a. 不能防守的,不能维持的,支持不住的
unthankful a. 不感谢的,不感恩的,不知感谢的
unthinkable adj.不可想象的
unthinking a. 无思想的,不留心的,无思虑的
untidy a. 不整齐的，零乱的
untie vt.解开，松开；解放
until conj.直到...为止
untimely a. 过时的
untiring a. 不疲倦的,不懈的,不屈不挠的
untold adj. 未说出的,未叙述的,没有说到的
untouched adj. 原样的；未动过的；未触动过的；未碰过的
untoward adj. 不幸的，（坏事）没料到的
untrue a. 不正确的,不忠实的
untruth n. 不真实,虚伪,谎言
untruthfulness n. 虚伪
untutored a. 未受教育的,粗野的,幼稚的
unusable adj. 无法使用的
unused a. 不用的,不使用的,从未用过的
unusual adj.不常见的；奇异的
unusually a. 不平常地，非常；ad. 异常地；非常
unutterable adj. 说不出的,非言语所能表达的
unveil vt. 揭开,揭幕,除去...的面纱
unversed adj不熟练的，不熟知的
unwanted a. 不需要的，多余的
unwarranted adj. 无根据的
unwary a. 不注意的,不留心的,疏忽的
unwearied a. 疲倦的,不累的,孜孜不倦的
unwelcome adj.不受欢迎的,不被喜欢的
unwept a. 无人哀悼的,无人悲泣的
unwholesome a. 不适合健康的,有害身体的,腐败的
unwieldy adj. 笨重的，笨拙的
unwilling a.不愿意的
unwillingly ad. 不情愿地，勉强地
unwise adj.愚蠢的
unwitting adj. 无心的，不经意的
unwittingly  adv. 不自觉地,非故意地,不经心地
unwonted a. 不习惯的,不寻常的,非习常的
unworkable adj. 行不通的
unworthiness n. 无价值,不配得到,不值得尊敬
unworthy a. 不值得的,不足取的
unwrap vt. & vi. 打开；解开
unwritten a. 没有写的,没有记录的,口头的
up ad.向上；起床，起来
upbraid v. 斥责，责骂
upbringing n.抚育，抚养；教养
update v. 更新，修改，校正
updated a. 适时的，更新的
upgrade v. 升级，提高质量
upheaval n. 大变动，改变；动乱
upheave vt.vi. 举起,推上去使上升,隆起
uphill a. 上坡的,向上的
uphold vt.举起；支撑；赞成
upholder n. 支持者
upholster vt. 装饰,装潢
upholsterer n. 室内装璜商
upholstery n. 室内装潢品（地毯，窗帘等）
upkeep n. 维持,维修费
upland n. 丘陵地,高地,丘阜
uplift n. 高扬,道德的向上,精神昂扬
upmost a. 最高的,最上的
upon prep.在...上面
upper a.上面的；地位较高的
uppercase n. 大写字母
uppercut n. (价格)上涨
uppermost a. 最上的,最高的,最上面的
upraise vt. 举起,提高
uprear vt. 扶起,养育
upright a.垂直的；正直的
uprightness n.正直，诚实
uprise n. 升起,起立,上坡,出现
uprising n. 叛乱；起义，暴动
uproar n.骚动，扰乱；喧嚣
uproot vt. 连根拔起
upset adj.难过的；不安的
upshot n. 结果,结局,结尾
upside n.上部；上边
upside-down a.颠倒的，乱七八糟的
upstage adj. 骄傲的，高傲的
upstairs adv.在楼上adj.楼上的
upstart n. 突然升官的人，暴发户
upstream ad. 向上游,逆流地
upsurge n. (情绪)高涨
upswing n. 上升，增长
uptight adj. 焦虑不安的，紧张的
up-to-date a.直到最近的，现代的
uptown n. 住宅区
upturn n. 情况好转,向上的趋势
upward adv.向上
upwards adv. 向上；趋向上升；以上；(同)upward
ural n. 乌拉尔(原苏联一地区)
uranium n.铀
Uranus n. 天王星
urban a. 城市的
urbane adj. 温文尔雅的，懂礼的
urbanity n. 都市风格,殷勤,文雅
urchin n. 淘气鬼,顽童,小孩
urea n. 尿素
urge vt.激励；催促
urgency n. 紧急,催促,强求
urgent a.紧急的；强求的
urgently adv. 紧急地
urgy (构词成分)制作工艺
uri 上呼吸道感染
urinal n. 尿壶,小便所
urinary a. 泌尿的；尿的
urine n. 小便,尿
urn n. 瓮,缸,坟墓
ursine adj. 熊的，像熊的
us pron.(宾格)我们
usa 美国
usage n.使用，对待；惯用法
use vt.用；耗费 n.用
used vi.过去常常
useful adj.有用的；有益的
usefully 通常
usefulness n.有用，有益
useless a.无用的，无价值的
uselessly ad. 无用地；徒劳地
user n.用户，使用者
usful a. 有用的，实用的
ush vi. 作招待员
usher n. 领座员，招待员，v. 引，领
usual adj.通常的；平常的
usually adv.通常
usufruct n. 用益权,使用权,行使用益权
usurer n. 高利贷者
usurious adj. 放高利贷的
usurp v. 篡夺，霸占
usurpation n. 篡夺,霸占,夺取
usurper n. 篡夺者,夺取者
usury n. 放高利贷
utah 犹他(美国一州名)
ute n. 载货汽车
utensil n.器皿，用具
uterus n. 子宫
utilise v. 利用，使用
utilitarian adj. 功利的，实利的
utility n.效用，有用，实用
utilization n.利用，效用
utilize vt.利用
utmost a.最远的 n.极限
Utopia n. 理想国
utopian adj. 乌托邦式的，梦想的
utter a.完全的，彻底的
utterance n. 说话,发表,说话的方式,死
utterly ad. 完全地
uttermost = utmost n.极限,最大限度,极力
utulization n. 利用
uvula n. 悬雍垂,小舌
uxorious adj. 宠爱妻子的
vacancy n. 空白，空缺
vacant a.空的；未被占用的
vacate v. 空出
vacation n.假期，休假
vaccinate vt.给…种牛痘
vaccination n. 预防注射，种痘
vaccine n. 牛痘苗，疫苗
vaccum n.真空
vacillate v. 游移不定，踌躇
vacillation n. 游移不定,踌躇,不果断
vacuity n. （想象力等）贫乏，无聊，空白
vacuous adj. 发呆的，无意义的
vacuum n.真空；真空吸尘器
vacuum-flask n.保温瓶，热水瓶
vagabond n. 浪荡子，流浪者，adj. 流浪的
vagary n. 奇想，异想天开
vagrancy n. 漂泊，流浪
vagrant n. 流浪汉,漂泊者,无赖
vague a.模糊的，含糊的
vaguely ad. 含糊地，暖昧地
vail v. 脱帽；低垂
vain a.徒劳的；自负的
vainglorious adj. 自负的，虚荣心强的
vainglory n. 自夸,自负,虚荣
vainly adv. 徒劳地；虚荣地；自负地
valance n. 帷幔,装饰窗帘
vale n. 谷,溪谷,再见
valediction n. 告别演说，告别词
valedictory a. 告别的
valence n. 价，原子价，化合价
valent (构词成分)(化学)…价的
valentine n. 情人
valerian n. 颉草属植物,自其根茎采制之镇静剂
valet n. 贴身男仆
valetudinarian n. 体弱的人，过份担心生病的人
valian n. 坏蛋
valiant adj. 勇敢的，英勇的
valiantly ad. 勇敢地，英勇地
valid a.有效的；正当的
validate v. 使…生效
validity n.有效，效力；正确
valise n. 旅行袋，手提旅行箱
valley n.流域；(山)谷
valleys 山谷
valor n. 勇猛；英勇
valorous a. 勇敢的,勇武的,刚勇的
valour n. 英勇（
valuable n.贵重物品，财宝
valuables 贵重物品
valuation n. 评价,估价,价值判断
value vt.尊重，重视，评价
valued adj. 宝贵的
valve n.阀，阀门；电子管
vamp n. 靴面，鞋面
vampire n. 吸血鬼
van n.大篷车，运货车
Vandal  n. 摧残文化、艺术者; 破坏他人或公
vandalism n. (对公物)恶意破坏；破坏公物
vandalize v. 肆意破坏
vane n. 风向标,风信旗,变化不定的事物
vanguard n. 前卫，先锋
vanilla n. 香草，香子兰
vanish vi.突然不见，消失
vanished a. 消失了的
vanity n.虚荣心，虚夸
vanquish v. 征服，击溃
vantage n. 优势,有利情况
vapid adj. 索然无味的
vapor n. 蒸汽
vaporize vt.vi. (使)蒸发
vaporous adj.发出蒸汽的
vapour n.汽，蒸气
vargas n. 瓦格斯(男名)
variability n. 变化性，变化无常
variable a.易变的 n.变量
variance n. 矛盾，不同
variant adj. 不同的，不一致的；易变的；n. 变体，变种，变形
variation n.变化，变动；变异
varied adj. 不同的；各种各样的
variegated adj. 斑驳的，形形色色的
variety n.多样化；种类；变种
various a.各种各样的，不同的
varlet n. 恶棍
varnish n. 清漆，v. 涂上清漆
vary vt.改变；使多样化
varying a. 不同的；变化的，可变的
vascular adj. 血管的，脉管的
vase n.(装饰用的)瓶；花瓶
vaseline n. 凡士林,凡士林的商标名
vassal n. 陪臣，诸侯
vassalage n.家臣的身分,效忠，服从
vast a.巨大的；大量的
vastly ad. 大大地；巨大地；广阔地
vastness n. 巨大,广大,广漠
vat n. 大桶
vaudeville n. 杂耍；轻歌舞剧
vault n.拱顶；地下室，地窖
vaunt v. 吹嘘，炫耀
vaunted  adj. 夸示的,自夸的
veal n. 小牛肉
vector n. 矢量；飞机航线；向量
veer v. 转向，改变（话题等）
vegetable n.植物；蔬菜
vegetarian n. 素食者
vegetate v. 象植物般生活，无所事事
vegetation n. 植物，草木，植被
vegetative adj. 有生长力的,生长的
vehemence n. 热切，激烈；猛烈
vehement adj. 猛烈的，强烈的
vehicle n.车辆，机动车
veil n.面纱，面罩；遮蔽物
vein n.静脉，血管，矿脉
vellum n. 上等皮纸,皮纸文书,牛皮纸
velocipede n. 脚踏两轮车,孩童用三轮车,手压车之一种
velocity n.速度，速率
velvet n.丝绒，天鹅绒
velvety adj. 柔软光滑的，爽口的
venal adj. 唯利是图的，贪脏枉法的
venality n. 唯利是图
vend 卖，出售
vendee 买主
vender n. 小贩,卖主,自动售货机
vendetta n. 世仇，宿怨
vendor n. 小贩
veneer n. （镶于劣质东西上的）镶面板，外表
venerable a. 令人尊敬的；神圣庄严的
venerate v. 崇敬，敬仰
veneration n. 尊敬,崇敬,崇拜
venereal a. 性交的,性病的
venetian a. 威尼斯城的
venge n,仇恨；报复
vengeance n.报复，报仇，复仇
vengeful a. 复仇心重的,报复的
venial adj. （错误等）轻微的，可原谅的
venice n. 威尼斯(意大利港市)
venison n. 鹿肉
venom n. 毒液，恶毒，痛恨
venomous a. 有毒的,恶毒的,分泌毒液的,
vent v. 发泄（情绪），开孔，n. 孔、口
ventilate vt.使通风，使换气
ventilation n. 通风孔；出口
ventral a. 腹的,腹部的,腹侧的
ventricle n. 室,脑室,心室
ventriloquist n. 口技者
venture n.&vi.冒险 vt.敢于
venturesome a. 好冒险的；大胆的
venturous a. 好冒险的,大胆的,不顾一切的
venue n. 集合地点，聚会地点；犯罪地点
venus n. 金星；维纳斯(罗马神话) ；美人；色情
veracious adj. 诚实的，说真话的
veracity n. 真实性，诚实
veranda n. 阳台,走廊
verandah n.阳台,走廊
verb n.动词
verbal a. 词语的,言语的,动词的,逐字的,
verbally ad. 语言上的
verbatim a. 逐字的,照字面的
verbena n. 马鞭草属植物
verbiage n. 罗嗦，冗长
verbose adj. 冗长的，罗嗦的
verbosity n. 唠叨，冗长
verdant adj. 青葱的，翠绿的
verdict n. 判决，决定
verdigris n. 铜锈，铜绿
verdure n. 翠绿,新绿,新鲜,精力旺盛
verdurous a. 碧绿的,绿叶
verge n.边缘，边界，界限
verification n. 检验；核实，核查；证实
verify vt.证实，查证；证明
verily ad. 实在,真
verisimilitude n. 逼真，可能性
veritable a. 真实的,确实的,真的
verity n. 真,真实,真理,真实的陈述
vermeil n. 朱红,朱红色,镀金的银
vermicular a. 蠕虫的,似蠕虫的,蠕动的
vermiform a. 蠕虫状的
vermilion n. 朱红,朱砂,朱红色
vermin n. 害虫，寄生虫
vermouth n. 味美思酒
vernacular adj. 本国语，地方语
vernal adj. 春季的，春季似的
versailles n. 凡尔赛(宫)(法国)
versatile a.多方面的；通用的
versatility n. 多功能；多用途
verse n.诗，韵文；诗行
versed adj. 熟练的，精通的
versification n. 诗律,作诗
versifier n. 诗人,将散文改成韵文的人,拙劣诗人
version n.译文；说法；改写本
versus prep.(比赛等中)对
vertebral a. 椎骨的,脊椎的,由椎骨组成的
vertebrate adj. 脊椎动物
vertex n. （三角形等）顶角，顶点
vertical a.垂直的，竖式的
vertically ad. 垂直地；竖直地，直立地
vertiginous adj. 令人眩晕的
vertigo n. 眩晕
verve n. (艺术作品的)神韵，(人)生机精力
very ad.很；完全 a.真的
vespers  n. 亦作 Vespers
vessel n.容器；船，飞船；管
vest n.汗衫；背心；内衣
vestal a. 女灶神的
vestee n.装饰布,背心形衣着
vestibule n. 前庭,门廊,前厅,
vestige n. (生)退化器官；痕迹,残余，遗迹
vestigial adj. 退化器官的，发音不全的
vestment n. （作礼拜时教士的）法衣，官服
vestry n. 法衣室,祭具室,教堂附属室
vesture n. 衣服，覆盖物
vetch n. 野豌豆
veteran n.老兵，老手
veterinarian n. 兽医
veterinary adj. 兽医的
veto n.否决，否决权，禁止
vex vt.使烦恼，使恼火
vexation n. 困扰，苦恼
vexatious a. 叫人发急的,为难的,着急的,
via prep.经过；通过
viability 可行性，寿命，耐用性
viable adj. 可行的，能活下去的
viaduct n. 高架桥
vial n. 小瓶
viand n. 一件食品
viands n. 食品，食物
vibrancy n. 生气勃勃，活泼
vibrant adj. 振动的，明快的，生气勃勃
vibrate vt.使颤动 vi.颤动
vibration n.颤动，振动；摆动
vibrator n. 振动的人,振动器,振动滚筒
vicar n. 教区牧师,教堂牧师,传教牧师,
vicarage n.教区 (代理) 牧师的住宅
vicarious adj. 间接的，代理的
vice n.罪恶；恶习；缺点
vice-chairman n. 副主席
vicegerent a. 代理的
vice-minister n. 副部长
vice-premier n. 副总理
vice-president n. 副总裁,副校长
viceroy n. 副王,总督,太守
vicinal a. 邻近的，附近的
vicinity n.邻近；附近地区
vicious a.邪恶的；恶性的
vicissitude n. 变化,变迁,荣枯,盛衰
vicissitudes n. (人生的)盛衰，变迁
victim n.牺牲者，受害者
victimize v.使牺牲；使受
victor n. 胜利者
victoria n. 维多利亚
victorian a. 维多利亚女王时代的
victorious a.胜利的，得胜的
victory n.胜利
victual n. 食物
victuals n. 食物，饮食
vide v. (拉)参看，参阅
video a.录象的
videocorder n. 录像机
vie vi. 争,竞争,争胜
vienna n. 维也纳(奥地利)
view n.视域
viewer n. 观众；观察者，电视观众
viewless adj. 看不见的; 无景色的
viewpoint n.观点，看法，见解
view-point n. 观点
vigil n. 警戒,监视,守夜
vigilance n. 警戒,警觉心,失眠症
vigilant adj. 机警的，警惕的
vignette n. (书中的)装饰图案；小品文
vigor n. 精力,活力
vigorous a.朝气蓬勃的
vigorously ad. 精力旺盛地；健壮地
vigour n.活力，精力；元气
vigourous a. 朝气蓬勃；精力充沛的；强有力的
Viking n. 维京人
vile adj. 可恨的，可耻的
vilify v. 辱骂，诽谤
villa n.别墅；城郊小屋
village n.乡村，村庄
villager n.村子里的居民
villagers 村民
villain n. 坏人,恶棍
villainous adj. 邪恶的，恶毒的
villainy n. 坏事,恶行,罪恶
vim n. 精力，活力
vincible adj. 可克服的，可征服的
vindicate n. 为…平反证明…正确
vindication n. 洗冤，证实
vindictive adj. 报复性的
vine n.葡萄树；藤
vinegar n.醋
vinegared adj. 酸的，尖刻的
vineyard n. 葡萄园
vinous a. 葡萄酒的,有葡萄酒性质的,喝醉酒的
vintage n. 采葡萄,酿酒,酒
vintner n. 酒商
viol n. 中世纪的弦乐器
viola n. 中提琴
violate vt.违犯，违背；侵犯
violation n.违犯；侵犯，妨碍
violence n.猛烈，激烈；暴力
violent a.猛烈的；狂暴的
violently ad. 猛烈地；剧烈地；凶暴地；强暴地
violet n.紫罗兰
violin n.小提琴
violinist n. 小提琴演奏者,小提琴家
violoncello n. 大提琴
viosterol n. 维生素d2；钙化醇
viper n. 毒蛇,毒蛇一样的家伙,阴险人
viperine a. 毒蛇的
virago n. 泼妇,悍妇,女英雄
viral a. 病毒的
virgin n.处女 a.处女的
virginal n. 维金纳琴(16-17世纪一种英国古钢琴类乐器)
virginia n. 佛吉尼亚(州)(美国)
virginity n. 处女,处女性,童贞
virile adj. 有男子气的，雄健的
virility n. 雄劲，丈夫气
virtual a.实际上的，实质上的
virtually ad. 实际上，事实上；实质上；几乎；adj. 几乎，差不多
virtue n.善，德；德行；优点
virtuosity n. 精湛技巧，高超
virtuoso n. 演艺精湛的人，大师
virtuous a. 有品德的,善良的,贞洁的,有效力的
virulence n. 有毒,毒性,恶意
virulent adj. 剧毒的，恶毒的
virus n. 病毒
visa n.签证
visage n. 面貌；外观；面容，脸
viscera n. 内脏,内容
visceral adj. 内脏的
viscid a. 粘的,胶粘的,粘质的
viscosity n. 粘度，粘性；粘滞度
viscount n. 子爵
viscous a.粘滞的，粘性的
viscousness n. 粘性，粘滞
vise n. 虎头钳,签证
visibility n. 能见度
visible a.可见的，看得见的
vision n.视力；眼光，想象力
visionary a. 幻影的,幻想的,梦想的
visionphone n. 电视电话
visit vt.常去
visitant n. 访问者; 参观者
visitation n. 访问,探望,正式的视察
visitor n.访问者；参观者
visor n. 面颊,帽舌,盔甲
vista n. 远景，展望
visual a.看的；看得见的
visualize vt. 使看得见,使具体化,想象,设想
vital a.生命的，生机的
vitality n. 活力,生命力
vitals n. 重要器官,要害,命脉
vitamin n.维生素，维他命
vitamine n. 维生素，维他命
vitiate v. 削弱，损害
vitreous adj. 玻璃的；似玻璃的
vitriolic adj. 刻薄的，强烈的
vituperate v. 痛斥，辱骂
vituperative adj. 辱骂的，责骂的
vivacious adj. 活泼的，快活的
vivacity n. 快活,活泼,精神充沛
vivid a.鲜艳的；生动的
vividly adv. 生动地；活泼地
vividness n. 生动(性)
vivify vt.给与生气,使生动,使活跃
vivifying a. 生机勃勃的
vivisection n. 活体解剖
vixen n. 雌狐，泼妇
vizier  n.  (从前回教国的) 高官,大臣
vocabulary n.词汇表，词汇汇编
vocal a. 声音的,有声的,歌唱的
vocalist n. 流行歌手，声乐家
vocation n.职业，行业
vocational a. 职业的
vociferate v. 大叫大嚷，叫喊
vociferous adj. 喧哗的，大叫大嚷的
vodka n.
vogue n. 时髦，时尚adj. 流行的
voice n.说话声；意见；语态
voiceless a. 无声的
void a.空的；无效的
voidable 可撤销的
voile n. 薄纱,纱
volatile adj. 反复无常的，挥发性的
volcanic a. 火山的
volcano n.火山
vole n. 野鼠，田鼠
volition n. 自决，自主
volley n. 群射,齐发,迸发
volleyball n.排球，排球运动
volley-ball n. 排球
volt n.伏特，伏
voltage n.电压
voltmeter n. 伏特计
volubility n. 健谈，流畅
voluble a. 流利的,健谈的,易旋转的,缠绕的
volume n.卷，册；容积；音量
voluminous adj. 长篇的，多产的，庞大的
voluntarily 自愿地
voluntary a.自愿的，志愿的
volunteer n.志愿者 vt.志愿
voluptuary n. 耽于逸乐的人
voluptuous adj. 撩人的，沉溺酒色的
volve  (构词成分)表示"卷"，"旋转"改变，变化
vomit vt. 吐出,呕吐
voracious adj. 狼吞虎咽的，贪婪的
voracity n. 贪食，贪婪
vortex n. 漩涡，漩风
votaress n. 女性信徒,女爱好者
votarist n. 热心者,崇拜者,支持者,信徒
votary n. 崇拜者，热心支持者
vote n.选举，投票，表决
voter n. 选举人
voting adj. 投票；有投票权的
votive a. 奉献的,还愿的,诚心祈求的
vouch vi. 担保,保证,证明,确定
voucher n. 证人,保证人,凭单,凭证
vouchsafe vt. 允许,给予
vow n.誓言，誓约，许愿
vowel n.元音；元音字母
voyage n.航海；航行
voyager n. 航行者,航海者
voyeur n. 窥淫狂者，窥隐私者
vulcanize  vt. 使 <橡胶> 硬化
vulgar a.粗俗的，庸俗的
vulgarity n. 粗俗，低级
vulgarize vt.使通俗化,使粗俗,使下流
vulnerability n. 易损性
vulnerable adj. 易受攻击的，脆弱的
vulpine adj. 狐狸的，狡猾的
vulture n. 秃鹰,贪婪的人
vying adj. 竞争的
wacky adj. (行为等)古怪的，愚蠢的
wad n. 圆团,小块,大量,填料
waddle v. （鸭子等）摇摇摆摆地走
wade vt.趟(河)，跋涉
wafer n. 晶片,圆片,薄饼,干胶片
waffle v. 胡扯，含糊其辞
waft v. 飘浮，飘荡
wag vt.摇，摇摆，摆动
wage n.工资，报酬
wage-earner n. 工资收入者
wager n. 赌,赌博,赌物
waggish adj. 诙谐的，滑稽的
waggly a. 摇摇晃晃的
waggon n.敞蓬车厢
wagon n. 篷车；四轮货运马车
wagoner n. 车夫,御夫座
waif n. 无主物,飘流物,流浪者,信号旗
wail v. 哀号，痛哭
wain n. 运货马车,北斗七星
wainscot n. 护壁板，adj. 用……装饰
waist n.腰，腰部
waistcoat n.背心，马甲
wait vi.等，等候 n.等待
waiter n.侍者(服务员)
waiting n. 等候；伺候；a. 等待的
waitress n.女侍者，女服务员
waive v. 放弃，推迟考虑
wake v.醒
wake...up 唤醒；弄醒
wakeful adj. <人>醒着的,未入睡的
waken vi.醒来 vt.弄醒
Wales n.威尔士
walk vi.&n.走，步行
walkabout n.王室成员或名人在民众中露面散步
walker n. 步行者；竞走者；散步者
walking 竞走
wall n.墙，壁，围墙，城墙
wallet n.钱夹；皮夹
wallflower n.『植物』桂竹香
wallop n./v. 重击，猛打
wallow n./v. （猪等）在泥水中打滚，沉溺于
walnut n.胡桃，核桃树
walrus n. 海象
waltz n. 华尔兹舞,圆舞曲
wampum n.贝壳串珠
wan adj. 虚弱的，病态的
wand n. 棒,棍,杖
wander vi.徘徊；流浪vt.漫游
wanderer n. 流浪者,徘徊者
wandering a. 云游四方的
wanderlust n. 漫游癖，旅游热
wane v. 减少，衰微
wannish a. 稍为苍白的
want vt.要，想要；需要
wanting a. 短缺的；不足的
wanton adj. 顽皮的，放纵的
wantonness n.顽皮，变化无常，任性
war n.战争；冲突，斗争
warble v. 柔和地唱n. 鸟啭
warbler n. 啭鸟,鸣鸟,歌手,用颤音歌唱的人
ward n.病房，病室；监房
warden n. 看守人，管理员
warder n. 看守,守卫,看门人
wardrobe n.衣柜，衣橱，藏衣室
wards 向…的，向
ware n.商品，货物；物品
warehouse n.仓库，货栈
warehousing n. 仓储
wares n. 货物，商品
warfare n.战争，战争状态
warily 留心地
wariness n. 注意,小心
warlike a. 战争的,好战的,尚武的,军事的
warlord n. 军阀
warm adj.暧和的
warm...up 使…暖和
warm-blooded adj. (动物)温血的
warmhearted a. 热情的
warm-hearted adj. 热情的；亲切的；亲近的
warming n. 暖和；加温
warmish a.尚暖和的，有点热的
warmly adv. 热烈地，热情地
warmonger n. 战争贩子；好战者
warmth n.暖和，温暖；热烈
warn vt.警告，告诫
warning n.警告，告诫，鉴诫
warp n./v. 翘起，弯曲
warrant n.许可证，委任状
warranted adj. 担保的
warrantee 被保证人
warrantor 保证人
warranty n. 担保,保证,根据
warren n. 养兔场,拥挤的地方
warrior n. 武士；斗士
warsaw n. 华沙(波兰首都)
warship n.军舰
wart n. 疣,瘿
war-torn a. 遭受战争破坏的
war-weary a. 厌战的
Warwick n.(地名)沃里克
wary a. 小心的,机警的,周到的,唯恐的
was  (动词am，is的过去式)；vi. be(是、在)的过去分词；是(were)
wash vt.洗；冲出 vi.洗涤
washboard n. 洗衣板
washer n. 垫圈,洗涤机
washerwoman  n. 洗衣妇
washing n. 洗；洗的
washing-machine n. 洗衣机
washington n.华盛顿(美国)；华盛顿(姓)
washroom n. 盥洗室
wash-tub n.洗衣盆
wasn't (同)was not
wasp n.黄蜂，蚂蜂
waspish adj. 易怒的，尖刻的
wassail vi. 痛饮
wastage n. 消瘦，衰老
waste n.&vt.浪费
wastebin n. 垃圾箱
wasteful a.浪费的；破坏性的
wastefully ad. 无谓地
wasterful a.使无用的；浪费
wasting a. & n. 浪费(的)
wastrel n. 败家子，挥霍无度的人
watch n.手表
watch-dog n. 看门狗
watcher n. 看守人,守望者,照顾者
watches 手表
watchful a.注意的，警惕的
watchmaker n. 表的制造人,钟表匠
watchman n. 巡夜者,看守人
watchtower n. 岗楼，峰火台；了望塔
watchword n. 口令,标语,口号
water n.水
waterbag n. 水袋
watercourse n. 水路
water-covered adj. 被水覆盖的
watercress  n. 『植物』水瓮菜,水田芥
watered 空头发行的，掺水的
waterfall n.瀑布
waterfowl n. 水鸟
waterfront n. 水边，滩
waterlogged a. 浸泡了水的
waterman n. 船夫,舟子
watermelon n. 西瓜
waterproof a.不透水的，防水的
watershed n. 分水岭，流域
waterskiing n. 滑水运动
water-skiing n. 滑水运动
waterspout n. 海上龙卷风,水落管
water-spout n. 喷水孔
watertight adj.不漏水的，防水的；不透水的；水密的；(计划，措辞等)严密的
water-tight a. 不漏水的
water-vapour n. 水蒸气
waterway n. 航路,水路,运河
water-way n. 水道，航路
waterwheel n. 水车
water-wheel n. 水轮
waterworks n. 供水系统,自来水厂,喷水装置,
watery a.水的；湿的；乏味的
watt n.瓦(特)
wattle n. 编条,枝条,枝条编成的篱笆,
wave n.波，波浪；波动
waveband n. 波段
wavelength n.波长
waver vi.摇摆；犹豫不决
waving adj. 波浪状的
wavy adj. 波浪形的，起伏的
wax n.蜡，蜂蜡
waxen a. 象蜡一样软的,蜡色的,苍白的
waxy a. 象蜡的,蜡色的,苍白的,光滑的,
way n.路；路线；方向
wayfarer n. 旅客
wayfaring a. 旅行的
waylay vt. 埋伏,伏击
wayside n. 路旁
wayward a. 任性的,不定的,刚愎的
we pron.(主格)我们
weak a.弱的；软弱的
weaken vt.削弱 vi.变弱
weakling n. 虚弱的人,病弱者,懦怯者
weakness n.虚弱，软弱；弱点
weal n. 条痕，福利，幸福
wealth n.财富，财产；丰富
wealthy a.富的，富裕的
wean n. 断奶，戒掉
weapon n.武器，兵器
wear vt.穿，戴
wearer n. 穿用者
wearily ad. 疲倦地；厌烦地
weariness n. 疲倦,厌倦,疲劳
wearing-out n. 穿破
wearisome a. 使疲倦的,使厌倦的,厌烦的
weary a.疲倦的 vt.使疲乏
weasel n. 黄鼠狼，鼬，v. 告密
weather n.天气
weather-beaten 经风吹日晒的
weathercock n. 风标,随风倒的人
weatherman n. 气象员
weave vt.织；编
weaver n.织布工，编织者
web n.网，丝，网状物
wed vt.与...结婚,使结合
we'd (同)we had；we should
wedded a. (已)结婚的；献身的
wedding n.婚礼
wedge n.楔 vt.楔入；挤入
wedlock n. 结婚生活
Wednesday n.星期三
wee a. 很小的,微小的
weed n.杂草，野草 vi.除草
weedy a. 尽是杂草的,似杂草的,丑陋的,
week n.星期，周
weekday n.周日，工作日
weekend n.周末，周末假期
week-end n. 周末
weekly a.每周的 ad.每周
ween vt. 想,以为
weep vi.流泪；哭泣
weeping a. & n. 哭泣(的)
weevil n. 象鼻虫之类
weigh vi. 重(若干)；权衡；有分量；估量；重；vt. 称…的重量；掂量；称量；重压；权衡，认真考虑
weight n.重；砝码；重担
weighting n. 偏重
weightless a. 失重的
weightlessness n. 失重
weight-lifter n. 举重者
weightlifting 举重
weighty a. 重的,有份量的,沉重的,肥大的,
weir n. 堰,鱼梁
weird adj. 古怪的，荒唐的
welcome int.&n.&vt.欢迎
weld vt.&n.焊接，熔接
welfare n.幸福，福利
welkin n. 天空
well n.井；泉水；深坑
we'll (同)we shall；we will
well-balanced a. 均衡的
well-being n. 幸福；健康；福利
well-cultivated adj. 精细耕种的
well-cut adj. 衣服剪裁得很好的；(衣服)剪裁得入时的；剪裁合身的
well-dressed a. 穿着讲究的
well-equipped 设备很好的
well-established a.固定下来的
well-informed a. 消息灵通的
well-know 著明的
well-known a.众所周知的，出名的
well-mannered a. 有礼貌的
well-nigh ad. 几乎
well-read a. 博学的
well-to-do a. 小康的，富裕的
well-too-do a.富有的
well-ventilated a. 通风好的
Welsh v. 赖债不还，失信
welt n. 贴边,鞭痕,殴打,世界
welter vi. 翻滚,滚动,挣扎,颠簸,浸湿
wench n. 少女,乡下姑娘,女仆
wend vi. 行,走
went (动词go的过去时)
wept weep的过去式(分词)
were  (动词are的过去式)；be的过去式复数；是
we're (同)we are
weren't (同)were not
werewolf n. 狼人,凶人
wesley n. 韦斯利(男名)
west n.西部，西方
westerly a. 向西的,自西的
western adj.西的，西方的
westerner n. 西方人；欧美人
westerns n. 西部电影或小说
westward a.向西的 ad.向西
westwards ad. 向西
wet adj.湿的
wether n. 阉羊
we've (同)we have
whack vt. 敲击,重打,瓜分,匆忙做好
whale n.鲸；庞然大物
whalebone n. 鲸须
whaler n. 捕鲸者,捕鲸船
whaling n. 捕鲸(业)
wharf n.码头，停泊所
wharfage n. 码头(费)；码头业务
wharves wharf的复数
what pron.&adj.什么
what...for 为了什么
whatever adj.&pron.无论什么
what's (同)what is
whatsoever pron. 无论什么
wheat n.小麦
wheaten a. 小麦的,小麦制成的
wheedle v. （用花言巧语）哄骗
wheel n.轮，车轮
wheelbarrow n. 独轮手推车
wheeze vi. 喘气
wheezy a. 气喘声的
whelk n. 峨螺,粉刺,青春痘
whelm v. 用…覆盖，淹没
whelming a. 淹没的，压倒的
whelp n. 小狗
when ad.什么时候；当…时
whence ad. 从何处；从那里
whenever conj. 每当；无论何时，无论什么时候；无论如何；随时；conj. & adv. 随时；无论何时；无论什么时候，每当
where adv.在哪里
whereabouts n. 下落,所在之处
whereas conj.而，却，反之
whereat ad. 对于…；在这里
whereby ad.靠什么；靠那个
wherefore conj. 为何,因此
wherein ad. 在何处,在其中
whereof ad. 什么的,关于什么的,以什么的
whereon ad. 在什么上面,在那上面
where's (同)where is
whereto ad. 何以,向何处,为什么
whereupon  conj. 于是 (马上) ,然后 (and then)
wherever adv.无论在(到)哪里
wherewith ad. 用什么,用那个,藉其
wherewithal n. 钱财
wherry n. 小船，舢板
whet v. 磨快，刺激
whether conj.是否
whether...or 不管是不是，无论如何；是…还是…
whether...or... 或者…或者…
whetstone n. 磨石
whew n. 吹哨声
whey n. 乳浆
which pron.哪一个
whichever a.无论哪个，无论哪些
whiff n. 一吹,一吸,香烟的一口,一点点,
while conj.当...的时候
whilst conj.同…同时；然而
whim n. 多变，怪念头
whimper v. 悲嗥，鸣咽
whimsical adj. 古怪的，异想天开的
whimsy n. 古怪，异想天开
whine v. 哀号，号哭
whiningly ad. 抱怨地
whinny a. 马嘶声
whip n.鞭子 vt.鞭笞；抽打
whippoorwill  n. 『鸟』嘈杂夜鹰
whir n. 呼呼声,飕飕声
whirl vt.,vi.&n.(使)旋转
whirligig n. 旋转玩具,旋转木马,旋转运动,
whirlpool n. 漩涡,涡流
whirlwind n. 旋风
whirr n. 呼呼声,飕飕声
whisk n. 扫帚,毛掸子,搅拌器,拂
whisker n.髯，连鬓胡子
whiskey n.威士忌酒
whisky n.威士忌酒
whisper vt.低声地讲，私下说
whist int. 嘘!,肃静!
whistle n.口哨声 vi.打口哨
whistler n. 吹口哨的人
whit n. 一点儿，少量
white adj.白色的
white-collar a. 白领的
white-haired adj. 白发的
whiten vt. 使白,漂白
whitener n. 漂白剂
whiteness n. 白；苍白
whitewash n.石灰水 vt.粉饰
whither ad. 到哪里
whithersoever ad. 到任何地方,无论何处
Whitsuntide  n. 圣灵降临节节期
whittle v. 削（木头），削减
whiz n. 子弹等在空中掠过的声音,精明的人,
whizz n. 子弹等在空中掠过的声音,精明的人,
who pron.谁；…的人
whoa  int. 遏!
whoever pron.究竟是谁
whole adj.整个的
wholesale n. 批发，adj. 大批的
wholesaler n. 批发商
wholesaling n. 批发
wholesome a.适合卫生的
who'll (同)who will；who shall
wholly ad.完全地，全部
whom pron.谁(宾格)
whoop n. 大叫,呐喊,喘息声,小块
whore n. 娼妓
whorl n. 轮生体,螺纹,螺旋一环,涡
who's (同)who is；who has
whose pron.谁的；哪个人的
whosesoever  pron. 无论是谁的
why ad.为什么
wick n. 灯芯；油绳
wicked a.坏的；令人厌恶的
wickedly ad. 居心叵测地
wickedness n.邪恶,不正; 恶意,坏心眼
wicker n. 柳条；柳条编的
wicket n. 小门,腰门,售票窗
wide adv.广阔地；充分地
widely adv.广阔地；广泛地
widen vt.加宽 vi.变宽
widespread a.分布广的，普遍的
widow n.寡妇
widower n. 鳏夫
widowhood n. 寡妇的身分,守寡
width n.宽阔，广阔；宽度
wield vt.挥(剑)；行使
wielder n. 行使者
wife n.妻子
wig n. 假发
wiggle vt. & vi. 摆动；扭动，蠕动
wight n. 人类,人
wigwam n. 帐蓬,小屋
wild a.野生的；野蛮的
wildcard n. 通配符
wildcat n. 野猫,莽撞的人
wilderness n. 荒地
wildfire n. 古时攻打敌船所用的燃料剂,
wildlife n. 野生植物
wild-life n. (集合词)野生动物
wildly adv. 暴风雨般地；疯狂地，急切地；发狂地，荒唐地
wile n. 诡计，花言巧语
wilful a. 任性的,固执的,故意的,存心的
wiliness n. 狡猾，诡计多端
will v.aux.将；会；愿
willful  adj. 任性的，固执的；故意的
willing adj.甘心情愿的
willingly adv. 乐意地，自愿地；情愿地
willingness n. 自动自发
willow n.柳树，柳木
willowy adj. 苗条的
willpower n.意志
wilt v. 使…凋谢，枯萎
wily adj. 狡猾的
wimble n. 锥,钻孔器,从钻孔中清除碎石的工具
win vi.获胜 vt.赢得
wince v. 避开，畏缩
winch n. 绞盘,曲柄,绞车
wind n.风
windfall n. 横财
winding n. 卷绕着的线；弯曲的，曲折的，迂回的adj. 卷曲的；弯曲的，蜿蜒的；迂回的
windlass a. 卷扬机,绞盘
windmill n.风车
window n.窗子，窗户，窗口
windowing n. 开窗口
window-seat n. 窗座
window-shop vi. 观看橱窗(而不买)
windowsill n. 窗台
windpipe n. 气管,嗓门
wind-pollination 风媒
windscreen n. 挡风玻璃
windward ad. 向上风
windy adj.有风的；风大的
wine n.酒
wine-cellar n. 酒窖
winery n. 酿酒厂
wing n.翅膀
winged a. 有翼的
wingless  adj. 无翼的; 不能飞的
wink vi.眨眼；使眼色
winkle vt. 挖掘
winner n.获胜者，优胜者
winning n. & a. 胜利(的)
winnow v. 把（谷物）的杂质吹掉，扬去
winsome adj. 媚人的，漂亮的
winter n.冬天，冬季
wintry a. 如冬的,寒冷的,冬的,冷淡的
wipe vt.揩，擦
wire n.(金属)线；电线
wireless adj.无线的，无线电的
wiry a. 金属线制的,铁丝似的,瘦长结实的
wisdom n.(古人的)名言，格言
wise adj.有智慧的，聪明的
wisely ad. 明智地，聪明地
wish vt.&n.希望；祝愿
wisp n. 小把,小物体,纤细的东西
wistful a. 渴望的,想望的
wistfully ad. 渴望地；不满足地
wit n.智力，才智，智能
witch n. 巫婆,女巫
witchcraft n. 巫术,魔法,魔力
witchery n. 巫术,魅力
with prep.带有
withal ad. 加之；同样；然而
withdraw vt.收回；撤回vi.撤退
withdrawal n. 撤退,退回,取消,停止服药,退股,
withdrawn withdraw的过去分词；adj. 隐退的，离群的
withdrew withdraw的过去式
wither vi.枯萎 vt.使衰弱
withheld withhold过去式(分词)
withhold vt. 扣留,保留,抑制
withholding n. 扣款
within prep. 在…里面；在…范围之内；不超过；在…以内；adv. 在里面，在内部
without prep.无，没有，不
withstand vt.抵挡，反抗
witless  adj. 无智慧
witness n.证据；证人 vt.目击
witticism n. 名言,妙语
wittily ad. 机智地；幽默地
witty a.机智的；风趣的
wive vt. 给…娶妻；娶…为妻
wives 妻子
wizard n. 男巫,术士,鬼才
wizardry n. 巫术
wizened adj. 干皱的，干巴巴的
wobble n. 摆动,动摇,不稳定,变度
woe n.悲哀，悲痛，苦恼
woeful adj. 悲伤的
woke wake的过去式(分词)；醒
woken 醒
wold n. 荒原，山地
wolf n.狼
wolfish  adj. 似狼的; 贪婪的; 残忍的
woman n.妇女，女人
womanhood n. 女人的身分; 女性; 女人的性质;
womanish adj.娘娘腔的
womankind n.妇女,女子,女人
womanly  adj.  (很) 有女人味的; 女子气质的,像女
womb n. 子宫,发源地
women n. (woman的复数)妇女；妇女(复数)
won 获胜；win的过去式与过去分词
wonder n.惊异，惊奇；奇迹
wonderful adj.极好的，精彩的
wonderfully adv. 极好地，精彩地；令人惊讶地；奇妙地
wonderous a.非常了不起
wondrous a. 令人惊奇的,非常的
wont n. 习惯
won't (同)will not
woo v. 向（女人）求爱，争取…的支持
wood n.树林
woodbine n.『植物』忍冬 (honeysuckle)
woodchuck n.土拨鼠
woodcock n. 鸟鹬
woodcutter n. 樵夫；伐木工
wood-cutter n.伐木者
wooded a. 树木繁茂的,森林多的
wooden adj.木制的
woodland n.林区
woodman n. 樵夫,居住于森林的人
woodpecker n.啄木鸟
woodprint 木版画
woods n. 树林；森林，树木
woodsman n. 住在森林中的人,详知森林者,
woodwind n. 木管乐器
woodwork n.(房屋等的) 木造部分
woody a. 多树木的,木质的,森林的
wooer n. 求婚者,求爱者
woof n. 织物,基本元素,低音,低吠声,
wool n.羊毛；毛线，绒线
woolen n. 毛制品
woollen a.羊毛制的，毛线的
woolly a. 毛茸茸的
woolly-minded a. 头脑糊涂的
word n.词，单词
wording n. 印字,语法,措词
wordless a. 沉默的,无言的
wordperfect a. 一字不错地熟记的
word-processor n.文字处理器
words 词语；单词
wordy a. 文字的,口头的,多言的
wore vt. wear(穿)的过去式
work v.&n.工作
workable a. 可使用的
workday n. 工作日
worker n.工人
worker's 工人的
workhouse n.感化院
working a. 工人的；劳动的；n. 工作，操作，作业；劳动的
workings n. 活动方式
workload 工作量
workman n.工人，劳动者，工匠
workmanship n. 手艺,技巧
workmate n. 工友，同事
workmen n. workman的复数
workpiece n. 工(作)件
workplace n. 工作场所；车间
workroom n. 工作室
works n.工事；工程
workshop n.专题讨论会
work-shop n. 车间(干重活的地方)
workweek 工作周
world n.世界
world-famous adj. 世界闻名的
worldly a. 世间的,世俗的,世上的
worldwide adj. 遍及全球的；世界性的，世界范围的；adj. & adv. 全世界的
world-wide a.遍及全球的
worm n.虫，蠕虫
wormwood n. 苦艾,苦恼
wormy a. 有虫的,虫多的,虫蛀的
worn adj. 用旧的；穿坏的；破旧的；用坏的，wear(穿)的过去分词；穿旧的，筋疲力尽的
worn-out a.疲惫不堪的；陈腐的
worried adj. 焦虑的；烦恼的；担心的；忧心忡忡的；担忧的；焦急的
worry vt.(使)担忧
worse adj.更坏的，更差的
worsen v.变
worship vt.崇拜 vi.做礼拜
worshiper n. 参加礼拜者,崇拜者
worshipful a. 可贵的,值得尊敬的,尊贵的
worshipper n.崇拜者
worst a.最坏的 ad.最坏地
worsted n.精纺绒线,毛纱
worth adj.值得...的
worthily ad. 相宜地,可敬地,正当地
worthiness n. 价值,相当,值得
worthless a.无价值的，无用的
worthwhile a.值得花时间的
worthy adj.有价值的；相称的
would aux.v.将；愿；总是
would-be a.所希望；意欲
wouldn't (同)would not
wound n.创伤，伤 vt.使受伤
wounded adj. 受伤的；n. 伤员
wove weave的过去式
woven weave的过去分词
wpm (缩)每分钟…词
wrack n. 冲上岸之海草,失事船只,破坏
wraith n. 幽灵，骨瘦如柴的人
wrangle v. 争论，激辩，吵架
wrangler 争吵者
wrap vt.裹，包，捆 n.披肩
wrapper n.包装者
wrapping n. (pl.)包装材料
wrath n.暴怒，狂怒，愤慨
wrathful a. 愤怒的,激怒的
wreak v. 泄愤，报仇
wreath n.花环，花圈，花冠
wreathe v. 完全笼罩，把…做成花环
wreck n.失事；残骸 vt.破坏
wreckage n. 残骸，碎片
wren n.少女,女子
wrench vt.拧，扭伤 n.拧
wrest n. 扭,拧,猛夺
wrestle n.摔交；斗争，搏斗
wrestler n. 摔角选手,扭
wrestling n. 摔跤；摔角
wretch n. 可怜的人,卑鄙的人,家伙
wretched a.不幸的；卑鄙的
wretchedness n.可怜，不幸，潦倒
wriggle n. 蠕动,蜿蜒
wright n. 建造者,制造者
wring vt.拧，挤，扭，榨
wringer n. 绞扭的人,绞扭机器,勒索者
wrinkle n.皱纹 vt.使起皱纹
wrist n.手腕
wristwatch n. 手表
writ n. 命令状，书面命令
write vt.书写；写 vi.写
write-back (对呆帐或已注销坏帐的)转回
write-down 资产帐面价值的)降低，划减
write-off (坏帐或无用资产等的)冲销
writer n.作者，作家，文学家
writhe vi. 扭动；缠绕
writing n.书写，写；著作
written adj. 写作的，书面的；write的过去分词
wrong a.错误的 ad.错，不对
wrongful a. 不正当的,不法的,不讲道理的
wrongly adv. 错误地，不正当地
wrote write的过去式；写
wroth a. 激怒的,愤怒的
wrought work的过去式(分词)
wrung wring的过去式(分词)
wry a. 扭歪的,歪曲的,歪斜的
wushu 武术
wyoming n. 怀俄明(州)(美国)
xenophobia n. 仇外，排外；对外国人的畏惧和憎恨
xerography n. 静电印刷法
xerophyte n. 旱生植物
Xerox vt.&vi.用静电复印
Xmas n. 圣诞节
X-ray n.X射线，X光
Xujiahui n.(地名)徐家汇
xylem n. 木质部
xylophone n. 木琴
yacht n.游艇，快艇
yak 犁牛
yam n. 山药,洋芋
yangtze n. (the-)长江(中国)
Yankee n. 美国人
yard n.码(英美长度单位)
yardstick n. 码尺,准绳
yarn n. 纱线
yarrow n. 西洋蓍草
yaw v. （船，飞机等）偏航
yawl n. 船载小艇,舰载杂用船,一种小帆船
yawn vi.打呵欠 n.呵欠
yea n. 肯定,赞成,赞成票
yeah ad. (口)(同)yes
year n.年；年年
yearbook n. 年鉴
yearling n. 一岁崽
yearly a.每年的 ad.一年一度
yearn vi.想念，怀念，向往
years 年
yeast n.酵母
yell vi.叫喊
yellow adj.黄色的
yellowstone n. 黄石公园(美国)
yelp vi. 狺吠；叫喊
yeoman n. 自耕农，乡下人
yeomanry n.小地主们
yes adv.是，是的
yes? 什么事？
yesterday n.&ad.昨天，昨日
yet adv.仍然
yew n. 紫杉,水松
yield vt.&vi.出产 n.产量
yielding adj. 弯曲自如的，灵活的
yoghurt n. 酸牛奶
yogurt n.酸奶酪
yoke n.轭，牛轭；枷锁
yokefellow n. 同事,配偶,伙伴
yokel n. 乡巴佬
yolk n.蛋黄，卵黄
yon adj. & adv. (古语)在远处
yond a. 那边的；彼处的；远处的
yonder a. 那边的
yore n.从前,往昔
Yorkshire n.(地名)约克郡
you pron.你，你们
you'd (同)you had；you would
you'll (同)you will；youshall
young adj.年青的
younger 较年轻的
youngling n. 年轻人,新手
youngster n.儿童，少年，年轻人
your pron.你的，你们的
you're (同)you are
yours pron.你们的(东西)
yourself pron.你自己；你亲自
yourselves pron.pl. 你们自己
youth n.青年
youthful a.年轻的，青年的
youth-oriented a.面向青年的
you've (同)you have
yoyo n.溜溜球（玩具）
yuan n. (人民币)元；元(中国货币单位)
yugoslavia n. 南斯拉夫
yugoslavian n. 南斯拉夫人
yule n. 耶稣圣诞节,圣诞季节
zany n. 小丑,笨人,丑角的配角
zap v. 迅速离去，击溃
zeal n.热心，热情，热忱
zealot n. 狂热份子，热心者
zealous a.热心的，热情的
zebra n.斑马
zebu n. 瘤牛
zenith n. 天顶，极点
zephyr n. 和风，西风
zeppelin n.  齐柏林式飞艇
zero n.零；零点，零度
zest n. 刺激性，热心，兴趣
zeus n. (希腊)宙斯
zigzag a. 之字形的，曲折的
zinc n.锌 vt.在…上镀锌
zion n. 天国
zip n. 拉链；活动，尖啸声；v. 拉上…拉链
zipcode n. 邮政编码
zipper n. 拉练
zither n. 筝
zodiac n. 十二宫图,黄道带
zone n.地区，区域，范围
zoo n. 动物园
zoological a. 动物学的
zoologist n. 动物学家
zoology n. 动物学,生态
zoom n. 急速上升,图象电子放大,嗡嗡声
zoos 动物园
zurich n. 苏黎世(瑞士城市名)
zygote n. 接合子，受精卵
'''
class ExampleCommand(sublime_plugin.EventListener):
    settings = None
    b_first_edit = True
    b_fully_loaded = True
    word_list = []
    characters_index={}
    my_dict=["algorithm n. 算法",]

    # on first modification in comments, get the dictionary and save items.
    def on_modified(self, view):
        if self.b_first_edit and self.b_fully_loaded:
            self.b_fully_loaded = False
            sublime.set_timeout(lambda: self.load_completions(view), 3)

    def load_completions(self, view):
        #print("view.scope_name ", view.scope_name(view.sel()[0].begin()))
        scope_name = view.scope_name(view.sel()[0].begin())       # sublime.windows()[0].active_view()
        if self.should_trigger(scope_name):
            words = words_raw.split('\n')
            words.pop(0)
            words.pop(-1)
            t = 0
            for index, i in enumerate(words):
                if "None"== self.characters_index.get(i[0].lower(),'None'):
                    self.characters_index[i[0].lower()]=[index,index]
                else:
                    self.characters_index[i[0].lower()][1]+=1
                self.word_list.append(i)

            self.b_first_edit = False
        else:
            self.b_fully_loaded = True
        print("kv ",self.characters_index)

    # This will return all words found in the dictionary.
    def get_autocomplete_list(self, word):
        autocomplete_list = []
        # filter relevant items:
        word_lower = word.lower()
        len_word = len(word)
        UPPER = word[0].isupper()
        #print("search ",word)
        start,end = self.characters_index[word_lower[0]]
        for index in range(start,end+1):
            w = self.word_list[index]
            if word_lower in w.split(" ")[0].lower():
                if UPPER:
                    W = w.title()
                    autocomplete_list.append((W.replace(" "," || ",1), W.split(" ")[0]))
                else:
                    autocomplete_list.append((w.replace(" "," || ",1), w.split(" ")[0]))

        # for w in self.word_list:
        #     try:
        #         if word_lower in w.split(" ")[0].lower():
        #
        #             if UPPER:
        #                 W = w.title()
        #                 autocomplete_list.append((W, W.split(" ")[0]))
        #             else:
        #                 autocomplete_list.append((w, w.split(" ")[0]))
        #     except UnicodeDecodeError:
        #         print(w)
        #         # autocomplete_list.append((w, w))
        #         continue

        return autocomplete_list

    def should_trigger(self, scope):
        if "comment" in scope or "string.quoted" in scope or "text" == scope[:4]:
            return True
        return False
    # gets called when auto-completion pops up.
    def on_query_completions(self, view, prefix, locations):
        #scope_name = sublime.windows()[0].active_view().scope_name(sublime.windows()[0].active_view().sel()[0].begin())
        #if self.should_trigger(scope_name):
        if len(prefix)== 0:
            return None
        #print("prefix is ",prefix)
        return self.get_autocomplete_list(prefix)