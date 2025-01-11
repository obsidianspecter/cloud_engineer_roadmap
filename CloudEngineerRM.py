import streamlit as st
import plotly.express as px
import pandas as pd

# --- Page Title ---
st.title("Comprehensive Cloud Engineer Career Roadmap")

# --- Section 1: Overview ---
st.header("Overview")
st.write("""
The Cloud Engineer career roadmap provides a detailed, step-by-step guide to mastering cloud technologies, 
earning certifications, and gaining the skills needed to secure a role in this rapidly growing field.
This roadmap includes skills, milestones, certifications, and timelines to guide your journey.
""")

# --- Section 2: Career Roadmap Timeline ---
st.header("Interactive Career Timeline")

timeline_data = pd.DataFrame({
    "Milestone": [
        "Learn Basics of Cloud",
        "Get Certified: AWS/GCP/Azure Fundamentals",
        "Build Hands-On Cloud Projects",
        "Master Networking & Security",
        "Get Certified: AWS Solutions Architect/Google PCA",
        "Learn DevOps Tools: Terraform, Docker, Kubernetes",
        "Master CI/CD Pipelines & Automation",
        "Build Scalable Cloud Applications",
        "Get Certified: Advanced Cloud Certifications",
        "Secure a Cloud Engineer Role"
    ],
    "Start Date": [
        "2025-01-01", "2025-02-01", "2025-03-01", "2025-05-01", "2025-06-01",
        "2025-08-01", "2025-10-01", "2025-11-01", "2026-01-01", "2026-03-01"
    ],
    "End Date": [
        "2025-01-31", "2025-02-28", "2025-04-30", "2025-05-31", "2025-07-31",
        "2025-09-30", "2025-10-31", "2025-12-31", "2026-02-28", "2026-03-31"
    ],
    "Description": [
        "Understand cloud computing basics, models, and services (IaaS, PaaS, SaaS).",
        "Earn a foundational certification to validate your cloud knowledge.",
        "Create hands-on projects to apply theoretical knowledge in real-world scenarios.",
        "Learn networking, subnets, VPCs, firewalls, and security best practices.",
        "Earn intermediate-level certifications to demonstrate architectural expertise.",
        "Gain expertise in Infrastructure as Code, containerization, and orchestration tools.",
        "Set up and optimize CI/CD pipelines to automate deployment processes.",
        "Design and implement scalable, high-availability cloud applications.",
        "Specialize in advanced certifications for niche cloud roles.",
        "Prepare and apply for Cloud Engineer roles in top organizations."
    ]
})

fig_timeline = px.timeline(
    timeline_data,
    x_start="Start Date",
    x_end="End Date",
    y="Milestone",
    color="Milestone",
    hover_name="Milestone",
    hover_data={"Description": True, "Start Date": True, "End Date": True},
    template="plotly_dark"
)
fig_timeline.update_yaxes(title_text="Milestones")
fig_timeline.update_layout(margin=dict(t=50, l=25, r=25, b=50))
st.plotly_chart(fig_timeline, use_container_width=True)

# --- Section 3: Skills Breakdown ---
st.header("Skills Breakdown by Proficiency Level")

skills_data = pd.DataFrame({
    "Skill": [
        "Cloud Fundamentals", "Networking", "Security", "DevOps", "CI/CD Pipelines",
        "Scripting (Python/Bash)", "Cloud Platforms (AWS/GCP/Azure)", "Infrastructure as Code (Terraform)",
        "Containers (Docker/Kubernetes)", "Monitoring & Logging"
    ],
    "Proficiency Required (%)": [80, 70, 65, 75, 70, 60, 90, 70, 75, 60]
})

fig_skills = px.bar(
    skills_data,
    x="Proficiency Required (%)",
    y="Skill",
    orientation="h",
    color="Proficiency Required (%)",
    title="Proficiency Levels for Cloud Engineering Skills",
    template="plotly_dark"
)
st.plotly_chart(fig_skills, use_container_width=True)

st.write("""
### Key Skills:
- **Cloud Fundamentals**: Understanding of cloud computing models, services, and basic terminology.
- **Networking & Security**: Knowledge of subnets, VPCs, firewalls, and securing cloud infrastructure.
- **DevOps**: Expertise in tools like Terraform, Docker, and Kubernetes for automating workflows.
- **Monitoring & Logging**: Setting up alerts, dashboards, and monitoring systems to ensure uptime.
""")

# --- Section 4: Certifications Path ---
st.header("Certifications Path")

certifications_data = pd.DataFrame({
    "Certification": [
        "AWS Certified Cloud Practitioner",
        "Microsoft Azure Fundamentals",
        "Google Associate Cloud Engineer",
        "AWS Certified Solutions Architect",
        "Google Professional Cloud Architect",
        "AWS Certified DevOps Engineer",
        "Google Professional DevOps Engineer"
    ],
    "Difficulty Level": ["Beginner", "Beginner", "Beginner", "Intermediate", "Intermediate", "Advanced", "Advanced"]
})

fig_certifications = px.sunburst(
    certifications_data,
    path=["Difficulty Level", "Certification"],
    title="Certifications Path for Cloud Engineers",
    template="plotly_dark"
)
st.plotly_chart(fig_certifications, use_container_width=True)

st.write("""
### Certification Details:
- **Beginner**: Focus on foundational certifications like AWS Cloud Practitioner or Azure Fundamentals.
- **Intermediate**: Advance to certifications like AWS Solutions Architect or Google PCA.
- **Advanced**: Specialize in DevOps roles with certifications like AWS Certified DevOps Engineer.
""")

# --- Section 5: Learning Resources ---
st.header("Learning Resources")

resources = [
    {"Topic": "Cloud Fundamentals", "Resource": "[AWS Cloud Practitioner Essentials](https://aws.amazon.com/training/digital/aws-cloud-practitioner-essentials/)"},
    {"Topic": "Networking & Security", "Resource": "[Google Cloud Networking Fundamentals](https://cloud.google.com/training)"},
    {"Topic": "DevOps Tools", "Resource": "[Terraform on AWS](https://learn.hashicorp.com/terraform)"},
    {"Topic": "Containers & Kubernetes", "Resource": "[Docker & Kubernetes Guide](https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/)"},
    {"Topic": "CI/CD Pipelines", "Resource": "[CI/CD Pipelines on AWS](https://aws.amazon.com/cicd/)"},
]

resources_df = pd.DataFrame(resources)

st.table(resources_df)

# --- Section 6: Time Investment ---
st.header("Estimated Time Investment")

time_investment = pd.DataFrame({
    "Stage": ["Learning Fundamentals", "Hands-On Projects", "Certifications", "Job Applications"],
    "Duration (Months)": [3, 4, 6, 2]
})

fig_time = px.pie(
    time_investment,
    names="Stage",
    values="Duration (Months)",
    title="Estimated Time Investment for Becoming a Cloud Engineer",
    template="plotly_dark",
    hole=0.3
)
st.plotly_chart(fig_time, use_container_width=True)

st.write("""
The average time to become a Cloud Engineer is approximately **15 months**, depending on your learning pace, prior experience, and dedication.
""")

