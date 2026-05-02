# 不好意思喔, 這裡專收VT

- 只放720x720的全身圖, 必須對齊這張圖

<a href="vt/eason.png"><img src="vt/eason.png" alt="eason" width="160"></a>

# 若你想為這個project做出貢獻

- 使用gemini, 丟入以下prompt, edit_me.png, 以及一張或兩張參考照片, 我會先從PNG/twitch_emotes/裡的照片開始, 通常第一次會生不好, 要多生幾次, 如果一張參照圖一直生不好, 可以
把VT的皮圖也餵進去. 再不好就要改prompt, 通常生一個能看的要嘗試3~4次
```
fix the missing part using the reference image (add outfit , hair to pink creature with green background) the final image should contain full body
```

- 下載下來的圖丟到繪圖軟體去背，我用mac的medibang MagicWand工具, Expand要調1 (這很重要, 不然會清不乾淨), 選完綠色底色後去除. 有一些細部可能要手動修
-  去完背後要跟原圖對齊, 調成720x720, 把原圖擺在底圖層, 確認疊在上面的圖有確實對齊
-  最後我會用 scripts裡面的make_gif.py生成gif檢查所有圖有沒有清乾淨並對齊

## 預覽圖

> 此區塊由 `scripts/gen_gallery.py` 自動產生，請勿手動編輯。

<!-- gallery:start -->

### vt (22)

| | | | |
| --- | --- | --- | --- |
| <img src="vt/corcor.png" width="160"><br>corcor | <img src="vt/eason.png" width="160"><br>eason | <img src="vt/eason_maid.png" width="160"><br>eason_maid | <img src="vt/hakuzen.png" width="160"><br>hakuzen |
| <img src="vt/hitomi.png" width="160"><br>hitomi | <img src="vt/kuma.png" width="160"><br>kuma | <img src="vt/lianyun.png" width="160"><br>lianyun | <img src="vt/lingmu.png" width="160"><br>lingmu |
| <img src="vt/mitsuki.png" width="160"><br>mitsuki | <img src="vt/miwawaa.png" width="160"><br>miwawaa | <img src="vt/moko.png" width="160"><br>moko | <img src="vt/musha.png" width="160"><br>musha |
| <img src="vt/nein.png" width="160"><br>nein | <img src="vt/paroniie.png" width="160"><br>paroniie | <img src="vt/pele.png" width="160"><br>pele | <img src="vt/ranran.png" width="160"><br>ranran |
| <img src="vt/suaiya.png" width="160"><br>suaiya | <img src="vt/taotie.png" width="160"><br>taotie | <img src="vt/vivi.png" width="160"><br>vivi | <img src="vt/wuwutt.png" width="160"><br>wuwutt |
| <img src="vt/yukito.png" width="160"><br>yukito | <img src="vt/zeskr.png" width="160"><br>zeskr |  |  |

<!-- gallery:end -->
