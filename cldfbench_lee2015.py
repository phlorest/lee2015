import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "lee2015"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.read_tree(
                'phylogeny_koreanic.tre', detranslate=True),
            self.metadata,
            args.log)

        # only have 1001 trees, so just keep 800
        posterior = self.raw_dir.read_trees(
            'Koreanic_COV_UCLD.trees.gz',
            burnin=201, detranslate=True)
        args.writer.add_posterior(posterior, self.metadata, args.log)
        
        args.writer.add_data(
            self.raw_dir.read_nexus('Koreanic.nex'),
            self.characters,
            args.log)
 