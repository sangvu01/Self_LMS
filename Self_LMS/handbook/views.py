from django.http import Http404
from django.shortcuts import render

COURSES = [
    {
        "slug": "ai-fundamentals",
        "title": "AI Fundamentals",
        "description": "Khóa học nền tảng về trí tuệ nhân tạo, tập trung vào prompt, mô hình và ứng dụng trong doanh nghiệp.",
        "duration": "6 weeks",
        "level": "Beginner",
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

#serializers.py : class để validdate dữ liệu
def chapter_detail(req, course_slug, chapter_slug):
    course = get_course(course_slug)
    if course is None:
        raise Http404("Course not found")

    chapter = next((item for item in course["chapters"] if item["slug"] == chapter_slug), None)
    if chapter is None:
        raise Http404("Chapter not found")

    return render(req, 'chapter.html', {"course": course, "chapter": chapter})


# def c1(req):
#     return render(req, 'docs/chap1.html', {
#         "page": "c1"
#     })


# def c2(req):
#     return render(req, 'docs/chap2.html', {
#         "page": "c2"
#     })


# def c3(req):
#     return render(req, 'docs/chap3.html', {
#         "page": "c3"
#     })


# def c4(req):
#     return render(req, 'docs/chap4.html', {
#         "page": "c4"
#     })


# def c5(req):
#     return render(req, 'docs/chap5.html', {
#         "page": "c5"
#     })


# def c6(req):
#     return render(req, 'docs/chap6.html', {
#         "page": "c6"
#     })
