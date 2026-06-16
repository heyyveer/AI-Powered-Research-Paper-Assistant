import hashlib
import os


def generate_pdf_hash(pdf):

    pdf_bytes = pdf.getvalue()

    pdf_hash = hashlib.md5(
        pdf_bytes
    ).hexdigest()

    return pdf_hash


def get_index_path(pdf_hash):

    return os.path.join(
        "data",
        "faiss_indexes",
        pdf_hash
    )


def index_exists(pdf_hash):

    index_path = get_index_path(
        pdf_hash
    )

    return os.path.exists(
        index_path
    )