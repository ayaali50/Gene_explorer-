import streamlit as st

# قاعدة بيانات الجينات والطفرات المرتبطة بها
mutation_data = {
    "L858R": {
        "Gene": "EGFR",
        "Chromosome": "7",
        "Location": "7p11.2",
        "Diseases": "Lung cancer",
        "Additional Info": "Point mutation in exon 21.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/EGFR_gene_map.svg/220px-EGFR_gene_map.svg.png"
    },
    "T790M": {
        "Gene": "EGFR",
        "Chromosome": "7",
        "Location": "7p11.2",
        "Diseases": "Lung cancer",
        "Additional Info": "Resistance mutation.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/EGFR_gene_map.svg/220px-EGFR_gene_map.svg.png"
    },
    "ΔF508": {
        "Gene": "CFTR",
        "Chromosome": "7",
        "Location": "7q31.2",
        "Diseases": "Cystic fibrosis",
        "Additional Info": "Deletion mutation causing defective protein.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/CFTR_gene_map.svg/300px-CFTR_gene_map.svg.png"
    }
}

# قاعدة بيانات الجينات الأساسية
gene_data = {
    "BRCA1": {
        "Chromosome": "17",
        "Location": "17q21.31",
        "Function": "DNA repair associated with homologous recombination",
        "Diseases": "Breast and ovarian cancer",
        "Common Mutations": ["185delAG", "5382insC"]
    },
    "TP53": {
        "Chromosome": "17",
        "Location": "17p13.1",
        "Function": "Tumor suppressor, regulates cell cycle",
        "Diseases": "Li-Fraumeni syndrome, many cancers",
        "Common Mutations": ["R175H", "R248Q"]
    },
    "CFTR": {
        "Chromosome": "7",
        "Location": "7q31.2",
        "Function": "Chloride channel, regulates salt transport",
        "Diseases": "Cystic fibrosis",
        "Common Mutations": ["ΔF508", "G551D"]
    },
    "EGFR": {
        "Chromosome": "7",
        "Location": "7p11.2",
        "Function": "Receptor tyrosine kinase involved in cell growth",
        "Diseases": "Lung cancer, glioblastoma",
        "Common Mutations": ["L858R", "T790M"]
    },
    "MYC": {
        "Chromosome": "8",
        "Location": "8q24.21",
        "Function": "Transcription factor that regulates cell proliferation",
        "Diseases": "Burkitt lymphoma, other cancers",
        "Common Mutations": ["Amplification", "Translocation"]
    }
}

# إضافة فلاتر للجينات
gene_type = st.selectbox("اختر نوع الجين:", ["سرطاني", "وراثي", "مناعي"])

# اختيار الطفرة من المستخدم
mutation_input = st.text_input("أدخل الطفرة الجينية (مثال: L858R)")

# عرض البيانات المتعلقة بالطفرة
if mutation_input:
    mutation_info = mutation_data.get(mutation_input.upper(), None)
    
    if mutation_info:
        st.subheader(f"معلومات عن الطفرة {mutation_input}:")
        st.write(f"**الجين المرتبط:** {mutation_info['Gene']}")
        st.write(f"**الكروموسوم:** {mutation_info['Chromosome']}")
        st.write(f"**الموقع الجيني:** {mutation_info['Location']}")
        st.write(f"**الأمراض المرتبطة:** {mutation_info['Diseases']}")
        st.write(f"**معلومات إضافية:** {mutation_info['Additional Info']}")
        
        # عرض صورة الجين
        st.image(mutation_info["Image"], caption=f"خريطة الجين {mutation_info['Gene']}")
    else:
        st.write("الطفرة غير موجودة في قاعدة البيانات.")
