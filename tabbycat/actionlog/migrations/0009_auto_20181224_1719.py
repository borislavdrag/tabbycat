# Generated by Django 2.1.3 on 2018-12-24 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actionlog', '0008_auto_20180928_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionlogentry',
            name='type',
            field=models.CharField(choices=[('ba.disc', 'Discarded ballot set'), ('ba.ckin', 'Checked in ballot set'), ('ba.crea', 'Created ballot set'), ('ba.edit', 'Edited ballot set'), ('ba.conf', 'Confirmed ballot set'), ('ba.subm', 'Submitted ballot set from the public form'), ('fb.subm', 'Submitted feedback from the public form'), ('fb.save', 'Saved feedback'), ('ts.edit', 'Edited adjudicator test score'), ('aj.note', 'Set adjudicator note'), ('aa.save', 'Saved adjudicator allocation'), ('aa.auto', 'Auto-allocated adjudicators'), ('ve.save', 'Saved a venue manual edit'), ('ve.auto', 'Auto-allocated venues'), ('ve.ca.edit', 'Edited venue categories'), ('ve.co.edit', 'Edited venue constraints'), ('dr.crea', 'Created draw'), ('dr.conf', 'Confirmed draw'), ('dr.rege', 'Regenerated draw'), ('dr.rele', 'Released draw'), ('dr.unre', 'Unreleased draw'), ('mu.save', 'Saved a matchup manual edit'), ('ms.save', 'Saved the sides status of a matchup'), ('dv.save', 'Saved divisions'), ('mo.edit', 'Added/edited motion'), ('mo.rele', 'Released motions'), ('mo.unre', 'Unreleased motions'), ('db.im.auto', 'Auto-prioritized debate importance'), ('db.im.edit', 'Edited debate importance'), ('br.aj.set', 'Changed adjudicator breaking status'), ('br.el.edit', 'Edited break eligibility'), ('br.ca.edit', 'Edited break categories'), ('br.gene', 'Generated the team break for all categories'), ('br.upda', 'Edited breaking team remarks and updated all team breaks'), ('br.upd1', 'Edited breaking team remarks and updated this team break'), ('br.rm.edit', 'Edited breaking team remarks'), ('rd.st.set', 'Set start time'), ('rd.adva', 'Advanced the current round to'), ('rd.comp', 'Marked round as completed'), ('av.tm.save', 'Edited teams availability'), ('av.aj.save', 'Edited adjudicators availability'), ('av.ve.save', 'Edited venue availability'), ('op.edit', 'Edited tournament options'), ('se.edit', 'Edited speaker category eligibility'), ('se.ca.edit', 'Edited speaker categories'), ('si.inst', 'Imported institutions using the simple importer'), ('si.venu', 'Imported venues using the simple importer'), ('si.team', 'Imported teams using the simple importer'), ('si.adju', 'Imported adjudicators using the simple importer'), ('aj.sc.upda', 'Updated adjudicator scores in bulk'), ('ac.at.edit', 'Edited adjudicator-team conflicts'), ('ac.aa.edit', 'Edited adjudicator-adjudicator conflicts'), ('ac.ai.edit', 'Edited adjudicator-institution conflicts'), ('ac.ti.edit', 'Edited team-institution conflicts'), ('ch.sp.gene', 'Generated check in identifiers for speakers'), ('ch.aj.gene', 'Generated check in identifiers for adjudicators'), ('ch.ve.gene', 'Generated check in identifiers for venues'), ('pp.crea', 'Created preformed panels'), ('pp.im.auto', 'Auto-prioritized preformed panels'), ('pp.im.edit', 'Edited preformed panel importance'), ('pp.aj.auto', 'Auto-allocated adjudicators to preformed panels'), ('pp.aj.auto', 'Edited preformed panel adjudicator'), ('pp.db.auto', 'Auto-allocated preformed panels to debates')], max_length=10, verbose_name='type'),
        ),
    ]
