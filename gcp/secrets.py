import logging

from google.cloud import secretmanager

from gcp import PROJECT_ID

logger = logging.getLogger(__name__)


def create_secret(project_id, secret_id):
    """
    Create a new secret with the given name. A secret is a logical wrapper
    around a collection of secret versions. Secret versions hold the actual
    secret material.
    """
    from google.cloud import secretmanager

    client = secretmanager.SecretManagerServiceClient()

    parent = client.project_path(project_id)

    response = client.create_secret(parent, secret_id, {
        'replication': {
            'automatic': {},
        },
    })
    logger.info('Created secret: {}'.format(response.name))


def add_secret_version(project_id, secret_id, payload):
    """
    Add a new secret version to the given secret with the provided payload.
    """
    client = secretmanager.SecretManagerServiceClient()
    parent = client.secret_path(project_id, secret_id)
    payload = payload.encode('UTF-8')

    response = client.add_secret_version(parent, {'data': payload})

    logger.info('Added secret version: {}'.format(response.name))


def list_secrets(project_id):
    """
    List all secrets in the given project.
    """
    client = secretmanager.SecretManagerServiceClient()
    parent = client.project_path(project_id)
    secrets = client.list_secrets(parent)

    for secret in secrets:
        logger.info('Found secret: {}'.format(secret.name))

    return secrets


def delete_secret(project_id, secret_id):
    """
    Delete the secret with the given name and all of its versions.
    """
    client = secretmanager.SecretManagerServiceClient()

    name = client.secret_path(project_id, secret_id)
    client.delete_secret(name)
    logger.info(f"Secret deleted '{secret_id}'")


def get_secret(project_id, secret_id):
    """
    Get information about the given secret. This only returns metadata about
    the secret container, not any secret material.
    """
    client = secretmanager.SecretManagerServiceClient()
    name = client.secret_path(project_id, secret_id)
    response = client.get_secret(name)

    if response.replication.automatic:
        replication = 'AUTOMATIC'
    elif response.replication.user_managed:
        replication = 'MANAGED'
    else:
        raise 'Unknown replication {}'.format(response.replication)

    logger.info('Got secret {} with replication policy {}'.format(response.name, replication))
    return response


def access_secret_version(project_id, secret_id, version_id='latest'):
    """
    Access the payload for the given secret version if one exists. The version
    can be a version number as a string (e.g. "5") or an alias (e.g. "latest").
    """
    client = secretmanager.SecretManagerServiceClient()
    name = client.secret_version_path(project_id, secret_id, version_id)
    response = client.access_secret_version(name)
    payload = response.payload.data.decode('UTF-8')
    logger.info('Plaintext: {}'.format(payload))
    return payload

#create_secret(PROJECT_ID, 'wsj-cookie')

# wsj_cookie = 'DJSESSION=country%3Dus%7C%7Ccontinent%3D%7C%7Cregion%3D; wsjregion=na%2Cus; gdprApplies=false; ccpaApplies=true; usr_prof_v2=eyJpYyI6MH0%3D; ab_uuid=d67a8346-a701-40b7-8793-77ea593228c9; usr_bkt=830nwKog3K; utag_main=v_id:01716b0a2d1a00af9795c6f0c87003079007b07100b78$_sn:1$_se:1$_ss:1$_st:1586640561243$ses_id:1586638761243%3Bexp-session$_pn:1%3Bexp-session$_prevpage:WSJ_Article_World_Health%20Officials%20Plead%20for%20Public%20to%20Observe%20a%20Locked-Down%20Easter%3Bexp-1586642361250$vapi_domain:wsj.com; __gads=ID=27fca69fe76ad228:T=1586638761:S=ALNI_MbR4YarVfVCNj9vwBpbh-U4-qXNnQ; vidoraUserId=0u848ts8ccrcg03gk07mgjni4m83h4; s_fid=17F672BAFF553C93-1404E320AA10E362; s_sq=dowjdev%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fwww.wsj.com%25252Farticles%25252Fhealth-officials-plead-for-public-to-observe-a-locked-down-easter-11586592822%25253Fmod%25253Dhp_lead_pos1%2526link%253DSign%252520In%2526region%253Dfull-header%2526.activitymap%2526.a%2526.c; _scid=777fe324-64a4-422a-8554-49aa88414bdd; bkuuid=WwywBvVX99eOwoJK; AMCVS_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1; _mibhv=anon-1586638762296-8550260453_4171; _micpn=esp:-1::1586638762296; _tq_id.TV-63639009-1.1fc3=0ac2c4cbff7bda8f.1586638762.0.1586638762..; _fbp=fb.1.1586638762469.1194725928; djcs_route=4add59b1-81a6-41de-bcad-ef6c0e5c3a95; _ncg_sp_ses.5378=*; _ncg_sp_id.5378=dfae2b18-6b65-409e-be3a-46036b5b262a.1586638763.1.1586638763.1586638763.ef256172-16fb-4873-b45f-e3ec7255828c; _ncg_id_=dfae2b18-6b65-409e-be3a-46036b5b262a; ResponsiveConditional_initialBreakpoint=md; s_tp=2503; s_ppv=WSJ_Article_World_Health%2520Officials%2520Plead%2520for%2520Public%2520to%2520Observe%2520a%2520Locked-Down%2520Easter%2C41%2C41%2C1018; s_cc=true; AMCV_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1585540135%7CMCIDTS%7C18364%7CMCMID%7C32275238016596913983244368174724401487%7CMCAAMLH-1587243562%7C6%7CMCAAMB-1587243562%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1586645963s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; cX_P=k8w3r53ystnu6bnt; cX_S=k8w3r546bpxq6t1p; run-sso=true; TR=V2-01ed257b90057f8b957d4cefa29ea7ce1bb80f926765bd074600a791f2a7aeb0; djcs_auto=M1586552624%2Fv0T9EZySNUphQB%2FBPeiTp9azSg6lzJDUMmRwa0C3aojCtmoZASZrJFFvL8mNwme7Em%2FhAxOTtMwn6sZ7MwW1rIN18GU7hUzZaet86Wzvp8bfNVhR3%2F7vb%2F7B342pZlKUB7UDzlY9GT1N2QOzdqFqBWVnMvD5MK3kFjJu%2BRJIQHizXekWZUYY%2BLQbozmEiBOxUjtsqsK1L3veydTjJNLsQQd4p9ZRVw%2FmsBNt2k5oSxDbv%2FpGKnDv2fwzam6Rg54UyZ7l6%2F4ycztXKLhi3It9Knbg%2FtYTsq6JTTAXputhU4QhoGCWd9MJoV1YeaJ7VliKebfFW%2BEhg9cAon%2FyFk7BBw%3D%3DG; djcs_session=M1586637828%2FUlWbCZXd1axirJIjC%2Br%2F%2FZoUMdXciN2edPkTrrLiEv31WPGlBmq%2F72WZSlV57ZDeysTCpOKVeVG9XfLaGXfByPRYo6UaJNbJno1hXbabyCfXY6WdBE2%2FA9i%2FZMgyXNfxbVvmYsLueLJ3oUqKdqUUcGSNzW4hZdtTZgSYB4aioD2OeNkPbj0Q8W0xlzKIXpxjxFu7yKGQblAItOR1lB9NhqmnCnx2%2B1gfn9zWp%2FAmByDyhQjMc6UJy6ad4kyq3tP3HkqUQq2D9uln0%2FSuqhRN%2Bz%2B2UQN0xrANSkaeEqlL6uOviwRIS07EaimRpx1fHvy%2BO1SYtIltKYcmSUCoPpbiz%2Fm7gbiK6QThC6s6xN%2BU8FW3rPyuyifEvMIjft0cKR23TkiS7kAdVrGKVbjtXHtNLkBOmbNp0Sk2NfLFSx9zBlho%2BNKmTJE9D8Idp1wUpGcQdfLImwTMd0s2Fs6DK5PkZd56orN%2F4pPRZyyCu4vor%2B%2B3rzZUYoOqwMixe1sJeDRZwG2aBWvn%2BNLJ8OugMUwOFGAlcgxPGWQHIiKO8za%2BJd8%3DG'
# add_secret_version(PROJECT_ID, 'wsj-cookie', wsj_cookie)

access_secret_version(PROJECT_ID, 'wsj-cookie')
