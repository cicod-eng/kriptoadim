# KriptoAdım — 站点规格与 URL 结构（定稿）

> 本文档是 KriptoAdım 建站的唯一事实来源。开发、写文章、配 SEO 都以此为准。

## 0. 站点元信息

| 项 | 值 |
|---|---|
| 品牌名 | **KriptoAdım**（Adım 作强调，土耳其语展示名） |
| 域名 | `kriptoadim.com`（纯 ASCII，无 IDN 兼容问题） |
| 语言 | Türkçe (tr-TR) |
| 定位 | Türkiye için adım adım kripto rehberleri ve sorun çözme merkezi |
| 部署 | GitHub Pages（干净 URL，`slug/index.html`） |
| 主色 | 深青绿 / 蓝绿（非 Binance 黄） |

**不做**：每日币价新闻、喊单、币价预测、百倍币、项目介绍堆砌、纯邀请码页。

**只做**：怎么操作 + 为什么失败 + 怎么检查 + 有什么区别。

---

## 1. URL 规范（必须遵守）

1. **所有 slug 只用 ASCII**：土耳其语特殊字符一律转写
   - `ı → i`　`ş → s`　`ğ → g`　`ü → u`　`ö → o`　`ç → c`
   - 例：`ağ → ag`，`çözme → cozme`，`cüzdan → cuzdan`，`güvenlik → guvenlik`，`yatırma → yatirma`
2. **分类页 / 平台专题页用目录**：`/baslangic/`、`/borsalar/binance-tr/`
3. **文章用短目录 URL**（不塞进多层目录）：`/binance-tr-para-yatirma/`
4. 每个 URL 落地为 `slug/index.html`（GitHub Pages 干净 URL）

---

## 2. 完整 URL 结构树

```
/
├── baslangic/                    # 新手基础
├── borsalar/                     # 交易平台 Hub
│   ├── binance-tr/               # Binance TR 专题页
│   └── okx-tr/                   # OKX TR 专题页
├── usdt-transfer/                # USDT & 转账
├── cuzdan/                       # 钱包
├── guvenlik/                     # 安全
├── sorun-cozme/                  # 故障排查（核心栏目）
│
├── kripto-para-nedir/
├── usdt-nedir/
├── kripto-cuzdani-nedir/
├── blockchain-nedir/
├── seed-phrase-nedir/
├── trc20-nedir/
├── kripto-transferi-nasil-calisir/
│
├── binance-tr-nasil-kullanilir/
├── binance-tr-para-yatirma/
├── binance-tr-para-cekme/
├── binance-tr-komisyon/
├── binance-tr-48-saat-kurali/
├── binance-trden-binance-transfer/
├── binance-tr-vs-binance/
├── binance-transfer-yapamiyorum/
│
├── okx-tr-nasil-kullanilir/
├── okx-tr-para-yatirma/
├── okx-tr-para-cekme/
├── okx-tr-komisyon/
├── binance-tr-vs-okx-tr/
│
├── turkiyede-usdt-nasil-alinir/
├── usdt-nasil-gonderilir/
├── usdt-hangi-agdan-gonderilmeli/
├── trc20-vs-erc20/
├── usdt-transferi-ne-kadar-surer/
├── usdt-transferi-gelmedi/
├── yanlis-agdan-usdt-gonderdim/
│
├── cuzdan-adresi-nedir/
├── metamask-kullanimi/
├── trust-wallet-kullanimi/
├── kripto-transferi-nasil-takip-edilir/
│
├── kripto-dolandiriciligi/
├── sagte-destek/
├── phishing-nedir/
├── seed-phrase-guvenligi/
├── yanlis-adrese-gonderim/
├── hesap-guvenligi/
│
├── para-yatirdim-ama-gelmedi/
├── para-cekemiyorum/
├── transfer-bekliyor/
├── usdt-gelmedi/
├── yanlis-ag-sectim/
├── yanlis-adrese-gonderdim/
└── txid-nasil-kontrol-edilir/
```

---

## 3. 分类页规格（6 个）

> 每个分类页做成 **主题 Hub 页**：不是文章列表，而是「按用户任务/问题分组」的入口页。

### 3.1 Başlangıç — `/baslangic/`

- **Title**: `Kripto Para Temel Rehberler | KriptoAdım`
- **Meta Description**: `Kripto para, USDT, cüzdan, blockchain ve seed phrase nedir? Yeni başlayanlar için adım adım, Türkiye'ye özel temel rehberler.`
- **H1**: `Kriptoya Başlangıç Rehberleri`
- **引导文案**:
  > Kripto dünyasına yeni mi başlıyorsunuz? Temel kavramları sade bir dille, adım adım anlatıyoruz. Her rehberde bir kavramı öğrenir, ne işe yaradığını ve neden önemli olduğunu görürsünüz.

- **文章清单**（标题 → slug）:

| 标题 | slug |
|---|---|
| Kripto para nedir? | `/kripto-para-nedir/` |
| USDT nedir? | `/usdt-nedir/` |
| Kripto cüzdanı nedir? | `/kripto-cuzdani-nedir/` |
| Blockchain nedir? | `/blockchain-nedir/` |
| Seed phrase nedir? | `/seed-phrase-nedir/` |
| TRC20 nedir? | `/trc20-nedir/` |
| Kripto transferi nasıl çalışır? | `/kripto-transferi-nasil-calisir/` |

---

### 3.2 Borsalar — `/borsalar/`

- **Title**: `Binance TR, OKX TR ve Borsa Rehberleri | KriptoAdım`
- **Meta Description**: `Binance TR ve OKX TR'ye para yatırma, çekme, komisyon ve kullanım rehberleri. Türkiye'deki kripto borsalarının adım adım karşılaştırması.`
- **H1**: `Kripto Borsa Rehberleri`
- **引导文案**:
  > Türkiye'de hangi borsa size uygun? Binance TR ve OKX TR'yi para yatırma, çekme, komisyon ve kullanım açısından karşılaştırıyoruz.

- **分组结构**（Hub 页按三组展示）:

**① Binance TR** → 专题页 `/borsalar/binance-tr/`
- Binance TR nasıl kullanılır? → `/binance-tr-nasil-kullanilir/`
- Binance TR'ye nasıl para yatırılır? → `/binance-tr-para-yatirma/`
- Binance TR'den para çekme → `/binance-tr-para-cekme/`
- Binance TR komisyonları → `/binance-tr-komisyon/`
- Binance TR 48 saat kuralı → `/binance-tr-48-saat-kurali/`

**② OKX TR** → 专题页 `/borsalar/okx-tr/`
- OKX TR nasıl kullanılır? → `/okx-tr-nasil-kullanilir/`
- OKX TR'ye para yatırma → `/okx-tr-para-yatirma/`
- OKX TR'den para çekme → `/okx-tr-para-cekme/`
- OKX TR komisyonları → `/okx-tr-komisyon/`

**③ Karşılaştırmalar**
- Binance TR mi Binance mi? → `/binance-tr-vs-binance/`
- Binance TR vs OKX TR → `/binance-tr-vs-okx-tr/`
- Binance TR vs BtcTurk → `/binance-tr-vs-btcturk/`

---

### 3.3 USDT & Transfer — `/usdt-transfer/`

- **Title**: `USDT Alma, Gönderme ve Transfer Rehberleri | KriptoAdım`
- **Meta Description**: `USDT nasıl alınır, hangi ağ seçilmeli, TRC20 mi ERC20 mi? USDT transferi, ağ seçimi ve süreler hakkında Türkiye'ye özel rehberler.`
- **H1**: `USDT ve Transfer Rehberleri`
- **引导文案**:
  > USDT, Türkiye'de en çok kullanılan sabit kripto paradır. Doğru ağı seçmek, transfer ücreti ve süresi işlemlerinizi doğrudan etkiler. Burada tüm adımları net şekilde açıklıyoruz.

- **文章清单**:

| 标题 | slug |
|---|---|
| Türkiye'de USDT nasıl alınır? | `/turkiyede-usdt-nasil-alinir/` |
| USDT nasıl gönderilir? | `/usdt-nasil-gonderilir/` |
| USDT hangi ağdan gönderilmeli? | `/usdt-hangi-agdan-gonderilmeli/` |
| TRC20 vs ERC20 farkları | `/trc20-vs-erc20/` |
| USDT transferi ne kadar sürer? | `/usdt-transferi-ne-kadar-surer/` |
| USDT transferi gelmedi | `/usdt-transferi-gelmedi/` |

---

### 3.4 Cüzdan — `/cuzdan/`

- **Title**: `Kripto Cüzdan Rehberleri: Adres, Seed Phrase | KriptoAdım`
- **Meta Description**: `Kripto cüzdanı nedir, cüzdan adresi nedir, seed phrase güvenliği, MetaMask ve Trust Wallet kullanımı hakkında adım adım rehberler.`
- **H1**: `Kripto Cüzdan Rehberleri`
- **引导文案**:
  > Cüzdan, kripto varlıklarınızın anahtarıdır. Cüzdan, adres ve seed phrase kavramlarını öğrenin; MetaMask ve Trust Wallet'ı güvenle kullanın.

- **文章清单**:

| 标题 | slug |
|---|---|
| Kripto cüzdanı nedir? | `/kripto-cuzdani-nedir/` |
| Cüzdan adresi nedir? | `/cuzdan-adresi-nedir/` |
| Seed phrase nedir? | `/seed-phrase-nedir/` |
| MetaMask kullanımı | `/metamask-kullanimi/` |
| Trust Wallet kullanımı | `/trust-wallet-kullanimi/` |
| Kripto transferi nasıl takip edilir? | `/kripto-transferi-nasil-takip-edilir/` |

---

### 3.5 Güvenlik — `/guvenlik/`

- **Title**: `Kripto Güvenlik Rehberleri: Dolandırıcılıktan Korunma | KriptoAdım`
- **Meta Description**: `Kripto dolandırıcılığı, sahte destek, phishing ve seed phrase güvenliği. Kripto varlıklarınızı korumak için Türkiye'ye özel güvenlik rehberleri.`
- **H1**: `Kripto Güvenlik Rehberleri`
- **引导文案**:
  > Kriptoda en büyük risk fiyat değil, dolandırıcılıktır. Yaygın tuzakları tanıyın, seed phrase'inizi koruyun ve hesabınızı güvene alın.

- **文章清单**:

| 标题 | slug |
|---|---|
| Kripto dolandırıcılığı türleri | `/kripto-dolandiriciligi/` |
| Sahte destek dolandırıcılığı | `/sagte-destek/` |
| Phishing nedir? | `/phishing-nedir/` |
| Seed phrase güvenliği | `/seed-phrase-guvenligi/` |
| Yanlış adrese gönderim | `/yanlis-adrese-gonderim/` |
| Hesap güvenliği | `/hesap-guvenligi/` |

---

### 3.6 Sorun Çözme — `/sorun-cozme/`（核心栏目）

- **Title**: `Kripto İşlem Sorunları ve Çözümleri | KriptoAdım`
- **Meta Description**: `Para yatırdım ama gelmedi, para çekemiyorum, transfer bekliyor, yanlış ağ seçtim... Kripto işlem sorunlarınızı adım adım çözün.`
- **H1**: `Kripto İşlemlerinde Sorun mu Yaşıyorsunuz?`
- **引导文案**:
  > Kriptoda işlemler bazen beklenenden uzun sürer veya hata verir. Aşağıdan yaşadığınız sorunu seçin; ne olduğunu, nedenini ve adım adım ne yapmanız gerektiğini anlatalım.

- **问题入口清单**（按故障分组）:

| 问题 | slug |
|---|---|
| Para yatırdım ama gelmedi | `/para-yatirdim-ama-gelmedi/` |
| Para çekemiyorum | `/para-cekemiyorum/` |
| Transfer bekliyor | `/transfer-bekliyor/` |
| USDT gelmedi | `/usdt-gelmedi/` |
| Yanlış ağ seçtim | `/yanlis-ag-sectim/` |
| Yanlış adrese gönderdim | `/yanlis-adrese-gonderdim/` |
| Binance TR 48 saat | `/binance-tr-48-saat-kurali/` |
| TxID nasıl kontrol edilir? | `/txid-nasil-kontrol-edilir/` |

---

## 4. 平台专题页规格（2 个）

### 4.1 Binance TR — `/borsalar/binance-tr/`

- **Title**: `Binance TR Rehberleri: Para Yatırma, Çekme, Komisyon | KriptoAdım`
- **Meta Description**: `Binance TR hesabı, para yatırma, para çekme, komisyon ve 48 saat kuralı hakkında adım adım rehberler. Binance TR mi Binance mi, farkları öğrenin.`
- **H1**: `Binance TR Rehberleri`
- **引导文案**:
  > Binance TR, Türkiye'de TL ile kripto işlemi yapmanın en yaygın yollarından biridir. Para yatırma, çekme, komisyon ve sık yaşanan sorunlara dair tüm rehberler burada.

- **文章清单**:
  1. Binance TR nasıl kullanılır? → `/binance-tr-nasil-kullanilir/`
  2. Binance TR'ye nasıl para yatırılır? → `/binance-tr-para-yatirma/`
  3. Binance TR'den para çekme → `/binance-tr-para-cekme/`
  4. Binance TR komisyonları → `/binance-tr-komisyon/`
  5. Binance TR 48 saat kuralı → `/binance-tr-48-saat-kurali/`
  6. Binance TR'den Binance'e transfer → `/binance-trden-binance-transfer/`
  7. Binance TR'de transfer yapamıyorum → `/binance-transfer-yapamiyorum/`
  8. Binance TR mi Binance mi? → `/binance-tr-vs-binance/`

### 4.2 OKX TR — `/borsalar/okx-tr/`

- **Title**: `OKX TR Rehberleri: Para Yatırma, Çekme, Komisyon | KriptoAdım`
- **Meta Description**: `OKX TR hesabı, para yatırma, para çekme ve komisyon hakkında adım adım rehberler. Binance TR ile OKX TR karşılaştırmasını görün.`
- **H1**: `OKX TR Rehberleri`
- **引导文案**:
  > OKX TR, Türkiye'de TL ile kripto işlemi yapmak isteyenler için bir diğer önemli platformdur. Para yatırma, çekme ve komisyon adımlarını net şekilde anlatıyoruz.

- **文章清单**:
  1. OKX TR nasıl kullanılır? → `/okx-tr-nasil-kullanilir/`
  2. OKX TR'ye para yatırma → `/okx-tr-para-yatirma/`
  3. OKX TR'den para çekme → `/okx-tr-para-cekme/`
  4. OKX TR komisyonları → `/okx-tr-komisyon/`
  5. Binance TR vs OKX TR → `/binance-tr-vs-okx-tr/`

---

## 5. 首页结构（对应 14 模块）

```
HEADER（6 个一级导航）
↓ HERO — Kriptoyu adım adım öğrenin, işlemlerinizi daha güvenli yapın
↓ NE YAPMAK İSTİYORSUNUZ?（6 任务卡）
↓ SORUN ÇÖZME（6 故障卡）
↓ BINANCE TR REHBERLERİ（4 篇）
↓ USDT & TRANSFER（4 篇）
↓ PLATFORM KARŞILAŞTIRMALARI（3 篇）
↓ BAŞLANGIÇ（4–6 篇）
↓ GÜNCELLENEN REHBERLER
↓ BİLGİLERİ NASIL HAZIRLIYORUZ?
↓ ŞEFFAFLIK（affiliate 声明）
↓ FOOTER（4 列）
```

---

## 6. 待办（下一步）

- [ ] 首页完整 HTML 成稿（土耳其语）
- [ ] 6 个分类页 HTML（按本文档 Hub 结构）
- [ ] 2 个平台专题页 HTML
- [ ] CNAME / robots.txt / sitemap.xml / 404 / favicon.svg / .nojekyll
- [ ] 土耳其语写作模板 + 内容地图（对应首篇文章清单 ~40 篇）
- [ ] GSC / Bing WMT / IndexNow 三件套
- [ ] 邀请码体系确认（BN522/OK800 或单独）
