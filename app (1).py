import streamlit as st
from datetime import date
from typing import Dict, List, Optional

st.set_page_config(page_title="読書リフレクション", page_icon="📚", layout="wide")


# -----------------------------
# モックデータ
# -----------------------------
def sample_books() -> List[Dict]:
    return [
        {
            "id": 1,
            "title": "Atomic Habits",
            "subtitle": "小さな習慣の積み重ね",
            "thumbnail": "https://covers.openlibrary.org/b/isbn/9780735211292-M.jpg",
            "amazon_url": "https://www.amazon.co.jp/",
            "status": "読了",
            "read_dates": ["2026-06-01", "2026-06-10"],
            "themes": ["習慣", "継続", "働き方", "行動変容"],
            "goal": "習慣化を、仕事の仕組み化とどうつなげるかを考える",
            "core_impression": "習慣を意志の問題ではなく環境設計として扱う視点が強く残った。",
            "social_discussion": "多くの読者は『小さく始める』『仕組みで継続する』点を重視し、実践性の高さがよく議論される。",
            "share_message": "成果を急ぐ前に、続けられる構造を作ることの重要性を伝えたい。",
            "message_candidates": [
                "やる気より環境設計のほうが再現性が高い",
                "小さな改善の積み重ねが大きな変化になる",
            ],
            "author": {
                "id": 101,
                "name": "James Clear",
                "photo": "👤",
                "short_title": "習慣形成の実務家・著述家",
                "industry_position": "行動変容・習慣化分野で広く読まれる実務家",
                "authority_summary": "習慣形成を行動科学と実践の橋渡しで広めた著述家。",
                "career": "習慣・意思決定・継続改善をテーマに執筆と講演を行う。",
                "achievements": "世界的ベストセラーを持ち、習慣形成の実践フレームを普及。",
                "episodes": "小さな改善の積み重ねを重視する考え方で広く知られる。",
            },
            "sessions": [
                {
                    "id": 1,
                    "title": "初回感想",
                    "date": "2026-06-10",
                    "tags": ["音声", "壁打ち"],
                    "raw_note": "習慣は気合ではなく環境設計という話が特に刺さった。",
                    "ai_summary": "継続の仕組みを作る発想として、仕事にも転用しやすいと整理。",
                },
                {
                    "id": 2,
                    "title": "読書会前",
                    "date": "2026-06-13",
                    "tags": ["追記"],
                    "raw_note": "他人に伝えるなら、才能より再現性のある仕組みの話として紹介したい。",
                    "ai_summary": "共有メッセージは『誰でも改善できる構造』に寄せると伝わりやすい。",
                },
            ],
            "latest_outputs": {
                "private_memo": "仕事の継続課題は、行動目標より環境設計の見直しとして再定義する。",
                "reading_group": "『頑張る方法』より『続く仕組み』を作る本として紹介する。",
                "sns": "続ける力は意志力より設計力。小さく始められる環境づくりが強い。",
            },
            "change_log": {
                "before": "最初は習慣化のテクニック本だと思っていた。",
                "after": "今は組織や仕事の運用設計に転用できる本だと見ている。",
            },
        },
        {
            "id": 2,
            "title": "THE 7 HABITS",
            "subtitle": "主体性と原則中心の考え方",
            "thumbnail": "https://covers.openlibrary.org/b/isbn/9780743269513-M.jpg",
            "amazon_url": "https://www.amazon.co.jp/",
            "status": "読書中",
            "read_dates": ["2026-06-12"],
            "themes": ["価値観", "主体性", "目標設定", "人間関係", "働き方"],
            "goal": "原則中心の考え方を、対人関係と意思決定にどう活かすか整理する",
            "core_impression": "主体性の話は知っていたが、実際の対人場面に落とし込むとまだ浅い。",
            "social_discussion": "『主体性』『Win-Win』『重要事項を優先』が広く取り上げられる。",
            "share_message": "成果より前に、自分の反応の選び方を見直す大切さを伝えたい。",
            "message_candidates": [
                "知っていることと、実際に使えていることは違う",
                "目先の効率より、原則に基づく判断が長期的に効く",
            ],
            "author": {
                "id": 102,
                "name": "Stephen R. Covey",
                "photo": "👤",
                "short_title": "リーダーシップ思想家・著述家",
                "industry_position": "自己啓発・リーダーシップ分野の古典的著者",
                "authority_summary": "原則中心のリーダーシップを広めた著者として長く参照される。",
                "career": "教育・組織開発・リーダーシップ領域で著述と研修を展開。",
                "achievements": "7つの習慣を通じて自己啓発分野で世界的な影響を持つ。",
                "episodes": "価値観と原則に基づく生き方を強調した点で長く支持される。",
            },
            "sessions": [
                {
                    "id": 3,
                    "title": "読書中メモ",
                    "date": "2026-06-14",
                    "tags": ["音声"],
                    "raw_note": "理解したつもりの概念を、実際の職場の場面でまだ使いきれていない。",
                    "ai_summary": "概念理解から行動転用へ移る段階で、具体シーンの想起が必要。",
                }
            ],
            "latest_outputs": {
                "private_memo": "主体性は感情を抑えることではなく、反応を選び直す力として扱う。",
                "reading_group": "知っていることと使えていることの差が大きい本として共有する。",
                "sns": "知っている言葉ほど、生活の具体場面に落とさないと空回りする。",
            },
            "change_log": {
                "before": "有名な概念を学ぶ本という印象。",
                "after": "対人関係の反応を選び直す実践書として読み直している。",
            },
        },
        {
            "id": 3,
            "title": "LIFE SHIFT",
            "subtitle": "100年時代の人生戦略",
            "thumbnail": "https://covers.openlibrary.org/b/isbn/9781509527496-M.jpg",
            "amazon_url": "https://www.amazon.co.jp/",
            "status": "読了",
            "read_dates": ["2026-05-20"],
            "themes": ["キャリア", "働き方", "未来予測", "目標設定"],
            "goal": "長期的なキャリア視点を持ち、今の選択を見直す材料を得る",
            "core_impression": "転職を単発で考えるのではなく、長い人生の設計として捉え直す必要を感じた。",
            "social_discussion": "100年時代という前提から、学び直しや複数ステージの人生設計がよく議論される。",
            "share_message": "今の不安を解消するには、短期最適より長期視点の設計が必要だと伝えたい。",
            "message_candidates": [
                "長寿化でキャリア設計の前提が変わる",
                "目先の転職ではなく人生全体の設計が必要",
            ],
            "author": {
                "id": 103,
                "name": "Lynda Gratton",
                "photo": "👤",
                "short_title": "組織論・未来の働き方研究者",
                "industry_position": "未来の働き方やキャリア設計領域で影響力のある研究者",
                "authority_summary": "長寿化と働き方の変化を踏まえたキャリア論で広く参照される研究者。",
                "career": "ロンドン・ビジネススクールで組織論と未来の働き方を研究。",
                "achievements": "100年時代のキャリア論を一般層にも届く形で広めた。",
                "episodes": "雇用・学び・人生設計を一体で捉える視点が広く受け入れられた。",
            },
            "sessions": [
                {
                    "id": 4,
                    "title": "未来予測の整理",
                    "date": "2026-05-21",
                    "tags": ["壁打ち", "追記"],
                    "raw_note": "転職の話をしている人ほど、この本の長期視点が必要だと思った。",
                    "ai_summary": "短期的な不満解消ではなく、長期の人生設計の視点を持ってもらう導入本として使いやすい。",
                }
            ],
            "latest_outputs": {
                "private_memo": "目先の条件改善だけではなく、人生全体の持続可能性を考える必要がある。",
                "reading_group": "転職や将来不安の話を、長期視点に広げる起点として使う。",
                "sns": "キャリアは次の会社選びだけでなく、長い人生でどう学び、どう働くかの設計そのもの。",
            },
            "change_log": {
                "before": "未来予測の本という印象だった。",
                "after": "人生設計と働き方の前提を問い直す本だと感じている。",
            },
        },
    ]


def sample_guests() -> List[Dict]:
    return [
        {
            "id": 201,
            "name": "Aさん",
            "relationship": "友人の紹介",
            "occupation": "営業職 / 27歳",
            "current_concerns": "今の仕事を続けるか迷っている。転職も考えているが軸が曖昧。",
            "recent_conversation": "最近、将来がなんとなく不安で転職サイトを見ていると話していた。",
            "values_memo": "自由度は高めたいが、安定も捨てたくない。人とのつながりは重視。",
            "animal_note": "動物占い: 柔軟で人当たりが良いタイプとして見立て。会話は共感から入るとよさそう。",
            "sync_status": "別アプリ連携済み",
            "current_phase": "目標設計の手前",
            "missing_pieces": ["中長期の目標", "働き方の価値観", "未来の経済変化の認識"],
            "recommended_themes": ["目標設定", "価値観", "未来予測", "働き方"],
        },
        {
            "id": 202,
            "name": "Bさん",
            "relationship": "読書会で何度か同席",
            "occupation": "事務職 / 31歳",
            "current_concerns": "日々が忙しく、やりたいことが後回しになっている。",
            "recent_conversation": "やるべきことは分かっているのに、続かないし変われないと話していた。",
            "values_memo": "安心感と成長実感の両方を求めている。",
            "animal_note": "動物占い: 慎重で積み上げ型として仮説。具体例があると納得しやすそう。",
            "sync_status": "別アプリ連携済み",
            "current_phase": "行動変容の入口",
            "missing_pieces": ["継続の仕組み", "小さく始める感覚"],
            "recommended_themes": ["習慣", "継続", "働き方"],
        },
    ]


# -----------------------------
# 初期化 / ユーティリティ
# -----------------------------
def init_state() -> None:
    if "books" not in st.session_state:
        st.session_state.books = sample_books()
    if "guests" not in st.session_state:
        st.session_state.guests = sample_guests()
    if "nav_page" not in st.session_state:
        st.session_state.nav_page = "ホーム"
    if "library_tab" not in st.session_state:
        st.session_state.library_tab = "本"
    if "selected_book_id" not in st.session_state:
        st.session_state.selected_book_id = 1
    if "selected_guest_id" not in st.session_state:
        st.session_state.selected_guest_id = 201
    if "detail_return_page" not in st.session_state:
        st.session_state.detail_return_page = "ライブラリ"


def get_selected_book() -> Dict:
    for book in st.session_state.books:
        if book["id"] == st.session_state.selected_book_id:
            return book
    return st.session_state.books[0]


def get_selected_guest() -> Dict:
    for guest in st.session_state.guests:
        if guest["id"] == st.session_state.selected_guest_id:
            return guest
    return st.session_state.guests[0]


def render_avatar(photo: Optional[str], size: int = 72) -> None:
    if not photo or photo == "👤":
        st.markdown(
            f"<div style='font-size:{size}px; text-align:center; line-height:1;'>👤</div>",
            unsafe_allow_html=True,
        )
    else:
        st.image(photo, use_container_width=True)


def open_book_detail(book_id: int, return_page: str) -> None:
    st.session_state.selected_book_id = book_id
    st.session_state.detail_return_page = return_page
    st.session_state.nav_page = "本詳細"
    st.rerun()


def unique_authors() -> List[Dict]:
    seen = set()
    authors = []
    for book in st.session_state.books:
        author = book["author"]
        if author["id"] not in seen:
            authors.append(author)
            seen.add(author["id"])
    return authors


def grouped_books_by_theme() -> Dict[str, List[Dict]]:
    grouped: Dict[str, List[Dict]] = {}
    for book in st.session_state.books:
        for theme in book.get("themes", []):
            grouped.setdefault(theme, []).append(book)
    return dict(sorted(grouped.items(), key=lambda x: x[0]))


# -----------------------------
# サイドバー
# -----------------------------
def sidebar_menu_button(label: str, page_name: str, icon: str) -> None:
    active = st.session_state.nav_page == page_name
    if st.sidebar.button(
        f"{icon}  {label}",
        use_container_width=True,
        type="primary" if active else "secondary",
    ):
        st.session_state.nav_page = page_name
        st.rerun()


def render_sidebar() -> None:
    st.sidebar.title("📚 読書リフレクション")
    st.sidebar.caption("再設計版ナビゲーション")
    sidebar_menu_button("ホーム", "ホーム", "🏠")
    sidebar_menu_button("本を深める", "本を深める", "🧠")
    sidebar_menu_button("伝え方を考える", "伝え方を考える", "🧭")
    sidebar_menu_button("ライブラリ", "ライブラリ", "🗂️")

    st.sidebar.divider()
    if st.session_state.nav_page == "本詳細":
        book = get_selected_book()
        st.sidebar.caption("表示中の本")
        st.sidebar.write(f"**{book['title']}**")
        st.sidebar.caption(book["author"]["name"])
        if st.sidebar.button("← 元の画面に戻る", use_container_width=True):
            st.session_state.nav_page = st.session_state.detail_return_page
            st.rerun()
    elif st.session_state.nav_page == "ライブラリ":
        st.sidebar.caption("ライブラリ内タブ")
        for tab_name in ["本", "著者", "テーマ"]:
            if st.sidebar.button(
                f"{tab_name}を見る",
                use_container_width=True,
                type="primary" if st.session_state.library_tab == tab_name else "secondary",
                key=f"library_tab_{tab_name}",
            ):
                st.session_state.library_tab = tab_name
                st.rerun()


# -----------------------------
# ホーム
# -----------------------------
def render_home() -> None:
    st.title("ホーム")
    st.caption("やりたいことから入口を選ぶ構成です。")

    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.subheader("本を深める")
            st.write("感想を発散し、壁打ちし、まとめまで整理します。")
            if st.button("本を深めるへ", use_container_width=True):
                st.session_state.nav_page = "本を深める"
                st.rerun()
    with c2:
        with st.container(border=True):
            st.subheader("伝え方を考える")
            st.write("ゲストに何をどう伝えるか、テーマや本を壁打ちします。")
            if st.button("伝え方を考えるへ", use_container_width=True):
                st.session_state.nav_page = "伝え方を考える"
                st.rerun()
    with c3:
        with st.container(border=True):
            st.subheader("ライブラリ")
            st.write("本・著者・テーマを管理し、必要な本にすぐ遷移できます。")
            if st.button("ライブラリへ", use_container_width=True):
                st.session_state.nav_page = "ライブラリ"
                st.rerun()


# -----------------------------
# 本を深める
# -----------------------------
def render_deepen_book_page() -> None:
    st.title("本を深める")
    book_options = {f"{b['title']} / {b['author']['name']}": b["id"] for b in st.session_state.books}
    selected_label = st.selectbox("書籍選択", list(book_options.keys()))
    st.session_state.selected_book_id = book_options[selected_label]
    book = get_selected_book()

    progress1, progress2, progress3 = st.columns(3)
    progress1.metric("1. 発散", "進行中")
    progress2.metric("2. 壁打ち", "準備OK")
    progress3.metric("3. まとめ", "出力可")

    left, center, right = st.columns([1.2, 1.4, 1])
    with left:
        with st.container(border=True):
            st.subheader("発散")
            st.text_area("印象に残ったこと", placeholder="音声やテキストで自由入力", height=120)
            st.text_area("違和感・反論", placeholder="引っかかった点をメモ", height=100)
            st.text_area("自分に引きつける", placeholder="仕事や生活との接点", height=100)
            st.text_area("人に伝えたいメッセージ", placeholder="共有したい気づき", height=100)
    with center:
        with st.container(border=True):
            st.subheader("壁打ち")
            st.chat_message("assistant").write("この本で特に印象に残ったフレーズや考え方はありますか？")
            st.chat_message("user").write(book["core_impression"])
            st.chat_message("assistant").write("その考え方を、あなたの仕事や日常ではどう活かせそうですか？")
            st.text_input("壁打ちメッセージ", placeholder="AIに追加で相談する内容")
    with right:
        with st.container(border=True):
            st.subheader("まとめ")
            st.write("**自分用メモ**")
            st.caption(book["latest_outputs"]["private_memo"] or "未整理")
            st.write("**読書会メモ**")
            st.caption(book["latest_outputs"]["reading_group"] or "未整理")
            st.write("**SNS下書き**")
            st.caption(book["latest_outputs"]["sns"] or "未整理")
            if st.button("本詳細を開く", use_container_width=True):
                open_book_detail(book["id"], "本を深める")


# -----------------------------
# 伝え方を考える
# -----------------------------
def score_book(book: Dict, guest: Dict) -> int:
    score = 0
    text = " ".join(book.get("themes", []) + book.get("message_candidates", []))
    for theme in guest.get("recommended_themes", []):
        if theme in text:
            score += 2
    for piece in guest.get("missing_pieces", []):
        if piece in text:
            score += 1
    if "転職" in guest.get("current_concerns", "") and "未来予測" in text:
        score += 2
    return score


def recommended_books_for_guest(guest: Dict) -> List[Dict]:
    scored = [(score_book(book, guest), book) for book in st.session_state.books]
    scored.sort(key=lambda x: x[0], reverse=True)
    return [book for _, book in scored[:3]]


def render_message_design_page() -> None:
    st.title("伝え方を考える")
    guest_options = {f"{g['name']} / {g['relationship']}": g["id"] for g in st.session_state.guests}
    selected_label = st.selectbox(
        "ゲスト選択",
        list(guest_options.keys()),
        index=list(guest_options.values()).index(st.session_state.selected_guest_id),
    )
    st.session_state.selected_guest_id = guest_options[selected_label]
    guest = get_selected_guest()

    left, center, right = st.columns([1, 1.4, 1])
    with left:
        with st.container(border=True):
            st.subheader("相手理解")
            st.write(f"**{guest['name']}**")
            st.caption(guest["relationship"])
            st.caption(guest["occupation"])
            st.write("**現在の悩み**")
            st.write(guest["current_concerns"])
            st.write("**最近の会話**")
            st.write(guest["recent_conversation"])
            st.write("**価値観メモ**")
            st.write(guest["values_memo"])
    with center:
        with st.container(border=True):
            st.subheader("AI壁打ち")
            st.text_area("今回伝えたいこと", placeholder="例: 長期視点の必要性に気づいてほしい", height=100)
            st.chat_message("assistant").write(
                f"{guest['name']}さんは今『{guest['current_phase']}』の段階に見えます。まずは価値観や長期視点の整理が良さそうです。"
            )
            st.chat_message("assistant").write("テーマとしては『価値観』『目標設定』『未来予測』が相性よさそうです。")
            st.text_input("追加相談", placeholder="この相手に今どの本が自然？")
    with right:
        with st.container(border=True):
            st.subheader("診断")
            st.write("**足りないピース**")
            for item in guest["missing_pieces"]:
                st.write(f"- {item}")
            st.write("**おすすめテーマ**")
            st.write(" ".join([f"`#{t}`" for t in guest["recommended_themes"]]))

    st.subheader("候補本")
    cols = st.columns(3)
    for idx, book in enumerate(recommended_books_for_guest(guest)):
        with cols[idx]:
            with st.container(border=True):
                st.image(book["thumbnail"], use_container_width=True)
                st.markdown(f"**{book['title']}**")
                st.caption(book["author"]["name"])
                st.write(" ".join([f"`#{t}`" for t in book.get("themes", [])]))
                st.caption(book["share_message"])
                if st.button("本詳細へ", key=f"message_detail_{book['id']}", use_container_width=True):
                    open_book_detail(book["id"], "伝え方を考える")


# -----------------------------
# ライブラリ
# -----------------------------
def add_book_form() -> None:
    with st.expander("＋ 本を追加", expanded=False):
        with st.form("add_book_form"):
            title = st.text_input("書名")
            subtitle = st.text_input("サブタイトル")
            author_name = st.text_input("著者名")
            thumbnail = st.text_input("表紙画像URL", placeholder="未入力ならプレースホルダ")
            status = st.selectbox("読書ステータス", ["読書中", "読了", "未着手"])
            themes = st.text_input("テーマ", placeholder="例: 習慣, 継続, 働き方")
            share_message = st.text_area("人に伝えたいメッセージ")
            submitted = st.form_submit_button("追加する", use_container_width=True)
            if submitted and title and author_name:
                author = {
                    "id": max([b["author"]["id"] for b in st.session_state.books]) + 1,
                    "name": author_name,
                    "photo": "👤",
                    "short_title": "著者情報未登録",
                    "industry_position": "未設定",
                    "authority_summary": "著者プロフィールは未整理です。",
                    "career": "未設定",
                    "achievements": "未設定",
                    "episodes": "未設定",
                }
                new_id = max([b["id"] for b in st.session_state.books]) + 1
                st.session_state.books.insert(
                    0,
                    {
                        "id": new_id,
                        "title": title,
                        "subtitle": subtitle,
                        "thumbnail": thumbnail or "https://placehold.co/300x420?text=NO+COVER",
                        "amazon_url": "",
                        "status": status,
                        "read_dates": [str(date.today())],
                        "themes": [t.strip() for t in themes.split(",") if t.strip()],
                        "goal": "",
                        "core_impression": "",
                        "social_discussion": "",
                        "share_message": share_message,
                        "message_candidates": [share_message] if share_message else [],
                        "author": author,
                        "sessions": [],
                        "latest_outputs": {"private_memo": "", "reading_group": "", "sns": ""},
                        "change_log": {"before": "", "after": ""},
                    },
                )
                st.success("本を追加しました。")
                open_book_detail(new_id, "ライブラリ")


def render_library_books_tab() -> None:
    st.subheader("本")
    add_book_form()
    search = st.text_input("本を検索", placeholder="タイトル・著者・テーマ")
    cols = st.columns(3)
    filtered = []
    for book in st.session_state.books:
        haystack = (book["title"] + book["author"]["name"] + " ".join(book.get("themes", []))).lower()
        if search and search.lower() not in haystack:
            continue
        filtered.append(book)
    for idx, book in enumerate(filtered):
        with cols[idx % 3]:
            with st.container(border=True):
                st.image(book["thumbnail"], use_container_width=True)
                st.markdown(f"**{book['title']}**")
                st.caption(book["author"]["name"])
                st.caption(f"状態: {book['status']}")
                st.write(" ".join([f"`#{t}`" for t in book.get("themes", [])]))
                if st.button("本詳細へ", key=f"library_book_{book['id']}", use_container_width=True):
                    open_book_detail(book["id"], "ライブラリ")


def render_library_authors_tab() -> None:
    st.subheader("著者")
    cols = st.columns(2)
    authors = unique_authors()
    for idx, author in enumerate(authors):
        with cols[idx % 2]:
            with st.container(border=True):
                left, right = st.columns([1, 3])
                with left:
                    render_avatar(author.get("photo"), size=64)
                with right:
                    st.markdown(f"**{author['name']}**")
                    st.caption(author["short_title"])
                    st.write(author["industry_position"])
                linked_books = [b for b in st.session_state.books if b["author"]["id"] == author["id"]]
                st.caption("紐づく本")
                for book in linked_books:
                    if st.button(book["title"], key=f"author_link_{author['id']}_{book['id']}", use_container_width=True):
                        open_book_detail(book["id"], "ライブラリ")


def render_library_themes_tab() -> None:
    st.subheader("テーマ")
    grouped = grouped_books_by_theme()
    cols = st.columns(3)
    for idx, (theme, books) in enumerate(grouped.items()):
        with cols[idx % 3]:
            with st.container(border=True):
                st.markdown(f"**#{theme}**")
                st.caption(f"関連本: {len(books)}冊")
                for book in books[:3]:
                    if st.button(book["title"], key=f"theme_link_{theme}_{book['id']}", use_container_width=True):
                        open_book_detail(book["id"], "ライブラリ")


def render_library_page() -> None:
    st.title("ライブラリ")
    tab_book, tab_author, tab_theme = st.tabs(["本", "著者", "テーマ"])
    if st.session_state.library_tab == "著者":
        default_tab = 1
    elif st.session_state.library_tab == "テーマ":
        default_tab = 2
    else:
        default_tab = 0
    st.caption(f"現在のライブラリ内フォーカス: {['本', '著者', 'テーマ'][default_tab]}")

    with tab_book:
        st.session_state.library_tab = "本"
        render_library_books_tab()
    with tab_author:
        st.session_state.library_tab = "著者"
        render_library_authors_tab()
    with tab_theme:
        st.session_state.library_tab = "テーマ"
        render_library_themes_tab()


# -----------------------------
# 本詳細（トップメニューには出さない）
# -----------------------------
def render_book_detail_page() -> None:
    book = get_selected_book()
    left, main = st.columns([1, 3])

    with left:
        st.image(book["thumbnail"], use_container_width=True)
        st.markdown(f"### {book['title']}")
        st.caption(book["author"]["name"])
        st.write(f"状態: {book['status']}")
        st.write(f"記録日: {', '.join(book['read_dates'])}")
        st.write(" ".join([f"`#{t}`" for t in book.get("themes", [])]))
        if st.button("← 元の画面へ戻る", use_container_width=True):
            st.session_state.nav_page = st.session_state.detail_return_page
            st.rerun()

    with main:
        st.caption(f"{st.session_state.detail_return_page} > 本詳細")
        st.title(book["title"])
        overview, sessions, summary, author_info = st.tabs(["概要", "セッション履歴", "最新まとめ", "著者情報"])

        with overview:
            c1, c2 = st.columns(2)
            with c1:
                with st.container(border=True):
                    st.subheader("この本の目的")
                    st.write(book["goal"] or "未設定")
                with st.container(border=True):
                    st.subheader("自分の感想の核")
                    st.write(book["core_impression"] or "未整理")
            with c2:
                with st.container(border=True):
                    st.subheader("世の中の論点")
                    st.write(book["social_discussion"] or "未整理")
                with st.container(border=True):
                    st.subheader("人に伝えたいメッセージ")
                    st.write(book["share_message"] or "未整理")

        with sessions:
            left_col, right_col = st.columns([2, 1])
            with left_col:
                for session in book["sessions"]:
                    with st.container(border=True):
                        st.markdown(f"**{session['title']}**")
                        st.caption(f"{session['date']} / {' ・ '.join(session['tags'])}")
                        st.write(session["raw_note"])
                        st.info(session["ai_summary"])
            with right_col:
                with st.container(border=True):
                    st.subheader("変化ログ")
                    st.caption("最初に注目した点")
                    st.write(book["change_log"]["before"] or "未記録")
                    st.caption("後から重要になった点")
                    st.write(book["change_log"]["after"] or "未記録")

        with summary:
            c1, c2, c3 = st.columns(3)
            with c1:
                with st.container(border=True):
                    st.subheader("自分用メモ")
                    st.write(book["latest_outputs"]["private_memo"] or "未整理")
            with c2:
                with st.container(border=True):
                    st.subheader("読書会メモ")
                    st.write(book["latest_outputs"]["reading_group"] or "未整理")
            with c3:
                with st.container(border=True):
                    st.subheader("SNS下書き")
                    st.write(book["latest_outputs"]["sns"] or "未整理")

        with author_info:
            author = book["author"]
            head1, head2 = st.columns([1, 3])
            with head1:
                render_avatar(author.get("photo"), size=96)
            with head2:
                st.subheader(author["name"])
                st.caption(author["short_title"])
                st.write(author["authority_summary"])

            c1, c2 = st.columns(2)
            with c1:
                with st.container(border=True):
                    st.subheader("経歴")
                    st.write(author["career"])
                with st.container(border=True):
                    st.subheader("功績")
                    st.write(author["achievements"])
            with c2:
                with st.container(border=True):
                    st.subheader("有名エピソード")
                    st.write(author["episodes"])
                with st.container(border=True):
                    st.subheader("業界ポジション")
                    st.write(author["industry_position"])


# -----------------------------
# メイン
# -----------------------------
def main() -> None:
    init_state()
    render_sidebar()

    if st.session_state.nav_page == "ホーム":
        render_home()
    elif st.session_state.nav_page == "本を深める":
        render_deepen_book_page()
    elif st.session_state.nav_page == "伝え方を考える":
        render_message_design_page()
    elif st.session_state.nav_page == "ライブラリ":
        render_library_page()
    else:
        render_book_detail_page()


if __name__ == "__main__":
    main()
