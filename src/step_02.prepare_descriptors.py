# %%
import pandas as pd  # type: ignore
from techminer2.packages.networks.co_occurrence.descriptors import (  # type: ignore
    TermsByClusterDataFrame,
)
from techminer2.thesaurus.descriptors import *  # type: ignore

pd.set_option("display.max_rows", 100)


# %%
# RemoveParentheses(root_directory="../").run()  #  type: ignore
# ReplaceAbbreviations(root_directory="../").run()  #  type: ignore
# ReplaceHyphenatedWords(root_directory="../").run()  #  type: ignore
# BritishToAmericanSpelling(root_directory="../").run()  #  type: ignore
RemoveInitialDeterminers(root_directory="../").run()  #  type: ignore
# RemoveInitialStopwords(root_directory="../").run()  #  type: ignore
# RemoveCommonInitialWords(root_directory="../").run()  #  type: ignore
# RemoveCommonLastWords(root_directory="../").run()  #  type: ignore
# CleanupThesaurus(root_directory="../").run()  #  type: ignore
ReduceKeys(root_directory="../").run()  #  type: ignore


# %%
ExplodeKeys(root_directory="../").run()

# %%
ReduceKeys(root_directory="../").run()

# %%
SortByExactKeyMatch(pattern=["WHO"], root_directory="../").run()


# %%
SortByMatch(pattern=["Tecnológico Nacional de México"], root_directory="../").run()

import pandas as pd  # type: ignore

# %%

# ReduceKeys(root_directory="../").run()  #  type: ignore
ApplyThesaurus(root_directory="../").run()  #  type: ignore

df = (
    TermsByClusterDataFrame()
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

df.head(10)

# %%
from techminer2.thesaurus.abbreviations import CreateThesaurus  # type: ignore

CreateThesaurus(root_directory="../").run()

# %%

from techminer2.thesaurus.descriptors import ReplaceWord  # type: ignore

(
    ReplaceWord()
    .having_word("CARBON_DI_OXIDE")
    .having_replacement("CARBON_DIOXIDE")
    .where_root_directory_is("../")
).run()
# %%
