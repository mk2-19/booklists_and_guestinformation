import json
import os
import sqlite3
from datetime import date, datetime
from pathlib import Path
from typing import Dict, List, Optional

import streamlit as st

try:
    from openai import OpenAI
except Exception:
    OpenAI = None

st.set_page_config(page_title="読書リフレクション", page_icon="📚", layout="wide")

# Streamlit Cloud で書き込み可能な一時領域を利用
DB_DIR = Path("/tmp/book_reflection_app")
DB_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DB_DIR / "books_app.db"


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def jdump(value) -> str:
    return json.dumps(value, ensure_ascii=False)


def jload(value: Optional[str], default):
    if not value:
        return default
    try:
        return json.loads(value)
    except Exception:
        return default


def init_db() -> None:
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            photo TEXT,
            short_title TEXT,
            industry_position TEXT,
            authority_summary TEXT,
            career TEXT,
            achievements TEXT,
            episodes TEXT
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            subtitle TEXT,
            thumbnail TEXT,
            amazon_url TEXT,
            status TEXT,
            read_dates TEXT,
            themes TEXT,
            goal TEXT,
            core_impression TEXT,
            social_discussion TEXT,
            share_message TEXT,
            message_candidates TEXT,
            latest_private TEXT,
            latest_reading_group TEXT,
            latest_sns TEXT,
            change_before TEXT,
            change_after TEXT,
            author_id INTEGER,
            created_at TEXT,
            FOREIGN KEY(author_id) REFERENCES authors(id)
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            tags TEXT,
            impression_note TEXT,
            counter_note TEXT,
            personal_note TEXT,
            share_note TEXT,
            ai_response TEXT,
            created_at TEXT,
            FOREIGN KEY(book_id) REFERENCES books(id)
        )
        """
    )

    conn.commit()

    count = cur.execute("SELECT COUNT(*) FROM books").fetchone()[0]
    if count == 0:
        seed_data(conn)

    conn.close()


def seed_data(conn: sqlite3.Connection) -> None:
    authors = [
        (
            101,
            "James Clear",
            "👤",
            "習慣形成の実務家・著述家",
            "行動変容・習慣化分野で広く読まれる実務家",
            "習慣形成を行動科学と実践の橋渡しで広めた著述家。",
            "習慣・意思決定・継続改善をテーマに執筆と講演を行う。",
            "世界的ベストセラーを持ち、習慣形成の実践フレームを普及。",
            "小さな改善の積み重ねを重視する考え方で広く知られる。",
        ),
        (
            102,
            "Stephen R. Covey",
            "👤",
            "リーダーシップ思想家・著述家",
            "自己啓発・リーダーシップ分野の古典的著者",
            "原則中心のリーダーシップを広めた著者として長く参照される。",
            "教育・組織開発・リーダーシップ領域で著述と研修を展開。",
            "7つの習慣を通じて自己啓発分野で世界的な影響を持つ。",
            "価値観と原則に基づく生き方を強調した点で長く支持される。",
        ),
        (
            103,
            "Lynda Gratton",
            "👤",
            "組織論・未来の働き方研究者",
            "未来の働き方やキャリア設計領域で影響力のある研究者",
            "長寿化と働き方の変化を踏まえたキャリア論で広く参照される研究者。",
            "ロンドン・ビジネススクールで組織論と未来の働き方を研究。",
            "100年時代のキャリア論を一般層にも届く形で広めた。",
            "雇用・学び・人生設計を一体で捉える視点が広く受け入れられた。",
        ),
    ]
    conn.executemany("INSERT OR IGNORE INTO authors VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", authors)

    books = [
        (
            1,
            "Atomic Habits",
            "小さな習慣の積み重ね",
            "https://covers.openlibrary.org/b/isbn/9780735211292-M.jpg",
            "https://www.amazon.co.jp/",
            "読了",
            jdump(["2026-06-01", "2026-06-10"]),
            jdump(["習慣", "継続", "働き方", "行動変容"]),
            "習慣化を、仕事の仕組み化とどうつなげるかを考える",
            "習慣を意志の問題ではなく環境設計として扱う視点が強く残った。",
            "多くの読者は『小さく始める』『仕組みで継続する』点を重視し、実践性の高さがよく議論される。",
            "成果を急ぐ前に、続けられる構造を作ることの重要性を伝えたい。",
            jdump([
                "やる気より環境設計のほうが再現性が高い",
                "小さな改善の積み重ねが大きな変化になる",
            ]),
            "仕事の継続課題は、行動目標より環境設計の見直しとして再定義する。",
            "『頑張る方法』より『続く仕組み』を作る本として紹介する。",
            "続ける力は意志力より設計力。小さく始められる環境づくりが強い。",
            "最初は習慣化のテクニック本だと思っていた。",
            "今は組織や仕事の運用設計に転用できる本だと見ている。",
            101,
            datetime.now().isoformat(),
        ),
        (
            2,
            "THE 7 HABITS",
            "主体性と原則中心の考え方",
            "https://covers.openlibrary.org/b/isbn/9780743269513-M.jpg",
            "https://www.amazon.co.jp/",
            "読書中",
            jdump(["2026-06-12"]),
            jdump(["価値観", "主体性", "目標設定", "人間関係", "働き方"]),
            "原則中心の考え方を、対人関係と意思決定にどう活かすか整理する",
            "主体性の話は知っていたが、実際の対人場面に落とし込むとまだ浅い。",
            "『主体性』『Win-Win』『重要事項を優先』が広く取り上げられる。",
            "成果より前に、自分の反応の選び方を見直す大切さを伝えたい。",
            jdump([
                "知っていることと、実際に使えていることは違う",
                "目先の効率より、原則に基づく判断が長期的に効く",
            ]),
            "主体性は感情を抑えることではなく、反応を選び直す力として扱う。",
            "知っていることと使えていることの差が大きい本として共有する。",
            "知っている言葉ほど、生活の具体場面に落とさないと空回りする。",
            "有名な概念を学ぶ本という印象。",
            "対人関係の反応を選び直す実践書として読み直している。",
            102,
            datetime.now().isoformat(),
        ),
        (
            3,
            "LIFE SHIFT",
            "100年時代の人生戦略",
            "https://covers.openlibrary.org/b/isbn/9781509527496-M.jpg",
            "https://www.amazon.co.jp/",
            "読了",
            jdump(["2026-05-20"]),
            jdump(["キャリア", "働き方", "未来予測", "目標設定"]),
            "長期的なキャリア視点を持ち、今の選択を見直す材料を得る",
            "転職を単発で考えるのではなく、長い人生の設計として捉え直す必要を感じた。",
            "100年時代という前提から、学び直しや複数ステージの人生設計がよく議論される。",
            "今の不安を解消するには、短期最適より長期視点の設計が必要だと伝えたい。",
            jdump([
                "長寿化でキャリア設計の前提が変わる",
                "目先の転職ではなく人生全体の設計が必要",
            ]),
            "目先の条件改善だけではなく、人生全体の持続可能性を考える必要がある。",
            "転職や将来不安の話を、長期視点に広げる起点として使う。",
            "キャリアは次の会社選びだけでなく、長い人生でどう学び、どう働くかの設計そのもの。",
            "未来予測の本という印象だった。",
            "人生設計と働き方の前提を問い直す本だと感じている。",
            103,
            datetime.now().isoformat(),
        ),
    ]
    conn.executemany(
        "INSERT OR IGNORE INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        books,
    )

    existing_session_count = conn.execute("SELECT COUNT(*) FROM sessions").fetchone()[0]
    if existing_session_count == 0:
        sessions = [
            (
                1,
                "初回感想",
                jdump(["音声", "壁打ち"]),
                "習慣は気合ではなく環境設計という話が特に刺さった。",
                "根性論ではなく仕組みの話として紹介できそう。",
                "仕事の継続課題にも当てはまりそう。",
                "続く仕組みを作ることを伝えたい。",
                "継続の仕組みを作る発想として、仕事にも転用しやすいと整理。",
                "2026-06-10T10:30:00",
            ),
            (
                1,
                "読書会前",
                jdump(["追記"]),
                "他人に伝えるなら、才能より再現性のある仕組みの話として紹介したい。",
                "反論が来たら、才能ではなく環境の話として返せそう。",
                "自分の朝の習慣にも落とし込める。",
                "誰でも改善できる構造というメッセージにしたい。",
                "共有メッセージは『誰でも改善できる構造』に寄せると伝わりやすい。",
                "2026-06-13T09:00:00",
            ),
            (
                2,
                "読書中メモ",
                jdump(["音声"]),
                "理解したつもりの概念を、実際の職場の場面でまだ使いきれていない。",
                "抽象概念で終わらせず、対人場面での具体例に変える必要がある。",
                "会議や人間関係での反応の選び方に関係する。",
                "知っていることと使えることの差を伝えたい。",
                "概念理解から行動転用へ移る段階で、具体シーンの想起が必要。",
                "2026-06-14T08:00:00",
            ),
        ]
        conn.executemany(
            "INSERT INTO sessions (book_id, title, tags, impression_note, counter_note, personal_note, share_note, ai_response, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            sessions,
        )

    conn.commit()


def book_from_row(row: sqlite3.Row) -> Dict:
    return {
        "id": row["id"],
        "title": row["title"],
        "subtitle": row["subtitle"],
        "thumbnail": row["thumbnail"],
        "amazon_url": row["amazon_url"],
        "status": row["status"],
        "read_dates": jload(row["read_dates"], []),
        "themes": jload(row["themes"], []),
        "goal": row["goal"] or "",
        "core_impression": row["core_impression"] or "",
        "social_discussion": row["social_discussion"] or "",
        "share_message": row["share_message"] or "",
        "message_candidates": jload(row["message_candidates"], []),
        "latest_outputs": {
            "private_memo": row["latest_private"] or "",
            "reading_group": row["latest_reading_group"] or "",
            "sns": row["latest_sns"] or "",
        },
        "change_log": {
            "before": row["change_before"] or "",
            "after": row["change_after"] or "",
        },
        "author": {
            "id": row["author_id"],
            "name": row["author_name"],
            "photo": row["photo"],
            "short_title": row["short_title"],
            "industry_position": row["industry_position"],
            "authority_summary": row["authority_summary"],
            "career": row["career"],
            "achievements": row["achievements"],
            "episodes": row["episodes"],
        },
    }


@st.cache_data(ttl=3)
def list_books() -> List[Dict]:
    conn = get_conn()
    rows = conn.execute(
        """
        SELECT b.*, a.name AS author_name, a.photo, a.short_title, a.industry_position,
               a.authority_summary, a.career, a.achievements, a.episodes
        FROM books b
        JOIN authors a ON b.author_id = a.id
        ORDER BY b.id DESC
        """
    ).fetchall()
    conn.close()
    return [book_from_row(row) for row in rows]


@st.cache_data(ttl=3)
def get_book(book_id: int) -> Dict:
    conn = get_conn()
    row = conn.execute(
        """
        SELECT b.*, a.name AS author_name, a.photo, a.short_title, a.industry_position,
               a.authority_summary, a.career, a.achievements, a.episodes
        FROM books b
        JOIN authors a ON b.author_id = a.id
        WHERE b.id = ?
        """,
        (book_id,),
    ).fetchone()
    conn.close()
    if row is None:
        raise ValueError(f"book_id={book_id} の本が見つかりません")
    return book_from_row(row)


@st.cache_data(ttl=3)
def list_sessions(book_id: int) -> List[Dict]:
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM sessions WHERE book_id = ? ORDER BY datetime(created_at) DESC, id DESC",
        (book_id,),
    ).fetchall()
    conn.close()
    return [
        {
            "id": row["id"],
            "title": row["title"],
            "tags": jload(row["tags"], []),
            "impression_note": row["impression_note"] or "",
            "counter_note": row["counter_note"] or "",
            "personal_note": row["personal_note"] or "",
            "share_note": row["share_note"] or "",
            "ai_response": row["ai_response"] or "",
            "created_at": row["created_at"],
        }
        for row in rows
    ]


def clear_data_cache() -> None:
    list_books.clear()
    get_book.clear()
    list_sessions.clear()


def save_book_fields(book_id: int, goal: str, core_impression: str, share_message: str) -> None:
    conn = get_conn()
    conn.execute(
        "UPDATE books SET goal = ?, core_impression = ?, share_message = ? WHERE id = ?",
        (goal, core_impression, share_message, book_id),
    )
    conn.commit()
    conn.close()
    clear_data_cache()


def save_session(
    book_id: int,
    title: str,
    impression_note: str,
    counter_note: str,
    personal_note: str,
    share_note: str,
    ai_response: str,
) -> None:
    conn = get_conn()
    conn.execute(
        """
        INSERT INTO sessions (book_id, title, tags, impression_note, counter_note, personal_note, share_note, ai_response, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            book_id,
            title,
            jdump(["深める", "保存"]),
            impression_note,
            counter_note,
            personal_note,
            share_note,
            ai_response,
            datetime.now().isoformat(),
        ),
    )
    conn.commit()
    conn.close()
    clear_data_cache()


def find_or_create_author(author_name: str) -> int:
    conn = get_conn()
    row = conn.execute(
        "SELECT id FROM authors WHERE lower(name) = lower(?)",
        (author_name.strip(),),
    ).fetchone()
    if row:
        conn.close()
        return row["id"]

    next_id = conn.execute("SELECT COALESCE(MAX(id), 100) + 1 FROM authors").fetchone()[0]
    conn.execute(
        "INSERT INTO authors VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (
            next_id,
            author_name.strip(),
            "👤",
            "著者情報未登録",
            "未設定",
            "著者プロフィールは未整理です。",
            "未設定",
            "未設定",
            "未設定",
        ),
    )
    conn.commit()
    conn.close()
    clear_data_cache()
    return next_id


def add_book(
    title: str,
    subtitle: str,
    author_name: str,
    thumbnail: str,
    status: str,
    themes: List[str],
    share_message: str,
    amazon_url: str = "",
) -> int:
    author_id = find_or_create_author(author_name)
    conn = get_conn()
    next_id = conn.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM books").fetchone()[0]
    conn.execute(
        """
        INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            next_id,
            title,
            subtitle,
            thumbnail or "https://placehold.co/300x420?text=NO+COVER",
            amazon_url,
            status,
            jdump([str(date.today())]),
            jdump(themes),
            "",
            "",
            "",
            share_message,
            jdump([share_message] if share_message else []),
            "",
            "",
            "",
            "",
            "",
            author_id,
            datetime.now().isoformat(),
        ),
    )
    conn.commit()
    conn.close()
    clear_data_cache()
    return next_id


@st.cache_data(ttl=10)
def list_authors() -> List[Dict]:
    conn = get_conn()
    rows = conn.execute("SELECT * FROM authors ORDER BY name").fetchall()
    conn.close()
    return [dict(row) for row in rows]


@st.cache_data(ttl=10)
def grouped_books_by_theme() -> Dict[str, List[Dict]]:
    grouped: Dict[str, List[Dict]] = {}
    for book in list_books():
        for theme in book.get("themes", []):
            grouped.setdefault(theme, []).append(book)
    return dict(sorted(grouped.items(), key=lambda x: x[0]))


def ai_reflect(book: Dict, impression: str, counter: str, personal: str, share_note: str) -> str:
    prompt = f"""
あなたは読書内省を深めるコーチです。
以下の内容をもとに、
1. 読者の理解を深める要約
2. 追加で考えるべき問いを3つ
3. 読書会で人に伝えるならどこを切り出すか
を日本語で簡潔に出力してください。

本: {book['title']}
テーマ: {', '.join(book.get('themes', []))}
本の目的: {book['goal']}
印象に残ったこと: {impression}
違和感・反論: {counter}
自分に引きつける: {personal}
人に伝えたいメッセージ: {share_note}
""".strip()

    api_key = os.getenv("OPENAI_API_KEY")
    if OpenAI is None or not api_key:
        return (
            "【AI要約（フォールバック）】\n"
            "- あなたはこの本を『自分の行動や判断にどう転用するか』の観点で捉えています。\n"
            "- 違和感も残しているので、単なる要約ではなく自分の解釈に進めています。\n\n"
            "【追加で考える問い】\n"
            "1. その考え方を、次の1週間でどの場面に試せますか？\n"
            "2. その主張に反対する人は、何を根拠にしそうですか？\n"
            "3. 読書会で1つだけ問いを渡すなら何にしますか？\n\n"
            "【読書会で切り出すなら】\n"
            "- 自分の体験とつなげて話せるポイント\n"
            "- 相手が行動や価値観を見直せるポイント"
        )

    try:
        client = OpenAI(api_key=api_key)
        response = client.responses.create(model="gpt-4.1-mini", input=prompt)
        text = getattr(response, "output_text", "").strip()
        return text or "AIからの応答を取得できませんでした。"
    except Exception as e:
        return f"AI呼び出しに失敗しました: {e}"


def ensure_state() -> None:
    if "nav_page" not in st.session_state:
        st.session_state.nav_page = "ホーム"
    if "selected_book_id" not in st.session_state:
        st.session_state.selected_book_id = 1
    if "selected_guest_id" not in st.session_state:
        st.session_state.selected_guest_id = 201
    if "detail_return_page" not in st.session_state:
        st.session_state.detail_return_page = "ライブラリ"


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


def render_avatar(photo: Optional[str], size: int = 72) -> None:
    if not photo or photo == "👤":
        st.markdown(
            f"<div style='font-size:{size}px; text-align:center;'>👤</div>",
            unsafe_allow_html=True,
        )
    else:
        st.image(photo, use_container_width=True)


def open_book_detail(book_id: int, return_page: str) -> None:
    st.session_state.selected_book_id = book_id
    st.session_state.detail_return_page = return_page
    st.session_state.nav_page = "本詳細"
    st.rerun()


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
    sidebar_menu_button("ホーム", "ホーム", "🏠")
    sidebar_menu_button("本を深める", "本を深める", "🧠")
    sidebar_menu_button("伝え方を考える", "伝え方を考える", "🧭")
    sidebar_menu_button("ライブラリ", "ライブラリ", "🗂️")
    st.sidebar.divider()

    if st.session_state.nav_page == "本詳細":
        book = get_book(st.session_state.selected_book_id)
        st.sidebar.caption("表示中の本")
        st.sidebar.write(f"**{book['title']}**")
        st.sidebar.caption(book["author"]["name"])
        if st.sidebar.button("← 元の画面に戻る", use_container_width=True):
            st.session_state.nav_page = st.session_state.detail_return_page
            st.rerun()

    st.sidebar.divider()
    st.sidebar.caption("DB保存先")
    st.sidebar.code(str(DB_PATH), language="text")


def render_home() -> None:
    st.title("ホーム")
    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.subheader("本を深める")
            st.write("入力・保存・AI壁打ちで、本の理解を深めます。")
            if st.button("本を深めるへ", use_container_width=True):
                st.session_state.nav_page = "本を深める"
                st.rerun()

    with c2:
        with st.container(border=True):
            st.subheader("伝え方を考える")
            st.write("相手やテーマから、どの本を使うか考えます。")
            if st.button("伝え方を考えるへ", use_container_width=True):
                st.session_state.nav_page = "伝え方を考える"
                st.rerun()

    with c3:
        with st.container(border=True):
            st.subheader("ライブラリ")
            st.write("本・著者・テーマを管理します。")
            if st.button("ライブラリへ", use_container_width=True):
                st.session_state.nav_page = "ライブラリ"
                st.rerun()


def render_deepen_book_page() -> None:
    st.title("本を深める")
    books = list_books()
    book_options = {f"{b['title']} / {b['author']['name']}": b["id"] for b in books}
    selected_label = st.selectbox("書籍選択", list(book_options.keys()))
    st.session_state.selected_book_id = book_options[selected_label]
    book = get_book(st.session_state.selected_book_id)

    form_key = f"draft_{book['id']}"
    if form_key not in st.session_state:
        st.session_state[form_key] = {
            "goal": book["goal"],
            "impression": book["core_impression"],
            "counter": "",
            "personal": "",
            "share": book["share_message"],
            "title": f"{date.today()} の内省",
            "ai_response": "",
        }
    draft = st.session_state[form_key]

    c1, c2, c3 = st.columns(3)
    c1.metric("保存済みセッション", len(list_sessions(book["id"])))
    c2.metric("テーマ数", len(book.get("themes", [])))
    c3.metric("状態", book["status"])

    left, center, right = st.columns([1.2, 1.3, 1])

    with left:
        with st.form(f"deepen_form_{book['id']}"):
            st.subheader("発散 / 入力")
            title = st.text_input("セッション名", value=draft["title"])
            goal = st.text_area("この本の目的", value=draft["goal"], height=80)
            impression = st.text_area("印象に残ったこと", value=draft["impression"], height=120)
            counter = st.text_area("違和感・反論", value=draft["counter"], height=100)
            personal = st.text_area("自分に引きつける", value=draft["personal"], height=100)
            share = st.text_area("人に伝えたいメッセージ", value=draft["share"], height=100)

            ai_btn = st.form_submit_button("AIで深める", use_container_width=True)
            save_btn = st.form_submit_button("保存する", use_container_width=True)

            st.session_state[form_key] = {
                "goal": goal,
                "impression": impression,
                "counter": counter,
                "personal": personal,
                "share": share,
                "title": title,
                "ai_response": draft.get("ai_response", ""),
            }

            if ai_btn:
                ai_text =def ai_reflect(book, impression, counter, personal, share_note):

    st.write("DEBUG")

    try:
        api_key = st.secrets["OPENAI_API_KEY"]
        st.success("APIキー取得成功")
    except Exception as e:
        st.error(f"APIキー取得失敗: {e}")
        return "APIキーが取得できません"

    ...
            if save_btn:
                save_book_fields(book["id"], goal, impression, share)
                save_session(
                    book["id"],
                    title,
                    impression,
                    counter,
                    personal,
                    share,
                    st.session_state[form_key].get("ai_response", ""),
                )
                st.success("保存しました。")
                st.rerun()

    with center:
        with st.container(border=True):
            st.subheader("AI壁打ち")
            ai_text = st.session_state[form_key].get("ai_response", "")
            if ai_text:
                st.write(ai_text)
            else:
                st.caption("「AIで深める」を押すと、要約・追加質問・読書会での切り出し方を表示します。")

    with right:
        with st.container(border=True):
            st.subheader("最近のセッション")
            sessions = list_sessions(book["id"])
            if not sessions:
                st.caption("まだ保存されたセッションはありません。")
            for session in sessions[:5]:
                st.markdown(f"**{session['title']}**")
                st.caption(session["created_at"][:16].replace("T", " "))
                preview = session["impression_note"][:80]
                if len(session["impression_note"]) > 80:
                    preview += "..."
                st.write(preview)
                st.divider()
            if st.button("本詳細を開く", use_container_width=True):
                open_book_detail(book["id"], "本を深める")


def score_book(book: Dict, guest: Dict) -> int:
    score = 0
    text = " ".join(book.get("themes", []) + book.get("message_candidates", []))
    for theme in guest.get("recommended_themes", []):
        if theme in text:
            score += 2
    return score


def render_message_design_page() -> None:
    st.title("伝え方を考える")
    guests = sample_guests()
    guest_map = {f"{g['name']} / {g['relationship']}": g for g in guests}
    selected = st.selectbox("ゲスト選択", list(guest_map.keys()))
    guest = guest_map[selected]

    left, center, right = st.columns([1, 1.3, 1])

    with left:
        with st.container(border=True):
            st.subheader("相手理解")
            st.write(f"**{guest['name']}**")
            st.caption(guest["relationship"])
            st.caption(guest["occupation"])
            st.write(guest["current_concerns"])
            st.write(guest["recent_conversation"])

    with center:
        with st.container(border=True):
            st.subheader("壁打ち")
            st.text_area(
                "今回伝えたいこと",
                placeholder="例: 長期視点の必要性に気づいてほしい",
                height=100,
            )
            st.write(f"おすすめテーマ: {' / '.join(guest['recommended_themes'])}")

    with right:
        with st.container(border=True):
            st.subheader("足りないピース")
            for item in guest["missing_pieces"]:
                st.write(f"- {item}")

    st.subheader("候補本")
    books = sorted(list_books(), key=lambda b: score_book(b, guest), reverse=True)[:3]
    cols = st.columns(3)
    for idx, book in enumerate(books):
        with cols[idx]:
            with st.container(border=True):
                st.image(book["thumbnail"], use_container_width=True)
                st.markdown(f"**{book['title']}**")
                st.caption(book["author"]["name"])
                st.write(" ".join([f"`#{t}`" for t in book.get("themes", [])]))
                if st.button("本詳細へ", key=f"plan_{book['id']}", use_container_width=True):
                    open_book_detail(book["id"], "伝え方を考える")


def add_book_form() -> None:
    with st.expander("＋ 本を追加", expanded=False):
        with st.form("add_book_form"):
            title = st.text_input("書名")
            subtitle = st.text_input("サブタイトル")
            author_name = st.text_input("著者名")
            amazon_url = st.text_input("Amazon URL")
            thumbnail = st.text_input("表紙画像URL", placeholder="未入力ならプレースホルダ")
            status = st.selectbox("読書ステータス", ["読書中", "読了", "未着手"])
            themes = st.text_input("テーマ", placeholder="例: 習慣, 継続, 働き方")
            share_message = st.text_area("人に伝えたいメッセージ")
            submitted = st.form_submit_button("追加する", use_container_width=True)

            if submitted and title and author_name:
                new_id = add_book(
                    title=title,
                    subtitle=subtitle,
                    author_name=author_name,
                    thumbnail=thumbnail,
                    status=status,
                    themes=[t.strip() for t in themes.split(",") if t.strip()],
                    share_message=share_message,
                    amazon_url=amazon_url,
                )
                st.success("本を追加しました。")
                open_book_detail(new_id, "ライブラリ")


def render_library_page() -> None:
    st.title("ライブラリ")
    add_book_form()
    tab_books, tab_authors, tab_themes = st.tabs(["本", "著者", "テーマ"])

    with tab_books:
        search = st.text_input("本を検索", placeholder="タイトル・著者・テーマ")
        books = list_books()
        cols = st.columns(3)
        filtered = []

        for book in books:
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
                    st.write(" ".join([f"`#{t}`" for t in book.get("themes", [])]))
                    if st.button("本詳細へ", key=f"book_{book['id']}", use_container_width=True):
                        open_book_detail(book["id"], "ライブラリ")

    with tab_authors:
        cols = st.columns(2)
        for idx, author in enumerate(list_authors()):
            with cols[idx % 2]:
                with st.container(border=True):
                    left, right = st.columns([1, 3])
                    with left:
                        render_avatar(author.get("photo"), size=64)
                    with right:
                        st.markdown(f"**{author['name']}**")
                        st.caption(author["short_title"])
                        st.write(author["industry_position"])

    with tab_themes:
        grouped = grouped_books_by_theme()
        cols = st.columns(3)
        for idx, (theme, books_in_theme) in enumerate(grouped.items()):
            with cols[idx % 3]:
                with st.container(border=True):
                    st.markdown(f"**#{theme}**")
                    st.caption(f"関連本: {len(books_in_theme)}冊")
                    for book in books_in_theme[:3]:
                        if st.button(book["title"], key=f"theme_{theme}_{book['id']}", use_container_width=True):
                            open_book_detail(book["id"], "ライブラリ")


def render_book_detail_page() -> None:
    book = get_book(st.session_state.selected_book_id)
    sessions = list_sessions(book["id"])
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
        tab1, tab2, tab3, tab4 = st.tabs(["概要", "セッション履歴", "最新まとめ", "著者情報"])

        with tab1:
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

        with tab2:
            if not sessions:
                st.caption("セッションはまだありません。")
            for session in sessions:
                with st.container(border=True):
                    st.markdown(f"**{session['title']}**")
                    st.caption(session["created_at"][:16].replace("T", " "))
                    st.write("**印象に残ったこと**")
                    st.write(session["impression_note"] or "-")
                    st.write("**違和感・反論**")
                    st.write(session["counter_note"] or "-")
                    st.write("**自分に引きつける**")
                    st.write(session["personal_note"] or "-")
                    st.write("**人に伝えたいメッセージ**")
                    st.write(session["share_note"] or "-")
                    if session["ai_response"]:
                        st.info(session["ai_response"])

        with tab3:
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

        with tab4:
            author = book["author"]
            h1, h2 = st.columns([1, 3])
            with h1:
                render_avatar(author.get("photo"), size=96)
            with h2:
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


def main() -> None:
    init_db()
    ensure_state()
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
