# %%

from techminer2.packages.networks.co_occurrence.descriptors import TermsByClusterSummary # type: ignore
df = (
    TermsByClusterSummary()
    #
    # FIELD:
    .having_terms_in_top(None)
    .having_terms_ordered_by("OCC")
    .having_term_occurrences_between(7, None)
    .having_term_citations_between(None, None)
    .having_terms_in(None)
    #
    # COUNTERS:
    .using_term_counters(True)
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

df["Terms"] = df["Terms"].str.split("; ")
df["Terms"] = df["Terms"].str[:10]
df["Terms"] = df["Terms"].map(lambda x: [y.split(" ")[0].lower().capitalize()  for y in x])
df["Terms"] = df["Terms"].str.join("; ")
df["Terms"] = df["Terms"].str.replace("_", " ")

print(df.to_string())
# %%
