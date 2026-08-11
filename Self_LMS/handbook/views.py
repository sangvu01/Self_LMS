import random

from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import ListView
from .models import Course, Chapter
from .serializers import CourseSerializer, ChapterSerializer, SideBarChapterSerializer, ChapterDetailSerializer
from rest_framework import status

from .models import Choice, Course, Question, Quiz, QuizAttempt, QuizAttemptAnswer
from .quiz_service import calculate_attempt_result
from .serializers import CourseSerializer, QuizSerializer


class CourseListAPIView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        data = []
        for course in courses:
            course_data = CourseSerializer(course).data
            quiz = Quiz.objects.filter(course=course, is_active=True).first()
            course_data["quiz_count"] = quiz.questions.count() if quiz else 0
            data.append(course_data)
        return Response(data)

    def post(self, req):
        s = CourseSerializer(data=req.data)
        if (s.is_valid()):
            # newcourse = Course(s)
            s.save()

            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailAPIView(APIView):
    def get(self, req, course_slug):
        c = get_object_or_404(Course, slug=course_slug)
        # s = CourseSerializer(c)
        
        # return Response(s.data)
        s = CourseSerializer(c)
        data = s.data
        quiz = Quiz.objects.filter(course=c, is_active=True).first()
        recent_attempts = []
        if quiz:
            attempts = (
                QuizAttempt.objects.filter(quiz=quiz)
                .select_related("user")
                .order_by("-created_at")[:3]
            )
            recent_attempts = []
            for attempt in attempts:
                recent_attempts.append({
                    "id": attempt.id,
                    "score": attempt.score,
                    "total_questions": attempt.total_questions,
                    "created_at": attempt.created_at.strftime("%Y-%m-%d %H:%M"),
                    "user": attempt.user.username if attempt.user else "Anonymous",
                    "correct_answers": attempt.answers.filter(is_correct=True).count(),
                })
        data["quiz_count"] = quiz.questions.count() if quiz else 0
        data["recent_attempts"] = recent_attempts
        return Response(data)

class ChapterAPIView(APIView):
    def get(self, req, course_slug, chapter_slug):
        chapter = get_object_or_404(
            Chapter, 
            course__slug = course_slug,
            slug = chapter_slug
        )
        s = ChapterDetailSerializer(chapter)
        return Response(s.data)
class QuizListAPIView(APIView):
    def get(self, request):
        quizzes = Quiz.objects.filter(is_active=True).select_related("course")
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)


class QuizDetailAPIView(APIView):
    def get(self, request, quiz_id):
        quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)

"""
{"id" : 5}
"""
"""
from django.views.generic import ListView
from .models import Course


class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"

    def get_queryset(self):
        return Course.objects.all()
        """
    
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
                "id": 1,
                "slug": "intro-ai",
                "title": "Chapter 1: Giới thiệu AI",
                "description": "Hiểu khái niệm AI và cách nó được ứng dụng trong đời sống.",
                "summary": "AI là công nghệ giúp máy tính mô phỏng một số năng lực trí tuệ của con người.",
                "content": "<h5>1. AI là gì?</h5><p>AI là quá trình cho phép máy tính phân loại, dự đoán và đưa ra quyết định dựa trên dữ liệu.</p><h5>2. Ứng dụng phổ biến</h5><p>AI được dùng trong chatbot, gợi ý sản phẩm, nhận diện hình ảnh và tự động hóa quy trình.</p>"
            },
            {
                "id": 2,
                "slug": "prompt-engineering",
                "title": "Chapter 2: Prompt Engineering",
                "description": "Học cách viết prompt rõ ràng, ngắn gọn và hiệu quả.",
                "summary": "Prompt tốt giúp mô hình tạo ra câu trả lời đúng và hữu ích hơn.",
                "content": "<h5>1. Nguyên tắc viết prompt</h5><p>Đặt mục tiêu rõ ràng, cung cấp ngữ cảnh và yêu cầu đầu ra cụ thể.</p><h5>2. Ví dụ</h5><p>Thay vì hỏi 'Giải thích AI', hãy hỏi 'Giải thích AI cho sinh viên mới bắt đầu bằng 3 điểm chính'.</p>"
            },
            {
                "id": 3,
                "slug": "language-models",
                "title": "Chapter 3: Mô hình ngôn ngữ",
                "description": "Tìm hiểu cách các mô hình ngôn ngữ hoạt động và được huấn luyện.",
                "summary": "Mô hình ngôn ngữ học các mẫu từ dữ liệu để dự đoán và tạo văn bản.",
                "content": "<h5>1. Cấu trúc mô hình</h5><p>Chúng ta dùng các lớp mạng thần kinh để học các mẫu ngôn ngữ.</p><h5>2. Mục đích</h5><p>Đây là nền tảng cho chatbot, tóm tắt tài liệu và hỗ trợ nội dung.</p>"
            },
            {
                "id": 4,
                "slug": "evaluate-ai",
                "title": "Chapter 4: Đánh giá kết quả AI",
                "description": "Biết cách kiểm tra chất lượng câu trả lời và tối ưu đầu ra.",
                "summary": "Đánh giá giúp chọn ra kết quả phù hợp và đáng tin cậy hơn.",
                "content": "<h5>1. Tiêu chí đánh giá</h5><p>Độ chính xác, tính hữu ích, tính rõ ràng và sự phù hợp với nhu cầu.</p><h5>2. Mẹo</h5><p>Luôn thử nhiều prompt và so sánh kết quả trước khi dùng cho mục tiêu thực tế.</p>"
            },
            {
                "id": 5,
                "slug": "responsible-ai",
                "title": "Chapter 5: AI có trách nhiệm",
                "description": "Nắm được rủi ro, bias và nguyên tắc dùng AI đúng cách.",
                "summary": "AI chỉ hiệu quả khi được sử dụng có trách nhiệm và kiểm soát được rủi ro.",
                "content": "<h5>1. Rủi ro</h5><p>Thông tin sai lệch, thiên vị dữ liệu và dữ liệu nhạy cảm cần được kiểm soát.</p><h5>2. Nguyên tắc</h5><p>Luôn kiểm tra nguồn và bảo vệ quyền riêng tư khi dùng dữ liệu.</p>"
            },
            {
                "id": 6,
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
                "id": 1,
                "slug": "setup-python",
                "title": "Chapter 1: Cài đặt môi trường",
                "description": "Chuẩn bị Python, VS Code và các thư viện cần thiết.",
                "summary": "Chuẩn bị môi trường là bước đầu tiên để lập trình Python hiệu quả.",
                "content": "<h5>1. Cài đặt Python</h5><p>Tải Python phiên bản phù hợp và kiểm tra bằng lệnh python --version.</p><h5>2. Công cụ hỗ trợ</h5><p>VS Code, Jupyter Notebook và pip giúp tăng năng suất lập trình.</p>"
            },
            {
                "id": 2,
                "slug": "variables-functions",
                "title": "Chapter 2: Biến, hàm và vòng lặp",
                "description": "Hiểu cấu trúc cơ bản của Python để viết script ngắn gọn.",
                "summary": "Biến, hàm và vòng lặp là nền tảng của mọi chương trình Python.",
                "content": "<h5>1. Biến</h5><p>Biến lưu dữ liệu và giúp chương trình linh hoạt hơn.</p><h5>2. Hàm và vòng lặp</h5><p>Hàm giúp tái sử dụng code, vòng lặp giúp xử lý dữ liệu lặp lại.</p>"
            },
            {
                "id": 3,
                "slug": "file-and-data",
                "title": "Chapter 3: Xử lý file và dữ liệu",
                "description": "Đọc ghi file, làm việc với JSON và CSV.",
                "summary": "Python rất mạnh trong việc xử lý dữ liệu cấu trúc từ nhiều định dạng khác nhau.",
                "content": "<h5>1. Đọc file</h5><p>Python có thể đọc file txt, json và csv một cách dễ dàng.</p><h5>2. Làm việc với dữ liệu</h5><p>Đây là bước quan trọng để chuẩn bị cho các mô hình AI.</p>"
            },
            {
                "id": 4,
                "slug": "data-visualization",
                "title": "Chapter 4: Thư viện phân tích dữ liệu",
                "description": "Sử dụng pandas và matplotlib để trực quan hóa dữ liệu.",
                "summary": "Pandas và matplotlib giúp phân tích và trình bày dữ liệu trực quan.",
                "content": "<h5>1. Pandas</h5><p>Pandas giúp thao tác bảng dữ liệu dễ dàng hơn.</p><h5>2. Matplotlib</h5><p>Matplotlib cho phép vẽ biểu đồ đơn giản và hiệu quả.</p>"
            },
            {
                "id": 5,
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
    return render(req, "courses.html")


def get_course(course_slug):
    return get_object_or_404(Course, slug=course_slug)


def get_or_create_course_quiz(course):
    quiz = Quiz.objects.filter(course=course, is_active=True).first()
    if quiz:
        return quiz

    quiz = Quiz.objects.create(
        course=course,
        title=f"{course.title} Quiz",
        description="Demo quiz for the course.",
        is_active=True,
    )

    sample_questions = [
        (
            "What does AI stand for?",
            [
                ("Artificial Intelligence", True),
                ("Automated Information", False),
                ("Advanced Internet", False),
            ],
        ),
        (
            "Machine learning is a subset of artificial intelligence.",
            [("True", True), ("False", False)],
        ),
        (
            "Which tool is commonly used for Python data science work?",
            [("Pandas", True), ("Photoshop", False), ("Figma", False)],
        ),
    ]

    for order, (question_text, choices) in enumerate(sample_questions, start=1):
        question = Question.objects.create(quiz=quiz, text=question_text, order=order)
        for choice_text, is_correct in choices:
            Choice.objects.create(question=question, text=choice_text, is_correct=is_correct)

    return quiz


def get_shuffled_question_ids(quiz, req, force_new=False):
    key = f"quiz_order_{quiz.id}"
    questions = list(quiz.questions.all())
    all_ids = [question.id for question in questions]

    if not all_ids:
        req.session.pop(key, None)
        req.session.modified = True
        return []

    if force_new or key not in req.session:
        shuffled = all_ids[:]
        random.shuffle(shuffled)
        req.session[key] = shuffled
        req.session.modified = True

    return req.session[key]


def course_detail(req, course_slug):
    course = get_course(course_slug)
    return render(req, 'course_detail.html', {"course": course, "course_slug": course_slug})


def chapter_detail(req, course_slug, chapter_slug):
    # course = get_course(course_slug)
    # chapter = get_object_or_404(course.chapters, slug=chapter_slug)
    return render(req, "chapter.html", {
        "course_slug": course_slug,
        "chapter_slug": chapter_slug
    })
    # course = get_course(course_slug)
    # if course is None:
    #     raise Http404("Course not found")

    # chapter = next((item for item in course["chapters"] if item["slug"] == chapter_slug), None)
    # if chapter is None:
    #     raise Http404("Chapter not found")

    # return render(req, 'chapter.html', {"course": course, "chapter": chapter})


def quiz_id(req, course_slug, quiz_id):
    course = get_course(course_slug)
    quiz = get_or_create_course_quiz(course)
    question_number = int(quiz_id)

    if req.session.get(f"quiz_finished_{course.slug}"):
        return redirect("quiz_result", course_slug=course.slug)

    order = get_shuffled_question_ids(quiz, req, force_new=False)
    if not order:
        return redirect("start_quiz", course_slug=course.slug)

    if question_number < 1 or question_number > len(order):
        raise Http404("Quiz not found")

    question_id = order[question_number - 1]
    question = get_object_or_404(quiz.questions, id=question_id)

    if req.GET.get("retake") == "1":
        req.session.pop("quiz_answers", None)
        req.session.pop(f"quiz_finished_{course.slug}", None)
        req.session.pop(f"quiz_order_{quiz.id}", None)
        get_shuffled_question_ids(quiz, req, force_new=True)
        req.session.modified = True
        req.session.save()
        order = get_shuffled_question_ids(quiz, req, force_new=False)
        question_id = order[question_number - 1]
        question = get_object_or_404(quiz.questions, id=question_id)

    if "quiz_answers" not in req.session:
        req.session["quiz_answers"] = {}

    previous_answer = None
    if str(question.id) in req.session["quiz_answers"]:
        previous_answer = req.session["quiz_answers"][str(question.id)]

    answered_ids = []
    for pos, question_key in enumerate(order, start=1):
        if str(question_key) in req.session.get("quiz_answers", {}):
            answered_ids.append(pos)

    if req.method == "POST":
        selected_choice_id = req.POST.get("selected_answer")
        action = req.POST.get("action")
        goto = req.POST.get("goto")

        if selected_choice_id:
            req.session["quiz_answers"][str(question.id)] = int(selected_choice_id)
            req.session.modified = True

        if action == "save":
            return JsonResponse({"status": "ok"})

        if action == "submit":
            return redirect("quiz_result", course_slug=course.slug)

        if goto:
            return redirect("quiz_detail", course_slug=course.slug, quiz_id=int(goto))

        total_quizzes = len(order)
        if question_number < total_quizzes:
            return redirect("quiz_detail", course_slug=course.slug, quiz_id=question_number + 1)
        return redirect("quiz_result", course_slug=course.slug)

    response = render(req, 'quizs/quiz.html', {
        "course": course,
        "quiz": quiz,
        "question": question,
        "quiz_id": question_number,
        "total_questions": len(order),
        "question_numbers": list(range(1, len(order) + 1)),
        "previous_answer": previous_answer,
        "answered_ids": answered_ids,
    })
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response


def quiz_result(req, course_slug):
    course = get_course(course_slug)
    quiz = get_or_create_course_quiz(course)

    if not quiz.questions.exists():
        return redirect("start_quiz", course_slug=course.slug)

    answers = req.session.get("quiz_answers", {})
    questions = list(quiz.questions.prefetch_related("choices").all())
    selected_answers = {int(question_id): int(choice_id) for question_id, choice_id in answers.items() if isinstance(choice_id, int)}
    result = calculate_attempt_result(questions, selected_answers)

    attempt = QuizAttempt.objects.create(
        quiz=quiz,
        user=req.user if getattr(req, "user", None) and req.user.is_authenticated else None,
        score=result["score"],
        total_questions=result["total"],
    )

    for item in result["review"]:
        selected_choice = Choice.objects.filter(id=item["selected_choice_id"]).first() if item["selected_choice_id"] else None
        QuizAttemptAnswer.objects.create(
            attempt=attempt,
            question=quiz.questions.get(id=item["question_id"]),
            selected_choice=selected_choice,
            is_correct=item["is_correct"],
        )

    req.session[f"quiz_finished_{course.slug}"] = True
    req.session.pop("quiz_answers", None)
    req.session.pop(f"quiz_order_{quiz.id}", None)
    req.session.modified = True

    response = render(req, 'quizs/result.html', {
        "course": course,
        "score": result["score"],
        "correct": result["correct"],
        "total": result["total"],
        "passed": result["passed"],
        "review": [
            {
                "question_id": item["question_id"],
                "question": item["question_text"],
                "selected": item["selected_choice_text"],
                "correct_answer": item["correct_choice_text"],
                "is_correct": item["is_correct"],
                "options": [choice.text for choice in quiz.questions.get(id=item["question_id"]).choices.all()],
            }
            for item in result["review"]
        ],
    })
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response


def retake_quiz(req, course_slug):
    course = get_course(course_slug)
    quiz = get_or_create_course_quiz(course)

    req.session.pop("quiz_answers", None)
    req.session.pop(f"quiz_finished_{course.slug}", None)
    req.session.pop(f"quiz_order_{quiz.id}", None)
    get_shuffled_question_ids(quiz, req, force_new=True)
    req.session.modified = True
    req.session.save()
    return redirect("start_quiz", course_slug=course.slug)


def start_quiz(req, course_slug):
    course = get_course(course_slug)
    quiz = get_or_create_course_quiz(course)
    total_questions = quiz.questions.count() if quiz else 0

    if quiz:
        req.session.pop("quiz_answers", None)
        req.session.pop(f"quiz_finished_{course.slug}", None)
        req.session.pop(f"quiz_order_{quiz.id}", None)
        get_shuffled_question_ids(quiz, req, force_new=True)
        req.session.modified = True

    return render(req, 'quizs/start_quiz.html', {
        "course": course,
        "quiz": quiz,
        "total_questions": total_questions,
        "duration": 5,
        "max_score": total_questions * 10,
        "has_quiz": total_questions > 0,
    })