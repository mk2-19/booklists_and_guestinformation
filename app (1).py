import streamlit as st
from datetime import date
from typing import Dict, List, Optional

st.set_page_config(
    page_title="読書内省アプリ MVP",
    page_icon="📚",
    layout="wide",
)


def sample_books() -> List[Dict]:
    return [
        {
            "id": 1,
            "title": "Atomic Habits",
            "subtitle": "小さな習慣の積み重ね",
            "amazon_url": "https://www.amazon.co.jp/",
            "thumbnail": "https://covers.openlibrary.org/b/isbn/9780735211292-M.jpg",
            "status": "読了",
            "read_dates": ["2026-06-01", "2026-06-10"],
            "themes": ["習慣", "継続", "働き方", "行動変容"],
            "message_candidates": [
                "成果を急ぐ前に、続けられる構造を作ることが大切",
                "やる気より環境設計のほうが再現性が高い",
                "小さな改善の積み重ねが大きな変化になる",
            ],
            "suitable_for": ["行動はしたいが続かない人", "習慣化したい人", "実務寄りに考えたい人"],
            "goal": "習慣化を、仕事の仕組み化とどうつなげるかを考える",
            "core_impression": "習慣を意志の問題ではなく環境設計として扱う視点が強く残った。",
            "social_discussion": "多くの読者は『小さく始める』『仕組みで継続する』点を重視し、実践性の高さがよく議論される。",
            "share_message": "成果を急ぐ前に、続けられる構造を作ることの重要性を伝えたい。",
            "author": {
                "id": 101,
                "name": "James Clear",
                "photo": "👤",
                "short_title": "習慣形成の実務家・著述家",
                "industry_position": "行動変容・習慣化分野で広く読まれる実務家",
                "authority_summary": "習慣形成を行動科学と実践の橋渡しで広めた著述家。",
                "career": "習慣・意思決定・継続改善をテーマに執筆と講演を行う。",
                "achievements": "世界的ベストセラーを持ち、習慣形成の実践フレームを普及。",
                "episodes": "怪我の経験や自身の回復過程を通じて、小さな改善の積み重ねを重視する考え方を発信。",
            },
            "sessions": [
                {
                    "id": 1,
                    "title": "初回感想",
                    "date": "2026-06-10",
                    "tags": ["音声", "壁打ち"],
                    "raw_note": "習慣は気合ではなく環境設計という話が特に刺さった。",
                    "ai_summary": "自分の仕事では、個人の努力よりも継続しやすい業務設計に置き換える発想が重要と整理。",
                },
                {
                    "id": 2,
                    "title": "読書会前",
                    "date": "2026-06-13",
                    "tags": ["追記"],
                    "raw_note": "他人に伝えるなら、才能より再現性のある仕組みの話として紹介したい。",
                    "ai_summary": "共有メッセージは『できる人の根性論ではなく、誰でも改善できる構造』に寄せるとよい。",
                },
            ],
            "latest_outputs": {
                "private_memo": "仕事の継続課題は、行動目標ではなく環境設計の見直しとして再定義する。",
                "reading_group": "この本は『頑張る方法』より『続く仕組み』を作る本として紹介する。",
                "sns": "続ける力は意志力より設計力。小さく始められる環境を作る方が、やる気に頼るよりずっと強い。",
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
            "amazon_url": "https://www.amazon.co.jp/",
            "thumbnail": "https://covers.openlibrary.org/b/isbn/9780743269513-M.jpg",
            "status": "読書中",
            "read_dates": ["2026-06-12"],
            "themes": ["価値観", "主体性", "目標設定", "人間関係", "働き方"],
            "message_candidates": [
                "成果の前に、自分の反応の選び方を見直すことが大切",
                "知っていることと、実際に使えていることは違う",
                "目先の効率より、原則に基づく判断が長期的に効く",
            ],
            "suitable_for": ["価値観を整理したい人", "対人関係を見直したい人", "考え方の土台から整えたい人"],
            "goal": "原則中心の考え方を、対人関係と意思決定にどう活かすか整理する",
            "core_impression": "主体性の話は知っていたが、実際の対人場面に落とし込むとまだ浅い。",
            "social_discussion": "『主体性』『Win-Win』『重要事項を優先』が広く取り上げられる。",
            "share_message": "成果より前に、自分の反応の選び方を見直す大切さを伝えたい。",
            "author": {
                "id": 102,
                "name": "Stephen R. Covey",
                "photo": "👤",
                "short_title": "リーダーシップ思想家・著述家",
                "industry_position": "自己啓発・リーダーシップ分野の古典的著者",
                "authority_summary": "原則中心のリーダーシップを広めた著者として長く参照される。",
                "career": "教育・組織開発・リーダーシップ領域で著述と研修を展開。",
                "achievements": "7つの習慣を通じて自己啓発分野で世界的な影響を持つ。",
                "episodes": "日々の効率より、価値観と原則に基づく生き方を強調した点で長く支持される。",
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
                "reading_group": "有名な本だが、知っていることと使えていることの差が大きい本として共有する。",
                "sns": "知っている言葉ほど、生活の具体場面に落とさないと空回りする。主体性も同じ。",
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
            "amazon_url": "https://www.amazon.co.jp/",
            "thumbnail": "https://covers.openlibrary.org/b/isbn/9781509527496-M.jpg",
            "status": "読了",
            "read_dates": ["2026-05-20"],
            "themes": ["キャリア", "働き方", "未来予測", "目標設定"],
            "message_candidates": [
                "長寿化でキャリア設計の前提が変わる",
                "目先の転職ではなく人生全体の設計が必要",
                "学び直しと柔軟性がこれからの武器になる",
            ],
            "suitable_for": ["転職を考えている人", "将来不安がある人", "長期目線を持ちたい人"],
            "goal": "長期的なキャリア視点を持ち、今の選択を見直す材料を得る",
            "core_impression": "キャリアを単発の転職で考えるのではなく、長い人生の設計として捉え直す必要を感じた。",
            "social_discussion": "100年時代という前提から、学び直しや複数ステージの人生設計が議論されることが多い。",
            "share_message": "今の不安を解消するには、短期最適より長期視点の設計が必要だと伝えたい。",
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
                "sns": "キャリアは次の会社選びだけじゃなく、長い人生でどう学び、どう働くかの設計そのもの。",
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
            "recent_conversation": "最近、将来がなんとなく不安で転職サイトを見ていると話していた。収入面の不安も少しある。",
            "values_memo": "自由度は高めたいが、安定も捨てたくない。人とのつながりは重視。",
            "animal_note": "動物占い: 柔軟で人当たりが良いタイプとして見立て。会話は共感から入るとよさそう。",
            "sync_status": "別アプリ連携済み",
            "current_phase": "目標設計の手前",
            "missing_pieces": ["中長期の目標", "働き方の価値観", "未来の経済変化の認識"],
            "recommended_themes": ["目標設定", "価値観", "未来予測", "働き方"],
            "cautions": ["最初から選択肢比較に行きすぎない", "不安を煽りすぎず、視点を広げる形で進める"],
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
            "cautions": ["理想論より、できる範囲の小さな実践に寄せる"],
        },
    ]



def init_state() -> None:
    if "books" not in st.session_state:
        st.session_state.books = sample_books()
    if "guests" not in st.session_state:
        st.session_state.guests = sample_guests()
    if "selected_book_id" not in st.session_state:
        st.session_state.selected_book_id = 1
    if "selected_guest_id" not in st.session_state:
        st.session_state.selected_guest_id = 201
    if "page" not in st.session_state:
        st.session_state.page = "本詳細"
    if "new_session_counter" not in st.session_state:
        st.session_state.new_session_counter = 100
    if "planning_notes" not in st.session_state:
        st.session_state.planning_notes = {
            "desired_message": "今の不安を解消するには、目先の転職より人生全体の設計が必要かもしれないと気づいてほしい",
            "event_goal": "次回読書会で長期視点の問いを持ち帰ってもらう",
            "guest_realization": "働き方の選択を、条件比較だけでなく価値観や長期設計で見直してほしい",
            "audience_attributes": "転職意向あり / 将来不安あり / まだ目標が明確ではない",
        }


def get_next_book_id() -> int:
    return max(book["id"] for book in st.session_state.books) + 1


def get_next_author_id() -> int:
    author_ids = [book["author"]["id"] for book in st.session_state.books]
    return max(author_ids) + 1


def find_author_by_name(author_name: str) -> Optional[Dict]:
    for book in st.session_state.books:
        if book["author"]["name"].strip().lower() == author_name.strip().lower():
            return book["author"]
    return None


def add_book_to_library(
    title: str,
    subtitle: str,
    author_name: str,
    amazon_url: str,
    thumbnail_url: str,
    status: str,
    read_date: str,
    themes: List[str],
    goal: str,
    share_message: str,
) -> int:
    existing_author = find_author_by_name(author_name)
    author = existing_author or {
        "id": get_next_author_id(),
        "name": author_name,
        "photo": "👤",
        "short_title": "著者情報未登録",
        "industry_position": "未設定",
        "authority_summary": "著者プロフィールは未整理です。",
        "career": "未設定",
        "achievements": "未設定",
        "episodes": "未設定",
    }

    new_book_id = get_next_book_id()
    book = {
        "id": new_book_id,
        "title": title,
        "subtitle": subtitle,
        "amazon_url": amazon_url,
        "thumbnail": thumbnail_url or "https://placehold.co/300x420?text=NO+COVER",
        "status": status,
        "read_dates": [read_date] if read_date else [str(date.today())],
        "themes": themes,
        "message_candidates": [share_message] if share_message else [],
        "suitable_for": [],
        "goal": goal or "未設定",
        "core_impression": "",
        "social_discussion": "",
        "share_message": share_message,
        "author": author,
        "sessions": [],
        "latest_outputs": {
            "private_memo": "",
            "reading_group": "",
            "sns": "",
        },
        "change_log": {
            "before": "",
            "after": "",
        },
    }
    st.session_state.books = [book] + st.session_state.books
    return new_book_id



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



def upsert_book(updated_book: Dict) -> None:
    books = []
    for book in st.session_state.books:
        books.append(updated_book if book["id"] == updated_book["id"] else book)
    st.session_state.books = books



def add_session(book_id: int, title: str, tags: List[str], raw_note: str, ai_summary: str) -> None:
    book = get_selected_book()
    st.session_state.new_session_counter += 1
    session = {
        "id": st.session_state.new_session_counter,
        "title": title,
        "date": str(date.today()),
        "tags": tags,
        "raw_note": raw_note,
        "ai_summary": ai_summary,
    }
    book["sessions"] = [session] + book["sessions"]
    if raw_note:
        book["core_impression"] = raw_note[:140]
    upsert_book(book)



def score_book_for_guest(book: Dict, guest: Dict, desired_message: str) -> int:
    text = " ".join(book.get("themes", []) + book.get("message_candidates", []) + book.get("suitable_for", []))
    score = 0
    for item in guest.get("recommended_themes", []):
        if item in text:
            score += 2
    for item in guest.get("missing_pieces", []):
        if item in desired_message or item in text:
            score += 1
    if "転職" in guest.get("current_concerns", "") and ("未来予測" in text or "キャリア" in text):
        score += 2
    if "続かない" in guest.get("recent_conversation", "") and ("習慣" in text or "継続" in text):
        score += 2
    return score



def get_recommended_books(guest: Dict, desired_message: str) -> List[Dict]:
    scored = []
    for book in st.session_state.books:
        scored.append((score_book_for_guest(book, guest, desired_message), book))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [book for _, book in scored[:3]]



def render_avatar(photo: Optional[str], size: int = 72) -> None:
    if not photo or photo == "👤":
        st.markdown(
            f"<div style='font-size:{size}px; text-align:center; line-height:1;'>👤</div>",
            unsafe_allow_html=True,
        )
    else:
        st.image(photo, use_container_width=True)



def render_sidebar_menu_button(label: str, icon: str, page_name: str) -> None:
    is_active = st.session_state.page == page_name
    button_label = f"{icon}  {label}"
    if st.sidebar.button(button_label, use_container_width=True, type="primary" if is_active else "secondary"):
        st.session_state.page = page_name
        st.rerun()



def sidebar_navigation() -> None:
    st.sidebar.title("📚 読書内省アプリ MVP")
    st.sidebar.caption("メニュー")
    render_sidebar_menu_button("本一覧", "📚", "本一覧")
    render_sidebar_menu_button("著者一覧", "🧑", "著者一覧")
    render_sidebar_menu_button("本詳細", "📖", "本詳細")
    render_sidebar_menu_button("本を追加", "➕", "本を追加")
    render_sidebar_menu_button("伝えたいことから探す", "🧭", "伝えたいことから探す")
    st.sidebar.divider()

    if st.session_state.page == "伝えたいことから探す":
        guest = get_selected_guest()
        st.sidebar.caption("現在のゲスト")
        st.sidebar.write(f"**{guest['name']}**")
        st.sidebar.caption(guest["relationship"])
        st.sidebar.caption(guest["occupation"])
        st.sidebar.success(guest["sync_status"])
    elif st.session_state.page == "本を追加":
        st.sidebar.caption("追加ヒント")
        st.sidebar.write("表紙URLが未入力でも追加できます。")
        st.sidebar.write("著者写真がない場合は自動で 👤 表示になります。")
    else:
        book = get_selected_book()
        st.sidebar.caption("現在の本")
        st.sidebar.image(book["thumbnail"], width=140)
        st.sidebar.write(f"**{book['title']}**")
        st.sidebar.write(book["author"]["name"])
        st.sidebar.caption("テーマ")
        st.sidebar.write(" ".join([f"`#{theme}`" for theme in book.get("themes", [])]))
        if st.sidebar.button("この本を開く", use_container_width=True):
            st.session_state.page = "本詳細"



def render_book_grid() -> None:
    st.title("本一覧")
    search = st.text_input("検索", placeholder="タイトル・著者・テーマで検索")
    c1, c2, c3 = st.columns([1, 1, 1])
    author_filter = c1.selectbox("著者", ["すべて"] + sorted({b['author']['name'] for b in st.session_state.books}))
    status_filter = c2.selectbox("ステータス", ["すべて", "読了", "読書中"])
    view = c3.radio("表示", ["グリッド", "一覧"], horizontal=True)

    filtered = []
    for book in st.session_state.books:
        haystack = (book["title"] + book["author"]["name"] + " ".join(book.get("themes", []))).lower()
        if search and search.lower() not in haystack:
            continue
        if author_filter != "すべて" and book["author"]["name"] != author_filter:
            continue
        if status_filter != "すべて" and book["status"] != status_filter:
            continue
        filtered.append(book)

    if view == "グリッド":
        cols = st.columns(3)
        for idx, book in enumerate(filtered):
            with cols[idx % 3]:
                with st.container(border=True):
                    st.image(book["thumbnail"], use_container_width=True)
                    st.markdown(f"**{book['title']}**")
                    st.caption(book["author"]["name"])
                    st.caption(f"状態: {book['status']}")
                    st.caption(f"読了/記録日: {', '.join(book['read_dates'])}")
                    st.write(" ".join([f"`#{theme}`" for theme in book.get("themes", [])]))
                    tags = []
                    if book["sessions"]:
                        tags.append("壁打ち済み")
                    if book["share_message"]:
                        tags.append("共有メモあり")
                    st.write(" ".join([f"`{tag}`" for tag in tags]))
                    if st.button("詳細を見る", key=f"book_detail_{book['id']}", use_container_width=True):
                        st.session_state.selected_book_id = book["id"]
                        st.session_state.page = "本詳細"
                        st.rerun()
    else:
        for book in filtered:
            cols = st.columns([1, 4, 2, 1])
            cols[0].image(book["thumbnail"], width=80)
            cols[1].markdown(f"**{book['title']}**  \n{book['author']['name']}  \n{' '.join([f'`#{t}`' for t in book.get('themes', [])])}")
            cols[2].write(f"状態: {book['status']}")
            if cols[3].button("開く", key=f"book_open_{book['id']}"):
                st.session_state.selected_book_id = book["id"]
                st.session_state.page = "本詳細"
                st.rerun()



def render_author_grid() -> None:
    st.title("著者一覧")
    search = st.text_input("著者検索", placeholder="著者名で検索")
    show_photo_only = st.checkbox("写真ありのみ")

    authors = []
    for book in st.session_state.books:
        authors.append({**book["author"], "book": book})

    cols = st.columns(2)
    visible = []
    for item in authors:
        if search and search.lower() not in item["name"].lower():
            continue
        has_photo = bool(item["photo"] and item["photo"] != "👤")
        if show_photo_only and not has_photo:
            continue
        visible.append(item)

    for idx, item in enumerate(visible):
        with cols[idx % 2]:
            with st.container(border=True):
                avatar_col, text_col = st.columns([1, 3])
                with avatar_col:
                    render_avatar(item["photo"], size=64)
                text_col.markdown(f"**{item['name']}**")
                text_col.caption(item["short_title"])
                st.write(item["industry_position"])
                st.caption("読んだ本: 1冊")
                st.caption(f"紐づく本: {item['book']['title']}")
                if st.button("関連本を見る", key=f"author_book_{item['id']}", use_container_width=True):
                    st.session_state.selected_book_id = item["book"]["id"]
                    st.session_state.page = "本詳細"
                    st.rerun()



def render_overview_tab(book: Dict) -> None:
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.subheader("この本の目的")
            st.write(book["goal"])
        with st.container(border=True):
            st.subheader("自分の感想の核")
            st.write(book["core_impression"])
        with st.container(border=True):
            st.subheader("テーマ")
            st.write(" ".join([f"`#{theme}`" for theme in book.get("themes", [])]))
    with c2:
        with st.container(border=True):
            st.subheader("世の中の論点")
            st.write(book["social_discussion"])
        with st.container(border=True):
            st.subheader("人に伝えたいメッセージ")
            st.write(book["share_message"])
        with st.container(border=True):
            st.subheader("この本から切り出しやすいメッセージ")
            for msg in book.get("message_candidates", []):
                st.write(f"- {msg}")



def render_sessions_tab(book: Dict) -> None:
    left, right = st.columns([2, 1])
    with left:
        st.subheader("セッション履歴")
        for session in book["sessions"]:
            with st.container(border=True):
                st.markdown(f"**{session['title']}**")
                st.caption(f"{session['date']} / {' ・ '.join(session['tags'])}")
                st.write(session["raw_note"])
                st.info(session["ai_summary"])

        st.subheader("追加入力")
        with st.form("add_session_form"):
            title = st.text_input("セッション名", placeholder="例: 読書会後の追記")
            mode = st.multiselect("種別", ["音声", "壁打ち", "追記"], default=["追記"])
            raw_note = st.text_area("今の考え", placeholder="話したこと・新しく気づいたことを追加")
            ai_summary = st.text_area("AIとの整理メモ", placeholder="ここには壁打ち後の要約を入れる想定")
            submitted = st.form_submit_button("セッションを追加", use_container_width=True)
            if submitted and title and raw_note:
                add_session(book["id"], title, mode, raw_note, ai_summary or "AI整理メモ未入力")
                st.success("セッションを追加しました")
                st.rerun()
    with right:
        with st.container(border=True):
            st.subheader("変化ログ")
            st.caption("最初に注目した点")
            st.write(book["change_log"]["before"])
            st.caption("後から重要になった点")
            st.write(book["change_log"]["after"])



def render_summary_tab(book: Dict) -> None:
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.subheader("自分用メモ")
            st.write(book["latest_outputs"]["private_memo"])
    with c2:
        with st.container(border=True):
            st.subheader("読書会メモ")
            st.write(book["latest_outputs"]["reading_group"])
    with c3:
        with st.container(border=True):
            st.subheader("SNS下書き")
            st.write(book["latest_outputs"]["sns"])



def render_author_tab(book: Dict) -> None:
    author = book["author"]
    head1, head2 = st.columns([1, 3])
    with head1:
        render_avatar(author["photo"], size=96)
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



def render_book_detail() -> None:
    book = get_selected_book()
    left, main = st.columns([1, 3])

    with left:
        st.image(book["thumbnail"], use_container_width=True)
        st.markdown(f"### {book['title']}")
        st.caption(book["author"]["name"])
        st.write(f"状態: {book['status']}")
        st.write(f"記録日: {', '.join(book['read_dates'])}")
        st.write(" ".join([f"`#{theme}`" for theme in book.get("themes", [])]))
        st.button("感想を追加", use_container_width=True)
        st.button("壁打ちを再開", use_container_width=True)
        st.button("まとめを更新", use_container_width=True)
        st.divider()
        st.caption("関連する著者")
        render_avatar(book["author"]["photo"], size=72)
        st.write(f"**{book['author']['name']}**")
        st.caption(book["author"]["short_title"])

    with main:
        st.caption("本一覧 > 本詳細")
        st.title(book["title"])
        overview_tab, sessions_tab, summary_tab, author_tab = st.tabs([
            "概要", "セッション履歴", "最新まとめ", "著者情報"
        ])
        with overview_tab:
            render_overview_tab(book)
        with sessions_tab:
            render_sessions_tab(book)
        with summary_tab:
            render_summary_tab(book)
        with author_tab:
            render_author_tab(book)



def render_guest_sidebar(guest: Dict) -> None:
    st.subheader("ゲスト情報")
    with st.container(border=True):
        st.write(f"**{guest['name']}**")
        st.caption(guest["relationship"])
        st.caption(guest["occupation"])
        st.success(guest["sync_status"])
    with st.container(border=True):
        st.caption("現在の悩み")
        st.write(guest["current_concerns"])
    with st.container(border=True):
        st.caption("最近の会話要約")
        st.write(guest["recent_conversation"])
    with st.container(border=True):
        st.caption("価値観メモ")
        st.write(guest["values_memo"])
    with st.container(border=True):
        st.caption("補助メモ")
        st.write(guest["animal_note"])



def render_step_flow() -> None:
    cols = st.columns(4)
    steps = [
        ("1", "相手を理解"),
        ("2", "足りないピース診断"),
        ("3", "テーマ決定"),
        ("4", "本とメッセージ選定"),
    ]
    for idx, (num, label) in enumerate(steps):
        with cols[idx]:
            st.markdown(f"### {num}")
            st.caption(label)



def render_ai_mock_chat(guest: Dict, desired_message: str) -> None:
    st.subheader("AI壁打ち")
    with st.container(border=True):
        st.chat_message("assistant").write(
            f"{guest['name']}さんの最近の会話を見ると、まずは『{guest['current_phase']}』の整理が大切そうです。"
        )
        st.chat_message("assistant").write(
            f"いま伝えたいのは『{desired_message}』ですね。やや広いので、まずは価値観か長期視点のどちらを入口にするか考えましょう。"
        )
        st.chat_message("user").write("今回は、転職の話にすぐ行きすぎず、長期視点を持ってもらいたいです。")
        st.chat_message("assistant").write(
            "それなら、将来不安を直接解決しようとするより、『そもそも何を軸にキャリアを考えるか』を問い直す流れが自然です。"
        )
        st.text_input("メッセージを入力", placeholder="例: この相手に今どんな気づきを渡すべき？", key="planning_chat_input")



def render_diagnosis_panel(guest: Dict) -> None:
    st.subheader("診断結果")
    with st.container(border=True):
        st.caption("現在フェーズ")
        st.write(f"**{guest['current_phase']}**")
    with st.container(border=True):
        st.caption("足りないピース")
        for item in guest["missing_pieces"]:
            st.write(f"- {item}")
    with st.container(border=True):
        st.caption("おすすめテーマ")
        st.write(" ".join([f"`#{theme}`" for theme in guest["recommended_themes"]]))
    with st.container(border=True):
        st.caption("投げる質問")
        st.write("- 5年後どうなっていたいですか？")
        st.write("- 今の働き方を続けた先に納得感はありますか？")
        st.write("- 仕事に何を求めているか、条件以外で言うと何が大事ですか？")
    with st.container(border=True):
        st.caption("注意点")
        for caution in guest["cautions"]:
            st.write(f"- {caution}")



def render_candidate_books(guest: Dict, desired_message: str) -> None:
    st.subheader("候補本・使い方")
    books = get_recommended_books(guest, desired_message)
    cols = st.columns(3)
    for idx, book in enumerate(books):
        with cols[idx]:
            with st.container(border=True):
                st.image(book["thumbnail"], use_container_width=True)
                st.markdown(f"**{book['title']}**")
                st.caption(book["author"]["name"])
                st.write(" ".join([f"`#{theme}`" for theme in book.get("themes", [])]))
                st.caption("この本が合う理由")
                st.write(book["goal"])
                st.caption("切り出しやすいメッセージ")
                st.write(f"- {book['message_candidates'][0]}")
                if st.button("本詳細へ", key=f"plan_book_detail_{book['id']}", use_container_width=True):
                    st.session_state.selected_book_id = book["id"]
                    st.session_state.page = "本詳細"
                    st.rerun()
                if st.button("読書会メモに追加", key=f"plan_add_{book['id']}", use_container_width=True):
                    st.success(f"{book['title']} を候補としてメモしました")



def render_export_card(guest: Dict, books: List[Dict]) -> None:
    selected_title = books[0]["title"] if books else "未選択"
    selected_theme = guest["recommended_themes"][0] if guest["recommended_themes"] else "未選択"
    with st.container(border=True):
        st.subheader("次回読書会設計")
        st.caption("採用テーマ")
        st.write(selected_theme)
        st.caption("採用本")
        st.write(selected_title)
        st.caption("オープニング質問")
        st.write("今の働き方を続けた先で、どんな未来なら納得できますか？")
        st.caption("先輩への依頼メッセージ")
        st.write("長期視点を持つようになったきっかけや、価値観が変わった経験を一言で共有してもらう。")
        st.caption("次回フォローメモ")
        st.write("価値観と言語化できた目標が出てきたら、次は選択肢比較のテーマへ進める。")



def render_message_search_page() -> None:
    guest = get_selected_guest()
    st.title("伝えたいことから探す")
    render_step_flow()
    st.divider()

    left, main = st.columns([1, 3])
    with left:
        guest_options = {f"{g['name']} / {g['relationship']}": g["id"] for g in st.session_state.guests}
        selected_label = st.selectbox(
            "ゲスト選択",
            list(guest_options.keys()),
            index=list(guest_options.values()).index(st.session_state.selected_guest_id),
        )
        st.session_state.selected_guest_id = guest_options[selected_label]
        guest = get_selected_guest()
        render_guest_sidebar(guest)

    with main:
        c1, c2, c3 = st.columns([1.2, 1.2, 1])
        with c1:
            with st.container(border=True):
                st.subheader("今回伝えたいこと")
                desired_message = st.text_area(
                    "伝えたいメッセージ",
                    key="desired_message",
                    value=st.session_state.planning_notes["desired_message"],
                    height=120,
                )
                event_goal = st.text_area(
                    "今回のイベント目的",
                    key="event_goal",
                    value=st.session_state.planning_notes["event_goal"],
                    height=90,
                )
                guest_realization = st.text_area(
                    "相手に気づいてほしいこと",
                    key="guest_realization",
                    value=st.session_state.planning_notes["guest_realization"],
                    height=90,
                )
                audience_attributes = st.text_area(
                    "相手属性メモ",
                    key="audience_attributes",
                    value=st.session_state.planning_notes["audience_attributes"],
                    height=90,
                )
                st.session_state.planning_notes = {
                    "desired_message": desired_message,
                    "event_goal": event_goal,
                    "guest_realization": guest_realization,
                    "audience_attributes": audience_attributes,
                }
        with c2:
            render_ai_mock_chat(guest, desired_message)
        with c3:
            render_diagnosis_panel(guest)

        st.divider()
        candidate_books = get_recommended_books(guest, st.session_state.planning_notes["desired_message"])
        lower_left, lower_right = st.columns([2.3, 1])
        with lower_left:
            render_candidate_books(guest, st.session_state.planning_notes["desired_message"])
        with lower_right:
            render_export_card(guest, candidate_books)



def render_add_book_page() -> None:
    st.title("本をライブラリに追加")
    st.caption("Amazon URLや基本情報から、本をライブラリへ追加するための画面です。")

    left, right = st.columns([1.4, 1])
    with left:
        with st.form("add_book_form"):
            st.subheader("基本情報")
            amazon_url = st.text_input("Amazon URL", placeholder="https://www.amazon.co.jp/... ")
            title = st.text_input("書名", placeholder="例: Atomic Habits")
            subtitle = st.text_input("サブタイトル", placeholder="例: 小さな習慣の積み重ね")
            author_name = st.text_input("著者名", placeholder="例: James Clear")
            thumbnail_url = st.text_input("表紙画像URL", placeholder="未入力ならプレースホルダを使用")

            st.subheader("整理情報")
            status = st.selectbox("読書ステータス", ["読書中", "読了", "未着手"])
            read_date = st.date_input("記録日", value=date.today())
            themes_text = st.text_input("テーマ", placeholder="例: 習慣, 継続, 働き方")
            goal = st.text_area("この本を読む目的", placeholder="この本から何を得たいか")
            share_message = st.text_area("人に伝えたいメッセージ", placeholder="この本から切り出したいメッセージ")

            submitted = st.form_submit_button("ライブラリに追加", use_container_width=True)

            if submitted:
                if not title or not author_name:
                    st.error("書名と著者名は必須です。")
                else:
                    themes = [item.strip() for item in themes_text.split(",") if item.strip()]
                    new_book_id = add_book_to_library(
                        title=title,
                        subtitle=subtitle,
                        author_name=author_name,
                        amazon_url=amazon_url,
                        thumbnail_url=thumbnail_url,
                        status=status,
                        read_date=str(read_date),
                        themes=themes,
                        goal=goal,
                        share_message=share_message,
                    )
                    st.session_state.selected_book_id = new_book_id
                    st.session_state.page = "本詳細"
                    st.success("本をライブラリに追加しました。")
                    st.rerun()

    with right:
        with st.container(border=True):
            st.subheader("追加時のメモ")
            st.write("- 著者写真が未登録なら 👤 を表示")
            st.write("- 同じ著者名が既にある場合は、その著者情報を再利用")
            st.write("- テーマはカンマ区切りで複数登録可能")
            st.write("- 追加後は本詳細画面へ移動")
        with st.container(border=True):
            st.subheader("入力例")
            st.code(
                """書名: LIFE SHIFT\n著者名: Lynda Gratton\nテーマ: キャリア, 働き方, 未来予測\n人に伝えたいメッセージ: 目先の転職ではなく人生全体の設計が必要"""
            )



def main() -> None:
    init_state()
    sidebar_navigation()

    if st.session_state.page == "本一覧":
        render_book_grid()
    elif st.session_state.page == "著者一覧":
        render_author_grid()
    elif st.session_state.page == "本を追加":
        render_add_book_page()
    elif st.session_state.page == "伝えたいことから探す":
        render_message_search_page()
    else:
        render_book_detail()


if __name__ == "__main__":
    main()
