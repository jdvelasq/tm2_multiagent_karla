# %%
import os
import pandas as pd  # type: ignore

from techminer2.packages.networks.co_occurrence.descriptors import DocumentsByClusterMapping # type: ignore


if not os.path.exists("../reports/sec_40_dominant_clusters"):
    os.makedirs("../reports/sec_40_dominant_clusters")



documents_by_cluster = (
    DocumentsByClusterMapping()
    #
    # FIELD:
    .having_terms_in_top(None)
    .having_terms_ordered_by("OCC")
    .having_term_occurrences_between(7, None)
    .having_term_citations_between(None, None)
    .having_terms_in(None)
    #
    # NETWORK:
    .using_clustering_algorithm_or_dict("louvain")
    .using_association_index("association")
    #
    # DATABASE:
    .where_root_directory_is("../")
    .where_database_is("main")
    .where_record_years_range_is(2015, 2024)
    .where_record_citations_range_is(None, None)
    .where_records_ordered_by("date_newest")
    .where_records_match(
        {
            "document_type": [
                'Article',
                'Book',
                'Book chapter',
                'Conference paper',
                'Conference review',
                'Editorial',
                'Review',
            ]
        }
    ) 
    
    #
    .run()
)

for i_cluster, key in enumerate(documents_by_cluster.keys()):

    documents = documents_by_cluster[key]
    documents = [doc for doc in documents if "AB " in doc]
    documents = documents[:50]
    documents = [documents[i : i + 10] for i in range(0, len(documents), 10)]

    for i_group, group in enumerate(documents):

        group = "\n---\n\n".join(group)
        group = "---\n\n" + group + "\n\n---"
        cluster = f"{i_cluster:02d}"
        i_group = f"{i_group:02d}"
        if not os.path.exists(f"../reports/sec_40_dominant_clusters/{cluster}"):
            os.makedirs(f"../reports/sec_40_dominant_clusters/{cluster}")
        with open(
            f"../reports/sec_40_dominant_clusters/{cluster}/cl_{cluster}_{i_group}.txt",
            "wt",
            encoding="utf-8",
        ) as f:
            print(group, file=f)

            
# %%
