import json
from string import Template

# render_resume renders the resume as tex file
def render_resume():
    resume = json.load(open('resume.json'))
    src = render_opening()
    src += render_header(resume["name"], resume["sex"], resume["birth"]["date"], resume["nationality"])
    contact = resume["contact"]
    src += render_contacts(contact["email"], contact["phone"], contact["messaging"]["whatsapp"], 
                           contact["messaging"]["telegram"], contact["address"])
    src += render_sosial_links(resume["social_links"])
    src += render_education(resume["education"])
    src += render_summary(resume["summary"])
    src += render_qualification(resume["qualification"])
    src += render_career_objective(resume["career_objective"])
    src += render_personal_research(resume["personal_research"])
    src += render_experiences(resume["experience"])
    src += render_closing()
    print(src)
    target = open("temp-resume.tex", "wt")
    target.write(src)
    target.close()

def render_opening():
    return r"""
\documentclass[12pt]{res} 
\usepackage{helvet} 
\usepackage{multicol}
\usepackage{hyperref}
\usepackage{soul}
\usepackage{xcolor}

\setlength{\columnsep}{1.5em}
\newsectionwidth{0pt}
\hypersetup{
	colorlinks   = true, 
	urlcolor     = blue, 
	linkcolor    = green,
	citecolor   = blue 
}
\pagestyle{plain}
\begin{document}
"""

def render_closing():
    return r"""
\end{resume} 
\end{document}
"""

def render_header(name, sex, birth, nationality):
    sexStr = "He/Him"
    if sex != "male":
        sexStr = "She/Her" 
    str = r"""
\begin{center}
	{\large{\bf{\textsc{$name}}}}\\
	\vspace{16pt}
    \emph{$sexStr}\\
	\emph{Birth}: $dob\\
    \emph{Nationality}: $nationality
\end{center}

\begin{resume}
\vspace{-10pt}
"""
    strTpl = Template(str)
    return strTpl.substitute(name=name, sexStr=sexStr, dob=birth, nationality="Indonesian")

def render_bio():
    pass

def render_contacts(email, phone, wa, telegram, address):
    str = r"""
\begin{minipage}[t]{0.45\linewidth}
	\section{\centerline{contacts}}
	{\small 
		\emph{email} \hfill \href{mailto:$email}{$email}\\
		\emph{phone} \hfill $phone\\
		\emph{whatsapp} \hfill \href{$wa_url}{$wa_label}\\
		\emph{telegram} \hfill \href{$telegram_url}{$telegram_label}\\
		\emph{location} \hfill $address_city (UTC $address_utc), $address_country\\}
\end{minipage}%
\hfill"""
    strTpl = Template(str)
    return strTpl.substitute(email=email, phone=phone, wa_url=wa["url"], wa_label=wa["label"], 
                             telegram_url=telegram["url"], telegram_label=telegram["label"], 
                             address_city=address["city"], address_utc=address["utc_offset"], address_country=address["country"])

def render_sosial_links(social):
    str = r"""
\begin{minipage}[t]{0.45\linewidth}
	\section{\centerline{social links}}
	{\small \emph{resume} \hfill \href{$resume_url}{$resume_label}\\
		\emph{website} \hfill \href{$website_url}{$website_label}\\
		\emph{blog} \hfill \href{$blog_url}{$blog_label}\\
		\emph{linkedIn} \hfill \href{$linkedin_url}{$linkedin_label}\\
		\emph{twitter} \hfill \href{$twitter_url}{$twitter_label}\\
		\emph{github} \hfill \href{$github_url}{$github_label}\\}
\end{minipage}
"""
    resume = social["resume"]
    website = social["website"]
    blog = social["blog"]
    linkedin = social["linkedin"]
    twitter = social["twitter"]
    github = social["github"]
    strTpl = Template(str)
    return strTpl.substitute(resume_url=resume["url"], resume_label=resume["label"],
                             website_url=website["url"], website_label=website["label"],
                             blog_url=blog["url"], blog_label=blog["label"],
                             linkedin_url=linkedin["url"], linkedin_label=linkedin["label"],
                             twitter_url=twitter["url"], twitter_label=twitter["label"],
                             github_url=github["url"], github_label=github["label"])

def render_education(education):
    edu = education[0]
    str = r"""
\vspace{-20pt}
\begin{center}
	\rule{1.0\textwidth}{0.1pt}
\end{center}

\section{\centerline{education}}
\vspace{-10pt} % Gap between title and text
\begin{center}
	$level in \emph{$major} ($end)\\
    $institution\\
    Majoring in \emph{$subject}
\end{center}

"""
    level = edu["level"]
    major = edu["major"]
    subject = edu["subject"]
    end = edu["end"]
    institution = edu["institution"]
    strTpl = Template(str)
    return strTpl.substitute(level=level, major=major, subject=subject, end=end, institution=institution)

def render_summary(summary):
    str = r"""
\vspace{-30pt}
\begin{center}
	\rule{0.5\textwidth}{0.1pt}
\end{center}

\begin{quotation}
	{\large 
	\emph{$summary}};
\end{quotation}

\vspace{-25pt}
\begin{center}
	\rule{0.5\textwidth}{0.1pt}
\end{center}

"""
    strTpl = Template(str)
    return strTpl.substitute(summary=summary)

def render_qualification(qualification):
    str = r"""
\section{\centerline{QUALIFICATION}}
\vspace{10pt}
\begin{multicols}{2}
$paragraphs
\end{multicols}
"""
    paragraphs = ""
    for paragraph in qualification:
        paragraphs += paragraph + "\n\n"
    strTpl = Template(str)
    return strTpl.substitute(paragraphs=paragraphs)

def render_career_objective(objective):
    str = r"""
\begin{minipage}[t]{0.48\linewidth}
	\section{\centerline{CAREER OBJECTIVE}}
	\vspace{10pt}
    $objective
\end{minipage}%
\hfill"""
    strTpl = Template(str)
    return strTpl.substitute(objective=objective[0])

def render_personal_research(research):
    str = r"""
\begin{minipage}[t]{0.48\linewidth}
	\section{\centerline{PERSONAL RESEARCHES}}
	\vspace{10pt}
    $research
\end{minipage}

\rule{1.0\textwidth}{0.1pt}
"""
    strTpl = Template(str)
    return strTpl.substitute(research=research[0])

def render_experiences(experiences):
    str = r"""
\section{\centerline{PROFESSIONAL EXPERIENCE}} 
"""
    for exp in experiences:
        str += render_experience(exp)
    return str

def render_experience(exp):
    str = r"""
\begin{multicols}{2}
	{\large {\bf \href{$company_url}{$company}}} \\
	{\footnotesize{\sl $start--$end} \hfill ($duration)}\\
	{\footnotesize{\sl position} \hfill \bf{$position}}\\
	{\footnotesize{\sl reports to} \hfill $reports_to}\\
	{\footnotesize{\sl team} \hfill $teams}\\

	\columnbreak
	{\footnotesize{$company_description}}\\
\end{multicols}
\vspace{-20pt}

\begin{multicols}{2}
	\section{\leftline{Responsibilities}}
		\begin{itemize}
			$responsibilities
		\end{itemize}
	\section{\leftline{Accomplishments}}
		\begin{itemize}
			\setlength{\itemindent}{0pt}
			$accomplishments
		\end{itemize}
\end{multicols}

\vspace{-20pt}
\begin{minipage}[t]{0.55\linewidth}
	\rule{0.25\textwidth}{2pt}
	\begin{multicols}{2}
		\section{Technology Stack}
		\raggedleft{{\footnotesize{$techstack}}}
		\columnbreak
		\section{\rightline{Standards}}
		\raggedleft{{\footnotesize{$standards}}}
	\end{multicols}
	\vspace{1pt}
\end{minipage}
\hfill
\begin{minipage}[t]{0.42\linewidth}
	\vspace{18pt}
	\section{Achievement}
	\begin{flushleft}
        \begin{itemize}
		\footnotesize{$achievements}
        \end{itemize}
	\end{flushleft}
\end{minipage}

\vspace{10pt}
\rule{1.0\textwidth}{0.1pt}
"""
    company = exp["company"]
    company_url = exp["company_url"]
    start = to_month_year(exp["start"])
    end = "present" if exp["end"] == "" else to_month_year(exp["end"])
    duration = to_duration(start, end)
    position = ", ".join(exp["positions"])
    reports_to = exp["report_to"]
    teams = ", ".join(exp["team"])
    company_description = exp["company_description"]
    responsibilities = "\n\n".join(["\item " + r for r in exp["responsibilities"]])
    accomplishments = "\n\n".join(["\item " + r for r in exp["accomplishments"]])
    techstack = ", ".join(exp["technologies"])
    standards = "(none)" if len(exp["standards"]) == 0 else ", ".join(["\href{" + s["url"] + "}{" + s["name"] + "}" for s in exp["standards"]])
    achievements = "(none specific)" if len(exp["achievements"]) == 0 else "\n\n".join(["\item " + r for r in exp["achievements"]])
    strTpl = Template(str)
    return strTpl.substitute(company_url=company_url, company=company, start=start, end=end,
                            duration=duration, position=position, reports_to=reports_to,
                            teams=teams, company_description=company_description,
                            responsibilities=responsibilities, accomplishments=accomplishments,
                            techstack=techstack, standards=standards, achievements=achievements)


def to_month_year(ym):
    if ym == "":
        return "present"
    d = ym.split("-")
    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return month[int(d[1])-1] + " " + d[0]

def to_duration(start, end):
    return "1 year 4 months"

render_resume()