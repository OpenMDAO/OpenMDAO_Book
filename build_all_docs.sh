#!/bin/bash
if [ ! -d "./openmdao_book/OpenMDAO/" ]; then
    echo "Temporarily installing OpenMDAO repo to build the source docs";
    cd openmdao_book/;
    git clone https://github.com/OpenMDAO/OpenMDAO.git;
    cd ..;
fi
python build_source_docs.py;
python build_jupyter_book.py;
rm -rf openmdao_book/OpenMDAO;