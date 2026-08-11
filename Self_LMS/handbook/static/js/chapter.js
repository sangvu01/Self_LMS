function renderSidebar(
    chapters,
    courseSlug,
    current_chapter_slug,
    course_title,
    isMobile
) {

    let sidebar = "";

    // =========================
    // MOBILE
    // =========================
    if (isMobile) {

        sidebar += `
            <div class="offcanvas-header">

                <a href="/courses/${courseSlug}/"
                   class="text-decoration-none text-dark">

                    <h5 class="fw-bold mb-0">
                        <i class="bi bi-journal-bookmark"></i>
                        ${course_title}
                    </h5>

                </a>

                <button
                    class="btn-close"
                    data-bs-dismiss="offcanvas">
                </button>

            </div>

            <div class="offcanvas-body">

                <div class="list-group">
        `;

    }

    // =========================
    // DESKTOP
    // =========================
    else {

        sidebar += `
            <h5 class="fw-bold mb-4">
                <i class="bi bi-journal-bookmark"></i>
                ${course_title}
            </h5>

            <div class="list-group">
        `;

    }

    // =========================
    // CHAPTERS
    // =========================

    chapters.forEach(chapter => {

        const active =
            chapter.slug === current_chapter_slug
                ? "active"
                : "";

        sidebar += `
            <a href="/courses/${courseSlug}/${chapter.slug}/"
               class="list-group-item list-group-item-action ${active}">
                ${chapter.title}
            </a>
        `;
    });
    sidebar += `<a href="/course/${courseSlug}/start/" 
   class="list-group-item list-group-item-action">
    📝 Start Quiz
</a>`


    // =========================
    // CLOSE WRAPPER
    // =========================

    sidebar += `
            </div>
        `;

    if (isMobile) {
        sidebar += `
            </div>
        `;
    }

    return sidebar;
}
function renderSidebar1(chapters, courseSlug, current_chapter_slug, course_title, isMobile){
    let button = isMobile ? `<button
                class="btn-close"
                data-bs-dismiss="offcanvas">
            </button>` : ``
    let sidebar = `
        <div class="offcanvas-header">

            <a href="/courses/${courseSlug}/"
               class="text-decoration-none text-dark">

                <h5 class="fw-bold mb-0">
                    <i class="bi bi-journal-bookmark"></i>
                    ${course_title}
                </h5>

            </a>

            ${button}

        </div>


        <div class="offcanvas-body">

            <div class="list-group">
    `;


    chapters.forEach(chapter => {

        const active = (
            chapter.slug === current_chapter_slug
            ? "active"
            : ""
        );

        sidebar += `
                <a href="/courses/${courseSlug}/${chapter.slug}/"
                   class="list-group-item list-group-item-action ${active}">
                    ${chapter.title}
                </a>
        `;
    });


    sidebar += `
            </div>

        </div>
    `;


    return sidebar;
}
function renderSidebar_old(chapters, courseSlug, current_chapter_slug, course_title){
    // href = "/courses/${courseSlug}/"
    let sidebar = ` <a href = "/courses/${courseSlug}/" class="text-decoration-none text-dark">
    <h5 class="fw-bold mb-4" >
           
              <i class="bi bi-journal-bookmark"></i>


                ${course_title}
            
            </h5><button
            class="btn-close"
            data-bs-dismiss="offcanvas">
        </button></a>
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
// function renderChapter(chapter,course_title,courseSlug){

//     htmlcode = `
//     <div class="mb-4">
//         <a href="/courses/${courseSlug}/" class="btn btn-outline-secondary btn-sm mb-3">← Back to Course</a>
//         <h2 class="fw-bold mb-2">${ chapter.title }</h2>
//         <p class="text-muted mb-0">${ chapter.summary }</p>
//     </div>

//     <div class="card shadow-sm border-0">
//         <div class="card-body">
//             <div class="mb-4">
//                 <span class="badge bg-primary">${ course_title }</span>
//             </div>
//             <div class="content">
//                 ${ chapter.content }
//             </div>
//         </div>
//     </div>
//     `
//     return htmlcode
// }
function renderChapter(chapter, course_title, courseSlug){

    const prevBtn = chapter.prev_chap_slug
        ? `<a href="/courses/${courseSlug}/${chapter.prev_chap_slug}/"
              class="btn btn-outline-secondary">
                ← Previous
           </a>`
        : `<span></span>`;

    const nextBtn = chapter.next_chap_slug
        ? `<a href="/courses/${courseSlug}/${chapter.next_chap_slug}/"
              class="btn btn-primary">
                Next →
           </a>`
        : `<span></span>`;

    return `
    <div class="mb-4">
        <a href="/courses/${courseSlug}/"
           class="btn btn-outline-secondary btn-sm mb-3">
           ← Back to Course
        </a>

        <h2 class="fw-bold mb-2">${chapter.title}</h2>
        <p class="text-muted mb-0">${chapter.summary}</p>
    </div>

    <div class="card shadow-sm border-0">
        <div class="card-body">

            <div class="mb-4">
                <span class="badge bg-primary">${course_title}</span>
            </div>

            <div class="content">
                ${chapter.content}
            </div>

            <hr>

            <div class="d-flex justify-content-between mt-4">
                ${prevBtn}
                ${nextBtn}
            </div>

        </div>
    </div>
    `;
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
        const sidebarHTML = renderSidebar(data.chapters, courseSlug, data.current_chap, data.course_title, false);
        const sidebarHTML_mobile = renderSidebar(data.chapters, courseSlug, data.current_chap, data.course_title, true);
        const contenthtml = renderChapter(data, data.course_title,courseSlug)

        // $("#sidebar_small_width").html(`${sidebarHTML_mobile}`);
        // $("#sidebar_big_width").html(`${sidebarHTML}`);
        $("#sidebar_small_width").html(`${sidebarHTML_mobile}` + `<a href="/course/${courseSlug}/start/" 
   class="list-group-item list-group-item-action">
    📝 Start Quiz
</a>`);
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
