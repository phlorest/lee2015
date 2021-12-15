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
        posterior = self.sample(
            self.remove_burnin(
                self.raw_dir.read('Koreanic_COV_UCLD.trees.gz'),
                901),
            n=100,
            detranslate=True,
            as_nexus=True)
                   
        args.writer.add_posterior(
            posterior.trees.trees,
            self.metadata,
            args.log)
                   
        args.writer.add_data(
            self.raw_dir.read_nexus('Koreanic.nex'),
            self.characters,
            args.log)
 