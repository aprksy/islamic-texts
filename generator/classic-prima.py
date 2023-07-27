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

def render_education():
    pass

def render_summary():
    pass

def render_qualification():
    pass

def render_career_objective():
    pass

def render_personal_research():
    pass

def render_experiences():
    pass

render_resume()