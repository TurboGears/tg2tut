# -*- coding: utf-8 -*-
"""Setup the hiringpond application"""

import logging
from datetime import date

from tg import config
from hiringpond import model

import transaction

from pkg_resources import Requirement, resource_string
from sqlalchemy.util import buffer

def bootstrap(command, conf, vars):
    """Place any commands to setup hiringpond here"""

    # <websetup.bootstrap.before.auth
    from sqlalchemy.exc import IntegrityError
    try:
        u = model.User()
        u.user_name = u'wilee'
        u.display_name = u'Wile E. Coyote'
        u.title = u'Super Genius'
        u.email_address = u'wilee@example.com'
        u.password = u'wilee'
        u.streetaddress = u'The Unknown Highway'
        u.city = u'Desert Springs'
        u.state_province = u'NM'
        u.postal_code = u'THE-RE'
        u.country = u'USA'
        u.phones = u'{"cell": "908-555-1313"}'
        u.logo = None
        u.callingcard = None
        u.photo = buffer(resource_string(Requirement.parse("hiringpond"),"hiringpond/websetup/Wile_E_Coyote.png"))
        u.external_links = '{"wikipedia": "http://en.wikipedia.org/wiki/Wile_E._Coyote_and_Road_Runner", "homepage": "http://looneytunes.kidswb.com/"}'
        u.default_summary = u"I have held a wide variety of jobs over the past several decades, ranging from tunnel painter to inventor to product tester. I have a knack for finding out ways in which things will break, bringing harm to their users, and would be happy to help any company avoid the liability from such mishaps. Especially if that company's products can help me catch the Road RUnner finally.\n\n**Note: Wile E. Coyote is a trademark of Warner Bros, Inc, and is used here solely for satirical and education purposes.**"

        u.education.append(model.Education(education="Desert Springs University", date_completed=date(1940, 12, 20)))
        u.awards.append(model.Award(award="Medal of Valor for Courage in the face of adversity", date_awarded=date(1950, 1, 23)))
        
        j1 = model.JobHistory()
        j1.order = 3
        j1.company_name = u'Self-Employed'
        j1.job_title = u'Inventor and Super Genius'
        j1.job_city = u'Desert Springs'
        j1.job_state = u'Southwestern USA'
        j1.start_date = date(1948, 6, 1)
        j1.end_date = None
        j1.job_summary = u'In my continuing quest to capture the Road Runner (and finally have some lunch), I have worked on many devices, ranging from catapults, to rocket sleds, to helicopters. While my success rate has been suboptimal, I feel that it is only a matter of time before I devise the machine that will succeed.'
        j1.tags = u'["inventor", "genius", "mechanical"]'
        j1.hidden = False

        j1.job_bullets.append(model.JobPoints(order=2, bullet_text='Built rocket car capable of outrunning the Road Runner. Brakes proved inadequate, but this was still successful', tags='["mechanical", "rocket"]', hidden=False))
        j1.job_bullets.append(model.JobPoints(order=1, bullet_text='Used Newtonian physics and mecahanical engineering techniques to devise varieties of catapults (complete with hair triggers) to assist in Road Runner capture', tags='["physics", "mechanical", "catapult"]', hidden=False))

        u.jobs.append(j1)
        
        j2 = model.JobHistory()
        j2.order = 1
        j2.company_name = u'ACME Corporation'
        j2.job_title = u'Product Tester'
        j2.job_city = u'Desert Springs'
        j2.job_state = u'Southwestern USA'
        j2.start_date = date(1948, 6, 1)
        j2.end_date = None
        j2.job_summary = u'ACME Corporation makes a large variety of products. In my capacity as a product tester, I have used most of these products and found serious flaws. Fortunately, no lasting harm was done to me, and the products were sent back to the engineers for further development on safety features.'
        j2.tags = u'["safety", "testing", "injury"]'
        j2.hidden = False

        j2.job_bullets.append(model.JobPoints(order=2, bullet_text='Tested various release mechanisms from ACME, designed to disengage locks on catapults, boulders, braking systems, and other apparatus. Often times with detrimental effects.', tags='["testing", "injury"]', hidden=False))
        j2.job_bullets.append(model.JobPoints(order=1, bullet_text='Tested several machines capable of great speed. Found several of them that had such high acceleration that the fell apart on attempts to use full speed.', tags='["testing"]', hidden=False))
        
        u.jobs.append(j2)
        
        j3 = model.JobHistory()
        j3.order = 2
        j3.company_name = u'Stunt Animals, Inc.'
        j3.job_title = u'Professional Stunt Coyote'
        j3.job_city = u'Desert Springs'
        j3.job_state = u'Southwestern USA'
        j3.start_date = date(1948, 6, 1)
        j3.end_date = date(1966, 11, 05)
        j3.job_summary = u'Working at Stunt Animals, Inc. was an adventure. I never knew, on any given day, if I would have a boulder drop on me, or be run over by a truck or a train, or even be blown up. It was a fantastic place to work, and really allowed my talents to shine.'
        j3.tags = u'["stunt", "safety", "demolitions", "vehicles"]'
        j3.hidden = False

        j3.job_bullets.append(model.JobPoints(order=2, bullet_text='Fell off high cliffs, passing boulders on the way down, before getting hit by them, and walking away injury free.', tags='["injury", "stunt"]', hidden=False))
        j3.job_bullets.append(model.JobPoints(order=1, bullet_text='Crushed by various items (boulders, trains, passing vehicles) in many diverse situations. Walked away with minimal injuries.', tags='["injury", "stunt"]', hidden=False))
        u.jobs.append(j3)

        s1 = model.SkillGroups()
        s1.order = 1
        s1.name = u'Military Experience'
        s1.tags = u'["military", "demolitions", "vehicles", "safety"]'
        s1.hidden = False

        s1.skills.append(model.SpecificSkills(order=1, name='Demolitions', time_used='50+ years', last_used=date(2010, 12, 17), proficiency='Very Good', tags='[]', hidden=False))
        s1.skills.append(model.SpecificSkills(order=2, name='Trap Making', time_used='50+ years', last_used=date(2010, 12, 17), proficiency='Very Good', tags='[]', hidden=False))
        s1.skills.append(model.SpecificSkills(order=3, name='Trap Using', time_used='50+ years', last_used=date(2010, 12, 17), proficiency='Terrible', tags='[]', hidden=False))
        
        u.skillgroups.append(s1)
        
        s2 = model.SkillGroups()
        s2.order = 2
        s2.name = u'Artistic'
        s2.tags = u'[]'
        s2.hidden = False

        s2.skills.append(model.SpecificSkills(order=1, name='Tunnel Painting', time_used='50+ years', last_used=date(2010, 12, 17), proficiency='Very Good', tags='[]', hidden=False))
        s2.skills.append(model.SpecificSkills(order=2, name='Road Painting', time_used='50+ years', last_used=date(2010, 12, 17), proficiency='Very Good', tags='[]', hidden=False))
        s2.skills.append(model.SpecificSkills(order=3, name='Scenery Painting', time_used='50+years', last_used=date(2010, 12, 17), proficiency='Very Good', tags='[]', hidden=False))
        u.skillgroups.append(s2)
        
        s3 = model.SkillGroups()
        s3.order = 3
        s3.name = u'Mechanical'
        s3.tags = u'[]'
        s3.hidden = False

        s3.skills.append(model.SpecificSkills(order=1, name='Catapult Design', time_used='50+years', last_used=date(2010, 12, 17), proficiency='Very Good', tags='[]', hidden=False))
        s3.skills.append(model.SpecificSkills(order=2, name='Kit Assembly', time_used='50+ years', last_used=date(2010, 12, 17), proficiency='Very Good', tags='[]', hidden=False))
        
        u.skillgroups.append(s3)

        s4 = model.SkillGroups()
        s4.order = 4
        s4.name = u'Scientific'
        s4.tags = u'["physics", "kinetic", "fire", "gravity"]'
        s4.hidden = False

        s4.skills.append(model.SpecificSkills(order=1, name='Rocket Science', time_used='50+ years', last_used=date(2010, 12, 17), proficiency='Very Good', tags='[]', hidden=False))
        s4.skills.append(model.SpecificSkills(order=2, name='Gravitational Impact Studies', time_used='50+ years', last_used=date(2010, 12, 17), proficiency='Very Good', tags='[]', hidden=False))
        s4.skills.append(model.SpecificSkills(order=3, name='Explosive Reactions', time_used='50+ years', last_used=date(2010, 12, 17), proficiency='Very Good', tags='[]', hidden=False))
        u.skillgroups.append(s4)

        p1 = model.ProjectHistory()
        p1.order = 1
        p1.name = u'Gravitational Anomaly Research'
        p1.summary = u'In the southwestern United States, certain fauna appear to be immune to the effects of gravity. That is to say that they are capable of running off of cliffs without actually falling. I have been studying this for several decades, and attempting to capture a specimen. Unfortunately, capturing said specimen is considerably more difficult when I am *not* immune to the effects of gravity. As such, I have no conclusive results to explain the phenomena at this time'
        p1.start = date(1948, 6, 1)
        p1.end = None
        p1.tools_used = u'ACME Corporation Products, Rockets, Paint, Roller Skates'
        p1.tags = '["acme", "stunt", "mechanical", "physics", "gravity", "injury"]'
        p1.hidden = False

        p1.project_bullets.append(model.ProjectPoints(order=1, bullet_text='Unsuccessfully utilized various forms of attempts at flight (mechanical and natural) to evade consequences of gravity', tags='[]', hidden=False))
        p1.project_bullets.append(model.ProjectPoints(order=2, bullet_text='Unsuccessfully attempted to limit the problem fauna to the ground so as to enable proper study', tags='[]', hidden=False))
        u.projects.append(p1)
        
        p2 = model.ProjectHistory()
        p2.order = 2
        p2.name = u'Wildlife Control Studies'
        p2.summary = u'The fauna of the southwestern United States is rich. Certain aspects, though, require study and isloation. In particular, the road runner species has proved to be most damaging to other fauna of the region, and attempts to control it have been difficult at best. Over the past several decades, I have attempted to garner specimens of the population so as to determine how best to neutralize the damage it causes.'
        p2.start = date(1948, 6, 1)
        p2.end = None
        p1.tools_used = u'ACME Corporation Products, Rockets, Paint, Roller Skates'
        p2.tags = '["acme", "stunt", "mechanical", "physics", "gravity", "injury"]'
        p2.hidden = False

        p2.project_bullets.append(model.ProjectPoints(order=1, bullet_text='Utilized various rocket based vehicles to attempt to catch specimens', tags='[]', hidden=False))
        p2.project_bullets.append(model.ProjectPoints(order=2, bullet_text='Created traps (baited with food) to attempt to catch said specimens', tags='[]', hidden=False))
        u.projects.append(p2)
        
        model.DBSession.add(u)
    
        g = model.Group()
        g.group_name = u'managers'
        g.display_name = u'Managers Group'
    
        g.users.append(u)
    
        model.DBSession.add(g)
    
        p = model.Permission()
        p.permission_name = u'manage'
        p.description = u'This permission give an administrative right to the bearer'
        p.groups.append(g)
    
        model.DBSession.add(p)
    
        model.DBSession.flush()
        
        p1.companyid = j1.id
        p2.companyid = j1.id
        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print 'Warning, there was a problem adding your auth data, it may have already been added:'
        import traceback
        print traceback.format_exc()
        transaction.abort()
        print 'Continuing with bootstrapping...'
        

    # <websetup.bootstrap.after.auth>
