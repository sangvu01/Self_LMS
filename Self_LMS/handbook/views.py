from django.http import Http404
from django.shortcuts import render, redirect

COURSES = [
    {
        "slug": "ai-fundamentals",
        "title": "AI Fundamentals",
        "description": "Khóa học nền tảng về trí tuệ nhân tạo, tập trung vào prompt, mô hình và ứng dụng trong doanh nghiệp.",
        "duration": "6 weeks",
        "level": "Beginner",
        "quizs": [
    {
        "quizid": 1,
        "question": "What does AI stand for?",
        "options": [
            "Artificial Intelligence",
            "Automated Information",
            "Advanced Internet",
            "Applied Innovation"
        ],
        "answer": "Artificial Intelligence",
        "explanation": "AI stands for Artificial Intelligence. It refers to systems that can perform tasks that normally require human intelligence."
    },
    {
        "quizid": 2,
        "question": "Machine Learning is a subset of Artificial Intelligence.",
        "options": [
            "True",
            "False"
        ],
        "answer": "True",
        "explanation": "Yes, Machine Learning is a subset of AI that focuses on systems learning from data without being explicitly programmed."
    },
    {
        "quizid": 3,
        "question": "Which of the following is a popular Python library for Machine Learning?",
        "options": [
            "NumPy",
            "Pandas",
            "Scikit-learn",
            "All of the above"
        ],
        "answer": "All of the above",
        "explanation": "NumPy, Pandas, and Scikit-learn are all widely used libraries in Machine Learning with Python."
    },
    {
        "quizid": 4,
        "question": "What is the main purpose of Prompt Engineering?",
        "options": [
            "To design computer hardware",
            "To write clear and effective instructions for AI models",
            "To create mobile applications",
            "To manage databases"
        ],
        "answer": "To write clear and effective instructions for AI models",
        "explanation": "Prompt Engineering is the practice of crafting clear and effective prompts so that AI models can generate better and more accurate responses."
    },
    {
        "quizid": 5,
        "question": "Which of the following is an important principle of Responsible AI?",
        "options": [
            "Always use the fastest model",
            "Ignore data privacy",
            "Check for bias and protect user privacy",
            "Only use AI for entertainment"
        ],
        "answer": "Check for bias and protect user privacy",
        "explanation": "Responsible AI focuses on fairness, transparency, and protecting user privacy while reducing harmful bias in AI systems."
    }
],
        "chapters": [
            {
                "slug": "intro-ai",
                "title": "Chapter 1: Giới thiệu AI",
                "description": "Hiểu khái niệm AI và cách nó được ứng dụng trong đời sống.",
                "summary": "AI là công nghệ giúp máy tính mô phỏng một số năng lực trí tuệ của con người.",
                "content": "<h5>1. AI là gì?</h5><p>AI là quá trình cho phép máy tính phân loại, dự đoán và đưa ra quyết định dựa trên dữ liệu.</p><h5>2. Ứng dụng phổ biến</h5><p>AI được dùng trong chatbot, gợi ý sản phẩm, nhận diện hình ảnh và tự động hóa quy trình.</p>"
            },
            {
                "slug": "prompt-engineering",
                "title": "Chapter 2: Prompt Engineering",
                "description": "Học cách viết prompt rõ ràng, ngắn gọn và hiệu quả.",
                "summary": "Prompt tốt giúp mô hình tạo ra câu trả lời đúng và hữu ích hơn.",
                "content": "<h5>1. Nguyên tắc viết prompt</h5><p>Đặt mục tiêu rõ ràng, cung cấp ngữ cảnh và yêu cầu đầu ra cụ thể.</p><h5>2. Ví dụ</h5><p>Thay vì hỏi 'Giải thích AI', hãy hỏi 'Giải thích AI cho sinh viên mới bắt đầu bằng 3 điểm chính'.</p>"
            },
            {
                "slug": "language-models",
                "title": "Chapter 3: Mô hình ngôn ngữ",
                "description": "Tìm hiểu cách các mô hình ngôn ngữ hoạt động và được huấn luyện.",
                "summary": "Mô hình ngôn ngữ học các mẫu từ dữ liệu để dự đoán và tạo văn bản.",
                "content": "<h5>1. Cấu trúc mô hình</h5><p>Chúng ta dùng các lớp mạng thần kinh để học các mẫu ngôn ngữ.</p><h5>2. Mục đích</h5><p>Đây là nền tảng cho chatbot, tóm tắt tài liệu và hỗ trợ nội dung.</p>"
            },
            {
                "slug": "evaluate-ai",
                "title": "Chapter 4: Đánh giá kết quả AI",
                "description": "Biết cách kiểm tra chất lượng câu trả lời và tối ưu đầu ra.",
                "summary": "Đánh giá giúp chọn ra kết quả phù hợp và đáng tin cậy hơn.",
                "content": "<h5>1. Tiêu chí đánh giá</h5><p>Độ chính xác, tính hữu ích, tính rõ ràng và sự phù hợp với nhu cầu.</p><h5>2. Mẹo</h5><p>Luôn thử nhiều prompt và so sánh kết quả trước khi dùng cho mục tiêu thực tế.</p>"
            },
            {
                "slug": "responsible-ai",
                "title": "Chapter 5: AI có trách nhiệm",
                "description": "Nắm được rủi ro, bias và nguyên tắc dùng AI đúng cách.",
                "summary": "AI chỉ hiệu quả khi được sử dụng có trách nhiệm và kiểm soát được rủi ro.",
                "content": "<h5>1. Rủi ro</h5><p>Thông tin sai lệch, thiên vị dữ liệu và dữ liệu nhạy cảm cần được kiểm soát.</p><h5>2. Nguyên tắc</h5><p>Luôn kiểm tra nguồn và bảo vệ quyền riêng tư khi dùng dữ liệu.</p>"
            },
            {
                "slug": "real-world-usage",
                "title": "Chapter 6: Ứng dụng thực tế",
                "description": "Áp dụng AI vào công việc và quy trình sản xuất nội dung.",
                "summary": "AI trở nên giá trị khi được tích hợp vào các quy trình thật sự.",
                "content": "<h5>1. Ví dụ thực tế</h5><p>Viết email, tóm tắt tài liệu, dịch nội dung và hỗ trợ nghiên cứu.</p><h5>2. Lộ trình triển khai</h5><p>Đầu tiên thử nghiệm nhỏ, sau đó đo lường hiệu quả và mở rộng dần.</p>"
            },
        ],
    },
    {
        "slug": "python-for-ai",
        "title": "Python for AI",
        "description": "Khóa học Python dành cho người muốn xây dựng các quy trình AI và xử lý dữ liệu hiệu quả.",
        "duration": "5 weeks",
        "level": "Intermediate",
        "chapters": [
            {
                "slug": "setup-python",
                "title": "Chapter 1: Cài đặt môi trường",
                "description": "Chuẩn bị Python, VS Code và các thư viện cần thiết.",
                "summary": "Chuẩn bị môi trường là bước đầu tiên để lập trình Python hiệu quả.",
                "content": "<h5>1. Cài đặt Python</h5><p>Tải Python phiên bản phù hợp và kiểm tra bằng lệnh python --version.</p><h5>2. Công cụ hỗ trợ</h5><p>VS Code, Jupyter Notebook và pip giúp tăng năng suất lập trình.</p>"
            },
            {
                "slug": "variables-functions",
                "title": "Chapter 2: Biến, hàm và vòng lặp",
                "description": "Hiểu cấu trúc cơ bản của Python để viết script ngắn gọn.",
                "summary": "Biến, hàm và vòng lặp là nền tảng của mọi chương trình Python.",
                "content": "<h5>1. Biến</h5><p>Biến lưu dữ liệu và giúp chương trình linh hoạt hơn.</p><h5>2. Hàm và vòng lặp</h5><p>Hàm giúp tái sử dụng code, vòng lặp giúp xử lý dữ liệu lặp lại.</p>"
            },
            {
                "slug": "file-and-data",
                "title": "Chapter 3: Xử lý file và dữ liệu",
                "description": "Đọc ghi file, làm việc với JSON và CSV.",
                "summary": "Python rất mạnh trong việc xử lý dữ liệu cấu trúc từ nhiều định dạng khác nhau.",
                "content": "<h5>1. Đọc file</h5><p>Python có thể đọc file txt, json và csv một cách dễ dàng.</p><h5>2. Làm việc với dữ liệu</h5><p>Đây là bước quan trọng để chuẩn bị cho các mô hình AI.</p>"
            },
            {
                "slug": "data-visualization",
                "title": "Chapter 4: Thư viện phân tích dữ liệu",
                "description": "Sử dụng pandas và matplotlib để trực quan hóa dữ liệu.",
                "summary": "Pandas và matplotlib giúp phân tích và trình bày dữ liệu trực quan.",
                "content": "<h5>1. Pandas</h5><p>Pandas giúp thao tác bảng dữ liệu dễ dàng hơn.</p><h5>2. Matplotlib</h5><p>Matplotlib cho phép vẽ biểu đồ đơn giản và hiệu quả.</p>"
            },
            {
                "slug": "first-ai-script",
                "title": "Chapter 5: Tạo script AI đầu tiên",
                "description": "Kết nối Python với mô hình AI để tạo sản phẩm mẫu đầu tiên.",
                "summary": "Bạn sẽ tạo một script nhỏ để tương tác với mô hình AI bằng Python.",
                "content": "<h5>1. Gửi yêu cầu</h5><p>Python có thể gửi yêu cầu HTTP đến API AI và nhận kết quả trả về.</p><h5>2. Kết quả</h5><p>Đây là bước đầu để biến ý tưởng thành ứng dụng thực tế.</p>"
            },
        ],
    },
]


def home(req):
    # return render(req, 'quizs/quiz.html')
    return render(req, 'home.html')


def base(req):
    return render(req, 'base.html')


def courses(req):
    return render(req, 'courses.html', {"courses": COURSES})


def get_course(course_slug):
    return next((item for item in COURSES if item["slug"] == course_slug), None)


def course_detail(req, course_slug):
    course = get_course(course_slug)
    if course is None:
        raise Http404("Course not found")
    return render(req, 'course_detail.html', {"course": course})


def chapter_detail(req, course_slug, chapter_slug):
    course = get_course(course_slug)
    if course is None:
        raise Http404("Course not found")

    chapter = next((item for item in course["chapters"] if item["slug"] == chapter_slug), None)
    if chapter is None:
        raise Http404("Chapter not found")

    return render(req, 'chapter.html', {"course": course, "chapter": chapter})

def quiz_id(req, course_slug, quiz_id):
    course = get_course(course_slug)
    if course is None:
        raise Http404("Course not found")

    # Nếu đã nộp bài rồi → không cho vào lại câu hỏi
    if req.session.get(f"quiz_finished_{course_slug}"):
        return redirect("quiz_result", course_slug=course_slug)

    quiz = next(
        (item for item in course.get("quizs", []) if item["quizid"] == quiz_id),
        None
    )
    if quiz is None:
        raise Http404("Quiz not found")

    # Xử lý retake
    if req.GET.get("retake") == "1":
        req.session.pop("quiz_answers", None)
        req.session.pop(f"quiz_finished_{course_slug}", None)
        req.session.modified = True
        req.session.save()

    if "quiz_answers" not in req.session:
        req.session["quiz_answers"] = {}

    previous_answer = req.session["quiz_answers"].get(str(quiz_id), {}).get("selected")
    answered_ids = [int(qid) for qid in req.session.get("quiz_answers", {}).keys()]

    if req.method == "POST":
        selected = req.POST.get("selected_answer")
        action = req.POST.get("action")   # "next" hoặc "submit"
        goto = req.POST.get("goto")       # câu muốn nhảy đến từ navigator

        # Lưu đáp án hiện tại (nếu có chọn)
        if selected:
            is_correct = selected == quiz["answer"]
            req.session["quiz_answers"][str(quiz_id)] = {
                "selected": selected,
                "correct": is_correct
            }
            req.session.modified = True

        # 1. Bấm Submit Quiz → nộp bài ngay
        if action == "submit":
            return redirect("quiz_result", course_slug=course_slug)

        # 2. Bấm số câu hỏi ở Navigator → chuyển đến câu đó
        if goto:
            return redirect("quiz_detail", course_slug=course_slug, quiz_id=int(goto))

        # 3. Bấm Next → sang câu tiếp theo
        total_quizzes = len(course.get("quizs", []))
        if quiz_id < total_quizzes:
            return redirect("quiz_detail", course_slug=course_slug, quiz_id=quiz_id + 1)
        else:
            return redirect("quiz_result", course_slug=course_slug)

    response = render(req, 'quizs/quiz.html', {
        "course": course,
        "quiz": quiz,
        "previous_answer": previous_answer,
        "answered_ids": answered_ids,
    })

    # Chống cache
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response

def c1(req):
    return render(req, 'docs/chap1.html', {
        "page": "c1"
    })


def c2(req):
    return render(req, 'docs/chap2.html', {
        "page": "c2"
    })


def c3(req):
    return render(req, 'docs/chap3.html', {
        "page": "c3"
    })


def c4(req):
    return render(req, 'docs/chap4.html', {
        "page": "c4"
    })


def c5(req):
    return render(req, 'docs/chap5.html', {
        "page": "c5"
    })


def c6(req):
    return render(req, 'docs/chap6.html', {
        "page": "c6"
    })

def quiz_result(req, course_slug):
    course = get_course(course_slug)
    if course is None:
        raise Http404("Course not found")

    answers = req.session.get("quiz_answers", {})
    quizzes = course.get("quizs", [])
    total = len(quizzes)
    correct = sum(1 for a in answers.values() if a.get("correct") is True)

    score = round((correct / total) * 100) if total > 0 else 0
    passed = score > 50

    # Tạo review
    review = []
    for quiz in quizzes:
        qid = str(quiz["quizid"])
        user_data = answers.get(qid, {})
        selected = user_data.get("selected")
        is_correct = user_data.get("correct", False)

        review.append({
            "quizid": quiz["quizid"],
            "question": quiz["question"],
            "options": quiz["options"],
            "correct_answer": quiz["answer"],
            "selected": selected,
            "is_correct": is_correct,
            "explanation": quiz.get("explanation", ""),
        })

    # Đánh dấu đã hoàn thành quiz
    req.session[f"quiz_finished_{course_slug}"] = True

    # Xóa đáp án
    req.session.pop("quiz_answers", None)
    req.session.modified = True

    response = render(req, 'quizs/result.html', {
        "course": course,
        "score": score,
        "correct": correct,
        "total": total,
        "passed": passed,
        "review": review,
    })

    # Chống cache
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response


def retake_quiz(req, course_slug):
    # Xóa đáp án + cờ đã hoàn thành
    req.session.pop("quiz_answers", None)
    req.session.pop(f"quiz_finished_{course_slug}", None)
    req.session.modified = True
    req.session.save()

    return redirect(f"/course/{course_slug}/quiz/1/?retake=1")

def start_quiz(req, course_slug):
    course = get_course(course_slug)
    if course is None:
        raise Http404("Course not found")

    total_questions = len(course.get("quizs", []))
    
    return render(req, 'quizs/start_quiz.html', {
        "course": course,
        "total_questions": total_questions,
        "duration": 5,          # số phút
        "max_score": total_questions * 10,  # mỗi câu 10 điểm
    })