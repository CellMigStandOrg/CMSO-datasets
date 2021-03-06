import os
import glob

from isatools import isatab


def main():
    """
    The simplest checks for ISA-Tab correctness is to attempt to load ISA-Tab
    files, and then count certain objects to get an idea if the parser created
    the correct number of each entity.
    """

    expected_values = {
        'num_study_sources': [3, 1],
        'num_study_samples': [12, 60]
    }
    study_number = 0
    for d in sorted(glob.glob("cmso*/isa")):
        print("attempting to load {}".format(d))
        i_files = glob.glob(os.path.join(d, 'i_*.txt'))
        if len(i_files) != 1:
            raise FileNotFoundError(
                "Could not find an investigation file in {}".format(d))
        with open(os.path.join(next(iter(i_files)))) as i_fp:
            isa_objects = isatab.load(i_fp)
            assert isa_objects is not None  # if not created, error

            # Some simple checks to sanity check that loaded what we expected
            num_study_sources = len(
                isa_objects.studies[-1].materials['sources'])
            num_study_samples = len(
                isa_objects.studies[-1].materials['samples'])
            print("loaded {} study sources".format(num_study_sources))
            print("loaded {} study samples".format(num_study_samples))
            assert num_study_sources == \
                expected_values["num_study_sources"][study_number]
            assert num_study_samples == \
                expected_values["num_study_samples"][study_number]
            print("{} load OK".format(d))
            study_number += 1

    """
    Note that the validator validates against default configurations if none is
    provided. To validate against a config, do something like

        >>> isatab.validate(i_fp, '/path/to/isaconfig-default_v2015-07-02')
    There must be a configuration with matching measurement/technology type to
    run the validator.
    """
    # for d in glob.glob("cmso*/isa"):
    #     print("attempting to validate {}".format(d))
    #     i_files = glob.glob(os.path.join(d, 'i_*.txt'))
    #     if len(i_files) != 1:
    #         raise FileNotFoundError(
    #             "Could not find an investigation file in {}".format(d))
    #     with open(os.path.join(next(iter(i_files)))) as i_fp:
    #         report = isatab.validate(i_fp)
    #
    #     """when the report is generated, check the number of errors if
    #     there are errors or warnings, they will have been logged to stdout
    #     as well"""
    #     if report is not None:
    #         assert len(report.get('errors')) == 0
    #     else:
    #         raise RuntimeError(
    #             "No report generated by validator, problem during runtime")


if __name__ == "__main__":
    main()
