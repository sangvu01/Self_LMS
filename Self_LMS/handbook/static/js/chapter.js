function renderSidebar(chapters, courseSlug, current_chapter_slug, course_title){
    // href = "/courses/${courseSlug}/"
    let sidebar = ` <a href = "/courses/${courseSlug}/" class="text-decoration-none text-dark">
    <h5 class="fw-bold mb-4" >
           
              <i class="bi bi-journal-bookmark"></i>


                ${course_title}
            
            </h5></a>
            `
    chapters.forEach(chapter => {
        const active = (chapter.slug === current_chapter_slug ? "active" : "");
        sidebar += `
            <a href="/courses/${courseSlug}/${chapter.slug}/"
                class="list-group-item list-group-item-action ${active}">
                    ${chapter.title}
            </a>
        `
    });
    return sidebar;
}

function renderChapter(chapter,course_title,courseSlug){

    htmlcode = `
    <div class="mb-4">
        <a href="/courses/${courseSlug}/" class="btn btn-outline-secondary btn-sm mb-3">← Back to Course</a>
        <h2 class="fw-bold mb-2">${ chapter.title }</h2>
        <p class="text-muted mb-0">${ chapter.summary }</p>
    </div>

    <div class="card shadow-sm border-0">
        <div class="card-body">
            <div class="mb-4">
                <span class="badge bg-primary">${ course_title }</span>
            </div>
            <div class="content">
                ${ chapter.content }
            </div>
        </div>
    </div>
    `
    return htmlcode
}
index = () => {
    console.log("chapter.js/index() START");
    const courseSlug = $("#chapter-detail").data("course-slug");
    const chapterSlug = $("#chapter-detail").data("chapter-slug");
    
    const url = API.chapter
        .replace("COURSE_SLUG", courseSlug)
        .replace("CHAPTER_SLUG", chapterSlug);

    $.get(url, function(data){
        document.title = data.title
        console.log(data);
        const sidebarHTML = renderSidebar(data.chapters, courseSlug, data.current_chap, data.course_title);
        const contenthtml = renderChapter(data, data.course_title,courseSlug)

        $("#sidebar_small_width").html(`${sidebarHTML}`);
        $("#sidebar_big_width").html(`${sidebarHTML}`);
        $("#chapter-detail").html(contenthtml)
    });
    console.log("chapter.js/index() END");
}




index()
/*
    <div class="mb-4">
        <a href="{% url 'course_detail' course.slug %}" class="btn btn-outline-secondary btn-sm mb-3">← Back to Course</a>
        <h2 class="fw-bold mb-2">{{ chapter.title }}</h2>
        <p class="text-muted mb-0">{{ chapter.summary }}</p>
    </div>

    <div class="card shadow-sm border-0">
        <div class="card-body">
            <div class="mb-4">
                <span class="badge bg-primary">{{ course.title }}</span>
            </div>
            <div class="content">
                {{ chapter.content|safe }}
            </div>
        </div>
    </div>
*/
