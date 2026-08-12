function renderChapters(chapters, courseSlug) {
    let chapterHTML = "";
    chapters.forEach(chapter => {
        chapterHTML += `
            <a href="/courses/${courseSlug}/${chapter.slug}/" class="list-group-item list-group-item-action">
                <div class="d-flex justify-content-between align-items-start gap-3">
                    <div>
                        <div class="fw-semibold">${ chapter.title }</div>
                        <small class="text-muted">${ chapter.description }</small>
                    </div>
                    <i class="bi bi-chevron-right"></i>
                </div>
            </a>
        `
    });
    return chapterHTML;
}
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
    button = isMobile ? `<button
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
    let sidebar = `<a href = "/courses/${courseSlug}/" class="text-decoration-none text-dark"><h5 class="fw-bold mb-4">

              <i class="bi bi-journal-bookmark"></i>


                ${course_title}

            </h5>
            <a>
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

function renderCourse(data, chapterHTML){
    return `
        <div class="mb-4">
            <a href="/courses/" class="btn btn-outline-secondary btn-sm mb-3">← Back to Courses</a>
            <h2 class="fw-bold mb-2">${data.title}</h2>
            <p class="text-muted mb-0">${ data.description }</p>
        </div>

        <div class="card shadow-sm border-0">
            <div class="card-body">
                <div class="d-flex flex-wrap gap-2 mb-4">
                    <span class="badge bg-primary">${ data.level }</span>
                    <span class="badge bg-light text-dark">Duration: ${ data.duration }</span>
                </div>

                <div class="d-flex justify-content-between align-items-center mb-3">
                    <h5 class="fw-bold mb-0">Course Content</h5>
                    <span class="badge bg-secondary">${ data.chapters.length } chapters</span>
                </div>
                <div class="list-group">
                    ${chapterHTML}
                </div>
            </div>
        </div> 
    `
}
index = () => {
    console.log("courses_detail.js/index() START");
    const courseSlug = $("#course-detail").data("course-slug");
    const url = API.course.replace("COURSE_SLUG", courseSlug)
    console.log(courseSlug);
    $.get(url, (data) => {
        document.title = data.title;
        console.log(data)
        const chapterHTML = renderChapters(data.chapters, courseSlug); 
        const sidebar = renderSidebar(data.chapters, courseSlug, data.current_chapter, data.title, false);
        const sidebarHTML_mobile = renderSidebar(data.chapters, courseSlug, data.current_chapter, data.title, true);
        const courseHTML = renderCourse(data, chapterHTML);
        $("#sidebar_small_width").html(`${sidebarHTML_mobile}`);
        $("#sidebar_big_width").html(`${sidebar}`);
        // $("#course-detail").html(`${courseHTML}`);
        $("#course-detail").append(`
            <div class="mb-4">
                <a href="/courses/" class="btn btn-outline-secondary btn-sm mb-3">← My Courses</a>
                <h2 class="fw-bold mb-2">${data.title}</h2>
                <p class="text-muted mb-0">${ data.description }</p>
            </div>

            <div class="card shadow-sm border-0 mb-4 border-primary-subtle">
                <div class="card-body">
                    <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3">
                        <div>
                            <h5 class="fw-bold mb-1">📝 Quiz check</h5>
                            <p class="text-muted mb-0">Test your understanding of this course with a short randomized quiz.</p>
                        </div>
                        <a href="/course/${courseSlug}/start/" class="btn btn-primary">Start quiz</a>
                    </div>
                </div>
            </div>

            <div class="card shadow-sm border-0 mb-4">
                <div class="card-body">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h5 class="fw-bold mb-0">Recent attempts</h5>
                        <span class="badge bg-primary">Latest 3</span>
                    </div>
                    ${(data.recent_attempts || []).slice(0, 3).length ? (data.recent_attempts || []).slice(0, 3).map(attempt => `
                        <div class="d-flex justify-content-between align-items-center border rounded-2 px-3 py-2 mb-2">
                            <div>
                                <div class="fw-semibold">${attempt.user}</div>
                                <small class="text-muted">${attempt.created_at}</small>
                            </div>
                            <div class="text-end">
                                <div class="fw-bold">${attempt.score}%</div>
                                <small class="text-muted">${attempt.correct_answers ?? 0}/${attempt.total_questions}</small>
                            </div>
                        </div>
                    `).join("") : `<div class="text-muted">No quiz attempts yet for this course.</div>`}
                </div>
            </div>

            <div class="card shadow-sm border-0">
                <div class="card-body">
                    <div class="d-flex flex-wrap gap-2 mb-4">
                        <span class="badge bg-primary">${ data.level }</span>
                        <span class="badge bg-light text-dark">Duration: ${ data.duration }</span>
                    </div>

                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h5 class="fw-bold mb-0">Course Content</h5>
                        <span class="badge bg-secondary">${ data.chapters.length } chapters</span>
                    </div>
                    <div class="list-group">
                        ${chapterHTML}
                    </div>
                </div>
            </div> 
            `)
    })
    


    
    console.log("courses_detail.js/index() END");
}



index()
