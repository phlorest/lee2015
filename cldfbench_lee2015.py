import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "lee2015"

    def cmd_makecldf(self, args):
        """
summary.trees: original/phylogeny_koreanic.tre
	nexus trees -t -c $< -o $@

posterior.trees: original/Koreanic_COV_UCLD.trees.gz
	# remove first 900 trees as burn-in
	nexus trees -c -d 1-901 $< -o $@

data.nex:
	cp original/Koreanic.nex $@
        """
        self.init(args)
        with self.nexus_summary() as nex:
            self.add_tree_from_nexus(
                args,
                self.raw_dir / 'phylogeny_koreanic.tre',
                nex,
                'summary',
                detranslate=True,
            )
        posterior = self.sample(
            self.remove_burnin(
                self.read_gzipped_text(self.raw_dir / 'Koreanic_COV_UCLD.trees.gz'), 901,
            ),
            n=100,
            detranslate=True,
            as_nexus=True)

        with self.nexus_posterior() as nex:
            for i, tree in enumerate(posterior.trees.trees, start=1):
                self.add_tree(args, tree, nex, 'posterior-{}'.format(i))

        self.add_data(args, self.raw_dir / 'Koreanic.nex')
