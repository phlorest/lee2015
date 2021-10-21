from setuptools import setup


setup(
    name='cldfbench_lee2015',
    py_modules=['cldfbench_lee2015'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'lee2015=cldfbench_lee2015:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
